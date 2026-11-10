
from app import app

def test_hello_route():
    client = app.test_client()
    response = client.post('/hello', data={'username': 'Ibtissam'})
    assert response.status_code == 200
    assert b'Hello Ibtissam' in response.data

def test_sum_route():
    client = app.test_client()
    response = client.post('/sum', data={'a': '5', 'b': '3'})
    assert response.status_code == 200
    assert b'8.0' in response.data
