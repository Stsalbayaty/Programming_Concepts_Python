speed = int(input("What is the speed of the vehicle in miles per hours: "))
while speed < 1:
	speed = int(input("please enter a number greater than 0: "))
	
time = int(input("What is the number of hours the vehicle has traveled: "))
while time < 1:
	time = int(input("please enter a number greater than 0: "))
 #processing
#output for statement
print ("Hour""\t""Distance Traveled")
print ("_________________________")
for hour in range (1, time + 1):
	distance = speed * hour
	print (hour, "\t", distance)
	
 
