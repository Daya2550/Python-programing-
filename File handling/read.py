f = open("demofile.txt", "r")
print(f.read())
print(f.read(5))
print(f.readline())
for i in f:
    print(i)
f.close()    