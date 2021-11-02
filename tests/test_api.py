from se2021.server import app


def test_root_endpoint_should_return_hello_message():
    client = app.test_client()
    response = client.get('/')
    assert response.json == {'message': 'Hello, world'}


def test_morse_endpoint_should_return_three_dots_three_dashes_three_dots_for_sos():  # noqa
    client = app.test_client()
    response = client.get('/morse/sos')
    assert response.json == {'result': '... --- ...'}
