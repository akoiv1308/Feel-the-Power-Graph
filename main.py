#PART A SIMULATION (30 TRIALS OF 15 NUMBERS ROLLED)
#DETERMINES IF THE AVERAGE OF THE 15 NUMBERS IS AT LEAST 70

import random
import matplotlib.pyplot as plt

def avgList(simList):
  sum = 0
  for i in range(len(simList)):
    sum += simList[i]
  return sum/len(simList)

avg1 = 0
avg2 = 0
avg3 = 0
avg4 = 0
for j in range(10000):
  myData = []
  for i in range(15):
    randomDraw = random.randrange(0, 99)
    if randomDraw == 0:
      randomDraw = 100
    myData.append(randomDraw)
  print(myData)
  print("average: " + str(avgList(myData)))
  if avgList(myData) >= 70:
    avg1 += 1
  else:
    avg2 += 1

labels = 'yes: at least 70', 'no: not at least 70'
sizes = [avg1, avg2]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.savefig('graph.png')

