import json
import pytest
import logging as logger
import requests
from constants import api, server_ip, server_port


@pytest.fixture()
def is_server_up():
    logger.info(f"********* Test Setup *********")
    try:
        res = requests.get(f'http://{server_ip}:{server_port}/api/{api}')
        logger.info(f"Server response code is {res.status_code}")
        yield json.loads(res.content)
    except requests.exceptions.ConnectionError as e:
        logger.debug(f"error {e}")
        yield 0
    finally:
        logger.info(f"********* Test Teardown *********")

