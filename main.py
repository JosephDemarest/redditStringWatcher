import re
import threading
import praw

BOT_USERNAME = "x"
reddit = praw.Reddit(
    client_id="x",
    client_secret="x",
    password="x",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
    username="x",
)

def main():
    SUBREDDIT = input("What subreddit would you like to listen in?:: ")
    REGEX = input("Input Regex to reply to: ") 
    reply = input("Input reply text: ")
    
    subreddit = reddit.subreddit(SUBREDDIT)
    for submission in subreddit.stream.submissions(skip_existing=True):
        parse_submission(submission,reply,REGEX)

def parse_submission(submission, reply, REGEX):
    if (re.search(REGEX, submission.title, re.IGNORECASE) and canreply(submission)):
        submission.reply(reply)
    if (re.search(REGEX, submission.comments, re.IGNORECASE) and canreply(submission)):
        submission.reply(reply)

    
def canreply(s):
    if alreadyreplied(s):
        return False
    if not alreadyreplied(s):
        return True
    return False


def alreadyreplied(s):
    if type(s).__name__ == "Submission":
        for comment in s.comments:
            if comment.author == BOT_USERNAME:
                return True
    elif type(s).__name__ == "Comment":
        comment = reddit.comment(s.id)
        try:
            comment.refresh()
        except praw.exceptions.ClientException:
            try:
                comment.refresh()
            except praw.exceptions.ClientException:
                # ignore comment
                return True
        if comment.author == BOT_USERNAME:
            return True

    return False

if __name__ == "__main__":
    main()
