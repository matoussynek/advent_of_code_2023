memory = {}

def count_options(springs, nums, block=False):
    def helper():
        if springs == "":
            return 1 if sum(nums) == 0 else 0
        
        if sum(nums) == 0:
            return 1 if not '#' in springs else 0
        
        if springs[0] == '#':
            if block and nums[0] == 0:
                return 0
            return count_options(springs[1:], (nums[0] - 1, *nums[1:]), True)

        if springs[0] == '.':
            if block and nums[0] > 0:
                return 0
            return count_options(springs[1:], nums[1:] if nums[0] == 0 else nums, False)
        
        if block:
            if nums[0] == 0:
                return count_options(springs[1:], nums[1:], False)
            return count_options(springs[1:], (nums[0] - 1, *nums[1:]), True)
        
        return count_options(springs[1:], nums, False) + count_options(springs[1:], (nums[0] - 1, *nums[1:]), True)

    key = (springs, nums, block)
    if not key in memory:
        memory[key] = helper()
    return memory[key]

tot = 0
tot2 = 0
for line in open('./input.txt').readlines():
    springs, nums = line.split()
    springs2 = '?'.join([springs] * 5)
    nums = tuple(map(int, nums.split(",")))
    nums2 = nums * 5
    tot += count_options(springs, nums)
    tot2 += count_options(springs2, nums2)

print('Total number of options:', tot)
print('Total number of options unfolded:', tot2)