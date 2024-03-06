from bmi import BMI
import pytest


#Tests form bmi_calculate()
@pytest.mark.parametrize(
        "weight, height, height_inch, output",
        [
            (125, 5, 3, 22.7),#TC Calculate 01.1 -> test accuracy
            (125, "a", 3, "ERROR: Please use numbers only.")#TC Calculate 01.2 -> tests caught exception
        ]
)
def test_bmi_calculate(weight, height, height_inch, output):
    bmi = BMI(weight, height, height_inch)
    bmi_calc = bmi.bmi_calculate()
    assert bmi_calc == output


