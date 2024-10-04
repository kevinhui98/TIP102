from collections import defaultdict
# Standard Problem Set Version 1
#Problem 8: Equivalent Species Pairs
def num_equiv_species_pairs(species_pairs: list[int]):
    output = 0
    pair_set = set([])
    for pair in species_pairs:
        pair_set.add((pair[0], pair[1]))
        if (pair[1], pair[0]) in pair_set:
            output += 1
    return output

species_pairs1 = [[1,2],[2,1],[3,4],[5,6]]
species_pairs2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]

print(num_equiv_species_pairs(species_pairs1))
print(num_equiv_species_pairs(species_pairs2))
# Standard Problem Set Version 2
#Problem 8: Finding Common Tourist Attractions with Least Travel Time
def find_attractions(tourist_list1, tourist_list2):
  tl1_dict = defaultdict()
  tl2_dict = defaultdict()
  res = []

  for i in range(len(tourist_list1)):
      tl1_dict[tourist_list1[i]] = i

  for i in range(len(tourist_list2)):
      tl2_dict[tourist_list2[i]] = i

  shared = []

  if len(tourist_list1) < len(tourist_list2):
      for i in range(len(tourist_list1)):
          if tourist_list1[i] in tl2_dict:
              shared.append(tourist_list1[i])
  else:
      for i in range(len(tourist_list2)):
          if tourist_list2[i] in tl1_dict:
              shared.append(tourist_list2[i])

  min_so_far = float('inf')

  for attr in shared:  
      min_so_far = min(tl1_dict[attr] + tl2_dict[attr], min_so_far)

  for attr in shared:
      if min_so_far == tl1_dict[attr] + tl2_dict[attr]:
          res.append(attr)
  return res
tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Colosseum","Trevi Fountain","Pantheon","Eiffel Tower"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Disneyland","Eiffel Tower","Notre-Dame"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["beach","mountain","forest"]
tourist_list2 = ["mountain","beach","forest"]

print(find_attractions(tourist_list1, tourist_list2))
# Advanced Problem Set Version 1
# Problem 6: Counting Divisible Collections in the Gallery
def count_divisible_collections(collection_sizes, k):
  res = 0
  for i in range(len(collection_sizes)):
      sub = []
      counter = 0
      while len(sub) < len(collection_sizes) - i:
          sub.append(collection_sizes[i + counter])
          if sum(sub) % k == 0:
              res += 1
          counter += 1
  return res
nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2))  
# Advanced Problem Set Version 2
#Problem 6: Pair Contestants
def pair_contestants(scores, k):
  res = sum(scores)
  return res % k == 0
scores1 = [1,2,3,4,5,10,6,7,8,9]
k1 = 5
print(pair_contestants(scores1, k1))

scores2 = [1,2,3,4,5,6]
k2 = 7
print(pair_contestants(scores2, k2))

scores3 = [1,2,3,4,5,6]
k3 = 10
print(pair_contestants(scores3, k3)) 