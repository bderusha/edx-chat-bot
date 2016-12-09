
# development requirements
requirements :
	pip install -r requirements.txt

run :
	limbo --pluginpath edx_chat_bot/slack/limbo_plugins

.PHONY : run requirements
