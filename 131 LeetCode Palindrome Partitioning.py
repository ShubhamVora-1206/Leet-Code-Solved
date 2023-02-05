class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] # vector to store all possible partitions
        path = [] # vector to store current partition
        self.func(0, s, res, path) # call helper function to start recursion
        return res

    # helper function that uses recursion to find all possible partitions
    def func(self, ind, s, res, path):
        if ind == len(s): # base case: if we have reached the end of the string
            res.append(path[:]) # add current partition to the result vector
            return 
        for i in range(ind, len(s)): # iterate through all substrings starting from the current index
            if self.isPalindrome(s, ind, i): # check if the current substring is a palindrome
                path.append(s[ind:i+1]) # if it is, add it to the current partition
                self.func(i+1, s, res, path) # call function recursively with the next index as the starting point
                path.pop() # backtrack to check for other partitions

    # helper function that checks if a substring is a palindrome
    def isPalindrome(self, s, start, end):
        while start <= end: # iterate through the substring
            if s[start] != s[end]: # check if current characters are not equal
                return False # if they are not, return false
            start += 1
            end -= 1
        return True # if we reach this point, the substring is a palindrome
