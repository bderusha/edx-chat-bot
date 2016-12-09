
from unittest.mock import patch

import edx_chat_bot.limbo_plugins.room_recommender
from edx_chat_bot.limbo_plugins.room_recommender import room_recommender

def test_room_recommender():
    edx_chat_bot.limbo_plugins.room_recommender.CHANNELS = {
        'ecommerce': {
            'id': 'C0WL6SPRA',
        },
        'ops': {
            'id': 'C08B4LZEZ',
        },
    }
    edx_chat_bot.limbo_plugins.room_recommender.OPEN_EDX_ROOM_PATTERNS = [
        ('ecom|ecommerce|paypal|stripe|braintree|payment processor', {
            'channel': 'ecommerce',
        }),
        ('azure|docker|ubuntu|ansible', {
            'channel': 'ops',
        }),
    ]
    assert room_recommender('something azure something') == ('azure', 'ops')
    assert room_recommender('something ecom something') == ('ecom', 'ecommerce')
    assert room_recommender('azure and ecom') == ('ecom', 'ecommerce')
    assert room_recommender('nothing at all') is None
    assert room_recommender('') is None
