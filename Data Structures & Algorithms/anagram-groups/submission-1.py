class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        gp_map = defaultdict(list) # new key default value list

        for word in strs:
            count = [0] * 26  # 26 alphabet array

            for s in word:
                count[ord(s)-ord('a')] +=1

            gp_map[tuple(count)].append(word)

        return list(gp_map.values())


