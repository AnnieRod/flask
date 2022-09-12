from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Dojo: 
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

##Recupera info por cada instancia creada
    @classmethod
    def get_dojos(cls):
        query= "SELECT * FROM dojos;"
        results = connectToMySQL('encuesta_dojo').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

## Crea instancia de dojo+persona e integra registro en base de datos
    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos(name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        new_dojo = connectToMySQL('encuesta_dojo').query_db(query, data)
        return new_dojo
    
##Recupera info individual acorde a ID
    @classmethod
    def one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('encuesta_dojo').query_db(query, data)
        return result

##MÉTODO DE VALIDACION
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters long.")
            is_valid = False
        if (dojo['location']) == "-- Select a Location --":
            flash("You have to select a location from the list.")
            is_valid = False
        if (dojo['language']) == "-- Select a Language --":
            flash("You have to select a language from the list.")
            is_valid = False
        if len(dojo['comment']) < 2:
            flash("If you dont have any comments put NA")
            is_valid = False
        return is_valid