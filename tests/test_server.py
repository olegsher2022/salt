import json
import logging as logger
import requests
import pytest

from constants import server_ip, server_port, api


# @pytest.mark.skip
def test_get_positive(is_server_up):
    """
        Check response when server reachable, could be parametrized
    """
    logger.info(test_get_positive.__doc__)

    res_json = is_server_up
    assert res_json['version'] == 0.1
    assert res_json['name'] == 'salt'


@pytest.mark.xfail
def test_get_negative():
    """
    Check response when server down/unreachable, in this case I just point test to server_port + 1, no needs for
    teardown or setup
    """
    logger.info(test_get_negative.__doc__)
    requests.get(f'http://{server_ip}:{server_port + 1}/api/{api}')
    logger.info(f"Server is reachable, response code 200")

    res = requests.get(f'http://{server_ip}:{server_port + 1}/api/{api}')
    res_json = json.loads(res.content)

    assert res.status_code == 200 and res_json['version'] == 0.1 and res_json['name'] == 'salt'
