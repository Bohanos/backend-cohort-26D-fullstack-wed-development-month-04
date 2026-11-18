# whereami.py: shows which Python is running this file

import sys
print("Python running:", sys.executable)
print("Inside a venv?:", sys.prefix != sys.base_prefix)