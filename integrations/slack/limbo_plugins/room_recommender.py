"""Listens to all messages and recommends a room that may be better for that message"""
""" """
import json
import helpers

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
    print(msg)
    text = msg.get("text", "")
    room_name = room_recommender(text)
    if room_name:
        room_id = OPEN_EDX_ROOM_KEYWORDS[room_name]['id']
        response_msg = "Thanks for posting your message: \"{msg}\" \n You may have better luck posting this in <#{room_id}|{room_name}>".format(
            msg=text,
            room_id=room_id,
            room_name=room_name
        )
        helpers.dm_user(server, msg.get('user'), response_msg)
