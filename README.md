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
[Reddit App]((https://ssl.reddit.com/prefs/apps/)
Click the link
Go down and click "are you a developer? Create an app"
Give it a name
Select script
for redirect url, you can use this github page as the redirect url. It doen't matter

### A way to run the script 24/7 
If you don't have a device to run the script 24/7, consider checking out pythonanywhere.com
Click "create app"
Grab the fancy looking ids and keep them somewhere safe to use in the script
<img width="964" alt="Screenshot 2023-05-08 at 12 05 46 PM" src="https://user-images.githubusercontent.com/112908676/236886306-2466303c-717f-4b03-822e-fec18e52944d.png">



## How to set up
1) Download the python script
2) Make a text file in the same location as the script. It is recommended you put the script and text file into 1 dedicated folder for the script. Make sure to put the config file in the same folder also
3) Rename the text file as *comments_replied_to.txt*
4) Grab the path to the text file
5) Open up the python script in a code editor like VSCode or IDLE
6) On line *41*, change **path = "ADD PATH FILE HERE"** to include your path
For example **path = "C:\\Users\\wondows 101\\Desktop\\m!pin\\comments_replied_to.txt"**
7) On line 68, change **SUBREDDIT** to the subreddit of your choice
8) If you followed the instructions up above where it tells you how to make a reddit bot, then good. Open the config file in a code editor
9) change the following to the proper details
username = "reddit username here"
password = "reddit account password here"
client_id = "PUT ID HERE"
client_secret = "PUT SECRET HERE"

Save all the files.
Run main.py and enjoy!




This code was partially made with Chatgpt-4. We are accepting improved edits to the code so we can make it more efficent or just have an additional features. 
