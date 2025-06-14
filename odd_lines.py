fn = open("sample_doc5.txt", "r")
fn1 = open("sample_doc6.txt", "w")

cont = fn.readlines()
type(cont)
for i in range(1, len(cont)+1):
    if(i % 2 != 0):
        fn1.write(cont[i-1])
    else:
        pass

fn1.close()

fn1 = open("sample_doc6.txt", "r")

cont1 = fn.read()

print(cont1)

fn1.close()
fn.close()