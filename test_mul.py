from business_logic import multiplication
import pytest


@pytest.mark.parametrize("num1,num2,expected_result",[
    (423, 525,222075),

])

def test_calculator(num1,num2,expected_result):
    result = multiplication(num1,num2)
    assert result == expected_result
    print(result)

