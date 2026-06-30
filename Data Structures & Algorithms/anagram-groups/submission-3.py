class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            strs

        sol = {}

        for i in strs:
            key = "".join(sorted(i))

            if key not in sol:
                sol[key] = []
            
            sol[key].append(i)

        return list(sol.values())

        