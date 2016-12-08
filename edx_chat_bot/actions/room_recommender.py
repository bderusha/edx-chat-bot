""" """

OPEN_EDX_ROOM_KEYWORDS = {
    '#ecommerce': [
        'ecom', 'ecommerce', 'paypal', 'stripe', 'stripe', 'braintree', 'payment processor'
    ],
}


def room_recommender(text):
    clean_text = text.lower()
    for room, keywords in OPEN_EDX_ROOM_KEYWORDS.items():
        for keyword in keywords:
            if keyword in clean_text:
                return room


def respond(text):
    recommendation = room_recommender(text)
    if recommendation:
        return "Thanks for posting! You may have better luck posting this in {room}".format(room=recommendation)
