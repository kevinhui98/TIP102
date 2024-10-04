from collections import defaultdict
# Standard Problem Set Version 1
#Problem 12: Sort the Performers
def sort_performers(performer_names, performance_times):
  thisdict = {}
  for i in range(len(performer_names)):
    thisdict[performance_times[i]] = performer_names[i]
  thisdict = dict(sorted(thisdict.items(), reverse=True))
  # sorted_dict = dict(sorted(dict.items(), key=lambda item: item[1]))
  return thisdict.values()
performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1))
print(sort_performers(performer_names2, performance_times2))
def get_artist_info(artist, festival_schedule):
  if artist in festival_schedule:
    return festival_schedule[artist]
  else:
    return {"Message": 'Artist not found'}
festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
#Standard Problem Set Version 2
#Problem 12: Final Communication Hub
def find_final_hub(paths):
  dict = {}
  for i in range(len(paths)):
    dict[paths[i][0]] = paths[i][1]
  path = paths[0][0]
  while path in dict:
    path = dict[path]
  return path
paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
paths3 = [["StationA", "StationZ"]]

print(find_final_hub(paths1)) 
print(find_final_hub(paths2)) 
print(find_final_hub(paths3))
#Advanced Problem Set Version 1
# Problem 2: Pirate Message Check
def can_trust_message(message):
  myset = set()
  for i in message:
    myset.add(i)
  return len(myset) >= 26
message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
# Problem 3: Find All Duplicate Treasure Chests in an Array
def find_duplicate_chests(chests):
  mymap = {}
  res = []
  for i in chests:
    if i in mymap:
      mymap[i] += 1
    else:
      mymap[i] = 0
  for k,v in mymap.items():
    print(k,v)
    if v >= 1:
      res.append(k)
  return res
   
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
#Problem 8: Counting Pirates' Action Minutes
def counting_pirates_action_minutes(logs, k):
  pirateMap = defaultdict(lambda: set([]))
  freq = [0] * k
  for log in logs:
      pirateMap[log[0]].add(log[1])
  for pirate_id in pirateMap:
      freq[len(pirateMap[pirate_id]) - 1] += 1
  return freq
logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))
# # Advanced Problem Set Version 2
def analyze_library(library_catalog, actual_distribution):
  res = actual_distribution.copy()
  for k,v in library_catalog.items():
    for k1,v1 in actual_distribution.items():
      if k1 == k:
        res[k] = v1-v
  return res
library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}
print(analyze_library(library_catalog, actual_distribution))
# #Problem 8: Time Portal Usage
def display_time_portal_usage(usage_records : list[str]) -> list[str]:
  def time_str_to_int(time: str):
      hour = time[0:2]
      if hour[0] == '0':
          hour = int(hour[-1])
      else:
          hour = int(hour)

      minute = int(time[3:5])

      return hour * 60 + minute

  usage_records.sort(key = lambda x : time_str_to_int(x[2]))
  portal_dict = defaultdict(lambda: [])
  freq_dict = defaultdict(lambda: 0)

  time_set = set([])
  portal_set = set([])

  for record in usage_records:
      portal = record[1]
      time = record[2]
      portal_dict[portal].append(time)
      freq_dict[(portal, time)] += 1
      time_set.add(time)
      portal_set.add(portal)

  time_set = sorted(time_set, key = time_str_to_int)
  portal_set = sorted(portal_set, key = lambda x : int(x))

  res = []
  res1 = []

  res1.append("Portal")
  for time in time_set:
      res1.append(time)
  res.append(res1)

  for portal in portal_set:
      res2 = []
      res2.append(portal)
      for time in time_set:
              res2.append(freq_dict[(portal, time)])
      res.append(res2)

  return res
usage_records1 = [["David","3","10:00"],
  ["Corina","10","10:15"],
  ["David","3","10:30"],
  ["Carla","5","11:00"],
  ["Carla","5","10:00"],
  ["Rous","3","10:00"]]
usage_records2 = [["James","12","11:00"],
  ["Ratesh","12","11:00"],
  ["Amadeus","12","11:00"],
  ["Adam","1","09:00"],
  ["Brianna","1","09:00"]]
usage_records3 = [["Laura","2","08:00"],
  ["Jhon","2","08:15"],
  ["Melissa","2","08:30"]]

print(display_time_portal_usage(usage_records1))
print(display_time_portal_usage(usage_records2))
print(display_time_portal_usage(usage_records3))
