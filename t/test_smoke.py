from pathlib import Path


def test_repository_has_book_docs():
    assert Path("docs/book.html").is_file()


def test_short_package_directories_exist():
    assert Path("src/an").is_dir()
    assert Path("src/tx").is_dir()
    assert Path("ta").is_dir()
    assert Path("kad").is_dir()