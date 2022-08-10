classes = {}
num_classes = {}
files = ["./members/chemistry.txt", "./members/english.txt", "./members/extraperiod.txt", "./members/history.txt", "./members/math.txt", "./members/spanish.txt"]

for file in files:
   with open(file, "r") as f:
      lines = f.readlines()
   with open(file, "w") as f:
      for line in lines:
         if "Profile picture" not in line.strip("\n"):
            f.write(line)
   with open(file, "r") as f:
      unstripped_people = f.readlines()
      people = []
      for person in unstripped_people[1::]:
         people.append(person.strip("\n"))
      for person in people:
         if person not in classes.keys():
            classes[person] = [unstripped_people[0].strip("\n")]
         else:
            classes[person].append(unstripped_people[0].strip("\n"))
for (key,value) in classes.items():
   num_classes[key] = len(classes[key])

ordered_classes = sorted(num_classes.items(), key = lambda x: x[1], reverse=True)

with open("./members/results.txt", "w") as results:
   for group in ordered_classes:
      name = group[0]
      amount = num_classes[name]
      class_list = ", ".join(classes[name])
      message = name.strip("\t") + ", " + str(amount) + ": " + class_list
      if name != "Avery Jones\t":
         results.write(message + "\n")