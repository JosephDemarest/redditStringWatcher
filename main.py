import re
import threading
import praw

BOT_USERNAME = "x"
SUBREDDIT = "all"
JAX_REGEX = r'[^a-z]jax[^a-z]|^jax'
IRELIA_REGEX = r'[^a-z]irelia[^a-z]|^irelia'
LUX_REGEX = r'[^a-z]lux[^a-z]|^lux'
TEEMO_REGEX = r'[^a-z]teemo[^a-z]|^teemo'
ZOE_REGEX = r'[^a-z]zoe[^a-z]|^zoe'
reddit = praw.Reddit(
    client_id="x",
    client_secret="x",
    password="x",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
    username="x",
)


class SubListen(threading.Thread):
    print('Started listening sub: ' + SUBREDDIT)
    subreddit = reddit.subreddit(SUBREDDIT)
    while True:
        for submission in subreddit.stream.submissions():
            if re.search(JAX_REGEX, submission.title, re.IGNORECASE):
                submission.reply("string")
            elif re.search(IRELIA_REGEX, submission.title, re.IGNORECASE):
                submission.reply("string")
            elif re.search(LUX_REGEX, submission.title, re.IGNORECASE):
                submission.reply("string")
            elif re.search(TEEMO_REGEX, submission.title, re.IGNORECASE):
                submission.reply("string")
            elif re.search(ZOE_REGEX, submission.title, re.IGNORECASE):
                submission.reply("string")


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
    sublisten = SubListen()
    sublisten.start()
