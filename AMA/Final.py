import re

def remove_clutter(year_text: str) -> str:
    if not year_text or str(year_text).lower() == 'nan':
        return ""
    
    clean = re.sub(r'AD ASTR|CLASS AGENT|Faculty|Post Graduate', '', str(year_text), flags=re.IGNORECASE)
    clean = re.sub(r'[?Ss]', '', clean)
    return clean.strip()

def year_format(year: str) -> str:
    cleaned = remove_clutter(year)
    digits = re.sub(r'\D', '', str(cleaned))
    
    if len(digits) == 2:
        return "19" + digits
    return digits if len(digits) == 4 else ""

def extract_birth_year(text: str) -> str:
    match = re.search(r'\b(18|19)\d{2}\b', str(text))
    return match.group(0) if match else ""
