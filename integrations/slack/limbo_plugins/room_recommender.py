"""Listens to all messages and recommends a room that may be better for that message"""
""" """

OPEN_EDX_ROOM_KEYWORDS = {
    '<#C0WL6SPRA|ecommerce>': [
        'ecom', 'ecommerce', 'paypal', 'stripe', 'stripe', 'braintree', 'payment processor'
    ],
}


def room_recommender(text):
    clean_text = text.lower()
    for room, keywords in OPEN_EDX_ROOM_KEYWORDS.iteritems():
        for keyword in keywords:
            if keyword in clean_text:
                return room


def on_message(msg, server):
    print(msg)
    text = msg.get("text", "")
    recommendation = room_recommender(text)
    if recommendation:
        return "Thanks for posting! You may have better luck posting this in {room}".format(room=recommendation)
