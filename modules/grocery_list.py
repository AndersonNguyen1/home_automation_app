from peewee import *

DB = SqliteDatabase('glist.db')

class Glist(Model):
    description = TextField()
    title = CharField()

    class Meta:
        database = DB

    @classmethod
    def create_grocery(cls, title, description):
        cls.create(
            title = title,
            description = description
        )

def initialize():
    DB.connect()
    # tells it to create the connection with the class
    DB.create_tables([Glist], safe = True)
    DB.close()

if __name__ == '__main__':
    initialize()
    Glist.create_grocery('Banana', '29 cent one')