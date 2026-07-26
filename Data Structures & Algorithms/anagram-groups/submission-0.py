class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        gp_map = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in gp_map:
                gp_map[key] = []
            
            gp_map[key].append(word)

        return list(gp_map.values())
        