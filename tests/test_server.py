import json

import requests
import pytest

from constants import server_ip, server_port, api


# @pytest.mark.skip
def test_get_positive(is_server_up):
    res = requests.get(f'http://{server_ip}:{server_port}/api/{api}')
    res_json = json.loads(res.content)
    assert res.status_code == 200 and res_json['version'] == 0.1 and res_json['name'] == 'salt'


@pytest.mark.xfail
def test_get_negative(is_server_up):
    res = requests.get(f'http://{server_ip}:{server_port + 1}/api/{api}')
    res_json = json.loads(res.content)
    assert res.status_code == 200 and res_json['version'] == 0.1 and res_json['name'] == 'salt'
