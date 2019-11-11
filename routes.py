from flask import Flask, render_template, redirect
from forms import MyForm
app = Flask(__name__)
app.secret_key = 'abcdefg'

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='This is my Homepage!', subtitle='This is a subtitle!')

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)


@app.route('/success')
def success():
	return '<h1>Form submitted successfully!</h1>'


if __name__ == '__main__':
    app.run()
