import praw
import config
import time
import os
full_path = os.path.abspath(__file__)
dir_path = os.path.dirname(full_path)
praw_dest_path = os.path.join(dir_path, 'praw.ini')

praw_ini = """[DEFAULT]
# A boolean to indicate whether or not to check for package updates.
check_for_updates=True

# Object to kind mappings
comment_kind=t1
message_kind=t4
redditor_kind=t2
submission_kind=t3
subreddit_kind=t5
trophy_kind=t6

# The URL prefix for OAuth-related requests.
oauth_url=https://oauth.reddit.com

# The amount of seconds of ratelimit to sleep for upon encountering a specific type of 429 error.
ratelimit_seconds=5

# The URL prefix for regular requests.
reddit_url=https://www.reddit.com

# The URL prefix for short URLs.
short_url=https://redd.it

# The timeout for requests to Reddit in number of seconds
timeout=16
"""

if not os.path.exists(praw_dest_path):
    with open(praw_dest_path, "w") as f:
        f.write(praw_ini)

path = "ADD PATH FILE HERE" #path to comment file
ignored_users = ["automoderator", "DuplicateDestroyer"]

def bot_login():
	print("Logging in...")
	r = praw.Reddit(username = config.username,
	password = config.password,
	client_id = config.client_id,
	client_secret = config.client_secret,
	user_agent = "The Reddit commenter v1.0",
	check_for_updates=False,
	comment_kind="t1",
	message_kind="t4",
	redditor_kind="t2",
	submission_kind="t3",
	subreddit_kind="t5",
	trophy_kind="t6",
	oauth_url="https://oauth.reddit.com",
	reddit_url="https://www.reddit.com",
	short_url="https://redd.it",
	ratelimit_seconds=600,
	timeout=16)
	print("Logged in!")
	return r

def run_bot(r):
	print("Searching last 10000000000000 comments")
	target = "SUBREDDIT"
	#target = "test+"
	targets = target.split("+")
	while("" in targets):
		targets.remove("")
	for i in range(len(targets)):
		print(f"current target r/{targets[i]}")
		for comment in r.subreddit(targets[i]).comments(limit=5_000_000_000_000):
			try:
				txt = comment.body.lower()
				if comment.author is not None:
					a = comment.author.name.lower()
					if any([entry.lower() == a for entry in ignored_users]):
						continue
			except Exception as e:
				print(e)
			else:
				try:
					############
					if "m!pin" in txt and comment.id not in comments_replied_to and comment.author != r.user.me():
						print(f"String with \"m!pin\" found in comment {comment.id} by {comment.author}")
						if comment.author == comment.submission.author:
							try:
								reply_text = txt.split('m!pin', 1)[1].strip()
								if reply_text:
									reply = comment.submission.reply(reply_text)
									reply.mod.distinguish(how='yes', sticky=True)
									reply.report(reason='Pinned comment. Please review')
									comments_replied_to.append(comment.id)
								else:
									print("No text to reply with")
							except Exception as e:
								print(e)
								comments_replied_to.append(comment.id)
							with open(path,'a') as f:
								f.write(comment.id + "\n")
						else:
							comments_replied_to.append(comment.id)
							print("Replied to comment " + comment.id)
							with open(path,'a') as f:
								f.write(comment.id + "\n")
				except Exception as e:
					print(e)

print("Search Completed.")
print("Sleeping for 2000 seconds...") #Sleep for 2000 seconds...
time.sleep(10)

def get_saved_comments():
	with open(path, "r") as f:
		comments_replied_to = f.read()
		comments_replied_to = comments_replied_to.split("\n")
	return comments_replied_to

comments_replied_to = get_saved_comments()

while True:
	try:
		r = bot_login()
	except Exception as e:
		print(e)
		print("\n\nCouldnt login")
	else:
		run_bot(r)
