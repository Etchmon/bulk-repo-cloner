import requests
import json
import git
import os

# Replace with your GitHub username and personal access token
username = 'your_github_username'
token = 'your_personal_access_token'

# API URL to fetch repositories for a user
url = f'https://api.github.com/users/{username}/repos'

# Make the API request to fetch repositories
response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    repos = response.json()
    with open('repos.json', 'w') as f:
        json.dump(repos, f, indent=2)
    print("Repository list saved to repos.json")
else:
    print(f"Failed to fetch repositories: {response.status_code}")

# Load the list of repositories from the saved file
with open('repos.json') as f:
    repos = json.load(f)

# Directory where you want to clone the repos
clone_dir = 'cloned_repos'

# Create the directory if it doesn't exist
if not os.path.exists(clone_dir):
    os.makedirs(clone_dir)

# Clone each repository
for repo in repos:
    repo_name = repo['name']
    clone_url = repo['clone_url']
    repo_path = os.path.join(clone_dir, repo_name)
    
    if not os.path.exists(repo_path):
        print(f'Cloning {repo_name}...')
        git.Repo.clone_from(clone_url, repo_path)
    else:
        print(f'Repo {repo_name} already cloned.')

print("All repositories have been cloned.")
