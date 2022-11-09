from time import time
start = time()
l = [0,1]

#1000 can be changed to any quantity of fibonacci numbers you want to get. Keep in mind that values over 500000 can freeze even powerfull pc's.
for i in range(1000-2):
  l.append(l[i]+l[i+1])
print(l)

print(f"time to run: {time() - start} seconds")
