from utils import *

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    flat_list = [j for i in unitlist for j in i]

    grid_list = [j for i,j in enumerate(grid)]

    ### Another implementation:
    """
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(boxes, grid))

    """
    sdkdict = {flat_list[i]: grid_list[i] for i in range(81)}

    for i,j in sdkdict.items():
        if j == '.':
            sdkdict[i] = '123456789'

    return sdkdict


display(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))
