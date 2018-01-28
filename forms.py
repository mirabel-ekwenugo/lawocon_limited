from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms import validators


class ContactForm(FlaskForm):
    name = TextField("Name", [validators.Required("Please enter a Name")])
    email = TextField(
        "Email",
        [validators.Required("Please enter an email"),
            validators.Email("Please enter a valid email address.")])
    subject = TextField(
        "Subject",
        [validators.Required("Please enter a subject")])
    message = TextAreaField(
        "Message",
        [validators.Required("Please enter a message")])
    submit = SubmitField("Send Message")