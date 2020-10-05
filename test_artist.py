import peewee
from unittest import TestCase
import database_config
database_config.database_path = 'database/test_arts.db'

import db_manager
from model_artist import Artist

class DatabaseTests(TestCase):

    def setUp(self):
        database_config.database_path = 'database/test_arts.db'
        Artist.delete().execute()

    def test_add_artist(self):        
        new_artist = Artist(name='abdala', email='abdala@gmail.com')
        new_artist.save()
        self.assertEquals(new_artist.id, db_manager.check_if_artis_exist(new_artist.name))

    def test_add_artist_duplicate_name(self):
        new_artist = Artist(name='abdala', email='mtn@gmail.com')
        new_artist.save()
        with self.assertRaises(peewee.IntegrityError):
            same_artist = Artist(name='abdala', author='abdala@yahoo.com')
            same_artist.save()
    
    def test_add_artist_duplicate_email(self):
        new_artist = Artist(name='abdala', email='mtn@gmail.com')
        new_artist.save()
        with self.assertRaises(peewee.IntegrityError):
            same_artist = Artist(name='jama', author='mtn@gmail.com')
            same_artist.save()

    def test_case_sensitivity_constraint(self):
        new_artist = Artist(name='abdala', email='mtn@gmail.com')
        new_artist.save()
        with self.assertRaises(peewee.IntegrityError):
            same_artist = Artist(name='AbDaLA', author='mtn@gmail.com')
            same_artist.save()
