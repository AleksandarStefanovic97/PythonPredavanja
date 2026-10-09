import re


bonus_codes = "ABC123, bonus455, bonus22"

pattern1= r"\b[A-Za-z]{3}\d{3}\b"

product_codes = re.findall(pattern1, bonus_codes)
print(product_codes)


username = "coa1997"

username_pattern = r"[A-Za-z]{1-5}\d{2,}]"
match = re.match(username_pattern, username)


if match:
    print(match)