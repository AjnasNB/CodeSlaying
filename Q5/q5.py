from typing import List

def sumFirstN(n: int) -> int:
    sum=0
    # Write your code here.
    for i in range(n+1):
        sum+=i
    return sum
