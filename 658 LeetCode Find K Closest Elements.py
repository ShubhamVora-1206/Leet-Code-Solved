class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
		# first binary search where the value 'x' should be in the sorted array
        n = len(arr)
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == x:
                start, end = mid - 1, mid + 1
                k -= 1
                break
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
                
        if low > high:
            start = high
            end = low
        #  after we found where 'x' should be in the sorted array we expand to the left and to the right to find the next values until k (using two pointers start, end)
        while k > 0:
            if start == -1:
                end += 1
            elif end == n:
                start -= 1
            else:
                if abs(arr[start] - x) <= abs(arr[end] - x):
                    start -= 1
                else:
                    end += 1
            k -= 1
        return arr[start + 1:end]        
