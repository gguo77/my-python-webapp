#/usr/bin/env python3
#-*-coding: utf-8-*
configs=config_default.configs

try:
	import config_override
	configs=merge(config,config_override.configs)
except ImportError:
	pass