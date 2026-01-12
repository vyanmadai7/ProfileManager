import sys
from core.login_manager import login

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python main.py <profile_name>")
    else:
        login(sys.argv[1])
