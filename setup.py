
from setuptools import setup

# Dynamically calculate the version based on pyperclip.VERSION.
setup(
    name='edx_chat_bot',
    version='0.1.0',
    url='https://github.com/bderusha/edx-chat-bot',
    author='edx',
    author_email='info@edx.org',
    description=('a bot that lurks in the openedx slack'),
    packages=['edx_chat_bot'],
    install_requires=['limbo'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
