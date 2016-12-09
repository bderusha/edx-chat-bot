edx-slack-bot is a bot that lurks in the openedx slack and directs people to
channels, among other things.

Quickstart
==========

Make a virtualenv, source it, then install requirements::

  make requirements

Use the token of your slack bot to start the service::

  SLACK_TOKEN=<token> make run

Adding functionality
====================

Create a new python file under ``edx_chat_bot/limbo_plugins`` that
defines the following function::

  def on_message(msg, server):
      pass

``msg`` is a dictionary containing all the metadata corresponding to a message
(any message anywhere that the bot can see), and ``server`` lets you perform
actions such as sending messages.

``edx_chat_bot/limbo_plugins/helpers.py`` is your best friend.  Dump all
common code here.
