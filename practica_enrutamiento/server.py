from flask import Flask  

app = Flask(__name__)
    
@app.route('/')         
def saludo_inicio():
    return '¡Hola Mundo!' 

@app.route('/dojo')         
def dojo():
    return '¡Dojo!' 

@app.route ('/say/<string:username>')
def say_hello(username):
    return f"¡Hola, {username}!"

@app.route ('/repeat/<int:number>/<string:word>')
def phrase(number,word):
    phrase = ''
    for i in range (0, number):
        phrase += f"\n{word}"
    return phrase

if __name__=="__main__":   
    app.run(debug=True)    

