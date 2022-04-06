#User function Template for python3

class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        if n==0:
            return False
        else:
            res=(n & (n-1))
            return True if res==0 else False
