
"""
на плоскости дано N точек c целыми координатами. 
Нужно ответить, сколько равнобедренных треугольников можно построить, 
проводя отрезки между данными точками.

The program takes the following inputs:
- N: the number of points on the plane (3 ≤ N ≤ 3000)
- T: the type of problem:
    - If T = 1, the program calculates the number of isosceles triangles that can be formed.
    - If T = 2, the program calculates the number of equilateral triangles that can be formed.

The program then takes N lines of input, where each line contains the coordinates of a point on the plane: (xi, yi) (-10^9 ≤ xi, yi ≤ 10^9).

The program outputs the number of isosceles or equilateral triangles that can be formed based on the given inputs.
"""

from collections import defaultdict
from math import dist

N = int(4)
Type = int(1)
ListPoint = [(1, 1), (0, 1), (0, 0), (1, 0)]

def isoscaled(ListP : list) -> int:
    count = 0
    for point1 in ListP:
        distance_count = defaultdict(int)
        for point2 in ListP:
            if point1 != point2:
                distance = dist(point1, point2)
                distance_count[distance] +=1
        for distance in distance_count:
            count+= distance_count[distance]*(distance_count[distance] - 1) // 2
    return count

print(isoscaled(ListPoint))



