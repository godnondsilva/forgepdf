import app

# Initializing dotenv to read the .env file
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

if __name__ == '__main__':
    app.run()