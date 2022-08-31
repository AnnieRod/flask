from flask import Flask, render_template 

app = Flask(__name__)

# home ¿Como mostrar un div vacio o solo el H1 al entrar a la pagina inicial? 
@app.route ('/')
def Welcome():
    return render_template('index.html')

#Nivel 1
@app.route ('/play')
def blue_boxes():
    return render_template ('index.html', level = 1, color = "lightblue", count =3)

#Nivel 2
@app.route ('/play/<int:count>')
def many_boxes(count):
    return render_template ('index.html', level = 2, color = "lightblue", count=count)

#Nivel 3 
@app.route ('/play/<int:count>/<string:color>')
def color_boxes(color,count):
    return render_template ('index.html',level = 3, color=color, count=count)


if __name__=="__main__":   
    app.run(debug=True)    
