import socket
import platform
from datetime import datetime

def main():
    print("Dockerized Python App Running")
    print("-" * 40)
    print(f"Hostname      : {socket.gethostname()}")
    print(f"OS            : {platform.system()} {platform.release()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Current Time  : {datetime.now()}")
    print("-" * 40)

if __name__ == "__main__":
    main()
