""" This program is designed to test the functions of io_utils.py """
import pytest
from assignment4.io_utils import mkdir_from_infile


def test_mkdir_from_infile_existing_directory(tmp_path):
    """ Test case for existing directory """
    existing_dir = tmp_path / "existing_dir"
    existing_dir.mkdir()
    file_path = existing_dir / "test.txt"
    mkdir_from_infile(str(file_path))
    assert existing_dir.exists()


def test_mkdir_from_infile_create_directory(tmp_path):
    """ Test case for creating a new directory """
    new_dir = tmp_path / "new_dir"
    file_path = new_dir / "test.txt"
    mkdir_from_infile(str(file_path))
    assert new_dir.exists()


def test_mkdir_from_infile_os_error(tmp_path, monkeypatch):
    """Test case for OSError """
    def mock_os_mkdir(path, mode):
        raise OSError("Mock OS Error")

    monkeypatch.setattr("os.mkdir", mock_os_mkdir)

    dir_path = tmp_path / "directory"
    file_path = dir_path / "test.txt"
    with pytest.raises(OSError):
        mkdir_from_infile(str(file_path))
