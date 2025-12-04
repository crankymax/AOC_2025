from io import StringIO

from common.utils import parse_grid


def test_parse_grid():
    RAW_INPUT = """
    S...#
    .#..
    .##E
    ....
    """

    # The grid dictionary we will use (4x4)
    test_input = StringIO(RAW_INPUT.strip())
    grid = parse_grid(test_input)
    assert len(grid) > 0
    START_POINT = (0, 0)
    GOAL_POINT = (2, 3)  # The location of 'E'




