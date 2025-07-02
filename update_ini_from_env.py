import configparser
import os

config_file = 'settings.ini'
config = configparser.ConfigParser()
config.read(config_file)

for section in config.sections():
    for key in config[section]:
        env_var = f"{section.upper()}_{key.upper()}"
        new_value = os.environ.get(env_var)
        if new_value is not None and new_value != "":
            config[section][key] = new_value

with open(config_file, 'w') as configfile:
    config.write(configfile)

print("INI file updated with Jenkins build parameters.")
