import argparse
from fetch_data import RedditFetcher
from generate_persona import generate_persona, sanitize_persona_output, save_persona
import logging
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Reddit User Persona Generator")
    parser.add_argument('--username', type=str, required=True, help='Reddit username')
    parser.add_argument('--max_items', type=int, default=1000, help='Maximum number of posts/comments to fetch')

    args = parser.parse_args()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    user_agent = os.getenv("USER_AGENT")
    groq_api_key = os.getenv("GROQ_API_KEY")

    if not all([client_id, client_secret, user_agent, groq_api_key]):
        raise ValueError("Missing required API credentials. Ensure CLIENT_ID, CLIENT_SECRET, USER_AGENT, and GROQ_API_KEY are set in your .env file.")

    fetcher = RedditFetcher(client_id, client_secret, user_agent)
    data = fetcher.fetch_user_data(args.username, max_items=args.max_items)

    if not data:
        logging.warning(f"No data fetched for user {args.username}. Persona generation skipped.")
        return

    fetcher.save_data(data, f'user_data_{args.username}.json')

    persona = generate_persona(data, groq_api_key, args.username)
    persona_cleaned = sanitize_persona_output(persona)
    save_persona(persona, f'persona_output_{args.username}.txt')

if __name__ == "__main__":
    main()
