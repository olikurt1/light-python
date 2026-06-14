def twoSum(nums, target):
       #dicitionary to hold a value thats already been seen 
        seen = {}
        #first number looking for its pair
        for num in nums:
            #complement is automatically the right number for the current iteration num to make correct pair 
            complement = target - num
            #so if complement is in seen then can immediately return
            if complement in seen:
                return (complement, num)
            #always add current number to seen as it has been seen even if incorrect and can be used for future referece
            seen[num] = True
        return None
          