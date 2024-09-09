from calculator import square
import pytest

def main():
    test_square()

# assert => assert that something is true
#        => if false AssertionError => try, except
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")

# pytest => 3rd party library
# unit tests => tests for particular functions in your program
# in terminal => pytest test_calculator.py
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():    
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()
