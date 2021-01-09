from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from assets.forms import SearchForm
from assets.main import main
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        main(form.search_item.data, form.phone_number.data, form.time_interval.data)
        return redirect('/')
    return render_template('index.html', title="CraigsCall", form=form)

if __name__ == "__main__":
    app.run(debug=True)