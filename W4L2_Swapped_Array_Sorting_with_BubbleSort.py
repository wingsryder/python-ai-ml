'''
Title : Swapped Array Sorting with Bubble Sort

Description:
You are given an array of integers where exactly two elements are swapped from their correct positions. Your task is to sort the array using a modified version of Bubble Sort that detects and corrects the swapped elements in the minimum number of iterations.

Input Description:
A single line containing space-separated integers, which represent the unsorted arraynumswhere exactly two elements are swapped.

Output Description:
A single line containing the sorted array, with elements separated by spaces.

Sample Input:
[1,2,6,4,5,3,7,8]

Sample Output:
[1,2,3,4,5,6,7,8]

'''

def solve(nums):
  n = len(nums)
  for i in range(n-1):
    for j in range(n-i-1):
      if nums[j] > nums[j+1]:
        nums[j],nums[j+1] = nums[j+1],nums[j]
  return nums


solve([1, 2, 6, 4, 5, 3, 7, 8])

