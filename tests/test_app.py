from app import app


def test_index_returns_ok():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_generate_returns_password():
    client = app.test_client()
    response = client.post(
        "/generate",
        data={
            "length": "12",
            "uppercase": "on",
            "lowercase": "on",
            "numbers": "on",
            "symbols": "on",
        },
    )
    assert response.status_code == 200
    assert b"Senha gerada" in response.data


def test_generate_returns_error_for_invalid_input():
    client = app.test_client()
    response = client.post("/generate", data={"length": "2"})
    assert response.status_code == 400
