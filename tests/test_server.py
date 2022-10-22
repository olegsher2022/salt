import json
import logging as logger
import requests
import pytest

from constants import server_ip, server_port, api


@pytest.mark.parametrize("record, param, expected", [
    pytest.param(0, "sex", "F", marks=pytest.mark.skip),
    (0, "age", 18),
    (0, "address", "U"),
    pytest.param(0, "address", "B", marks=pytest.mark.xfail)
])
def test_get_positive(is_server_up, record, param, expected):
    """
        Parametrize Positive test
    """
    # logger.info(test_get_positive.__doc__)

    res_json = is_server_up
    assert res_json, f"Server unreachable"
    assert json.loads(res_json)[record][param] == expected
