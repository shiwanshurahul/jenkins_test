from app.add import *
from app.mult import *
from app.subtract import subtract

#Because Python resolves imports based on the project root, 
#NOT the folder of the test file.

# your-python-project/ here,jenins_test
# │
# ├── app/
# │     └── add.py
# |     └── mult.py
# |     └── subtract.py
# ├── requirements.txt
# ├── tests/
# │     └── test_sample.py  -> import app.core.py
# └── jenkinsfile

# pytest automatically adds the project root to PYTHONPATH.

# your-python-project/ is added to Python's import search path.
# So Python can find app.py from anywhere.


def test_add():
    assert add(2, 3) == 5

def test_mult():
    assert multiply(2, 3) == 6 

def test_multiply():
    assert multiply(4, 6) == 24  #shoudn't pass

def test_subtract():
    assert subtract(12, 8) == 4    

#By default, any non-zero exit code from a command fails the Jenkins stage, 
#which is why your build shows ERROR when a test fails.

#PYTHONPATH is an environment variable that Python uses to search for modules and
#packages when you import them.
# By default, Python searches in:
# The current directory
# Standard library directories
# Directories in PYTHONPATH (if set)

# Setting PYTHONPATH allows Python to find modules in custom directories that are not installed globally
# or in the current directory.

# %WORKSPACE% is a Jenkins environment variable.
# It points to the root directory of your job's workspace (where your code is checked out on the Jenkins agent).

# set PYTHONPATH=%WORKSPACE%
# Tells Python: “When importing modules, also look in the Jenkins workspace folder.”
# Useful if your Python scripts or tests import modules from your project directory

#set PYTHONPATH=%WORKSPACE% → Add your Jenkins workspace directory to Python’s module search path
# so that Python can import your project’s modules during tests or script execution.

#better alternative -> wheel, setup.py . here, no use of PYTHONPATH