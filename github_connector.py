import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

def connect_github():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN is not set in the environment variables.")
    
    gh = Github(token)

    user = gh.get_user()
    print(f"Connected to GitHub as {user.login}")

    return gh