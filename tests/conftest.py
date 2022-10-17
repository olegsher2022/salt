import json
import sys

import pytest
import logging as logger
import requests
from constants import api, server_ip, server_port


@pytest.fixture()
def is_server_up():
    logger.info("Checking server")
    try:
        requests.get(f'http://{server_ip}:{server_port}/api/{api}')
        logger.info(f"Server is reachable, response code 200")
    except requests.exceptions.ConnectionError as e:
        logger.error(f"ERROR {e}")
        return 0
    res = requests.get(f'http://{server_ip}:{server_port}/api/{api}')
    res_json = json.loads(res.content)
    return res_json
