class Solution(object):
    def removeDuplicates(self, nums):
        
        if not nums:
            return 0

        yazici = 1

        for okuyucu in range(1,len(nums)):

            if nums[okuyucu] != nums[okuyucu-1]:

                nums[yazici] = nums[okuyucu]
                yazici += 1
        return yazici           

                

