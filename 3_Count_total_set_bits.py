# User function Template for python3
ddef cal_x(n):
    x=0
    while ((1<< x) <= n):
        x+=1
    return x-1
    
def cal_total_bits(n):
    if n<=1:
        return n
    x=cal_x(n)
    msb= x * (1<<(x-1))
    n = n-(1<<x)
    res =  msb + n+1 + cal_total_bits(n)
    return res
    
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        return cal_total_bits(n)
