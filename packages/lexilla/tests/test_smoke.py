import lexilla
from lexilla import _lexilla


def test_version():
    assert lexilla.__version__


def test_extension_loads():
    assert _lexilla.smoke_test() == "lexilla"
