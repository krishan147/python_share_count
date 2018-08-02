import tweepy
import json
import pyodbc
import requests
import datetime
import time

print ("modules ran fine")

# Connect to ACHIM_and tables


# Twitter credentials

ct = client token
cs = client secret
at = access token
acs = access secret
auth = tweepy.OAuthHandler(ct,cs)
auth.set_access_token(at,acs)
api  = tweepy.API(auth)

# Facebook credentials

app_key = "app key"

# Pull feeds from ACHIM_CONTENT



print ("getting content_link...")

for row_achim_content in rows_achim_content:
    feed_id = row_achim_content[0]
    feed_name = row_achim_content[1]
    feed_url = row_achim_content[2]
    content_article_id = row_achim_content[3]
    content_creator = row_achim_content[4]
    content_name = row_achim_content[5]
    content_pubdate = row_achim_content[6]
    content_link = row_achim_content[7]
    content_id = row_achim_content[8]
    do_we_have_share_data_on_this_article = row_achim_content[9]
    last_updated =  datetime.datetime.now()

    print ("checking this link", content_link)

    content_link_dash = content_link + "/"

# Facebook shares + comments
    try:
        facebook = "https://graph.facebook.com/?ids=" + content_link_dash + "&accesstoken=" + app_key #this line isnt actually using the app key
        print (facebook)

        fb_request = requests.get(facebook)
        fb_datas = fb_request.json()
        fb_datas = (next (iter(fb_datas.values())))
        fb_shares = fb_datas["share"]["share_count"]
        fb_comment = fb_datas["share"]["comment_count"]

        print("facebook shares", fb_shares)
        print("facebook comments", fb_comment)
    except KeyError:
        print ("facebook share fail")
        pass

# Linkedin shares

    linkedin ="https://www.linkedin.com/countserv/count/share?url=" + content_link + "&format=json"
    linkedin_request = requests.get(linkedin)
    linkedin_datas = linkedin_request.json()
    linkedin_shares = linkedin_datas["count"]



    print ("linkedin shares", linkedin_shares)

# Twitter shares

    twitter_fetch = api.search(q=content_link)
    twitter_fetch_string = str(twitter_fetch)

    print (twitter_fetch_string)

    twitter_shares = 0

    time.sleep(40)

# Twitter meta-data

    for items in twitter_fetch:
        item = (items._json)
        tweet_id = item["id"]
        shared_date = item["created_at"]
        format = "%a %b %d %X %z %Y"
        new_format = '%Y-%m-%d %H:%M:%S'
        content_published = datetime.datetime.strptime(shared_date, format).strftime(new_format)

        tweet = item["text"]
        twitter_id = item["user"]["id"]
        follower_count = item["user"]["followers_count"]
        name = item["user"]["name"]
        location = item["user"]["location"]
        twitter_handle = item["user"]["screen_name"]
        twitter_bio = item["user"]["description"]
        tweet_url = "https://twitter.com/"+twitter_handle+"/status/"+ str(tweet_id)

        twitter_shares = twitter_shares + 1


    time.sleep(2)



    print("twitter shares", twitter_shares)

    # Update ACHIM_CONTENT that shares is being updated

    time.sleep(2)

    yes = "yes"

    print("We have marked it as checked", content_link)



