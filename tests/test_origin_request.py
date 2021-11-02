from cff.origin_request import Configuration, configure, handler


def test_get_directory() -> None:
    response = handler(
        {
            "Records": [
                {
                    "cf": {
                        "request": {
                            "method": "GET",
                            "uri": "/foo/",
                        }
                    }
                }
            ]
        }
    )
    assert response == {
        "method": "GET",
        "uri": "/foo/index.html",
    }


def test_get_directory__no_slash() -> None:
    response = handler(
        {
            "Records": [
                {
                    "cf": {
                        "request": {
                            "method": "GET",
                            "uri": "/foo",
                        }
                    }
                }
            ]
        }
    )
    assert response == {
        "headers": {
            "location": [
                {
                    "key": "Location",
                    "value": "/foo/",
                },
            ],
        },
        "status": 301,
    }


def test_get_directory__with_config() -> None:
    configure(Configuration(index="index.bar"))
    response = handler(
        {
            "Records": [
                {
                    "cf": {
                        "request": {
                            "method": "GET",
                            "uri": "/foo/",
                        }
                    }
                }
            ]
        }
    )
    assert response == {
        "method": "GET",
        "uri": "/foo/index.bar",
    }


def test_get_file() -> None:
    response = handler(
        {
            "Records": [
                {
                    "cf": {
                        "request": {
                            "method": "GET",
                            "uri": "/foo/bar.png",
                        }
                    }
                }
            ]
        }
    )
    assert response == {
        "method": "GET",
        "uri": "/foo/bar.png",
    }


def test_put() -> None:
    response = handler(
        {
            "Records": [
                {
                    "cf": {
                        "request": {
                            "method": "PUT",
                            "uri": "/foo",
                        }
                    }
                }
            ]
        }
    )
    assert response == {
        "method": "PUT",
        "uri": "/foo",
    }
