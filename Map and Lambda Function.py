'''
Input Format

One line of input: an integer N .

Constraints

0 <= N <= 15
Output Format

A list on a single line containing the cubes of the first  fibonacci numbers.

Sample Input

5
Sample Output

[0, 1, 1, 8, 27]
'''
# Code
def cube(x): return x*x*x


def fibonacci(n):
    List = []
    for i in range(n):
        if i == 0 or i == 1:
            List.append(i)
        else:
            y = List[i-2]+List[i-1]
            List.append(y)
    return List


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
