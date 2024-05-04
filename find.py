s = "hey , there . \n aravind , hey . \n hi , bye ,  hey\n"
l = s.split(sep="\n")
s = []
for i in l:

    s.append(i.split())

dictionary = {}


def find(target):
    for i in range(len(s)):
        for j in range(len(s[i])):

            if target == s[i][j]:

                dictionary[i] = j

                print(f"Sentence number {i+1} position {j}")
                print("")


find("hey")

print(dictionary)
