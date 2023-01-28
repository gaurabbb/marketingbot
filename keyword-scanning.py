import praw
import datetime

# Set the credentials for the Reddit API
reddit = praw.Reddit(client_id='g_RupeeKDZD2Xski9M1tAg',
                     client_secret='sEFfj-RItJ6OADuHrasj4xNFHkbpTQ',
                     user_agent='gorabb-personal_use_script/1.0')

# Specify the two subreddits to search
subreddit1 = reddit.subreddit("Entrepreneur")
subreddit2 = reddit.subreddit("hyperstress")

# Get the current time
now = datetime.datetime.now()
collection = []
# Get the new posts and comments from the first subreddit
print("New posts and comments from subreddit1:")
for submission in subreddit1.new(limit=None):
    if (now - submission.created_utc).total_seconds() < 86400:
        collection.append([submission.title, submission.author.selftext, submission.author])
        print("Post title:", submission.title)
        print("Author:", submission.author)
        print("Comment:", submission.selftext)
        print("\n")
    for comment in submission.comments:
        if (now - comment.created_utc).total_seconds() < 86400:
            print("Author:", comment.author)
            print("Comment:", comment.body)
            print("\n")

# Get the new posts and comments from the second subreddit
print("New posts and comments from subreddit2:")
for submission in subreddit2.new(limit=None):
    if (now - submission.created_utc).total_seconds() < 86400:
        
        print("Post title:", submission.title)
        print("Author:", submission.author)
        print("Comment:", submission.selftext)
        print("\n")
    for comment in submission.comments:
        if (now - comment.created_utc).total_seconds() < 86400:
            print("Author:", comment.author)
            print("Comment:", comment.body)
            print("\n")