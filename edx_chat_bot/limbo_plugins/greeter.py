"""Greet new users in a DM."""

import pprint

# This weirdness is because Limbo adds this directory to sys.path :(
try:
    from helpers import dm_user, get_dm_history
except ImportError:
    from .helpers import dm_user, get_dm_history


WELCOME_MESSAGE = """
Hey there! Welcome to Open edX Slack.
We have a number of channels.  Please use the best one.
"""

EASTER_EGG_TRIGGER = "Pretend this is my first message"


def on_message(msg, server):
    """Called when a message happens in a channel the bot is in.

    msg: dict
    server: Limbo object thingy
    """
    if msg.get("subtype") == "channel_join":
        # Don't talk to someone just because they joined the channel.
        return
    print("Greeter: {!r}".format(msg))
    message_history = get_dm_history(server, msg.get('user'))
    num_messages = len(message_history['messages'])
    if num_messages == 0 or EASTER_EGG_TRIGGER in msg.get('text'):
        dm_user(server, msg.get('user'), WELCOME_MESSAGE)
