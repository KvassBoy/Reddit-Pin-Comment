### Reddit-Pin-Comment
A light, python based script that was designed to allow regular reddit users to pin comments on their reddit post


### How does it work?
The python script will repeatedly scan a subreddit(s) of your choice and look for a specific command. By default the command is "m!pin"
Any message after the "m!pin" command will be extracted, then commented by the reddit bot and then it will pin its own comment.

It will only pin a comment if the person who is using the command also made the post that they are commenting on.
For example, if u/python_child uses "m!pin Howdy" on u/cat_mans post, the script won't execute the command
But, if u/python_child uses "m!pin Howdy" on his own post, the script will execute the command
![0q7v109kaixa1](https://user-images.githubusercontent.com/112908676/236886714-34bea20c-2cef-4909-9d62-d514233aaf11.jpeg)


## What do I need for this script
### Python installed
https://www.python.org/downloads/

### Install PRAW
Open up command prompt/terminal
use the command
**pip install praw**

### A reddit bot account
https://ssl.reddit.com/prefs/apps/

Click the link

Go down and click "are you a developer? Create an app"

Give it a name

Select script

for redirect url, you can use this github page as the redirect url. It doesn't matter

### A way to run the script 24/7 
If you don't have a device to run the script 24/7, consider checking out pythonanywhere.com

Click "create app"

Grab the fancy looking ids and keep them somewhere safe to use in the script

<img width="964" alt="Screenshot 2023-05-08 at 12 05 46 PM" src="https://user-images.githubusercontent.com/112908676/236886306-2466303c-717f-4b03-822e-fec18e52944d.png">



## How to set up
1) Download the python script
2) Open the script up and add in the details that it requests in the config on line 18 to line 22
    client_id='CLIENT ID HERE',
    client_secret='CLIENT SECRET HERE',
    username='USERNAME HERE',
    password='PASSWORD HERE',
3) Add the subreddit you want to target on line 27. Make sure the bot has moderation permissions on this subreddit
    subreddit = reddit.subreddit('SUBREDDIT HERE')

4) All done, the bot should run. Please make sure to run it in a dedicated folder or directory. The script will make a text file in the same directory/folder it runs in to keep track of comments it already replied to. If you delete this file or run the script in a folder/directory without this txt file, it could repeat the pin action to comments it has already seen.

## Notes for moderators:
The bot needs to be a moderator on the subreddit you plan to use it on

You can change the commanmd via changing "m!pin" to whatever throughout the script



This code was made with Chatgpt-4. We are accepting improved edits to the code so we can make it more efficent or just have an additional features. Thank you for your time and I hope you enjoy this!

I am accepting feature requests


## Extra

Thank you to the following people for helping. You guys are awesome and deserve some cookies :D
Go check them out!

https://github.com/JReesW

https://github.com/RDSSDR
