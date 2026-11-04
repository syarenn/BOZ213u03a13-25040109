# step 1
beatles = []
print("step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("step 2:", beatles)

# step 3
for i in range(2):
    member = input("Enter a Beatles member: ")
    beatles.append(member)
print("step 3:", beatles)

# step 4
del beatles[-1]
del beatles[-1]
print("step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("step 5:", beatles)

# testing list length
print("The Fab", len(beatles))
