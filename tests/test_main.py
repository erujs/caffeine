from caffeine_py.main import matrix_line


def test_matrix_line_length():
    assert len(matrix_line(80)) == 80


def test_matrix_line_default_length():
    assert len(matrix_line()) == 80
