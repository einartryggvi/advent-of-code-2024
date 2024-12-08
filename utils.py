
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def points_collinear(a, b, c):
    # Returns True if the slopes of (a, b) and (a, c) are the same
    return (b[1] - a[1]) * (c[0] - a[0]) == (c[1] - a[1]) * (b[0] - a[0])
