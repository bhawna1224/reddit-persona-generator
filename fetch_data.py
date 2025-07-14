import praw
import logging
import time
import json
from prawcore.exceptions import NotFound, Forbidden

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RedditFetcher:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(client_id=client_id,
                                  client_secret=client_secret,
                                  user_agent=user_agent)

    def fetch_user_data(self, username, max_items=1000):
        logging.info(f"Fetching data for user: {username}")

        try:
            user = self.reddit.redditor(username)
            _ = user.id

            data = []
            count = 0

            for comment in user.comments.new(limit=None):
                data.append({
                    'type': 'comment',
                    'body': comment.body,
                    'permalink': f"https://www.reddit.com{comment.permalink}"
                })
                count += 1
                if count >= max_items:
                    break
                time.sleep(0.1)

            for submission in user.submissions.new(limit=None):
                data.append({
                    'type': 'submission',
                    'title': submission.title,
                    'selftext': submission.selftext,
                    'permalink': f"https://www.reddit.com{submission.permalink}"
                })
                count += 1
                if count >= max_items:
                    break
                time.sleep(0.1)

            if not data:
                logging.warning(f"User '{username}' exists but has no posts or comments.")
                return None

            logging.info(f"Fetched {len(data)} items from user '{username}'.")
            return data

        except NotFound:
            logging.warning(f"User '{username}' does not exist or account is deleted.")
            return None

        except Forbidden:
            logging.warning(f"User '{username}' is suspended, shadowbanned, or inaccessible.")
            return None

        except Exception as e:
            logging.error(f"Unexpected error fetching data for '{username}': {str(e)}")
            return None

    def save_data(self, data, output_path):
        if data:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            logging.info(f"Data saved to {output_path}")
        else:
            logging.warning("No data to save. Skipping file write.")

