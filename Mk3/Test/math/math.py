a = input("What is your question:\n")
nums = list(a)
unwanted_num = {"+", " ", "/", "*", "-"}
if '+' in nums:
    nums = [ele for ele in nums if ele not in unwanted_num]
    print("It is " + str(int(nums[0]) + int(nums[1])))
if '-' in nums:
    nums = [ele for ele in nums if ele not in unwanted_num]
    print("It is " + str(int(nums[1]) - int(nums[0])))
if "*" in nums:
    nums = [ele for ele in nums if ele not in unwanted_num]
    print("It is " + str(int(nums[0]) * int(nums[1])))
if '/' in nums:
    nums = [ele for ele in nums if ele not in unwanted_num]
    print("It is " + str(int(nums[0]) / int(nums[1])))
