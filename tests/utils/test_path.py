import os
import tempfile
from maestral.utils.path import path_exists_case_insensitive, is_child, delete


def test_path_exists_case_insensitive():
    # choose a path which exists on all Unix systems
    path = '/usr/local/share'

    assert path_exists_case_insensitive(path) == path
    assert path_exists_case_insensitive(path.title()) == path
    assert path_exists_case_insensitive(path.upper()) == path

    # choose a random path that likely does not exist
    path = '/usr/local/share/test_folder/path_928'
    if not os.path.exists(path):
        assert not path_exists_case_insensitive(path)


def test_is_child():
    assert is_child('/parent/path/child', '/parent/path/')
    assert is_child('/parent/path/child/', '/parent/path')
    assert not is_child('/parent/path', '/parent/path')
    assert not is_child('/path1', '/path2')


def test_delete():
    # test deleting file
    test_file = tempfile.NamedTemporaryFile()
    assert os.path.isfile(test_file.name)
    delete(test_file.name)
    assert not os.path.exists(test_file.name)

    # test deleting directory
    test_dir = tempfile.TemporaryDirectory()
    assert os.path.isdir(test_dir.name)
    delete(test_dir.name)
    assert not os.path.exists(test_dir.name)
