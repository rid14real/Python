blocks = int(input("Enter the number of blocks: "))

i=0
j=1
while i<blocks:
    j+=1
    i+=j
else:
    print("The height of the pyramid:", j-1)