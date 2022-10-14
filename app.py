#!/usr/bin/python3

import importlib
import os

plugins = {}

# scan and register the plugins
app_directory = os.path.realpath(os.path.dirname(__file__))

plugin_directory = os.path.join(app_directory, "Plugins")


for plugin_file in os.listdir(plugin_directory):
    
    file_name, file_extension = os.path.splitext(plugin_file)
    if file_extension == ".py":
        plugin_module = importlib.import_module("plugins." + file_name)
        plugins[plugin_module.get_name()] = plugin_module

print(plugins['Test Plugin B'].print_help())
