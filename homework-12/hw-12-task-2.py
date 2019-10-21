nums = [23, 23, 33, 22, -32, 32, -21, 23]

def remove_positives(nums):
    return [num for num in nums if num < 0]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

def func_choose(nums, func1, func2):

    if any(n < 0 for n in nums):
        return func2(nums)
    else:
        return func1(nums)
    # for num in nums:
    #     if num < 0:
    #         f = func2
    #     else:
    #         f = func1
    # return f(nums)


print(func_choose(nums, remove_positives, remove_negatives))
