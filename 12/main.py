import platform

print(platform.system(), platform.platform())

version = platform.python_version()
print(f"Verzija pythona na mom racunaru je {version}")

version_tuple = platform.python_version_tuple()
version_first = int(version_tuple[0])

if version_first != 3:
    print("Ne koristite dobru verziju Pythona.")

