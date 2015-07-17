#!/usr/bin/python
#
# Program To Maintain An Email Address File From The Command Line
#    addressbook.py
#
# Created by: Jason M Wolosonovich
#    6/09/2015
#
# Lesson 12 - Exercise 2
"""
addressbook.py: Demonstrates maintaining an email address file from the
                command line
                
@author: Jason M. Wolosonovich
"""
import configparser
from optparse import OptionParser
import shelve


config = configparser.RawConfigParser()
config.read('V:/workspace/Python3_Lesson12/src/addressbook.cfg')
shelf_location = config.get('database', 'file')

class InvalidEmail(Exception):
    pass

def validate_email(email):
    if '@' not in email:
        raise InvalidEmail("Invalid email: "+email)
    
    
def email_add(email):
    validate_email(email)
    shelf = shelve.open(shelf_location)
    if 'emails' not in shelf:
        shelf['emails'] = []
    emails = shelf['emails']
    if email in emails:
        message = False, "Email {0} already in the address book"\
                         .format(email)
    else:
        emails.append(email)
        message = True, "Email {0} added to the address book"\
                        .format(email)
    shelf['emails'] = emails
    shelf.close()
    return message

def email_delete(email):
    validate_email(email)
    shelf = shelve.open(shelf_location)
    if 'emails' not in shelf:
        shelf['emails'] = []
    emails = shelf['emails']
    try:
        emails.remove(email)
        message = True, "Email {0} removed from address book"\
                        .format(email)
    except ValueError:
        message = False, "Email {0} was not in the address book"\
                         .format(email)
    shelf['emails'] = emails
    shelf.close()
    return message


def email_display():
    shelf = shelve.open(shelf_location)
    emails = shelf['emails']
    shelf.close()
    text = ''
    for email in emails:
        text += email + '\n'
    return True, text


def main(options):
    """
    Routes the requests
    """
    if options.action == 'add':
        return email_add(options.email)
    elif options.action == 'delete':
        return email_delete(options.email)
    elif options.display == True:
        return email_display()
    

if __name__=="__main__":
    shelf = shelve.open(shelf_location)
    if 'emails' not in shelf:
        shelf['emails'] = []
    shelf.close()
    parser = OptionParser()
    parser.add_option('-a', 
                      '--action', 
                      dest="action", 
                      action="store",
                      help="requires -e option. Actions: add/delete")
    parser.add_option('-e',
                      '--email',
                      dest="email",
                      action="store",
                      help="email used in the -a option")
    parser.add_option('-d',
                      '--display',
                      dest="display",
                      type="int",
                      action="store",
                      help="show all emails limited by value")
    (options, args) = parser.parse_args()
    
    
    # validation routine
    if options.action and not options.email:
        parser.error("option -a requires option -e")
    elif options.email and not options.action:
        parser.error("option -e requires option -a")
    try:
        print(main(options)[1])
    except InvalidEmail:
        parser.error("option -e requires a valid email address")