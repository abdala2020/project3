import peewee 
import db_manager
from model_artist import Artist
from model_artwork import Artwork
from menu import Menu
import ui

def main():
    menu = create_menu()
    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == 'Q':
            break


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add Artist', add_artist)
    menu.add_option('2', 'Add Art Work', add_artwork)
    menu.add_option('3', 'get all art', get_all_artist_artwork)
    menu.add_option('4', 'get available art only', get_artist_available_artwork)
    menu.add_option('5', 'delete art work', delete_artwork)
    menu.add_option('6', 'change availibility status', update_artwork_availibility)
    menu.add_option('Q', 'Quit', quit_program)

    return menu

def add_artist():
    name = ui.get_non_empty_string("enter name ")
    email = ui.get_email()
    try:
        new_artist = db_manager.create_artist(name, email)
        new_artist.save()
    except peewee.IntegrityError:
        ui.message(f"Failed to add! Either the Name: {name}, or the Email: {email} already exist in the database ")

def add_artwork():
    art_name = ui.get_non_empty_string("Enter the name of the art work? ")
    art_price = ui.get_positive_float("Enter the price of the art work? ")
    is_available = ui.get_availibility_value()
    artists_name = ui.get_non_empty_string("Enter name of artist ")
    artist = db_manager.check_if_artis_exist(artists_name)
    if artist:
        try:
            new_artwork = db_manager.create_art_work(artist, art_name, art_price, is_available)
            new_artwork.save()
        except peewee.IntegrityError:
            ui.message(f" name: {art_name} already exists")
    else:
        ui.message(f"name: {artists_name}, doesn't exist in the database. Please create one first")

def get_all_artist_artwork():
    name = input('Enter artist name ?')
    artist_id = db_manager.check_if_artis_exist(name)
    if artist_id:
        art_list = db_manager.get_all_artwork_of_artist(name)
        if art_list:
            ui.message(art_list)
        else:
            ui.message(f"name: {name}, doesn't have a database record")    
    else:
        ui.message(f"name: {name}, doesn't exist in the database. Please create one first")

def get_artist_available_artwork():
    name = input('Enter artist name ?')
    is_artist = db_manager.check_if_artis_exist(name)
    if is_artist:
        available_art = db_manager.get_available_artwork_of_artist(name)
        if available_art:
            ui.message(available_art)
        else:
            ui.message(f"name: {name}, has no available art in the database")    
    else:
        ui.message(f"name: {name}, doesn't exist in the database. Please create one first")

def delete_artwork():
    get_id = ui.get_arwork_id()
    try:
        delete_art = db_manager.delete_artwork_by_id(get_id)
        ui.message(f"successfully deleted {delete_art} row")
    except peewee.DoesNotExist:
        ui.message("The art work you are trying to delete doesn't exist")

def update_artwork_availibility():
    get_id = ui.get_arwork_id()
    sold_or_available = ui.get_availibility_value()
    try:
        updated_rows = db_manager.change_availibility_status(sold_or_available, get_id)
        ui.message(f"successfully updated {updated_rows} row")
    except peewee.DoesNotExist:
        ui.message("The art work you are trying to delete doesn't exist")



    
    
def quit_program():
    ui.message('Thanks and bye!')


if __name__ == '__main__':
    main()
