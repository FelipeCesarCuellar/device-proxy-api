import os
import logging

ENV_VARS_NAMES = {
    'DB_USER': {
        'type': 'string',
        'required': True
    },
    'DB_PASSWORD': {
        'type': 'string',
        'required': True
    },
    'DB_HOST': {
        'type': 'string',
        'required': True
    },
    'DB_PORT': {
        'type': 'string',
        'required': True
    },
    'DB_NAME': {
        'type': 'string',
        'required': True
    }
}

ENV_VARS = dict()
for var_name in ENV_VARS_NAMES:
    if ENV_VARS_NAMES[var_name].get('required', True) and os.environ.get(var_name) is None:
        raise Exception(f'Environment variable {var_name} not found in {os.environ}')
    if os.environ.get(var_name) is not None:
        value = os.environ.get(var_name)
        logging.getLogger(__name__).info(f'Loading environment variable {var_name}')
        ENV_VARS[var_name] = value

ENV_VARS['SERVICE_ROOT'] = os.path.abspath(os.path.dirname(__file__))
ENV_VARS['SCHEMA_PATH'] = os.path.join(ENV_VARS['SERVICE_ROOT'] + '/schemas/')