import re


def remove_clutter(year_text: str) -> str:
    if not year_text or str(year_text).lower() == 'nan':
        return ""
    
    clean = re.sub(r'AD ASTR|CLASS AGENT|Faculty|Post Graduate', '', str(year_text), flags=re.IGNORECASE)
    clean = re.sub(r'[?Ss]', '', clean)
    
    return clean.strip()

def contains_2_digits(year: str) -> bool:
    digits = re.sub(r'\D', '', str(year))
    return len(digits) == 2

def add_19(year: str) -> str:
    digits = re.sub(r'\D', '', str(year))
    if contains_2_digits(digits):
        return "19" + digits
    return digits

def year_format(year: str) -> str:
    cleaned = remove_clutter(year)
    formatted = add_19(cleaned)
    
    if len(formatted) == 4 and formatted.isdigit():
        return formatted
    return ""
