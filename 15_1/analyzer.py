import re


with open('logs/http.log', 'r') as file:
    lines = file.readlines()

err_pattern = r"Error \d{3}"
succ_pattern = r"Status \d{3}"


with open('logs/errors.log', 'a') as error_file, open('logs/success.log', 'a') as success_file:
    for line in lines:
        if re.search(err_pattern, line):
                error_file.write(line)
        elif re.search(succ_pattern, line):
                success_file.write(line)


