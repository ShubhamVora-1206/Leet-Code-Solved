from functools import cmp_to_key

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        def compare(a, b):
            p1, g1 = a
            p2, g2 = b
            
            return (p1 + max(p2+g2, g1)) - (p2 + max(p1+g1, g2))
        
        plant_grow_time = list(zip(plantTime, growTime))
        plant_grow_time.sort(key=cmp_to_key(compare))
        
        latest = 0
        current = 0
        for p, g in plant_grow_time:
            latest = max(latest, p+g+current)
            current+=p
            
        return latest
