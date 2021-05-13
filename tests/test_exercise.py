import pytest
from src.exercise import main

def test_exercise(capsys):
    main()
    output = []
    output,err = capsys.readouterr()

    assert output == "Chicken:\n9000\nBacon (kg):\n0.1\nTractor:\nZero\n\nAnd finally, a summary:\n3\n5.5\nZero\n"
