from flask_wtf import FlaskForm
# from wtforms.fields.html5 import StringField, DateField, DateTimeField, SelectField, SubmitField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from . import utils
from flask import flash


class NewMsgForm(FlaskForm):
    title_raw = StringField('Titre', validators=[DataRequired()])
    body_raw = StringField('Message', validators=[DataRequired()])

    submit = SubmitField('Proposer des tags!')
