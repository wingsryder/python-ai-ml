'''
Title: Custom Sorting by Frequency

Question:
Given a list of integers, sort the list such that the integers appear in increasing order of their frequency.
If two numbers have the same frequency, the one which appeared first in the original list should come first.

Explanation/Description:
You need to sort a list of integers based on how frequently each number appears.
Numbers that appear less frequently should come first.
If two numbers have the same frequency, their order in the original list should be preserved.
The task requires implementing custom sorting logic without using any external libraries or the built-in sort() function.

Input Format:
The first line contains an integer n, the number of elements in the list.
The second line contains n space-separated integers representing the list.

Output Format:
A single line containing the sorted list, with elements separated by spaces

Sample:
6
[4,5,6,5,4,3]

Output:
6 3 4 4 5 5

Hint:
You need to sort a list of integers based on how frequently each number appears. Numbers that appear less frequently should come first. If two numbers have the same frequency, their order in the original list should be preserved. The task requires implementing custom sorting logic without using any external libraries or the built-insort()function.

Hint: used bubble sort algorithm

'''

def solve(n, nums):
  freq_map = {}

  # Compute frequency of each element
  for num in nums:
    if num in freq_map:
      freq_map[num] += 1
    else:
      freq_map[num] = 1

  # Sorting part
  for i in range(n):
    for j in range(n-i-1):
      if (freq_map[nums[j]] > freq_map[nums[j+1]]) or (freq_map[nums[j]] == freq_map[nums[j+1]] and nums.index(nums[j]) > nums.index(nums[j+1])):
        nums[j] , nums[j+1] = nums[j+1], nums[j]

  return nums

#Call
g = solve(6,[4, 5, 6, 5, 4, 3])

#Format
c = ' '.join(str(num) for num in g)
print(c)