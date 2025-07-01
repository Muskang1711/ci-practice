from app import add, subtract 

def test_data():
    assert add(2,3) == 5


def test_subtract():
    assert subtract(5,2) == 3


# test_app.py
def test_add():
    assert add(2, 3) == 999  # Wrong on purpose
