import sys
import os
from decouple import config
from github import Github

USER = config('GIT_USER')
TOKEN=config('TOKEN')

def start_repo():
    project_name = sys.argv[1]
    user = Github(USER, TOKEN).get_user()

    try:
        user.create_repo(project_name)

    except Exception:
        print(Exception)

    finally:
        print("Successfully created repository!")

    return
    
if __name__ == "__main__":
    start_repo()
