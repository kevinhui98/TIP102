#Standard problem set v1
# PROBLEM 1
## Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".
def welcome():
  print("Welcome to The Hundred Acre Wood!")


welcome()


# PROBLEM 2
## Write a function greeting() that accepts a single parameter, a string name, and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."
def greetings(name):
  print("Welcome to The Hundred Acre Wood, " + name +
        "! My name is Christopher Robin")


greetings("Kevin")


# PROBLEM 3
## If the given character does not match one of the characters included above, print "Sorry! I don't know <character>'s catchphrase!"
def print_catchphrases(character):
  dic = {
      "Pooh": "Oh bother!",
      "Tigger": "TTFN: Ta-ta for now!",
      "Eeyore": "Thanks for noticing me.",
      "Christopher Robin": "Silly old bear.",
  }
  for [k, v] in dic.items():
    if (k == character):
      print(v)


print_catchphrases("Pooh")


# PROBLEM 4
## Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. If x is not a valid index of items, return None.
def get_item(items, x):
  if x < len(items):
    print(items[x])
  else:
    print("None")


items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)
items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)


#Standard Problem Set v2
# PROBLEM 1
def batman():
  return "I am vengeance. I am the night. I am Batman!"


print(batman())


#Advanced problem set v1
# PROBLEM 1 Hunny Hunt
##Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in the lst. Do not use any built-in functions.
def linear_search(items, target):
  for i in range(len(items)):
    if items[i] == target:
      return i
  return -1


items = ["piglet", "pooh", "roo", "rabbit"]
target = "piglet"
print(linear_search(items, target))
# PROBLEM 2
'''
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.
'''


def final_value_after_operations(operations):
  tigger = 1
  for i in range(len(operations)):
    if operations[i] == "bouncy" or operations[i] == "flouncy":
      tigger += 1
    elif operations[i] == "trouncy" or operations[i] == "pouncy":
      tigger -= 1
  return tigger


operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))


#Advanced problem set v2
# PROBLEM 1
def words_with_char(words, x):
  res = []
  for i in range(len(words)):
    if x in words[i]:
      res.append(i)
  return res


words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))


# PROBLEM 2
def hulk_smash(n):
  if n % 3 == 0 and n % 5 == 0:
    return "Hulk Smash"
  elif n % 3 == 0:
    return "Hulk"
  elif n % 5 == 0:
    return "Smash"
  else:
    return n


n = 15
print(hulk_smash(n))


# PROBLEM 3
def shuffle(message, indices):
  temp = message.split("")
  res = []
  for i in range(len(temp)):
    res[indices] = temp[i]
