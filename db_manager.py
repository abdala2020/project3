import peewee
from model_artist import Artist
from model_artwork import Artwork

def check_if_artis_exist(artist_name):
    """checks if artist exists. returns the primary ID, if it exists.
    and none value if it doesn't"""
    res = Artist.get_or_none(Artist.name == artist_name)
    if res:
        return res.id

def create_artist(name, email):
    """creates and returns a Model instance for the Artist Model using the Field instances - name, email. """
    artist = Artist.create(name=name, email=email)
    return artist


def create_art_work(artist, art_name, price, availibility):
    """creates and returns a Model instance for the Artwork Model
     using the Field instances - artist, art_name, price, and availibility """
    artwork = Artwork.create(artist=artist, art_name=art_name, price=price, available=availibility)
    return artwork
    
def get_all_artwork_of_artist(name):
    """returns a list of all the ark work of an artist regardless of the availibility status
       """
    artwork_list = []
    for art in Artwork.select().join(Artist).where(Artist.name == name):
            artwork_list.append(art.art_name)
    return ', '.join(artwork_list)
    
def get_available_artwork_of_artist(name):
    """returns a list of all the ark work of an artist regardless of the availibility status
       """
    artwork_list = []
    for art in Artwork.select().join(Artist).where(
        (Artist.name == name) & (Artwork.available == True)):
        artwork_list.append(art.art_name)
    return ', '.join(artwork_list)

def delete_artwork_by_id(primary_id):
    """get artwork by ID and deletes it and returns number of row deleted"""
    art = Artwork.get(Artwork.id == primary_id)
    num_row_deleted = art.delete_instance()
    return num_row_deleted

def change_availibility_status( availibilit_status, primary_id):
    """gets artwork by ID and updates it's availibility status. retuns 
    number of row updated """
    query = Artwork.update(available=availibilit_status).where(Artwork.id == primary_id)
    rows_updated = query.execute()
    return rows_updated

