a = {
"key": "value",
"harry": "code",
"marks": "100",
"list": [1, 2, 9]
}
print(a["key"]) # Output: "value"
print(a["list"]) # Output: [1, 2, 9]

print(a.items());
print(a.keys());

a.update({"friends":["Chetanya","Pajii"]});
print(a);

print(a.get("friends"));

dict = {
        "pankha" : "fan",
        "dabba" : "box",
        "kursi" : "chair",
        "billi" : "cat",
        "kutta" : "dog"
        };

word = input("Enter Hindi word: ");

print("Meaning: ", dict.get(word, "Word not found"));

nums = set();
for i in range(8):
    n = int(input("Enter the nubmer: "));
    nums.add(n);

print("Unique numbers: ", nums);

st = {20,"20"};
print(st);

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s));

si = {};
print(type(si));

fav = {};

for i in range(4):
    name = input("Enter your name");
    lang = input("Enter your favourite language");
    fav[name] = lang;

print(fav);


# if we change the value using key then the previous value will be overridden by new value.
# There can same value for different key.
# means key can never be same but values can be same.
# we can not insert list in sets because list is mutable(can modify or change value) but set is immutable.
