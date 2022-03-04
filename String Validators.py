'''
Task

You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format:

A single line containing a string .

Constraints:
0 < len(S) < 1000


Output Format:

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
'''
# Code

if __name__ == '__main__':
    s = input()
    Alphanum = 'False'
    Alpha = 'False'
    Num = 'False'
    Lower = 'False'
    Upper = 'False'

    for i in range(len(s)):
        if s[i].isalnum():
            Alphanum = "True"
        if s[i].isalpha():
            Alpha = "True"
        if s[i].isdigit():
            Num = "True"
        if s[i].islower():
            Lower = "True"
        if s[i].isupper():
            Upper = "True"

    print(Alphanum)
    print(Alpha)
    print(Num)
    print(Lower)
    print(Upper)
