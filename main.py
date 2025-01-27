from dotenv import load_dotenv
import os

def main():
    load_dotenv(dotenv_path='local.env') # Load .env variables from the file
    api_key = os.getenv('API_KEY') # Access the API key
    print(api_key)

main()