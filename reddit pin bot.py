import os
import praw
import time
import prawcore

# ADD THE INFORMATION NEEDED FROM LINE 14 TO 18 AND SUBREDDIT TO TARGET ON LINE 23. You can adjust the command used via changing "m!pin" throughout the script to whatever command you want to use. Please use the script properly and respect Reddits API limit

# This is all you need to do. Enjoy and please don't be afraid to send suggestions, push improved code to me or report an issue!


# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Join it with the filename
file_path = os.path.join(script_dir, 'processed_comments.txt')

reddit = praw.Reddit(
    client_id='CLIENT ID HERE',
    client_secret='CLIENT SECRET HERE',
    username='USERNAME HERE',
    password='PASSWORD HERE',
    user_agent='Reddit Unmoderated Post Alert Bot (by /u/python_child)'
)

print("Bot has booted up successfully!")

subreddit = reddit.subreddit('SUBREDDIT HERE')

# Load processed comments from file
try:
    with open(file_path, 'r') as f:
        processed_comments = set(line.strip() for line in f)
except FileNotFoundError:
    processed_comments = set()

while True:
    print("Starting to search for new comments...")

    try:
        # Get the 50 newest comments
        new_comments = subreddit.comments(limit=50)
        found = False

        for comment in new_comments:
            # Check if the comment has been processed
            if comment.id not in processed_comments:
                if comment.body.startswith('m!pin'):
                    # Check if the commenter is the author of the post
                    if comment.author == comment.submission.author:
                        text_to_pin = comment.body.split('m!pin', 1)[1].strip()
                        # Comment on the post with the copied text and pin it
                        reply = comment.submission.reply(text_to_pin)
                        reply.mod.distinguish(how='yes', sticky=True)
                        # Print the URL of the post in console
                        print(f"Found a match in post: {comment.submission.url}")
                        # Add the comment's ID to the set of processed comments
                        processed_comments.add(comment.id)
                        found = True

        if not found:
            print("No matching comments found in this search.")

        # Save processed comments to file
        with open(file_path, 'w') as f:
            for comment_id in processed_comments:
                f.write(f"{comment_id}\n")

    except prawcore.exceptions.NotFound:
        print("PRAW could not find the resource (status code 404).")
    except prawcore.exceptions.RequestException:
        print("A request exception occurred.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Wait for 5 min
    time.sleep(600)