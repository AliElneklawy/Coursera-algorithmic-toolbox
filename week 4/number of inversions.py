
# calculate number of inversions in an array until it is sorted
def inversions(arr):
    if len(arr) == 1:
        return 0
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        return inversions(left) + inversions(right) + merge(left, right)
def merge(left, right):
    count = 0
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            i += 1
        else:
            count += len(left) - i
            j += 1
    return count




# def Merge(nums, l, m, r):
#     noOfInversions = 0
#     left_arr = nums[l:m+1]
#     right_arr = nums[m+1:r+1]
#     left_cnter, right_cnter, srted_cnter = 0, 0, l

#     while left_cnter < len(left_arr) and right_cnter < len(right_arr):
#         if left_arr[left_cnter] <= right_arr[right_cnter]:
#             nums[srted_cnter] = left_arr[left_cnter]
#             left_cnter +=1
#             # noOfInversions +=1
#         else:
#             nums[srted_cnter] = right_arr[right_cnter]
#             right_cnter +=1
#             # noOfInversions +=1
#         srted_cnter +=1

#     while left_cnter < len(left_arr):
#         nums[srted_cnter] = left_arr[left_cnter]
#         left_cnter +=1
#         srted_cnter +=1

#     while right_cnter < len(right_arr):
#          nums[srted_cnter] = right_arr[right_cnter]
#          right_cnter +=1
#          srted_cnter +=1


#     return noOfInversions

# def inversions(nums, l, r):
#     if l < r:
#         q = (l+r)//2
#         inversions(nums, l, q)
#         inversions(nums, q+1, r)
#         invs = Merge(nums, l, q, r)
#         return invs

# calculate the number of inversions in an array until it is sorted



num_elems = int(input())
nums = list(map(int, input().split()))
assert num_elems == len(nums)
print(inversions(nums))