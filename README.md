# Subreddit Recomendatior
This program generates custom subreddit recomendations acording to your Google Chrome history

.
## Before using the script, you need to create your own Reddit App, and enter the Client ID and the secret token in the specified section of the code. Click [here](https://www.reddit.com/prefs/apps) to create it. Also, make sure to fill in all the details inside the python file, like the path to your History file or the details of your reddit aplication (line 12 and line 82)
.

## How it works
This script creates a CSV with the titles of the webpages that appears in your Google Chrome history and finds subreddits that you may like/be interested in. 

## Requisites:

PRAW

    pip install praw
    
## Installing

- Download or clone the repository.
- Install the requirements in "requirements.txt"
- Execute the main.py Python file (with launcher.bat or witht any other prefered method)
- A command prompt window should appear.

## Error solutions:
- Make sure that Google Chrome is not running.
- Make sure that the path of your Google Chrome History file is correct. (line 12)
- Make sure your reddit aplication info is correct (line 82) 
- Check if all the libraries are installed.


## How to use:
- Create a reddit application (mentioned above)
- Fill in all the information inside the source code
- Execute the script (a command prompt window should appear)
- Wait until the progress bar finishes loading
- Open the txt file and see if there's any subreddit you like

### Works for sure on:

- Windows 10 with Python 3.9
