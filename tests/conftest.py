import pytest
import logging as logger
import requests
from constants import api


@pytest.fixture()
def is_server_up(server_ip, server_port):
    logger.info("Checking server")
    if requests.get(f'http://{server_ip}:{server_port}/api/{api}').status_code == 200:
        logger.info(f"Server is reachable, response code 200")
