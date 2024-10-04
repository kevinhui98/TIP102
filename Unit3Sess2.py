#Standard Problem Set Version 1
#Problem 7: Sort Performances by Type
def sort_performances_by_type(performances):
    l = 0
    r = len(performances) - 1

    while l < r:
        if performances[l] % 2 == 0:
            l += 1
        elif performances[r] % 2 != 0:
            r -= 1
        else:
            temp = performances[l]
            performances[l] = performances[r]
            performances[r] = temp
            l += 1
            r -= 1
    return performances
print(sort_performances_by_type([3, 1, 2, 4]))  
print(sort_performances_by_type([0]))  
# Standard Problem Set Version 1
#Problem 7: Check if a Signal Occurs as a Prefix in Any Transmission
def is_prefix_of_signal(transmission, searchSignal):
    transmission_list = transmission.split(" ")
    for i in range(len(transmission_list)):
        found = True
        if len(transmission_list[i]) < len(searchSignal):
            continue
        for j in range(len(searchSignal)):
            if searchSignal[j] != transmission_list[i][j]:
                found = False
        if found:
            return i + 1
    return -1
print(is_prefix_of_signal("i love eating burger", "burg")) 
print(is_prefix_of_signal("this problem is an easy problem", "pro")) 
print(is_prefix_of_signal("i am tired", "you")) 
# Advanced Problem Set Version 1
#Problem 7: Next Greater Element
def next_greater_dream(dreams):
	sorted = dreams.sort()
	next_greater = []

	for dream in dreams:
		index = sorted.index(dream)

   		if index == len(dreams) - 1:
      	next_greater.append(-1)

    	else:
      	next_greater.append(sorted[index + 1])
  	return next_greater
print(next_greater_dream([1, 2, 1])) 
print(next_greater_dream([1, 2, 3, 4, 3])) 
# Advanced Problem Set Version 2
#Problem 7: Market Token Value
def token_value(token):
    stack = []
    for char in token:
        if char == '(':
            stack.append(0)
        elif char == ')':
            value = 0
            while stack and stack[-1] != 0:
                value += stack.pop()
        stack.pop()
        stack.append(max(1, 2 * value))

    return sum(stack)
print(token_value("()"))
print(token_value("(())")) 
print(token_value("()()")) 