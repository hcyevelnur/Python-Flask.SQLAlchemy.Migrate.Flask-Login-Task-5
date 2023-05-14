from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, email_validator, Length, Email
# from wtforms.widgets import TextArea
from models import *


class ContactForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])


class QeydiyyatFormu(FlaskForm):
    name = StringField('Ad', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Soyad', validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('istifadəçi adı', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = IntegerField('Telefon', validators=[DataRequired()])
    password = StringField('Şifrə', validators=[DataRequired(), Length(min=8, max=18)])


class GirisFormu(FlaskForm):
    username = StringField('istifadəçi adı', validators=[DataRequired(), Length(min=2, max=20)])
    password = StringField('Şifrə', validators=[DataRequired(), Length(min=8, max=18)])
