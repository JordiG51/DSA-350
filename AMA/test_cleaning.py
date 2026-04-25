from Final import year_format, extract_birth_year, remove_clutter

def test_clutter_removal():
    assert remove_clutter("48  AD ASTR") == "48"
    assert remove_clutter("64S") == "64"

def test_year_standardization():
    assert year_format("49") == "1949"
    assert year_format("1975?") == "1975"

def test_birth_regex():
    assert extract_birth_year("Born: 04/18/1873") == "1873"
    assert extract_birth_year("11/17/1902 DOB") == "1902"
