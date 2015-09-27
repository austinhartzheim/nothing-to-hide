import libs.api_setup
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
    api = libs.api_setup.create_tweepy_api()

    # Fetch user information
    user = api.get_user(user_handle)
    # TODO: Check if the user object exists
    # TODO: Lookup user in the graph
    graph.add_node(user.screen_name)
    user_name = user.name
    user_score = 100

    path = networkx.algorithms.shortest_path(graph, user.screen_name.lower(), '@')
    path.pop()  # Remove last element, whih is the final placeholder

    user_data = {
        'handle': user_handle,
        'name': user_name,
        'score': user_score,
        'route': path
    }
    return user_data
