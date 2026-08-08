import subprocess
import webbrowser
import asyncio
import time
import random
import threading
from desktop_notifier import DesktopNotifier


messages = [
    "Take a break.",
    "It's time to chill",
    "Vreme je za odmor.",
    "Predugo si ucio, 10 minuta pauze."
]



async def main():
    notifier = DesktopNotifier()

    while True:
        await notifier.send(title="Notice", message=random.choice(messages))
        await asyncio.sleep(10)


def start_notifier_thread():
    asyncio.run(main())

threadNotify = threading.Thread(target=start_notifier_thread, daemon=True)
threadNotify.start()

subprocess.Popen(["/snap/bin/pycharm"])
webbrowser.get("/snap/bin/brave %s").open("https://itskola.net/")

try:
    while True:
        asyncio.run(asyncio.sleep(1))
except KeyboardInterrupt:
    print("Exiting...")


