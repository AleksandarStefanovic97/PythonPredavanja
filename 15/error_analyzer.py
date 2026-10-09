import re



with open('logs/errors.log') as error_log:
    pattern = r"12:\d{2}:\d{2}"

    for error in error_log.readlines():
        match = re.search(pattern, error)
        print(match)