import re


name = "Aleksandar Stefanovic"

pattern = r"[A-Z][a-z]+ [A-Z][a-z]+$"

if re.match(pattern, name):
    print("Ime i prezime")
else:
    print("Nije ime i prezime")
