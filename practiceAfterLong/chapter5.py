a = {
        "name" : "Akhil",
        "from" : "Delhi/Himachal Pradesh"
    }

print(a["name"])
print(a["from"])


print(a.keys())

a.update({"from" : "Delhi"})

print(a.items())
print(a.get("name"))

s = {1,8,2,3}
print(len(s))

s.remove(8)
print(s)

print(s.pop())
#s.clear()
#print(s)

s = s.union({8,11})
print(s)

s = s.intersection({8,11})
print(s)

hind_eng_dict = {
    "kya" : "what",
    "hai" : "are"
}

print(hind_eng_dict.items())

s = set()
# for i in range(1,8):
#     number = int(input("Enter the number: "))
#     s.add(number)

print(s)

s2 = {18,"18"}
s2.add(18.0)
print(s2)

fav_language = {}
for i in range(1,4):
    name = input("Enter your Name: ")
    lang = input("Enter your favourite language: ")
    fav_language.update({name : lang})

print(fav_language)