"""Greet new users in a DM."""

import pprint

import helpers

def on_message(msg, server):
    """Called when a message happens in a channel the bot is in.

    msg: dict
    server: Limbo object thingy
    """
    print("Greeter: {!r}".format(msg))
    pprint.pprint(helpers.get_dm_history(server, msg.get('user')))

