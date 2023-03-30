import collections.abc
import os
from datetime import datetime

import yaml
from attrdict import AttrDict

DIR_CONFIGS = './configs'
BASE_CONFIG_NAME = 'base.yaml'


def load_config(config_file: str = "", **kwargs):
    """Load a yaml file and return a dict.
    Args:
        config_file (str): Path to the yaml file.
        kwargs (dict): Dictionary of additional arguments. These will be merged
            with the main arguments.
    Return:
        args (dict): Dictionary of the yaml file.
    """

    base_config_path = os.path.join(DIR_CONFIGS, BASE_CONFIG_NAME)
    with open(base_config_path, 'r') as f:
        args = yaml.load(f, Loader=yaml.FullLoader)

    yaml_path = os.path.join(DIR_CONFIGS, config_file)
    if os.path.exists(yaml_path) and os.path.isfile(yaml_path):
        with open(yaml_path, 'r') as f:
            args_child = yaml.load(f, Loader=yaml.FullLoader)
        args = update(args, args_child)
    else:
        print(f"Warning: {yaml_path} not found. Using default values.")

    for k, v in kwargs.items():
        if isinstance(v, dict):
            args = update(args, v)

    dt_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    args['run_id'] = f"{dt_str}"

    return AttrDict(args)


def update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update(d.get(k, {}), v)
        else:
            d[k] = v
    return d
