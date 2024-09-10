'''
Title: Kth Smallest Element with Restrictions

Question:
Given an unsorted list of integers, find the kth smallest element without using thesort()function. Implement the selection algorithm to achieve this.

Input Description:
The first line contains an integern, the number of elements in the list.
The second line containsnspace-separated integers representing the listnums.
The third line contains an integerk, representing the position of the smallest element to find.

Output Description:
A single integer representing the kth smallest element.

Sample:
6
7 10 4 3 20 15
3

Output:
7

Hint: used selection sort algorithm
'''

def solve(n, nums, k):
    for i in range(n):
      min_index = i
      print("OuterLoop :")
      for j in range(i+1,n):
        print(" InnerLoop :",j)
        if nums[j] < nums[min_index] :
          min_index = j

      nums[i],nums[min_index] = nums[min_index] ,nums[i]

    #print(nums)
    return nums[k-1]

# result
solve(6,[7, 10, 4, 3, 20, 15],3)