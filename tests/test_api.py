from se2021.server import app

def test_root_endpoint_should_return_hello_message():
    client = app.test_client()
    response = client.get('/')
    assert response.json == {'message': 'Hello, world'}
