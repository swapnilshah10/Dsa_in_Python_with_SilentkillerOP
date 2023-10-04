from collections import defaultdict

def max_points_on_a_line(points):
    if len(points) < 2:
        return len(points)

    max_points = 0

    for i in range(len(points)):
        slopes = defaultdict(int)
        duplicates = 0
        local_max = 0

        for j in range(i+1, len(points)):
            if points[i] == points[j]:
                duplicates += 1
            else:
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                gcd = gcd_helper(dx, dy)
                slope = (dx // gcd, dy // gcd)
                slopes[slope] += 1
                local_max = max(local_max, slopes[slope])

        max_points = max(max_points, local_max + duplicates + 1)

    return max_points

def gcd_helper(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
points = [(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (3, 2), (4, 2)]
result = max_points_on_a_line(points)
print("Maximum number of points on a line:", result)
