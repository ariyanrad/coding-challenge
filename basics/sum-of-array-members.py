'''
Input:
First line contains an integer denoting the test cases 'T'.
T testcases follow. Each testcase contains two lines of input.
First line contains N the size of the array A. 
The second line contains the elements of the array.

Output:
For each testcase, print the sum of all elements of the array in separate line.

ex:
Input:
2
3
3 2 1
4
1 2 3 4
Output:
6
10
'''
user = int(input())
output = []
for i in range(user):
    len_list = int(input())
    nums = [int(i) for i in input().split()]
    output.append(sum(num))

for out in output:
    print('{}'.format(out), end="\n")
