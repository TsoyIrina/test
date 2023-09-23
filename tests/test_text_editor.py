from main import text_editor


def test_1():
    assert text_editor("", "", "") == ""


def test_2():
    assert text_editor("1", "1", "2") == "2"


def test_3():
    assert text_editor("1", "2", "") == "1"


