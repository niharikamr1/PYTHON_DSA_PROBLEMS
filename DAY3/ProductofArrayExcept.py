def productExceptSelf(nums):

    n = len(nums)

    answer = [1] * n
    # Prefix products
    prefix = 1

    for i in range(n):
        answer[i] = prefix
        prefix = prefix * nums[i]


    # Suffix products
    suffix = 1

    for i in range(n-1,-1,-1):
        answer[i] = answer[i] * suffix
        suffix = suffix * nums[i]


    return answer


nums = [1,2,3,4]

print(productExceptSelf(nums))