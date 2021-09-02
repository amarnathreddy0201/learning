"""
if we want to report of the file in xml format
pytest -rA --junitxml="filename.xml"

if we want to report of the file in html format
pytest --html=filename.html
"""


def test_responcecode200():
    print("API working fine")




def test_responcecode400():
    print("API Notworking fine")