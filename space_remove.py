name,char=input("Enter name and a character of that name seperated by comma: \n").split(",")
print(f"Length of name is {len(name.strip())}")
print(f"count :{name.strip().lower().count(char.strip().lower())}")

