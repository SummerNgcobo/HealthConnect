from flask import Blueprint, render_template
from flask_login import  login_required, current_user
from flask import request, redirect, url_for
from flask import current_app
from . import db
from .models import Booking
# from website import app, db
# from models import Booking

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@views.route('/sick')
@login_required
def sick():
    return render_template("sick.html", user=current_user)

# @views.route('/booking')
# def booking():
#     return render_template("booking.html", user=current_user)

@views.route('/booking', methods=['GET', 'POST'])
@login_required
def booking():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        medical_service = request.form['medical-service']
        
        booking = Booking(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            medical_service=medical_service,
            user_id=current_user.id
        )
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('views.dashboard'))
    
    return render_template("booking.html", user=current_user)

@views.route('/medical-history')
@login_required
def medical_history():
    # Implement logic to fetch and display medical history
    return render_template("medical_history.html", user=current_user)

@views.route('/volunteer')
@login_required
def volunteer():
    # Implement volunteer registration or information page
    return render_template("volunteer.html", user=current_user)

@views.route('/mobile-clinic-dates')
@login_required
def mobile_clinic_dates():
    # Implement logic to display mobile clinic dates
    return render_template("mobile_clinic_dates.html", user=current_user)

@views.route('/doctors-near-me')
@login_required
def doctors_near_me():
    # Implement logic to display nearby doctors
    return render_template("doctors_near_me.html", user=current_user)

@views.route('/doctor-account')
@login_required
def doctor_account():
    # Implement doctor's account page
    return render_template("doctor_account.html", user=current_user)

@views.route('/student-account')
@login_required
def student_account():
    # Implement medical student's account page
    return render_template("student_account.html", user=current_user)

@views.route('/volunteer-account')
@login_required
def volunteer_account():
    # Implement volunteer's account page
    return render_template("volunteer_account.html", user=current_user) 

# @views.route('/')
# @login_required
# def home():
#     return render_template("home.html", user=current_user)

# @views.route('/dashboard')
# def dashboard():
#     return render_template("dashboard.html", user=current_user)


# @views.route('/sick')
# def sick():
#     return render_template("sick.html", user=current_user)

# @views.route('/booking')
# def booking():
#     return render_template("booking.html", user=current_user)



# @app.route('/make-booking', methods=['POST'])
# def make_booking():
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     date = request.form['date']
#     time = request.form['time']
#     medical_service = request.form['medical-service']

#     booking = Booking(
#         name=name,
#         email=email,
#         phone=phone,
#         date=date,
#         time=time,
#         medical_service=medical_service,
#         user_id=current_user.id
#     )
#     db.session.add(booking)
#     db.session.commit()

#     return redirect(url_for('dashboard'))