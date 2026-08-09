import re


ourNumbers = "12a345"
sentence = "I love python"
capitalSentence = "Today will rain"
phoneNumber = "38165432432"

pattern = r"^\d+$"
pattern2 = r"^[a-zA-Z ]+$"
pattern3 = r"^[A-Z]"
pattern4 = r"^38(1|2|5|9)"


if re.match(pattern, ourNumbers):
    print("Samo brojevi")
else:
    print("Nisu samo brojevi")


if re.match(pattern2, sentence):
    print("Samo slova")
else:
    print("Nisu samo slova")


if re.match(pattern3, capitalSentence):
    print("Pocinje velikim slovom")
else:
    print("Ne pocinje velikim slovom")


phone_match = re.match(pattern4, phoneNumber)

phone_map = {
    "381": "Serbia",
    "382": "Montenegro",
    "385": "B&H",
    "389": "Croatia"
}


if phone_match:
    prefix = "38"+phone_match.group(1)
    country = phone_map[prefix]
    print(f"Starting number is {prefix} and country is {country}")

