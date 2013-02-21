'''

Challenge #5.

Your challenge for today is to create a program which is password protected, and
wont open unless the correct user and password is given.
For extra credit, have the user and password in a seperate .txt file.
for even more extra credit, break into your own program :)

'''

import hashlib
import os

def check_authorisation(username, password):

    user_pw_file = open('/home/associat/h/hauk/bots/DailyProgrammer/tmp/users.txt', 'r')

    for i in user_pw_file.readlines():

        if( len(i.split()) > 1):
            user_details = i.split()

            if(user_details[0] == username and user_details[1] == password):

                user_pw_file.close()
                return True

    user_pw_file.close()
    return False

def sys_login():

    print("Welcome to the magical system! Please login to continue.")

    user = input("Enter your username: ")
    password = input("Enter your password: ")

    print("Verifying login...")

    pwhash = hashlib.sha1(password.encode('utf-8'))

    if(check_authorisation(user, pwhash.hexdigest()) == True):
       print("You are now verified... Loading secret modules...")
    else:
       print("You are TOTES unauthorised. GTFO.")

def add_user():

    user = input("Enter a new username: ")
    password = input("Please enter a new password: ")
    confirm_pw = input("Please confirm your new password: ")

    if(password == confirm_pw):
        pwhash = hashlib.sha1(password.encode('utf-8'))

        user_store = open('/home/associat/h/hauk/bots/DailyProgrammer/tmp/users.txt', 'at', encoding='utf-8')

        user_store.write(user + " " + (pwhash.hexdigest()) + '\n')

        user_store.close()

#add_user()

check_authorisation("eoghan", "blah")

sys_login()
