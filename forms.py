from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class RegisterForm(Form):
    first_name = StringField('First Name',validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired(),Email()])
    submit = SubmitField('Submit')