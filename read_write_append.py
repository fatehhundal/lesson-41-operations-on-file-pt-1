file = open("sample_doc2.txt", "r")
print(file.read())
file.close()

file = open("sample_doc2.txt", "w")
file.write("Hi, I am Penguin.")
file.close()

file = open("sample_doc2.txt", "r")
print(file.read())
file.close()

file = open("sample_doc2.txt", "a")
file.write(" I am a 1-year-old")
file.close()

file = open("sample_doc2.txt", "r")
print(file.read())
file.close()