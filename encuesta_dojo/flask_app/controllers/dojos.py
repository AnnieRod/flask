from flask import request, redirect, render_template,session

from flask_app import app

from flask_app.models.dojo import Dojo

@app.route('/')
def start_form():
    return render_template('index.html')

##Recibe info form y envia a resultado para ver info
@app.route('/process', methods = ['POST'])
def create_dojo():
    if not Dojo.validate_dojo(request.form):
        return redirect("/")
    Dojo.save_dojo(request.form)
    return redirect('/result')

##Recupera info para mostrar en pagina lista de students y dojos
@app.route('/result')
def all_dojos():
    return render_template("list.html", dojos = Dojo.get_dojos())

##Muestra info individual por estudiante del dojo
@app.route('/dojos/<int:id>')
def show_student(id):
    data = {
        "id": id
    }
    return render_template("show.html", dojos = Dojo.one_dojo(data))

if __name__ == "__main__":
    app.run(debug=True)
