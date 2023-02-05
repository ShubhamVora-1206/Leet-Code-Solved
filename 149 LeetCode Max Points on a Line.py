class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        if len(points)<=2: return len(points)
        
        # Line equation: y = slope * x + b
        # Given two points, solve for slope and b
        # The slope of a vertical line is undefined, and the form is x = a, 
        # Where a is the x-intercept, so return (x)
        def line(p1,p2):
            # Vertical line
            if p2[0]-p1[0] == 0:
                return (p1[0])
            slope = (p2[1]-p1[1]) / (p2[0]-p1[0])                
            b = p1[1] - slope * p1[0]
            return (slope,"%.5f" % b) #Floating Point has issues and limitations, using floating point as hash key isn't a good iead, so round it up a little bit. Check the comment below for the issue.

        res = 0
        # Let each point be the start point.
        # Check the lines formed using other points as the end point.
        # Only the distinct line equation matters here (Using hash map to count). 
        # We want to count how many points are in each line euqation.
        # Update the result with the maximum number of points in a line euqation.
        for i in range(len(points)):
            count = defaultdict(int)
            for j in range(i+1,len(points)):
                count[line(points[i],points[j])] += 1
            if count:
                res = max(res,max(count.values()))
        
        # We didn't count the start point, so +1 here.
        return res + 1
