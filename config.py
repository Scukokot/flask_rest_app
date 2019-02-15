from os import environ

VSTS_PUSH_PATH = '/api/v_0_0/push/ASUI/to_jira/created_item'
IP = environ.get('APP_IP', '0.0.0.0')
PORT = int(environ.get('APP_PORT', 5000))
