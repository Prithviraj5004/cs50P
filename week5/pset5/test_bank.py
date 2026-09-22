from bank import value

def test_hello():
    assert value("hello")==0

def test_startswith_h():
    assert value("hey")==20

def test_hello_phrase():
    assert value("hello there")==0

def test_other():
    assert value("good morning")==100

def test_case_insensitive():
    assert value("HELLO")==0
    assert value("Hello")==0
