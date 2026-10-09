import re


with open('logs/http.log', 'r') as file:
    lines = file.readlines()

error_pattern = r"Error \d{3}"
success_pattern = r"Status \d{3}"

with open('logs/errors.log', "a") as error_file, open('logs/success.log', "a") as success_file:
    for line in lines:
       if re.search(error_pattern, line):
               error_file.write(line)
       elif re.search(success_pattern, line):
               success_file.write(line)

