from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SearchForm(FlaskForm):
    search_item = StringField('Search Item')
    submit = SubmitField('Submit')