import os
import sys
from pathlib import Path

path = str(Path(f"{os.path.dirname(os.path.realpath(__file__))}/mcpy").absolute())
sys.path.append(path)
print(path)
