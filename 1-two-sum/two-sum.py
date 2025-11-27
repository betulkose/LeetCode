class Solution(object):
    def twoSum(self, nums, target):
        
        gorulen_sayi= {}

        indeks=0
        while indeks < len(nums):
            sayi = nums[indeks]
            gereken_sayi= target - sayi

            if gereken_sayi in gorulen_sayi:
                return [gorulen_sayi[gereken_sayi],indeks] 
            
            gorulen_sayi[sayi]=indeks
            indeks +=1

        