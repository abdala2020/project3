from model_artist import Artist
from model_artwork import Artwork
import peewee
import re

def message(msg):
    """ Prints a message for the user
     :param msg: the message to print"""
    print(msg)


def display_menu_get_choice(menu):
    """ Displays all of the menu options, checks that the user enters a valid choice and returns the choice.
     :param menu: the menu to display
     :returns: the user's choice """
    while True:
        print(menu)
        choice = input('Enter choice? ')
        if menu.is_valid(choice):
            return choice
        else:
            message('Not a valid choice, try again.')

def get_non_empty_string(question):
    """accepts only alpha characers for an answer """
    answer = input(question)
    while True:
        if answer.isalpha() == False:
            message("Please use alpha characters only!") 
            answer = input(question)
        else:
            return answer

def get_email(): 
    """define the regex pattern for valid email 
        pass the regular expression 
        and the string in search() method """ 
    regex = r"^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$"
    while True:
        email = input("Enter email? ")
        email = email.lower()
        if(re.search(regex,email)):  
            return email     
        else:  
            message("Invalid Email. Please a valid email address")  

def get_positive_float(question):
    """accepts only positive float number as the correct user input."""
    while True:
        try:
            answer = float(input(question))
            if not answer or answer < 0:
                message("Please use positive decimal values for the price")
                answer = float(input(question))
            else:
                return answer
        except ValueError:
            message("Please enter a number")
            
def get_availibility_value():
    """ Ask user to enter 'available' or 'sold'
     :returns: True if user enters 'available' or False if user enters 'sold' """
    while True:
        response = input('Enter \'available\' if art work is available or \'sold\' if art work is not available: ')
        if response.lower() == "available":
            return True
        elif response.lower() == "sold":
            return False
        else:
            message('Type \'available\' or \'sold\'')
           
    
def get_arwork_id():
    """ Ask for ID, validate to ensure is positive integer
    :returns: the ID value """
    while True:
        try:
            id = int(input('Enter art work ID: '))
            if id > 0:
                return id
            else:
                message('Please enter a positive number.')

        except ValueError:
            message('Please enter a number.')



        
    



