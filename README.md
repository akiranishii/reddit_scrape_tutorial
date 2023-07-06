# Reddit Scraper

This Python script is a Reddit scraper that uses PRAW (Python Reddit API Wrapper) to fetch data from specified subreddits. The script fetches the most recent posts and comments from the subreddits and stores them in a CSV file.

## Prerequisites

You will need the following to run this script:

- Python 3.6 or later
- Python packages as listed in `requirements.txt`
- Reddit "app" credentials (client ID, client secret, username, and password)

## Installation

To set up your environment to run this script, follow these steps:

1. Clone this repository to your local machine.

    ```
    git clone git@github.com:akiranishii/reddit_scrape_tutorial.git
    ```

2. Navigate to the cloned directory.

    ```
    cd <directory-name>
    ```

3. Set up a virtual environment (optional but recommended).

    ```
    python -m venv env
    source env/bin/activate  # For Unix or MacOS
    .\env\Scripts\activate   # For Windows
    ```

4. Install the required Python packages.

    ```
    pip install -r requirements.txt
    ```

## Usage

Before running the script, ensure that you've set up your Reddit app credentials in the `.env` file. Replace the placeholder values with your actual credentials:


``` python

CLIENT_ID=<your-client-id>
SECRET_KEY=<your-secret-key>
USERNAME=<your-username>
PASSWORD=<your-password>

```


Once you've set up your credentials, you can run the script:

```

python scrape.py

```


By default, the script will scrape data from the 'wearables', 'AppleWatch', and 'GarminWatches' subreddits. You can customize the list of subreddits in the `reddit_scraper.py` script.

The script will create a `reddit_data.csv` file in the same directory, containing the scraped data.

## Data Format

The data in the CSV file will have the following columns:

- subreddit: the name of the subreddit
- title: the title of the post
- id: the ID of the post
- url: the URL of the post
- author: the author of the post
- score: the score of the post
- upvote_ratio: the upvote ratio of the post
- num_comments: the number of comments on the post
- text: the text of the post
- flair: the flair of the post
- comment_id: the ID of the comment
- comment_author: the author of the comment
- comment_score: the score of the comment
- comment_text: the text of the comment
- post_date: the date and time when the post was created
- comment_date: the date and time when the comment was created


## Reddit App Setup

Before running the script, you need to create a Reddit "app" to get the necessary credentials. 

Here's how to do that:

1. First, if you do not already have a Reddit account, [create one](https://www.reddit.com/register/).

2. Once you have your Reddit account, go to [Reddit App Preferences](https://www.reddit.com/prefs/apps).

3. Scroll down to the "Developed Applications" section and click the "Create App" or "Create Another App" button.

4. Fill out the form as follows:

    - **name**: Enter a name for your app.
    - **App type**: Select "script".
    - **description**: Enter a description for your app (optional).
    - **about url**: Enter a URL where users can learn more about your app (optional).
    - **redirect uri**: Enter "http://localhost:8000" (without quotes).

5. Click the "Create app" button.

After the app is created, you'll see a section for your new app, which includes the following information:

- **client_id**: This is the ID under "personal use script".
- **client_secret**: This is the ID next to the word "secret".

## Environmental Variables Setup

The script uses the following environmental variables:

- `CLIENT_ID`: Your Reddit app's client ID.
- `SECRET_KEY`: Your Reddit app's client secret.
- `USERNAME`: Your Reddit account's username.
- `PASSWORD`: Your Reddit account's password.

You should store these in a `.env` file in the same directory as the script. Your `.env` file should look something like this:

```env
CLIENT_ID=<your-client-id>
SECRET_KEY=<your-secret-key>
USERNAME=<your-username>
PASSWORD=<your-password>
```

Replace <your-client-id>, <your-secret-key>, <your-username>, and <your-password> with your actual credentials.

Once you've set up your .env file, you can run the script as described in the Usage section.

## Configuration

The script is currently configured to fetch the 100 most recent posts from each specified subreddit. If you wish to fetch more or less posts, you can change the `limit` parameter in the following line of code:

```python
for post in subreddit.new(limit=100):
```

Just replace 100 with the number of posts you wish to fetch. For example, if you want to fetch the 500 most recent posts, the line would look like this:

```python
for post in subreddit.new(limit=500):
```

Note: Keep in mind that fetching more posts will take more time and may be rate-limited by Reddit.
