from collections import deque
#Standard Problem Set Version 1
#Problem 7: Post Compare
def post_draft(draft):
    result = []
    for char in draft:
        if char == '#':
            if result:
                result.pop()
        else:
            result.append(char)
    return ''.join(result)
def post_compare(draft1, draft2):
    return post_draft(draft1) == post_draft(draft2)
print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 
#Standard Problem Set Version 2
#Problem 7: Lexicographically Smallest Watchlist
def make_smallest_watchlist(watchlist):
    watchlist = list(watchlist)
    left = 0
    right = len(watchlist) - 1
    while left < right:
        if watchlist[left] != watchlist[right]:
            # Step 3b: Replace the larger character with the smaller one
            if watchlist[left] > watchlist[right]:
                watchlist[left] = watchlist[right]
            else:
                watchlist[right] = watchlist[left]
        left += 1
        right -= 1
    return ''.join(watchlist) 
print(make_smallest_watchlist("egcfe")) 
print(make_smallest_watchlist("abcd")) 
print(make_smallest_watchlist("seven")) 
#Advanced Problem Set Version 1
#Problem 6: Marking the Event Timeline
def mark_event_timeline(event, timeline):
    n = len(timeline)
    t = ['?'] * n
    result = []
    for _ in range(10 * n):
        for i in range(n - len(event) + 1):  
            can_place = True
            for j in range(len(event)):
                if t[i + j] != '?' and t[i + j] != event[j]:
                    can_place = False
                    break

            if can_place:
                for j in range(len(event)):
                    t[i + j] = event[j]

                result.append(i)

                if ''.join(t) == timeline:
                    return result

    return []  # no matches within allowed turns
print(mark_event_timeline("abc", "ababc"))  
print(mark_event_timeline("abca", "aabcaca")) 
# Advanced Problem Set Version 2
#Problem 6: Validate Animal Sheltering Sequence
def validate_shelter_sequence(admitted, adopted):
    stack = []
    i = 0 

    for animal in admitted:
        stack.append(animal)

    while stack and stack[-1] == adopted[i]:
        stack.pop()
        i += 1  

    return i == len(adopted)
print(validate_shelter_sequence([1,2,3,4,5], [4,5,3,2,1]))
print(validate_shelter_sequence([1,2,3,4,5], [4,3,5,1,2])) 