import pytest
import logging as logger
import requests
from constants import api, server_ip, server_port


@pytest.fixture()
def is_server_up():
    logger.info("Checking server")
    if requests.get(f'http://{server_ip}:{server_port}/api/{api}').status_code == 200:
        logger.info(f"Server is reachable, response code 200")
