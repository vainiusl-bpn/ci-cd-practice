from practice import app

def testing():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200