from flask import Flask, render_template 

app = Flask(__name__)

#localhost: renderiza tablero de 8*8
@app.route ('/')
def checkered_8 ():
    return render_template('index.html', row = 8, column= 8, color1 = "red", color2= "black")

#localhost:5000/4 : tablero de 8*4
@app.route ('/4')
def checkered_4 ():
    return render_template('index.html', row = 4, column= 8, color1 = "red", color2= "black")

#localhost:5000/(x)/(y): Un tablero de x*y
@app.route ('/<int:row>/<int:column>')
def checkered_random(row, column):
    return render_template ('index.html',row = row, column = column, color1 = "red", color2= "black")

#BONUS NINJA: Ruta que recibe x / y / color alterno
@app.route ('/<int:row>/<int:column>/<string:color1>')
def checkered_color(row, column, color1):
    return render_template('index.html', row = row, column = column, color1 = color1, color2 = "black")

#BONUS SENSEI:  Ruta que recibe x / y / color alterno /color alterno 2
@app.route ('/<int:row>/<int:column>/<string:color1>/<string:color2>')
def checkered_twoCol(row, column, color1, color2):
    return render_template('index.html', row = row, column = column, color1 = color1, color2 = color2)


if __name__=="__main__":   
    app.run(debug=True)    



