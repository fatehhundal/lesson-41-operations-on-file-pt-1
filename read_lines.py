file1 = open("sample_doc3.txt", "r")
file2 = open("sample_doc4.txt", "w")

for line in file1.readlines():
    if not (line.startswith("Coding")):
        print(line)
        file2.write(line)
    
file2.close()
file1.close()