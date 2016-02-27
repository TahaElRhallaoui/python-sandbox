from nose.tools import raises


def test_pass():
    """Do nothing."""
    pass


def test_false_assert():
    """Test false assertion."""
    assert 1 > 2


@raises(EnvironmentError)
def test_raise_exception():
    """Test exception raising."""
    raise EnvironmentError
