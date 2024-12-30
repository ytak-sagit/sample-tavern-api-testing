def test_add_1_to_2_then_3():
    # Arrange

    # Act
    actual = _add(1, 2)

    # Assert
    assert 3, actual

def _add(augend, addend):
    augend + addend
