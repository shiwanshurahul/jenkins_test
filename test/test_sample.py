from app.app_core import *

#Because Python resolves imports based on the project root, 
#NOT the folder of the test file.

# your-python-project/
# │
# ├── app.py
# ├── requirements.txt
# ├── tests/
# │     └── test_sample.py
# └── Jenkinsfile

# pytest automatically adds the project root to PYTHONPATH.

# your-python-project/ is added to Python's import search path.
# So Python can find app.py from anywhere.


def test_add():
    assert add(2, 3) == 5

def test_mult():
    assert multiply(2, 3) == 6 

def test_multiply():
    assert multiply(4, 6) == 12 
