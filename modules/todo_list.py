from peewee import *

DB = SqliteDatabase('todos.db')

class Todos(Model):
    title = CharField()
    location = CharField()

    class Meta:
        database = DB

    @classmethod
    def create_todo(cls, title, location):
        cls.create(
            title = title,
            location = location
        )

def initialize():
    DB.connect()
    # tells it to create the connection with the class
    DB.create_tables([Todos], safe = True)
    DB.close()

if __name__ == '__main__':
    initialize()
    Todos.create_todo('Update Resume', 'Computer')