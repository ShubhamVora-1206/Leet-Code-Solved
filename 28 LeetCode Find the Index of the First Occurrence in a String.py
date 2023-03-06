class Solution:
    def strStr(self, string: str, substring: str) -> int:
        n, m = len(string), len(substring)
        if m > n:
            return -1
        prime = 31
        MOD = 10**9 + 7
        substring_hash = 0
        string_hash = 0
        power = 1

        # Compute hash value of substring
        for i in range(m):
            substring_hash = (substring_hash * prime + ord(substring[i]) - ord('a') + 1) % MOD
            string_hash = (string_hash * prime + ord(string[i]) - ord('a') + 1) % MOD
            if i < m - 1:
                power = (power * prime) % MOD

        # Check if substring is found in string
        for i in range(n - m + 1):
            if substring_hash == string_hash and string[i:i+m] == substring:
                return i
            if i < n - m:
                string_hash = ((string_hash - (ord(string[i]) - ord('a') + 1) * power % MOD + MOD) % MOD * prime % MOD + ord(string[i+m]) - ord('a') + 1) % MOD

        return -1
