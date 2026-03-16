import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bloodgroup.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'bmp', 'gif'}

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# ------------------- Database Models -------------------
class Hospital(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    tests = db.relationship('Test', backref='hospital', lazy=True)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'), nullable=False)
    patient_name = db.Column(db.String(100), nullable=False)
    blood_group = db.Column(db.String(5), nullable=False)
    fingerprint_filename = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# ------------------- Load Trained Model -------------------
MODEL_PATH = 'model.h5'
model = load_model(MODEL_PATH)
class_names = ['A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-']  # match your notebook

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def predict_blood_group(image_path):
    """Predict blood group from fingerprint image."""
    img = load_img(image_path, target_size=(64, 64))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # (1,64,64,3)
    preds = model.predict(img_array)
    pred_class = np.argmax(preds, axis=1)[0]
    return class_names[pred_class]

# ------------------- Flask-Login -------------------
@login_manager.user_loader
def load_user(user_id):
    return Hospital.query.get(int(user_id))

# ------------------- Routes -------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hashed_pw = generate_password_hash(password)
        hospital = Hospital(name=name, email=email, password=hashed_pw)
        db.session.add(hospital)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hospital = Hospital.query.filter_by(email=email).first()
        if hospital and check_password_hash(hospital.password, password):
            login_user(hospital)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', hospital=current_user)

@app.route('/test', methods=['GET', 'POST'])
@login_required
def test():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        if 'fingerprint' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file = request.files['fingerprint']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Append timestamp to avoid name conflicts
            name, ext = os.path.splitext(filename)
            filename = f"{name}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{ext}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Predict blood group
            try:
                blood_group = predict_blood_group(filepath)
            except Exception as e:
                flash(f'Prediction error: {str(e)}', 'danger')
                return redirect(request.url)

            # Save test record
            test_record = Test(
                hospital_id=current_user.id,
                patient_name=patient_name,
                blood_group=blood_group,
                fingerprint_filename=filename
            )
            db.session.add(test_record)
            db.session.commit()

            flash(f'Test completed! Predicted Blood Group: {blood_group}', 'success')
            return redirect(url_for('history'))
        else:
            flash('Allowed file types: png, jpg, jpeg, bmp, gif', 'danger')
    return render_template('test.html')

@app.route('/history')
@login_required
def history():
    tests = Test.query.filter_by(hospital_id=current_user.id).order_by(Test.timestamp.desc()).all()
    return render_template('history.html', tests=tests)

@app.route('/plots')
def plots():
    # Public page to show model performance plots
    plot_folder = 'static/images/plots'
    plot_files = []
    if os.path.exists(plot_folder):
        plot_files = [f for f in os.listdir(plot_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    return render_template('plots.html', plot_files=plot_files)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Create upload folder if not exists
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)