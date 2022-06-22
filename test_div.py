from business_logic import division
import pytest


@pytest.mark.parametrize("num1,num2,expected_result",[
    (4000, 200,20),

])

def test_calculator(num1,num2,expected_result):
    result = division(num1,num2)
    assert result == expected_result
    print(result)

