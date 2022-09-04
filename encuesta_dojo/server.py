from flask import Flask, request, redirect, render_template,session
app = Flask(__name__)
app.secret_key = "youcantguessthis"

@app.route('/')
def start_form():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def collect_info():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def show_info():
    return render_template("show.html", name = session['name'], location = session['location'], language = session['language'], comments = session['comments'])

if __name__=="__main__":   
    app.run(debug=True)    