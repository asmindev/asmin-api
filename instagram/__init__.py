from .instagram import Instagram
import os

ig = instagram.Instagram()


def stories(arg):
    cookies_path = os.path.dirname(os.path.realpath(__file__)) + "/cookies.txt"
    cookies = open(cookies_path).read().strip()
    if not ig.is_logged:
        ig.set_cookies = cookies
        ig.login()
    return ig.get_stories(arg)


def reels(arg):
    cookies_path = os.path.dirname(os.path.realpath(__file__)) + "/cookies.txt"
    cookies = open(cookies_path).read().strip()
    if not ig.is_logged:
        ig.set_cookies = cookies
        ig.login()
    return ig.get_reel(arg)


def get_following(username, cookies, end_cursor=None):
    ig.set_cookies = cookies
    ig.login()
    user = ig.get_user_info(username)
    if user.get("id"):
        return ig.get_user_followings(user["id"], end_cursor=end_cursor)
    else:
        return user
