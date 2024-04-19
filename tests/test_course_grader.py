import pytest
from course_grader import convert_to_letter_grade

def test_exact_boundaries():
    assert convert_to_letter_grade(0) == 'F'
    assert convert_to_letter_grade(59) == 'F'
    assert convert_to_letter_grade(60) == 'D'
    assert convert_to_letter_grade(69) == 'D'
    assert convert_to_letter_grade(70) == 'C'
    assert convert_to_letter_grade(79) == 'C'
    assert convert_to_letter_grade(80) == 'B'
    assert convert_to_letter_grade(89) == 'B'
    assert convert_to_letter_grade(90) == 'A'
    assert convert_to_letter_grade(100) == 'A'

def test_invalid_numerical_score():
    with pytest.raises(ValueError) as e:
        convert_to_letter_grade(-1)
    assert str(e.value) == "Score must be between 0 and 100."

    with pytest.raises(ValueError) as e:
        convert_to_letter_grade(101)
    assert str(e.value) == "Score must be between 0 and 100."


def test_non_numeric_type():
    with pytest.raises(TypeError) as e:
        convert_to_letter_grade("abc")
    assert str(e.value) == "Score must be a numeric value."

    with pytest.raises(TypeError) as e:
        convert_to_letter_grade([1, 2, 3])
    assert str(e.value) == "Score must be a numeric value."

    with pytest.raises(TypeError) as e:
        convert_to_letter_grade(None)
    assert str(e.value) == "Score must be a numeric value."
