#! /usr/bin/env python3
import pytest

from Goku import update_stats, read_toker, read_server_id, on_member_join, on_message, on_ready


def test_update_stats():
    with pytest.raises(Exception):
        update_stats()


def test_read_token():
    assert line == f.readlines


def test_read_server_id():
    assert line == f.readlines


def test_on_member_join():
    assert 1 == 1


def test_on_message():
    assert id == client.get_guild(serverid)
