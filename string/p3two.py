"""string = 'greeks quiz practice code '

stack = []

for word in string.split():
    stack.append(word)

reversed_words = []

#getting reversed word using stack pop ...hmm
while(len(stack)!=0):
    reversed_words.append(stack.pop())

print(reversed_words)

#joining the reversed word to string ...
reversed_string = ' '.join(reversed_words)
print(reversed_string)
"""
# Function to reverse the words in string
def reverse_word(s, start, end):
	while start < end:
		s[start], s[end] = s[end], s[start]
		start += 1
		end -= 1

# Function to reverse the string
def reverse_string(s):
	s = list(s)
	start = 0
	end = len(s)-1
	reverse_word(s, start, end) #it will reverse the whole string...totally ...he

	start = end = 0 #now this is game changer..haha

	# Iterate over the string S
	while end < len(s):
		if s[end] == ' ':
			reverse_word(s, start, end - 1)
			start = end + 1 #end variable of the reverse_string function..+1
			
		end += 1 #if not space increase the length of the string...

	# Reverse the words
	reverse_word(s, start, end - 1)
	return ''.join(s)


# Driver Code
s = "geeks quiz practice code"

print(reverse_string(s)) #horriable code...haha....
