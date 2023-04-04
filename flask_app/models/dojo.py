from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
class Dojo:
    db = "dojos_and_ninjas"

    def __init__(self,db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results =  connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, updated_at, created_at) VALUES (%(name)s, NOW(), NOW() );"
        result = connectToMySQL('ninjas').query_db(query, data)
        return result
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        dojo = results(cls[0])
        for row in results:
            ninja_data ={
                "id": row['ninja.id'],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo
