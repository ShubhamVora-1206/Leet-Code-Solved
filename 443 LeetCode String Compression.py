class Solution(object):
    def compress(self, chars):
        n = len(chars)
        if n == 1:
            return 1
        
        write_idx = 0
        curr_idx = 0
        while curr_idx < n:
            curr_char = chars[curr_idx]
            cnt = 0
            while curr_idx < n and chars[curr_idx] == curr_char:
                curr_idx += 1
                cnt += 1
            chars[write_idx] = curr_char
            write_idx += 1
            if cnt > 1:
                cnt_str = str(cnt)
                for i in range(len(cnt_str)):
                    chars[write_idx] = cnt_str[i]
                    write_idx += 1
        
        return write_idx
