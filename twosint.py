# complete tool with cmd line interface for more advanced users

# author : falkensmaze (c0m3t-k2)

# project code name : coyote


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
print("twosint - v. 2.0.3")
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

def nearVan():
    print()
    c = twint.Config()
    c.Username = username
    
    city = input("twosint~# Enter the city -> ")

    c.Near = city

    twint.run.Search(c)

def cl0udchas3r():
    print()
    c = twint.Config()
    c.Username = username
    min_likes = int(input("twosint~# Minimum likes -> "))
    min_retweets = int(input("twosint~# Minimum retweets -> "))
    min_replies = int(input("twosint~# Minimum replies -> "))

    c.Min_likes = min_likes
    c.Min_retweets = min_retweets
    c.Min_replies = min_replies

    twint.run.Search(c)


def infoUsernameSearch():
    print(r"""
    usernameSearch - module number 0:
    This module allows you to gather the usernames of your
    target's followers. Just enter a limit to not crash the 
    program , and you are good to go!""")

def infoKeyHunter():
    print(r"""
    keyHunter - module number 1 :
    This module allows you to search for a specific word
    in your target's tweets. Enter the word and if everything
    goes as planned, you should gather your tweets.""")

def infoMailHunter():
    print(r"""
    mailHunter - module number 2 :
    This module allows you to gather possible emails from your
    target's tweets. The way it works is that it searches for
    specific keywords such as "email" or "mail" .""")

def infoNumHunter():
    print(r"""
    numHunter - module number 3 :
    This module allows you to gather possible phone numbers
    from your target's tweets. The way it works is that it
    searches for specific keywords such as "phone number" or
    "cellphone".""")

def infoFollowHunter():
    print(r"""
    followHunter - module number 4 :
    This module allows you to gather a lot of information on
    your target's followers. It uses a technique that firstly
    scrapes the target's followers usernames and then it investigates
    their profiles.""")

def infoWhoHunter():
    print(r"""
    whoHunter - module number 5 :
    This module allows you to gather the usernames of the 
    people that your target is following. Unlike followHunter,
    this module only scrapes the usernames and it does not
    investigate them!""")

def infoSoloInvestigation():
    print(r"""
    soloInvestigation - module number 6 :
    This module allow you to investigate your
    target by all means. It scrapes their bio, current tweets,
    followers , following etc. """)

def infoNearVan():
    print(r"""
    nearVan - module number 7
    This module allows you to scrape tweets that ONLY 
    have a specific city that you choose in them. For instance
    you choose New York, and the tweet(s) MUST have been tweeted
    in New York. The way this works is that it uses Geo-Coded tweets.
    So the target MUST have specified the city in the tweet(s)
    """)

def infoLink3r():
    print(r"""
    link3r - module number 8
    This module allows you to ONLY scrape tweets that have
    links in them. The way it works is that it only searches for
    tweets with links for instance 'look at this cool website my
    friend has developed -> http://example.com/skdw_?'
    """)

def infoCl0udChas3r():
    print(r"""
    cl0udchas3r - module number 9
    This module allows you to specify minimum likes,
    retweets and replies and with the information you
    provide it, it will try to gather the tweets that
    meet your requirements!
    """)

def introduction():
    choice = input("twosint~# ")
    if choice == 'help':
        print(r"""
                    twosint - version 2.0.3 Full Release
            
            version                     - displays current version
            clear                       - clears the screen
            exit                        - exit
            modulebomb                  - shows all modules
            username                    - shows current set username
            run [module name / module number]  - runs the chosen module
            info [module name / module number] - get more information on a specified module
        """)
        introduction()
    if choice == 'version':
        print("twosint~# twosint - version 2.0.3 ")
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
        7 - nearVan                     [scrape tweets near a city you specify]
        8 - link3R                      [scrape tweets that have links in them] {NOT RELEASED}
        9 - cl0udchas3r                 [scrape tweets with minimum likes/retweets/replies]
        """)
        print()
        introduction()
    if choice == 'username':
        print("twosint~#", username)
        introduction()
    if choice == 'run usernameSearch' or choice == 'run 0':
        print()
        usernameSearch()
    if choice == 'run 1' or choice == 'run keyHunter':
        print()
        keyHunter()
    if choice == 'run 2' or choice == 'run mailHunter':
        print()
        mailHunter()
    if choice == 'run 3' or choice == 'run numHunter':
        print()
        numHunter()
    if choice == 'run 4' or choice == 'run followHunter':
        print()
        followHunter()
    if choice == 'run 5' or choice == 'run whoHunter':
        print()
        whoHunter()
    if choice == 'run 6' or choice == 'run soloInvestigation':
        print()
        print("twosint~# Running the soloInvestigation module ... ")
        soloInvestigation()
    if choice == 'run 7' or choice == 'run nearVan':
        print()
        nearVan()
    if choice == 'run 8' or choice == 'run link3r':
        print()
        print("twosint~# This module is still in development")
        print()
    if choice == 'run 9' or choice == 'run cl0udchas3r':
        print()
        cl0udchas3r()
        print()
    if choice == 'info 0' or choice == 'info usernameSearch':
    	print()
    	infoUsernameSearch()
    	print()
    if choice == 'info 1' or choice == 'info keyHunter':
    	print()
    	infoKeyHunter()
    	print()
    if choice == 'info 2' or choice == 'info mailHunter':
    	print()
    	infoMailHunter()
    	print()
    if choice == 'info 3' or choice == 'info numHunter':
    	print()
    	infoNumHunter()
    	print()
    if choice == 'info 4' or choice == 'info followHunter':
    	print()
    	infoFollowHunter()
    	print()
    if choice == 'info 5' or choice == 'info whoHunter':
    	print()
    	infoWhoHunter()
    	print()
    if choice == 'info 6' or choice == 'info soloInvestigation':
    	print()
    	infoSoloInvestigation()
    	print()
    if choice == 'info 7' or choice == 'info nearVan':
        print()
        infoNearVan()
        print()
    if choice == 'info 8' or choice == 'info link3r':
        print()
        print("twosint~# This module is still in development ... ")
        print()
    if choice == 'info 9' or choice == 'info cl0udchas3r':
        print()
        infoCl0udChas3r()
        print()
    else:
        introduction()

introduction()
