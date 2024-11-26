#Array Modifier

nums = [int(i) for i in input().split(' ')]
cmd = input()

while cmd != "end":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]
    if action == "swap":
        index1 = int(cmdSplit[1])
        index2 = int(cmdSplit[2])
        if 0 <= index1 < len(nums) and 0 <= index2 < len(nums):
            value1 = nums[index1]
            value2 = nums[index2]
            nums[index1] = value2
            nums[index2] = value1
    if action == "multiply":
        index1 = int(cmdSplit[1])
        index2 = int(cmdSplit[2])
        if 0 <= index1 < len(nums) and 0 <= index2 < len(nums):
            value1 = nums[index1]
            value2 = nums[index2]
            nums[index1] = (value1 * value2)
    if action == "decrease":
        nums = [(i - 1) for i in nums]
    cmd = input()

numsToString = [str(i) for i in nums]
print (f"{', '.join(numsToString)}")