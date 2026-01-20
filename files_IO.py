# Open the file in write mode
#f = open("this.txt", "w")
# Write a string to the file
#f.write("this is nice")
# Close the file
#f.close()

f = open("poems.txt","r");
text = f.read();

if "twinkle" in text.lower():
    print("Twinkle is present in the poem");
else:
    print("Twinkle is not present in the poem");

f.close();
