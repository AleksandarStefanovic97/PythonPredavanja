import re
from datetime import datetime


times = []
with open('logs/errors.log', 'r') as error_log:

    time_pattern = r"\d{2}:\d{2}:\d{2}"

    for error in error_log.readlines():
        match = re.findall(time_pattern, error)
        times.extend(match)

start_time = datetime.strptime(times[0], "%H:%M:%S")
end_time = datetime.strptime(times[-1], "%H:%M:%S")

total_time_passed = end_time - start_time
print(total_time_passed)

avarage_time_between_errors = total_time_passed / len(times)
print(f"Prosecno vreme izmedju gresaka iznosi {avarage_time_between_errors}")