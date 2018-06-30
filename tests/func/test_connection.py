# coding: utf-8


import getpass
# import json
import sys
import pytest
# import requests
import steelconnection
# import steelconnection.__main__  # for cvoerage sake.
# import fake_requests

from PRIVATE import REALM_ADMIN, ORG_ADMIN, PASSWORD
from PRIVATE import REALM_2_8, REALM_2_9, REALM_2_10, REALM_2_11


def test_create_object_2_8():
    sc = steelconnection.SConAPI(REALM_2_8, REALM_ADMIN, PASSWORD)
    assert isinstance(sc, steelconnection.SConAPI)


def test_create_object_2_9():
    sc = steelconnection.SConAPI(REALM_2_9, REALM_ADMIN, PASSWORD)
    assert isinstance(sc, steelconnection.SConAPI)


def test_create_object_2_10():
    sc = steelconnection.SConAPI(REALM_2_10, REALM_ADMIN, PASSWORD)
    assert isinstance(sc, steelconnection.SConAPI)


def test_create_object_2_11():
    sc = steelconnection.SConAPI(REALM_2_11, REALM_ADMIN, PASSWORD)
    assert isinstance(sc, steelconnection.SConAPI)


def test_auth_attempt_netrc_fails(monkeypatch):
    """By not providing auth, netrc should be attempted and fail."""
    if sys.version_info.major < 3:
        monkeypatch.setattr('__builtin__.raw_input', lambda x: REALM_ADMIN)
    else:
        monkeypatch.setattr('builtins.input', lambda x: REALM_ADMIN)
    monkeypatch.setattr('getpass.getpass', lambda x: PASSWORD)
    sc = steelconnection.SConAPI(REALM_2_8)
    orgs = sc.get('orgs')
    assert sc
