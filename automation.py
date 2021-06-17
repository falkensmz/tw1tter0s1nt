import twint
from datetime import datetime


print("")
print("")
print("Automation tool for twosint 2.0 (old version --> tw1tter0s1nt )")
print("")
print("")

username = input("osinter@tw1tter0s1nt #> Enter your target's name : ")

print("")
print("1 - Only the usernames of", username, "'s followers")
print("2 - Custom keyword found in tweet(s)")
print("3 - Search for potential emails")
print("4 - Search for potential numbers")
print("5 - Pull all the followers from", username, " + a lot of information on them")
print("6 - Who is", username, "following?")
print("7 - Get more information on", username, "")
print("8 - Filter", username, "'s tweets by media")
print("9 - Filter results by minimum likes ")
print("10 - Search for geo-coded tweets by", username, "(Still in development)")
print("11 - Search tweets that were posted near a city you specify")
print("12 - What are", username, "'s stats? [Retweets, likes, folowers etc. ]")
print("")
print("osinter@tw1tter0s1nt #> Message from c0m3t-k2 ---> You may find bugs with option 10 since it just got released. Anything goes wrong, contact me on Github!")
print("")

choice = input("osinter@tw1tter0s1nt #> What would you like to search? :")

if choice == '1':
    limit111 = input("osinter@tw1tter0s1nt #> Enter a limit of tweets right here: ")
    today = datetime.now().strftime('%Y-%m-%d')

    c = twint.Config()
    c.To = username
    c.Limit = limit111
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

if choice == '2':
    search = input("osinter@tw1tter0s1nt #> Enter your SPECIAL keyword here: ")
    limit1 = input("osinter@tw1tter0s1nt #> Enter a limit of tweets: ")
    option = input("osinter@tw1tter0s1nt #> Would you like to specify a city where a possible tweet has been made?(y/n) : ")
    if option == 'y':
        city = input("osinter@tw1tter0s1nt #> Enter the city right here : ")
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
elif choice == '3':
    limit2 = input("osinter@tw1tter0s1nt #> Enter a limit of tweets right here: ")
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

elif choice == '4':
    limit3 = input("osinter@tw1tter0s1nt #> Enter a limit of tweets right here: ")
    print("osinter@tw1tter0s1nt #> pulling all the tweets that have the keyword 'phone' in it")
    c = twint.Config()
    c.Username = username
    c.Limit = limit3
    c.Phone = True
    twint.run.Search(c)
elif choice == '5':
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
elif choice == '6':
    # not 100% working, still trying to fix some bugs
    limit222 = input("osinter@tw1tter0s1nt #> Enter a limit of users : ")
    print("")
    print("coded by c0m3t-k2")
    print("Github page : https://github.com/c0m3t-k2/tw1tter0s1nt")
    print("")
    print("")
    c = twint.Config()
    c.Username = username
    c.Limit = limit222

    twint.run.Following(c)
elif choice == '7':
    c = twint.Config()
    c.Username = username

    twint.run.Lookup(c)
elif choice == '8':
    limit444 = input("osinter@tw1tter0s1nt #> Enter a limit for the tweets: ")
    c = twint.Config()
    c.Username = username
    c.Limit = limit444
    c.Media == True

    twint.run.Search(c)
elif choice == '9':
    special_keyword = input("osinter@tw1tter0s1nt #> What would you like to search for? : ")
    min_likes = input("osinter@tw1tter0s1nt #> Specify the minimum likes of a tweet : ")
    limit555 = input("osinter@tw1tter0s1nt #> And finally enter the limit of tweets here  :")
    c = twint.Config()
    c.Username = username
    c.Limit = limit555
    c.Min_likes = min_likes

    twint.run.Search(c)
elif choice == '10':
    print("osinter@tw1tter0s1nt #> This option is still in development! ")
elif choice == '11':
    print("osinter@tw1tter0s1nt #> Roger that!")
    near_city = input("osinter@tw1tter0s1nt #> Choose a city : ")
    limit777 = input("osinter@tw1tter0s1nt #> Input the limit right here : ")
    c = twint.Config()
    c.Username = username
    c.Limit = limit777
    c.Near = near_city
    twint.run.Search(c)
elif choice == '12':
    print("osinter@tw1tter0s1nt #> Alright!")
    limit_wish = input("osinter@tw1tter0s1nt #> Do you wish to enter a limit? (y/N)")
    if limit_wish == 'y' or 'Y' or 'yes' or 'YES':
        limit000 = input('osinter@tw1tter0s1nt #> Roger that! Enter the limit right here : ')
        c = twint.Config()
        c.Username = username
        c.Limit = limit000
        c.Stats = True
        twint.run.Search(c)
    else:
        print('osinter@tw1tter0s1nt #> Understood! Scraping all of', username, "'s stats")
        c = twint.Config()
        c.Username = username
        c.Stats = True
        twint.run.Search(c)

# Made with love by c0m3t-k2
# If you are seeing this. Thank you for peeking into the source code. If you find anything out of the ordinary or have better ideas, contact me!
