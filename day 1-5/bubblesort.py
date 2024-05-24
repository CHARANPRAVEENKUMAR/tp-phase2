def performBubbleSort(nums):
    n=len(nums)
    unSortedPosition=n-1
    while unSortedPosition>0:
        for i in range(unSortedPosition):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
        unSortedPosition-=1

arr=[23,124,574,134]
print("array before sorting",arr)
performBubbleSort(arr)
print("array after sorting",arr)