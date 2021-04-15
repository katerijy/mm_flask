from app import app, db, mail, Message
from flask import render_template, request, flash, redirect, url_for, jsonify
from app.forms import UserInfoForm, CreateMcardForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

@app.route('/')
@app.route('/base')
def welcome():
    return render_template('/base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = "Meridian Meditations | Register"
    form = UserInfoForm()
    if request.methods == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()
        flash("Thank you for signing up. Now you can track your meditation history!", "success")
        return redirect(url_for('welcome'))
    return render_template('register.html', title=title, form=form)

# def login():
#     title = "Meridian Meditations | LOGIN"
#     form = LoginForm()
#     if request.methods == 'POST' and form.validate():
#         username = form.username.data
#         password = form.password.data

#         user = User.query.filter_by(username=username).first()

#         if user is None or not check_password_hash(user.password, password):
#             flash("Incorrect Email/Password. Please try again", 'danger')
#             return redirect(url_for('register'))
        
#         login_user(user, remember=form.remember_me.data)
#         flash("You have successfully logged in!", 'success')
#         next_page = request.args.get('next')
#         if next_page:
#             return redirect(url_for('home'))

#     return render_template('register.html', title=title, form=form)


# @app.route('/logout')
# def logout():
#     logout_user()
#     flash("You have succesfully logged out", 'primary')
#     return redirect(url_for('home'))

# # @app.route('/createMcard')
# # @app.route('/createMcard.html', methods=['GET', 'POST'])
# # def createMcard():
# #     title = "Meridian Meditions | Get My Meditation"
# #     form = CreateMcardForm()
# #     if request.method == 'POST' and form.validate():
# #         climate = form.climate.data
# #         taste = form.taste.data
# #         emotions = form.emotions.data
# #           mcard = Mcard()
# #         db.session.commit()
      
         
# #        return render_template("mcards.html", form=form)

    