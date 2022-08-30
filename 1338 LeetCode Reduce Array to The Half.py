#My Solution-gives tle but answer is always right
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        occ = []
        nums = list(set(arr))
        for i in nums:
            occ.append(arr.count(i))
        num_occ = dict(zip(nums,occ))
        set1 = set()
        half = len(arr)//2
        while len(arr)>half:
            max_key = max(num_occ,key=num_occ.get)
            set1.add(max_key)
            arr = list(filter(lambda x: x != max_key, arr))
            #arr = [x for x in arr if x !=max_key]
            del num_occ[max_key]
        return len(set1)
#NON TLE solution
     n = len(arr)
        count = Counter(arr).most_common()
        count.sort(key=lambda c: -c[1])
        sum = 0
        for i, c in enumerate(count):
          sum += c[1]
          if sum >= n // 2:
            return i + 1
