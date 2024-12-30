def is_specified_json(response, expected):
    json = response.json()
    assert json.get("userId") == expected.get("userId")
    assert json.get("id") == expected.get("id")
    assert json.get("title") == expected.get("title")
    assert json.get("body") == expected.get("body")
