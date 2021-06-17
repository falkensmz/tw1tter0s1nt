# complete tool with cmd line interface for more advanced users

# author : falkensmaze (c0m3t-k2)

import twint
from datetime import datetime
import os
import sys

print()
print(r"""████████╗██╗    ██╗ ██████╗ ███████╗██╗███╗   ██╗████████╗
╚══██╔══╝██║    ██║██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
   ██║   ██║ █╗ ██║██║   ██║███████╗██║██╔██╗ ██║   ██║   
   ██║   ██║███╗██║██║   ██║╚════██║██║██║╚██╗██║   ██║   
   ██║   ╚███╔███╔╝╚██████╔╝███████║██║██║ ╚████║   ██║   
   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   

@c0m3t-k2 / falkensmaze                                                          

""")
print("twosint - v. 2.0.0")
print()
username = input("twosint~# Before we start the investigation, please enter your target's username -> ")
print("twosint~# Please enter 'help' if you are stuck!")

def usernameSearch():
    today = datetime.now().strftime('%Y-%m-%d')

    c = twint.Config()
    c.To = username
    c.Since = today
    c.Followers = True
    c.Hide_output = True
    c.Store_object = True

    twint.run.Search(c)

    tweets = twint.output.tweets_list

    followers = []

    for tweet in tweets:
            followers.append(('{}'.format(tweet.username)))

    print(followers)

    for user in followers:
            c = twint.Config
            c.Username = user
            c.Limit = 18
    twint.run.Search(c)


def keyHunter():
    limit = input("twosint~# Enter a limit of tweets :")
    keyword = input("twosint~# Enter keyword : ")
    print("twosint~# Searching ...")
    c = twint.Config()
    c.Limit = limit
    c.Search = keyword
    twint.run.Search(c)

def mailHunter():
    print()
    print("twosint~# Gathering possible emails ...")
    print()
    
    c = twint.Config()
    c.Username = username
    c.Email = True
    twint.run.Search(c)

def numHunter():
    print()
    print("twosint~# Gathering possible phone numbers ...")
    print()

    c = twint.Config()
    c.Username = username
    c.Phone = True
    twint.run.Search(c)

def followHunter():
    print()
    limit = input("twosint~# Please enter a limit of followers : ")

    c = twint.Config()
    c.Username = username
    c.Followers == True
    c.Limit = limit
    c.User_full == True

    twint.run.Search(c)

def whoHunter():
    print()
    limit = input("twosint~# Please enter a limit of users : ")
    c = twint.Config()
    c.Username = username
    c.Limit = limit

    twint.run.Following(c)

def soloInvestigation():
    print()
    c = twint.Config()
    c.Username = username
    
    twint.run.Lookup(c)

def introduction():
    choice = input("twosint~# ")
    if choice == 'help':
        print(r"""
                    twosint - version 2.0.0
            
            modulebomb                  - shows all modules
            username                    - shows current set username
            set [module name]           - selects the specified module
        """)
        introduction()
    if choice == 'clear':
        os.system("clear")
    if choice == 'exit':
        print("twosint~# Exitting ...")
        quit()
    if choice == 'modulebomb':
        print()
        print(r"""
        
        0 - usernameSearch              [get usernames of your target's followers]
        1 - keyHunter                   [get tweets that only have your chosen keyword in them]
        2 - mailHunter                  [search for potential emails]
        3 - numHunter                   [search for potential phone numbers]
        4 - followHunter                [get a lot of information on target's followers]
        5 - whoHunter                   [who is your target following]
        6 - soloInvestigation           [get current stats and more on your tareget]
        
        """)
        print()
        introduction()
    if choice == 'username':
        print("twosint~#", username)
        introduction()
    if choice == 'set usernameSearch':
        print()
        usernameSearch()
    if choice == 'set keyHunter':
        print()
        keyHunter()
    if choice == 'set mailHunter':
        print()
        mailHunter()
    if choice == 'set numHunter':
        print()
        numHunter()
    if choice == 'set followHunter':
        print()
        followHunter()
    if choice == 'set whoHunter':
        print()
        whoHunter()
    if 'set soloInvestigation' in choice:
        print()
        print("twosint~# Running the soloInvestigation module ... ")
        soloInvestigation()
    else:
        introduction()

introduction()
