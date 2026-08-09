import re


email = "coa@gmail.com"

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(email_pattern, email):
    print("e-mail")
else:
    print("Nije e-mail")