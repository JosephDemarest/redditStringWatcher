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
                submission.reply("ACTIVE: Jax enters Evasion, a defensive stance, for 2 seconds, causing all non-turret basic attacks against him to be dodged. Jax also takes 25% reduced damage from all champion area of effect abilities. Counter Strike can be recast after 1 second. At the end of the duration, Jax stuns all nearby enemies for 1 second and deals physical damage to them, increased by 20% for each attack dodged, up to a 100% increase.")
            elif re.search(IRELIA_REGEX, submission.title, re.IGNORECASE):
                submission.reply(
                    "I fucking love Irelia's butt, I want to bury myself between those cheeks and just inhale the raw scent of the stank as it slowly crushes my skull")
            elif re.search(LUX_REGEX, submission.title, re.IGNORECASE):
                submission.reply("Lux drives me absolutely wild and I need to vent She's just a dumb, slutty blonde that's super peppy and cheery, but as soon as you gank her lane and grab her hair she just turns into a sparkly-eyed, blushing whore for cock. Every time I win my lane against Lux I get a testosterone overload. I have to look at her hentai to let it all out. Your shield might protect you from my Q's but not this goddamn dick. Thank you for coming to my ted talk")
            elif re.search(TEEMO_REGEX, submission.title, re.IGNORECASE):
                submission.reply(
                    "As a teemo main at a respectably high elo, this game is hard to watch. Literally cringing at some of these mistakes. If you actually want to learn teemo PM me (im gold 3 24lp) I also do coaching")
            elif re.search(ZOE_REGEX, submission.title, re.IGNORECASE):
                submission.reply("I hope Zoe wins xD. I’m a Zoe main and she’s just so fun!! People get so trolled by the bubble, and her voice lines are so cute like when she sings about chocolate cake LOL! She’s super random but also smarter than she looks, just like me xD")


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
