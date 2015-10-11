# -*- coding: utf-8 -*-

import os

# blueprint
#from apps.myapp.views import myapp

# config
SYSTEM_CONFIG_NAME = "%(project_name)s".upper() + "_CONFIG"
SYSTEM_CONFIG_PATH = "%(project_name)s.configs.base.BaseConfig"
env_config = os.environ.get(SYSTEM_CONFIG_NAME)
if env_config:
    SYSTEM_CONFIG_PATH = "%(project_name)s.configs." + env_config


# blueprint
SYSTEM_BLUEPRINTS = (
    #(myapp, None),
)
