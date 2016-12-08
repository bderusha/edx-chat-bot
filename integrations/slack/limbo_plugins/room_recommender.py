"""Listens to all messages and recommends a room that may be better for that message"""
""" """
import json

OPEN_EDX_ROOM_KEYWORDS = {
    'ecommerce': {
        'id': 'C0WL6SPRA',
        'patterns': [
            'ecom', 'ecommerce', 'paypal', 'stripe', 'stripe', 'braintree', 'payment processor'
        ],
    },
    'ops': {
        'id': 'C08B4LZEZ',
        'patterns': [
            'azure', 'docker', 'ubuntu', 'ansible',
        ],
    },
}


def room_recommender(text):
    clean_text = text.lower()
    for room_name, room_data in OPEN_EDX_ROOM_KEYWORDS.iteritems():
        for keyword in room_data.get('patterns'):
            if keyword in clean_text:
                return room_name


def on_message(msg, server):
    res = server.slack.api_call('im.open', post_data={'user': msg.get('user')})
    user_info = json.loads(res)
    user_dm_channel_id = user_info['channel']['id']

    print(msg)
    text = msg.get("text", "")
    room_name = room_recommender(text)
    if room_name and user_dm_channel_id:
        room_id = OPEN_EDX_ROOM_KEYWORDS[room_name]['id']
        response_msg = "Thanks for posting your message: \"{msg}\" \n You may have better luck posting this in <#{room_id}|{room_name}>".format(
            msg=text,
            room_id=room_id,
            room_name=room_name
        )
        server.slack.post_message(user_dm_channel_id, response_msg)
