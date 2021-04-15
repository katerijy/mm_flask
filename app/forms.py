from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField, TextAreaField, BooleanField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, EqualTo, Email


class UserInfoForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()


class CreateMcardForm(FlaskForm):
    id = IntegerField('id', validators=None)
    user_id = StringField('User_id', validators=[DataRequired()])
    time = SelectField('Is there a time you wake from sleep? If no, then pick a time you are most tired during the day',
        validators=None,
        choices=["1am-3am", "3am-5am", "5am-7am", "9am-11am", "11am-1pm"])
    climate = SelectField('Pick a climate you are most sensitive to', validators=None,
        choices=["Wind", "Heat", "Cold", "Damp", "Dry"])
    taste=SelectField('What flavor do you crave the most', validators=None,
        choices=["Sweet", "Salty", "Pungent/Strong", "Sour", "Bitter"])
    emotions=SelectField('What emotion do you feel more strongly', validators=None,
        choices=["Anger", "Sadness", "Joy", "Fear", "Worry"])
    submit = SubmitField()


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField()