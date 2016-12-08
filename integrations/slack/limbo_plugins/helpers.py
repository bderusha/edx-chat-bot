'''
generic helper functions for doing slack things
'''

import json

def api_call(server, *args, **kwargs):
    '''
    Make a slack API call.

    List of supported methods:
    https://api.slack.com/methods?nojsmode=1

    Example:

        api_call(server, 'im.open', post_data={'user': 'alice'})

    '''
    res = server.slack.api_call(*args, **kwargs)
    return json.loads(res)

def dm_user(server, username, msg):
    '''
    direct message the user `username` with the message `msg`
    '''
    user_info = api_call(server, 'im.open', post_data={'user': username})
    user_dm_channel_id = user_info['channel']['id']
    server.slack.post_message(user_dm_channel_id, msg)
