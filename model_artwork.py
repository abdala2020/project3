import sqlite3
from peewee import *
from model_artist import Artist
from database_config import database_path

#create reference to SQLite database file
db = SqliteDatabase(database_path)

"""represtents a art work in the database
    """
class Artwork(Model):
    id = PrimaryKeyField()
    artist = ForeignKeyField(Artist, backref='arts')
    art_name = CharField(unique=True)
    price = FloatField()
    available = BooleanField(default=False)

    class Meta():
        database = db #this model uses the "arts.db" database
        constraints = [SQL('UNIQUE( art_name COLLATE NOCASE )')]

    def __str__(self):
        return f'{self.id}: Artist: {self.artist}: {self.art_name}: {self.price}: {self.available}' 
db.connect()
db.create_tables([Artwork]) 
