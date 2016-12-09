
# development requirements
requirements:
	pip install -r requirements.txt

test:
	py.test tests

run:
	limbo --pluginpath edx_chat_bot/limbo_plugins

clean:
	find . -name '__pycache__' -delete
	find . -name '*.pyc' -delete
	rm -rf edx_chat_bot.egg-info

.PHONY : run requirements test
