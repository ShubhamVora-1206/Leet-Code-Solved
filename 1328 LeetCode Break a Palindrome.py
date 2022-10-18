class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)<=1:
            return ''
        if palindrome!=palindrome[::-1]:
            print(palindrome,palindrome[::-1])
            return ''
        cmin='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
        for i in range(len(palindrome)):    
            x = list(palindrome)
            for j in range(97,123):
                x[i] = chr(j)
                rejoin = ''.join(x)
                if rejoin!=palindrome and rejoin!=rejoin[::-1]:
                    cmin = min(cmin,rejoin)
        return cmin
