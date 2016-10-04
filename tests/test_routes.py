# -*- coding: utf-8 -*-
"""
tests.test_routes.py
"""
import json
import pytest


def test_users_get_request(client):
    rv = client.get('/users')
    assert 200 == rv.status_code
    assert rv.headers.get('Content-Type') == 'application/json'


def test_users_empty_get(client):
    rv = client.get('/users')
    assert json.loads(rv.data.decode('utf-8')) == []


def test_users_post(client):
    payload = {"name": "Drew", "email": "drew@androiddrew.com"}
    rv = client.post('/users',
                     content_type='application/json',
                     data=json.dumps(payload)
                     )
    assert 201 == rv.status_code
    assert rv.headers.get('Content-Type') == 'application/json'
    assert json.loads(rv.data.decode('utf-8'))[0] == payload


def test_users_post_failure(client):
    rv = client.post('/users', content_type='application/json', data=json.dumps(''))
    assert 400 == rv.status_code
    assert rv.headers.get('Content-Type') == 'application/json'

