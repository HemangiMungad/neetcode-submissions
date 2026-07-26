class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nmap = {}
        nlist = []
        s_nlist=[]
        final_nlist = set()

        for i in nums:

            if i not in nmap:
                nmap[i] = 1
            else:
                nmap[i] +=1

        for x in nmap:
                nlist.append(nmap[x])

        nlist.sort(reverse=True)

        s_nlist =  nlist[0:k] 

        for i in s_nlist:
            for j in nmap:
                if i == nmap[j]:
                    final_nlist.add(j)
        return list(final_nlist)
            


        




        