from distutils.core import setup
import py2exe
import os
import re
from pathlib import Path
import sqlite3
from random import randrange
from time import sleep
import glob

# instead of writing console, write "windows" so that it runs in a window
setup(zipfile=None,
      options={'py2exe': {"bundle_files": 1}},
      console=["tets_txt.py"])
