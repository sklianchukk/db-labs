import os
import yaml


def _get_config_path() -> str:
    """
    Build absolute path to the app.yml configuration file.

    Returns
    -------
    str
        Absolute filesystem path to app.yml.
    """
    # Current file: app/my_project/utils/config_loader.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up to app/my_project
    my_project_dir = os.path.dirname(current_dir)
    # Go up to app
    app_dir = os.path.dirname(my_project_dir)
    # Config file inside app/config/app.yml
    return os.path.join(app_dir, "config", "app.yml")


def load_config() -> dict:
    """
    Load application configuration from YAML file.

    Returns
    -------
    dict
        Parsed YAML configuration as a Python dictionary.
    """
    config_path = _get_config_path()
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
