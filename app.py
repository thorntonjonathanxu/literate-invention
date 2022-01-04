
from flask import Flask, render_template, url_for, redirect, flash
import os
from forms import SampleForm

app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY'] = 'foo'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sampleform', methods=['GET', 'POST'])
def sampleform():
    form=SampleForm()
    if form.validate_on_submit():
        flash(form._fields)
        print(form._fields)
        return redirect('/index')

    return render_template('sampleform.html', form=form)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
    