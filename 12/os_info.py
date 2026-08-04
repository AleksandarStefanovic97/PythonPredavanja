import psutil


memory_info = psutil.virtual_memory()
memory_bites = memory_info.total
memory_GB = memory_bites / (1024**3)

print(f'{memory_GB:.2f} GB')

cpu_usage = psutil.cpu_percent(interval=1)
cores = psutil.cpu_count(logical=False)
logical_cores = psutil.cpu_count(logical=True)

current_process = psutil.Process()
num_threads = current_process.num_threads()

print(f"Total CPU usage: {cpu_usage}%")
print(f"Number of Physical cores: {cores}.")
print(f"Number of Logical cores: {logical_cores}.")
print(f"Number of threads in current process: {num_threads}")
