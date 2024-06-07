import os
import json
import io
import traceback

from dotenv import load_dotenv

load_dotenv()


def load_environment_variables():
    """
    Load environment variables and return them as a dictionary.

    This function retrieves all the environment variables and stores them in a dictionary.
    The keys of the dictionary are the names of the environment variables, and the values
    are the corresponding values.

    Returns:
        dict: A dictionary containing the environment variables and their values.
    """
    env_vars = {key: value for key, value in os.environ.items()}
    return env_vars


ENVIRONMENT_VARIABLES = load_environment_variables()
GLOBAL_CONFIG = {}


def load():
    """
    Load the configuration from the 'bot_config.json' file and store it in the global GLOBAL_CONFIG dictionary.

    This function reads the contents of the 'bot_config.json' file and populates the global GLOBAL_CONFIG dictionary
    with the configuration values. The configuration file is expected to be in JSON format.

    If the configuration file is not found, a 'FileNotFoundError' exception is raised and an appropriate error message
    is printed. If there is an error decoding the JSON from the configuration file, a 'json.JSONDecodeError' exception
    is raised and prints an appropriate error message. If any other unexpected error occurs during the loading process,
    an 'Exception' is raised and prints an appropriate error message along with the traceback.

    Parameters:
        None

    Returns:
        None
    """
    global GLOBAL_CONFIG

    try:
        with open("bot_config.json", "r") as config_file:
            config = json.load(config_file)

        for section, values in config.items():
            for key, value in values.items():
                GLOBAL_CONFIG[f"{section}.{key}"] = value

        for key, value in ENVIRONMENT_VARIABLES.items():
            if value:
                GLOBAL_CONFIG[key] = value

    except FileNotFoundError:
        print("Configuration file not found. Please ensure 'bot_config.json' exists.")
    except json.JSONDecodeError:
        print("Error decoding JSON from the configuration file.")
    except Exception as e:
        print(f"An unexpected error occurred while loading the configuration: {e}")
        traceback.print_exc()


def save():
    """
    Save the global configuration to a JSON file.

    This function saves the global configuration dictionary to a JSON file named 'bot_config.json'.
    The configuration is first converted to a nested dictionary where the keys are the section names
    and the values are dictionaries containing the sub-keys and their corresponding values.
    The resulting dictionary is then serialized to JSON using the 'json.dumps' function.
    The serialized JSON is then written to the 'bot_config.json' file using the 'io.open' function.

    If there is an error while writing to the file, an 'IOError' exception is raised and an appropriate
    error message is printed. If there is any other unexpected error, an 'Exception' is raised and an
    appropriate error message is printed along with the traceback.

    Parameters:
        None

    Returns:
        None
    """
    try:
        config = {}

        for key, value in GLOBAL_CONFIG.items():
            section, sub_key = key.split('.', 1)
            if section not in config:
                config[section] = {}
            config[section][sub_key] = value

        json_config = json.dumps(config, indent=4)
        with io.open("bot_config.json", 'w', encoding='utf-8') as config_file:
            config_file.write(json_config)

    except IOError:
        print("An error occurred while writing to the configuration file.")
    except Exception as e:
        print(f"An unexpected error occurred while saving the configuration: {e}")
        traceback.print_exc()
