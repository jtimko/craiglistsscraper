from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from assets.forms import SearchForm
from assets.main import main
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///craigstext.db'
db = SQLAlchemy(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class User(db.Model):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    phone = Column(String(12), nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)
    
    searches = relationship('Searches', backref='user', lazy='dynamic')

class Searches(db.Model):
    __tablename__ = "Searches"
    id = Column(Integer, primary_key=True)
    search = Column(String(25), nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    searchQuery = relationship('SearchQuery', backref='searches', lazy='dynamic')

class SearchQuery(db.Model):
    id = Column(Integer, primary_key=True)
    results = Column(String(2000), nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)

    search_id = Column(Integer, ForeignKey('Searches.id'), nullable=False)



@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        main(form.search_item.data, form.phone_number.data, form.time_interval.data)
        return redirect('/')
    return render_template('index.html', title="Craigs Text", form=form)

if __name__ == "__main__":
    app.run(debug=True)