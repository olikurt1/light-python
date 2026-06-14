def twoSum(nums, target):
        #first number looking for its pair
        for x in range(len(nums)):
            #runs through the list of numbers again except for the number that is looking for its pair
            for y in range(x+ 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return (nums[x], nums[y])
 