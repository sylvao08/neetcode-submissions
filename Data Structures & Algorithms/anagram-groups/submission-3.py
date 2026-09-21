class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for st in strs:
            # turn st into letter counts {'a':1, 'c':2}
            seen_lt = {l:0 for l in 'abcdefghijklmnopqrstuvwxyz'}
            for l in st.lower():
                seen_lt[l] += 1
            
            # if it is in seen, then append
            seen_lt = "-".join(map(str, seen_lt.values()))
            if seen_lt in seen:
                seen[seen_lt].append(st)
            else:
                seen[seen_lt] = [st]
            # else add a new entry to seen
        # return the list under each key
        return list(seen.values())



        