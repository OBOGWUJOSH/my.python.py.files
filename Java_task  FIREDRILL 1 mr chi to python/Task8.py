#Task8.py

listNumber = [1,2,3,4,5,6,7,8,9,10]
multiple_of_4 = 0
multiple_of_8 = 0
repeatfour = 4
repeateight = 8
Addnumber4 = 0
Addnumber8 = 0


for number in listNumber :
	
	for repeatfour in range (1,6):
		if (number == 4):
			multiple_of_4 = (number  ** repeatfour)
			print(multiple_of_4, end='')
	print()
	for repeateight in range (1,6):
		if (number == 8):
			multiple_of_8 = (number  ** repeateight)
			print(multiple_of_8, end='')

print(" ")

Addnumber4 = (4 + 16 + 64 + 256 + 1024);
Addnumber8 = (8 + 64 + 512 + 4096 + 32768);
print(" ")
print(Addnumber4, end="")
print(" ")
print(Addnumber8, end="")
print(" ")
sum = Addnumber4 + Addnumber8
print(" ")
print(sum)

	

