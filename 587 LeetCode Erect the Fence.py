def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        """
        Use Monotone Chain algorithm.
        """
        def is_clockwise(
                p0: List[int], p1: List[int], p2: List[int]) -> bool:
            """
            Determine the orientation the slope p0p2 is on the clockwise
            orientation of the slope p0p1.
            """
            return (p1[1] - p0[1]) * (p2[0] - p0[0]) > \
                (p2[1] - p0[1]) * (p1[0] - p0[0])

        sortedPoints = sorted(points)

        # Scan from left to right to generate the lower part of the hull.
        hull = []
        for p in sortedPoints:
            while len(hull) > 1 and is_clockwise(hull[-2], hull[-1], p):
                hull.pop()

            hull.append(p)

        if len(hull) == len(points):  # All the points are on the perimeter now.
            return hull

        # Scan from right to left to generate the higher part of the hull.
        # Remove the last point first as it will be scanned again.
        hull.pop()
        for p in reversed(sortedPoints):
            while len(hull) > 1 and is_clockwise(hull[-2], hull[-1], p):
                hull.pop()

            hull.append(p)

        # Pop the first point as it is already added to hull when processing
        # the lower part.
        hull.pop()

        return hull
