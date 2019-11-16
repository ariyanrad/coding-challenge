'''
Input:
First line contains an integer denoting the test cases 'T'.
T testcases follow. Each testcase contains two lines of input.
First line contains N the size of the array A. 
The second line contains the elements of the array.
Output:
find the second large number in the given array

ex:
Input:
2
3
3 2 1
4
1 2 3 4
Output:
2
3
'''

iter = int(input())

output = []
for i in range(iter):
    len_list = int(input())
    nums = [int(i) for i in input().split()]
    nums.sort(reverse=True)
    output.append(int_sort[1])

for out in output:
    print('{}'.format(out), end="\n")
