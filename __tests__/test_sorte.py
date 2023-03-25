from main import sorte


def test_sorte():
    assert list(sorte([2, 3, 1])) == [1, 2, 3]
    assert list(sorte([2, 9, 3, 1])) == [1, 2, 3, 9]
    assert list(sorte([1, 6, 7, 1, 2])) == [1, 1, 2, 6, 7]
    assert list(sorte([4, 3, 4, 3, 1, 3, 2])) == [1, 2, 3, 3, 3, 4, 4]
    assert list(sorte([3, 1, 2, -4, 4, 1])) == [-4, 1, 1, 2, 3, 4]
