def sortColors( nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count0,count1,count2=0,0,0
        for num in nums:
            if num==0:
                count0+=1
            elif num==1:
                count1+=1
            else:
                count2+=1
        l0=[0]*count0
        l1=[1]*count1
        l2=[2]*count2
        nums=l0+l1+l2
        return nums
print(sortColors([2,0,2,1,1,0,1,2,0] ))