from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db = "dojos_and_ninjas"

    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas VALUES (first_name, last_name, age, dojos_id, updated_at, created_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s, NOW(), NOW() );"
        return connectToMySQL('ninjas').query_db(query,data)