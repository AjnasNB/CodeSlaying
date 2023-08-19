from sys import stdin

def lookAndSequence(n):
	# Write your code here.
    sequence = ["1"]
    
    for _ in range(n - 1):
        print(sequence[-1])
        prev_term = sequence[-1]
        new_term = ""
        count = 1
        prev_digit = prev_term[0]
        
        for digit in prev_term[1:]:
            if digit == prev_digit:
                count += 1
            else:
                new_term += str(count) + prev_digit
                prev_digit = digit
                count = 1
        
        new_term += str(count) + prev_digit
        sequence.append(new_term)
    
    return sequence[n-1]




def takeInput() :

	n = int(input().strip())
	return n

t = int(input().strip())
for i in range(t) :

	n = takeInput()
	print(lookAndSequence(n))