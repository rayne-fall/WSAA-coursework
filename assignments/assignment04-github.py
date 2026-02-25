# Assignment 4: Github
# Author: Sylvia Chapman Kent
# Imports a file from a private repository, replaces the word "Andrew" with the word "Sylvia" and commits the changes

import requests
from config import apikeys as cfg
from github import Github

# import API key from config file
apikey=cfg["github"]
# provide authorisation and access private repository
account=Github(apikey)
repo=account.get_repo('rayne-fall/aprivateone')
# retrieve text file we want to use
file_path="andrew.txt"
file=repo.get_contents(file_path)
url=file.download_url
response=requests.get(url)
contents=response.text
# put contents of text file into local file
replacement_text='replace_text.txt'
with open (replacement_text,'w') as r_file:
    r_file.write(contents)
# replace the word Andrew with the word Sylvia
with open (replacement_text, 'r') as new_r_file:
    new_data=new_r_file.read().replace("Andrew", "Sylvia")
# add the changes to the file
with open (replacement_text, 'w') as text:
    new_text=text.write(new_data)
# commit and push the changed file
repo.update_file(
    path=file_path,
    message='Replaced Andrew with Sylvia',
    content=new_text,
    sha=file.sha
    )
print("Andrew has been replaced")

# 1. https://www.youtube.com/watch?v=ZOzYjv_BZeg (how to update a file on github in python using PyGithub - Computer Wizard)
# 2. https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file