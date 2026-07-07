"""Basic smoke tests for project setup."""
from namus.config import PROJECT_ROOT, DATA_RAW


def test_project_root_exists():
    assert PROJECT_ROOT.exists()
    assert PROJECT_ROOT.name == "NamUs" or PROJECT_ROOT.name.endswith("NamUs")


def test_data_dirs_configured():
    assert DATA_RAW.exists()
