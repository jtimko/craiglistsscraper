from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class SearchForm(FlaskForm):
    search_item = StringField('Search Item')
    phone_number = StringField('Phone Number')
    time_interval = IntegerField('Time Interval')
    submit = SubmitField('Submit')