from business_logic import subtraction
import pytest



@pytest.mark.parametrize("num1,num2,expected_result",[
    (234823, -23094823, 23329646),

])

def test_calculator(num1,num2,expected_result):
    result = subtraction(num1,num2)
    assert result == expected_result
    print(result)

