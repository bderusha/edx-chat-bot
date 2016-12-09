"""Listens to all messages and recommends a room that may be better for that message"""

import pprint
import re

from .helpers import dm_user


CHANNELS = {
    'ecommerce': {
        'id': 'C0WL6SPRA',
    },
    'ops': {
        'id': 'C08B4LZEZ',
    },
}

OPEN_EDX_ROOM_PATTERNS = [
    ('ecom|ecommerce|paypal|stripe|braintree|payment processor', {
        'channel': 'ecommerce',
    }),
    ('azure|docker|ubuntu|ansible', {
        'channel': 'ops',
    }),
]


def room_recommender(text):
    for pattern, actions in OPEN_EDX_ROOM_PATTERNS:
        if re.search(pattern, text):
            return actions['channel']


MY_INFO = None

def on_message(msg, server):
    """Called when a message happens in a channel the bot is in.

    msg: dict
    server: Limbo object thingy
    """
    global MY_INFO

    if MY_INFO is None:
        MY_INFO = server.slack.login_data['self']
        # MY_INFO['id']

    pprint.pprint(msg)
    text = msg.get("text", "").lower()
    text += msg.get("file", {}).get("preview", "")
    room_name = room_recommender(text)
    if room_name:
        room_id = CHANNELS[room_name]['id']
        response_text = "Thanks for posting your message: “{msg_text}”\n You may have better luck posting this in <#{room_id}|{room_name}>"
        response_msg = response_text.format(
            msg_text=text,
            room_id=room_id,
            room_name=room_name
        )
        dm_user(server, msg.get('user'), response_msg)
