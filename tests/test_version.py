from cff import get_version


def test() -> None:
    assert get_version() == "-1.-1.-1"
