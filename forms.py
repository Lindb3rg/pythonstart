from flask_wtf import FlaskForm
from wtforms import Form,BooleanField,StringField,validators,ValidationError
from wtforms.fields import IntegerField, TextAreaField, EmailField, SelectField,DecimalField,TelField,DateField,PasswordField
from wtforms.validators import EqualTo, InputRequired
from datetime import datetime


class Contact_form(FlaskForm):
    namn = StringField("namn", validators=[validators.DataRequired(), validators.length(max=20)])
    epost = EmailField("epost",validators=[validators.Email()])
    telefon = TelField("telefon")
    rubrik = SelectField("rubrik", choices=["Support", "Försäljning", "Samarbeten", "Övrigt"])
    text = TextAreaField(validators=[validators.length(max=512)])