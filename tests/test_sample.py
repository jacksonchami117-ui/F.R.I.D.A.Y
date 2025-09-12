"""Basic test to verify testing infrastructure works."""

def test_sample():
    """Sample test that always passes."""
    assert True


def test_basic_math():
    """Test basic arithmetic."""
    assert 2 + 2 == 4


def test_string_operations():
    """Test basic string operations."""
    assert "hello".upper() == "HELLO"
    assert len("test") == 4