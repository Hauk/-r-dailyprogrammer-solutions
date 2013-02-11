"""
Challenge #1.

Challenge Description:

Create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:

        Your name is (blank), you are (blank) years old, and your username is (blank).

For extra credit, have the program log this information in a file to be accessed later.

"""

name = input("What is your name?: ")
age = input("Whatis your age?: ") 
reddit_user = input("What is your Reddit user name?: ")

print("Your name is " + name + ". You are " + age + " years old, and your username is "  + reddit_user + ".")

#Extra credit.

store_it = open('/home/associat/h/hauk/bots/DailyProgrammer/tmp/store_it.txt', 'w')

store_it.write(name + '\n')
store_it.write(age + '\n')
store_it.write(reddit_user + '\n')

store_it.close()

get_it = open('/home/associat/h/hauk/bots/DailyProgrammer/tmp/store_it.txt', 'r')

for i in get_it.readlines():
    print(str(i.rstrip()))
