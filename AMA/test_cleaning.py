from Final import year_format, contains_2_digits, remove_clutter

def test_clutter_removal():
    assert remove_clutter("48  AD ASTR") == "48"
    assert remove_clutter("1978 CLASS AGENT") == "1978"

def test_s_designation():
    assert remove_clutter("64S") == "64"
    assert year_format("77S") == "1977"

def test_digit_restoration():
    assert year_format("49") == "1949"
    assert year_format("21") == "1921"

def test_question_marks():
    assert year_format("1975?") == "1975"

def test_contains_2_digits():
    assert contains_2_digits("28") is True
    assert contains_2_digits("1928") is False

def test_invalid_data():
    assert year_format("Faculty") == ""
