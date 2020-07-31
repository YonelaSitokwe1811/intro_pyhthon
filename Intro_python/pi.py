import math
pi=0.0
for i in range(1, 10000000,4):
  pi+=4/i
  pi-=4/(i+2)

print("Pi=",round(pi,3))

rad=float(input("Enter radius:"))
area=math.pi*rad**2
print("Area=", round(area,3))
