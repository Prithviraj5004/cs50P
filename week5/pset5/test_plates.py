from plates import is_valid


def test_maxlength():
    assert is_valid("mh5004") == True
    assert is_valid("mh125004")== False

def test_minlength():
    assert is_valid("mh")==True
    assert is_valid("m")== False

def test_empty():
    assert is_valid("")== False

def test_startswithchar():
    assert is_valid("MH")== True
    assert is_valid("50mh")== False
    assert is_valid("12344")== False
    assert is_valid("1mh")== False

def test_endsnum():
    assert is_valid("MH1200")==True

def test_numotherwise():
    assert is_valid("MH12ok")== False

def test_firstnumiszero():
    assert is_valid("MH05")== False

def test_alphanumeric():
    assert is_valid("Mh50") == True
    assert is_valid("Mh.50")== False
    assert is_valid("Mh,50") == False
    assert is_valid("Mh-50") == False
    assert is_valid("Mh 50") == False



