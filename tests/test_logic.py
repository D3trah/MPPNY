import pytest

def fitness_level(reps):
    return "Profi" if reps >= 15 else "Kezdő"

@pytest.mark.parametrize("reps, expected", [
    (20, "Profi"),
    (5, "Kezdő"),
    (15, "Profi"),
])
def test_fitness_logic(reps, expected):
    assert fitness_level(reps) == expected