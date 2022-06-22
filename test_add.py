from business_logic import *
import pytest


@pytest.mark.parametrize("num1,num2,expected_result",[
    (-234234, 345345, 111111),

])

def test_calculator(num1,num2,expected_result):
    result = addition(num1,num2)
    assert result == expected_result
    print(result)




