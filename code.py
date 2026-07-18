class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d={}
        s=[]
        n=len(nums)
        for num in nums:
            d[num]=1
        for i in range(1,n+1):
            if i not in d:
                s.append(i)
        return s


            

                
        



        
