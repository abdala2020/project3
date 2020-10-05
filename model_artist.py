import sqlite3
from peewee import *
from database_config import database_path

#create reference to SQLite database file
db = SqliteDatabase(database_path)

"""represents an artist in the database
    """
class Artist(Model):
    id = AutoField()
    name = CharField(unique=True)
    email = CharField(unique=True)

    class Meta():
        database = db #this model uses the "arts.db" database
        constraints = [SQL('UNIQUE( name COLLATE NOCASE, email COLLATE NOCASE )')]

    def __str__(self):
        return f'{self.id}: {self.name}: {self.email}'



db.connect()
db.create_tables([Artist])
    


 








