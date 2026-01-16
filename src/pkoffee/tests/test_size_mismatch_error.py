import pytest


def test_size_mismatch_error_message():
    """
    Verify that SizeMismatchError generates a clear and deterministic error message.

    What is tested:
        The string representation of the SizeMismatchError instance.

    Why it matters:
        Error messages are part of the public API. A stable and explicit message
        helps users quickly diagnose input shape issues and allows downstream
        code (or tests) to rely on predictable error reporting.

    Expected behavior:
        The error message must include both input sizes and follow the exact
        expected format.
    """
    from pkoffee.metrics import SizeMismatchError

    err = SizeMismatchError(10, 12)

    assert str(err) == "Arrays must have same length, got 10 and 12"


def test_size_mismatch_error_is_value_error():
    """
    Verify that SizeMismatchError is a subclass of ValueError.

    What is tested:
        The inheritance relationship between SizeMismatchError and ValueError.

    Why it matters:
        Many numerical and scientific workflows catch ValueError to handle
        invalid inputs generically. Ensuring correct inheritance preserves
        compatibility with such error-handling patterns.

    Expected behavior:
        A SizeMismatchError instance must be recognized as a ValueError.
    """
    from pkoffee.metrics import SizeMismatchError

    err = SizeMismatchError(1, 2)

    assert isinstance(err, ValueError)


def test_size_mismatch_error_can_be_raised():
    """
    Verify that SizeMismatchError can be raised and caught as expected.

    What is tested:
        The ability to raise SizeMismatchError and retrieve its message through
        pytest's exception handling utilities.

    Why it matters:
        This test validates the intended usage pattern of the exception in
        real-world code paths where size checks fail and an explicit error
        must be propagated to the caller.

    Expected behavior:
        Raising SizeMismatchError must be caught by pytest.raises, and the
        resulting exception message must contain the provided input sizes.
    """
    from pkoffee.metrics import SizeMismatchError

    with pytest.raises(SizeMismatchError) as excinfo:
        raise SizeMismatchError(3, 5)

    assert "got 3 and 5" in str(excinfo.value)
