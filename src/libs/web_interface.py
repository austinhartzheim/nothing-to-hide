import libs.api_setup
import libs.crawlers
import networkx
import tweepy

USER_HANDLE_IS_FOUND = True

graph = networkx.read_yaml('test.yaml')


def get_user_by_handle(user_handle):
    '''
    Calculate statistics for a user, looked up by their Twitter handle.

    :param user_handle: String of user handle EXCLUDING the '@' character
    :return: dictionary of the given user's information
    '''
    api = libs.api_setup.create_tweepy_api(rate_limit_wait=False)

    # Fetch user information
    try:
        user = api.get_user(user_handle)
    except tweepy.error.TweepError as err:
        if err.response.status_code == 404:
            raise KeyError('User name does not exist')

    graph.add_node(user.screen_name)

    try:
        path = networkx.algorithms.shortest_path(graph, user.screen_name.lower(), '@')
        path.pop()  # Remove last element, whih is the final placeholder
    except networkx.exception.NetworkXNoPath:
        crawler = libs.crawlers.RecursiveCrawler(api)
        try:
            crawler.fetch_following(user.screen_name)
        except tweepy.TweepError:
            print('Rate limit hit. Relying on existing graph')
        path = networkx.algorithms.shortest_path(graph, user.screen_name.lower(), '@')
        path.pop()  # Remove last element, whih is the final placeholder

    user_name = user.name
    user_score = 100

    user_data = {
        'handle': user_handle,
        'name': user_name,
        'score': user_score,
        'route': path
    }
    return user_data
