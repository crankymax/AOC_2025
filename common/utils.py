from io import StringIO
from typing import Iterator, Callable

from collections import deque
from typing import Optional, Set, Deque, Any

# --- Constants for Directions ---
# (dr, dc)
ORTHOGONAL_OFFSETS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
EIGHT_WAY_OFFSETS = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1),           (0, 1),
                     (1, -1),  (1, 0),  (1, 1)]

# --- Type Aliases ---
GridPoint = tuple[int, int]
Grid = dict[GridPoint, Any] # Use Any for flexibility in puzzle solutions


# --- Core GridPoint Operations (Keep these for tuple-based approach) ---
def add_points(a: GridPoint, b: GridPoint) -> GridPoint:
    return a[0] + b[0], a[1] + b[1]


def subtract_points(a: GridPoint, b: GridPoint) -> GridPoint:
    return a[0] - b[0], a[1] - b[1]


def parse_grid(raw_grid: StringIO, val_map: Callable[[str], Any] = str) -> Grid:
    """
    Returns a dictionary of (row, col) -> value from a multi-line string input.

    Args:
        raw_grid: The StringIO containing the puzzle input.
        val_map: A function to transform the character (e.g., int, float, or a custom function).
    """
    result = {}

    for row, line in enumerate(raw_grid):
        line = line.strip()
        if not line:
            continue

        for col, c in enumerate(line):
            result[row, col] = val_map(c)

    return result


def neighbours(point: GridPoint, include_diagonals: bool = False, include_self: bool = False) -> Iterator[GridPoint]:
    """
    Yields neighbouring GridPoints based on movement type (4-way or 8-way).
    """
    offsets = EIGHT_WAY_OFFSETS if include_diagonals else ORTHOGONAL_OFFSETS

    if include_self:
        yield point

    for offset in offsets:
        yield add_points(point, offset)


def bfs_template(start_point: GridPoint, grid: dict[GridPoint, Any]) -> Optional[int]:
    """
    Finds the shortest distance from a start_point to a goal condition.

    Args:
        start_point: The starting (row, col) GridPoint.
        grid: The input grid (used implicitly for boundary/obstacle checking).

    Returns:
        The shortest distance to the goal, or None if unreachable.
    """

    # 1. Initialization
    # Queue stores (point, distance_from_start)
    queue: Deque[tuple[GridPoint, int]] = deque([(start_point, 0)])
    # Set to track visited points to prevent infinite loops and redundant checks
    visited: Set[GridPoint] = {start_point}

    while queue:
        current_point, distance = queue.popleft()

        # 2. Check Goal Condition
        # --- MODIFY THIS PART FOR EACH PUZZLE ---
        # Example Goal: If the current point is a specific 'E' tile
        if grid.get(current_point) == 'E':
            print(f"Goal reached at {current_point}!")
            return distance
        # ---------------------------------------

        # 3. Explore Neighbors
        # Use include_diagonals=True if 8-way movement is allowed
        for neighbor in neighbours(current_point, include_diagonals=False):

            # 4. Check Validity and Visit Status
            # A valid move:
            # a) Must be within the grid (i.e., neighbor in grid)
            # b) Must not be an obstacle (e.g., '#' wall, water)
            # c) Must not have been visited before

            if neighbor in grid and neighbor not in visited:
                # --- MODIFY THIS PART FOR OBSTACLE CHECKING ---
                # Example Obstacle Check: Avoid '#' tiles
                if grid[neighbor] == '#':
                    continue
                # ----------------------------------------------

                visited.add(neighbor)
                # Enqueue neighbor with distance + 1
                queue.append((neighbor, distance + 1))

    return None  # Goal was not reached


def dfs_recursive_template(start_point: GridPoint, grid: dict[GridPoint, Any], visited: Set[GridPoint]) -> bool:
    """
    Recursively explores paths from start_point. Used for reachability/connectivity.

    Args:
        start_point: The current (row, col) GridPoint.
        grid: The input grid.
        visited: The set of points visited in the current search.

    Returns:
        True if the goal is found from this path, False otherwise.
    """

    # 1. Check Boundary/Obstacle and Visit Status
    if start_point not in grid or start_point in visited:
        return False

    # --- MODIFY THIS PART FOR OBSTACLE CHECKING ---
    # Example Obstacle Check: Avoid '#' tiles
    if grid[start_point] == '#':
        return False
    # ----------------------------------------------

    # 2. Check Goal Condition
    # --- MODIFY THIS PART FOR EACH PUZZLE ---
    # Example Goal: If the current point is a specific 'E' tile
    if grid.get(start_point) == 'E':
        print(f"Goal reached at {start_point}!")
        return True
    # ---------------------------------------

    visited.add(start_point)

    # 3. Explore Neighbors
    for neighbor in neighbours(start_point, include_diagonals=False):
        if dfs_recursive_template(neighbor, grid, visited):
            return True

    return False

# Initial call setup:
# visited_points = set()
# result = dfs_recursive_template(start, my_grid, visited_points)


def dfs_iterative_template(start_point: GridPoint, grid: dict[GridPoint, Any]) -> Optional[int]:
    """
    Iteratively explores paths using a stack. Useful for complex state tracking.

    Returns:
        The distance to the goal, or None if unreachable.
    """

    # 1. Initialization
    # Stack stores (point, distance_from_start)
    stack: list[tuple[GridPoint, int]] = [(start_point, 0)]
    # Set to track visited points for simple pathfinding (can be modified for cheapest paths)
    visited: Set[GridPoint] = {start_point}

    while stack:
        current_point, distance = stack.pop()  # LIFO (Last In, First Out) for stack behavior

        # 2. Check Goal Condition (Same as BFS)
        if grid.get(current_point) == 'E':
            print(f"Goal reached at {current_point}!")
            return distance

        # 3. Explore Neighbors (often in reverse order of desired exploration)
        for neighbor in neighbours(current_point, include_diagonals=False):

            # 4. Check Validity and Visit Status (Same as BFS)
            if neighbor in grid and neighbor not in visited:
                if grid[neighbor] == '#':
                    continue

                visited.add(neighbor)
                # Push neighbor onto the stack
                stack.append((neighbor, distance + 1))

    return None