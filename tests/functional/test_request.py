def test_request(client):
    response = client.get("/administration/lookups")
    assert response.status_code == 200