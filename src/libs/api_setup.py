import tweepy
import settings


def create_tweepy_api(rate_limit_wait=True):
    '''
    Set up the Tweepy API object and return it.
    :param bool rate_limit_wait: Wait if the rate limit is hit?
    '''
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
    auth.set_access_token(settings.access_token, settings.access_token_secret)
    return tweepy.API(auth, wait_on_rate_limit=rate_limit_wait,
                      wait_on_rate_limit_notify=rate_limit_wait)
