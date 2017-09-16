import os

def get_plugin_path(plug):
    pluginspath_parts = [os.path.expanduser('~'),
                         'projects',
                         'projects',
                         'plugins',
                         plug]
    pluginpath = os.path.join(*pluginspath_parts)
    return pluginpath


def list_plugins():
    """return a list of the available plugins."""
    pluginspath_parts = [os.path.expanduser('~'),
                         'projects',
                         'projects',
                         'plugins']
    pluginspath = os.path.join(*pluginspath_parts)
    plugins = [plugin.split('_')[0] for plugin in os.listdir(pluginspath)]
    return plugins
