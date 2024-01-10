def containsDuplicate(nums) -> bool:
    temp = set(nums)
    if len(temp) != len(nums):
        return True
    return False
