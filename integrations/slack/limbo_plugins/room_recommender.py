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
            'azure',
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
    # res = server.slack.api_call('channels.list')
    # print(json.dumps(json.loads(res), indent=4))
    text = msg.get("text", "")
    room_name = room_recommender(text)
    if room_name:
        room_id = OPEN_EDX_ROOM_KEYWORDS[room_name]['id']
        return "Thanks for posting! You may have better luck posting this in <#{room_id}|{room_name}>".format(
            room_id=room_id,
            room_name=room_name
        )
