
# development requirements
requirements :
	pip install -r requirements.txt

test :
	py.test tests

run :
	limbo --pluginpath edx_chat_bot/slack/limbo_plugins

clean:
	find . -name '__pycache__' -delete
	find . -name '*.pyc' -delete

.PHONY : run requirements test
