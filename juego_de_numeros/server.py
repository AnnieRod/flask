import random
from flask import Flask, render_template, redirect, session,request

app = Flask(__name__)
app.secret_key = 'trynexttime'

@app.route('/')
def start():
    if "number" not in session:
        session['number'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/play', methods = ['POST'])
def guess_num():
    session['guess_num'] = int(request.form['num'])
    return redirect('/')

@app.route('/restart')
def try_again():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)