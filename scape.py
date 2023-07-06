import datetime
import pandas as pd
import praw
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get the variables
client_id = os.getenv('CLIENT_ID')
secret_key = os.getenv('SECRET_KEY')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=secret_key,
                     user_agent='MyAPU/0.0.1',
                     username=username,
                     password=password)

subreddit_list = ['wearables', 'AppleWatch', 'GarminWatches']
df = pd.DataFrame()

for subreddit_name in subreddit_list:
    subreddit = reddit.subreddit(subreddit_name)
    for post in subreddit.new(limit=10000):
        post.comments.replace_more(limit=None)
        for comment in post.comments.list():
            df = df.append({
                'subreddit': subreddit_name,
                'title': post.title,
                'id': post.id,
                'url': post.url,
                'author': post.author.name if post.author else None,
                'score': post.score,
                'upvote_ratio': post.upvote_ratio,
                'num_comments': post.num_comments,
                'text': post.selftext,
                'flair': post.link_flair_text,
                'comment_id': comment.id,
                'comment_author': comment.author.name if comment.author else None,
                'comment_score': comment.score,
                'comment_text': comment.body,
                'post_date': datetime.datetime.fromtimestamp(post.created_utc),
                'comment_date': datetime.datetime.fromtimestamp(comment.created_utc)
            }, ignore_index=True)


df.to_csv('reddit_data.csv', index=False)
