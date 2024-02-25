user_text = str(input("Write your text:\n"))
space = 0
point = 0
comma = 0

for a in user_text:
    if a == " ":
        space += 1
    elif a == ".":
        point += 1
    elif a == ",":
        comma += 1

print("The amount\n"
      "spaces: {}, Points: {}, Commas: {}".format(space, point, comma))
