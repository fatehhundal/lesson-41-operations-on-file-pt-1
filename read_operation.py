file = open("sample_doc1.txt", "r")
print(file.read())
file.close()

file = open("sample_doc1.txt", "r")
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open("sample_doc1.txt", "a")
file.write(" I am Penguin. I am a 1-year-old")
file.close()