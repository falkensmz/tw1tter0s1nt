import twint
from datetime import datetime


print("tw1tter0s1nt - A tool for Penetration Testers and Ethical Hacking students")
print("")
print("tw1tter0s1nt is a twint based OSiNT tool for investigations on Twitter!")
print("This python script makes it much easier to use twint!")
print("Developer --> c0m3t-k2")
print("Github page --> https://github.com/c0m3t-k2/tw1tter0s1nt")
print("tw1tter0s1nt --version 1.0 ")
print("")
print("")
print("")

username = input("osinter@tw1tter0s1nt > Enter your target's name : ")

print("1 - Only the usernames of", username, "'s followers")
print("2 - Custom keyword found in tweet(s)")
print("3 - Search for potential emails")
print("4 - Search for potential numbers")
print("5 - Pull all the followers from", username, " + a lot of information on them")
print("")
print("")

choice = input("osinter@tw1tter0s1nt > What would you like to search? :")

if choice == '1':
    today = datetime.now().strftime('%Y-%m-%d')

    c = twint.Config()
    c.To = username
    c.Since = today
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

if choice == '2':
    search = input("osinter@tw1tter0s1nt > Enter your SPECIAL keyword here: ")
    limit1 = input("osinter@tw1tter0s1nt > Enter a limit of tweets: ")
    option = input("osinter@tw1tter0s1nt > Would you like to specify a city where a possible tweet has been made?(y/n) : ")
    if option == 'y':
        city = input("osinter@tw1tter0s1nt > Enter the city right here : ")
        c = twint.Config()
        c.Search = search
        c.Near = city
        c.Limit = limit1
        c.Popular_tweets = True
        twint.run.Search(c)
    else:
        print("Alright...searching")
        c = twint.Config()
        c.Search = search
        c.Limit = limit1
        c.Popular_tweets == True
        twint.run.Search(c)
if choice == '3':
	print("grabbing all the emails that", username, "has included in their tweets.....")
	print("")
	print("")
	print("coded by c0m3t")
	print("")
	print("")
	c = twint.Config()
	c.Username = username
	c.Email = True
	twint.run.Search(c)
if choice == '4':
	print("pulling all the tweets that have the keyword 'phone' in it")
	c = twint.Config()
	c.Username = username
	c.Phone = True
	twint.run.Search(c)
if choice == '5':
    limit = input("Enter a limit of followers otherwise the program might crash or there will be too many users: ")
    print("")
    print("coded by c0m3t")
    print("")
    c = twint.Config()
    c.Username = username
    c.Followers == True
    c.Limit = limit
    c.User_full == True

    twint.run.Search(c)
