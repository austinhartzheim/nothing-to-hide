__author__ = 'Joseph'

USER_HANDLE_IS_FOUND = True


def get_user_by_handle(user_handle):
    """
    Returns a package of the user's handle, name, calculated evil score, and route to evil kingpin. If the us

    :param user_handle: String of user handle EXCLUDING the '@' character
    :return: dictionary of the given user's information
    """
    if not USER_HANDLE_IS_FOUND:
        raise KeyError('That user does not exist or has not been processed.')
    user_name = 'Bob Fredgod'
    user_score = 100

    route_to_evil = ['me', 'austin', 'satan', 'anonymous', 'ioerror']

    user_data = {
        'handle': user_handle,
        'name': user_name,
        'score': user_score,
        'route': route_to_evil
    }

    return user_data