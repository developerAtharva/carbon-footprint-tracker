from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Account created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check email and password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)


@app.route('/calculator', methods=['GET', 'POST'])
@login_required
def calculator():
    emissions = None
    if request.method == 'POST':
        transport = float(request.form['transport']) 
        electricity = float(request.form['electricity'])
        diet = request.form['diet']

        emission_factors = {
            "transport": 0.12,  # kg CO₂ per km
            "electricity": 0.42,  # kg CO₂ per kWh
            "diet": {"vegan": 2.0, "vegetarian": 2.5, "meat": 5.0}  # kg CO₂ per day
        }

        transport_emissions = transport * emission_factors["transport"]
        electricity_emissions = electricity * emission_factors["electricity"]
        diet_emissions = emission_factors["diet"].get(diet, 3.0)

        total_emissions = transport_emissions + electricity_emissions + diet_emissions

        recommendations = []
        if transport > 20:
            recommendations.append("Consider using public transport or carpooling.")
        if electricity > 10:
            recommendations.append("Switch to energy-efficient appliances.")
        if diet == "meat":
            recommendations.append("Try reducing meat consumption for lower emissions.")

        return render_template("calculator.html", emissions=total_emissions, recommendations=recommendations)

    return render_template("calculator.html", emissions=emissions)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
