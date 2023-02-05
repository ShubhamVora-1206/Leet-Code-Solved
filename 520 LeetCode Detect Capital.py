class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)<=1:return True
        if word[0].isupper() and word[1].isupper():
            print("1st")
            for i in word:
                if i.islower():
                    return False
        if word[0].isupper() and not word[1].isupper():
            print("2nd")
            for i in word[1:]:
                if i.isupper():
                    return False
        if not word[0].isupper():
            print("3rd")
            for i in word:
                if i.isupper():
                    return False
        return True
