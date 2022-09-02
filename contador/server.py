from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'countersecretkey'

## numero de veces que se ha visitado localhost:5000
@app.route('/')
def counter_visit():
    if 'count' in session:
        session['count'] += 1
    else: 
        session['count'] = 1
    if session['count'] >= 2:
        times = "times"
    else:
        times = "time"
    return render_template('index.html', count =  session['count'],times = times)

## elimina sesión y redirige a ruta raiz - BONUS NINJA, se conecta a boton por url
@app.route('/destroy_session')
def delete_visits():
    session.clear()
    return redirect('/') ##ojo, va ruta, no pagina html

## BONUS NINJA: Nueva ruta para boton de contador +2
@app.route('/count_2')
def count_two():
    if 'count' in session:
        session['count'] += 2
    else: 
        session['count'] = 2
    if session['count'] >= 2:
        times = "times"
    else:
        times = "time"
    return render_template('index.html', count =  session['count'],times = times)

if __name__ == "__main__":
    app.run(debug=True)

##BONUS SENSEI DE SOLICUTD CON FORM -PENDEINTE POR HACER!!!

##BONUS SENSEI: Decodificando las cookies, resultado en python shell

# >>> import base64
# >>> base64.urlsafe_b64decode('eyJjb3VudCI6OH0 ===')
# b'{"count":8}'
# >>> base64.urlsafe_b64decode('eyJjb3VudCI6MTF9 ===')
# b'{"count":11}'
# >>>



