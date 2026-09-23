class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        if len(strs)>0:
            for st in strs:
                encoded += f'{len(st)}#{st}'
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == '': # original list is empty
            return []

        decoded = []
        sub_len = ''
        i = 0
        while i < len(s):
            if 48 <= ord(s[i]) <= 57: # if it is a digit
                sub_len += s[i]
                i +=1
            elif ord(s[i])==35: # meet "#"
                decoded.append(s[i+1 : i+1+int(sub_len)])
                i = i+1+int(sub_len)
                sub_len = ''
        return decoded

