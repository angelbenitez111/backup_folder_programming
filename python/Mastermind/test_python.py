title = "welcome to the tets about cheese"
print("\n" + title + "\n" + len(title) * "_" + "\n")

score = int(0)

question1 = input("Question 1: what do you do see a cheese board?\n"
                  "A- I run away\n"
                  "B- I try a cheese or even several\n"
                  "C- I can not avoid devour her\n"
                  "response: ")
if question1 == "A":
    score += 0
elif question1 == "B":
    score += 5
elif question1 == "C":
    score += 10
else:
    print("your answer is not valid")
    exit()

question2 = input("Question 2: how do you like the burger?\n"
                  "A- without cheese\n"
                  "B- with cheese\n"
                  "C- with breat and chesse\n"
                  "response: ")
if question2 == "A":
    score += 0
elif question2 == "B":
    score += 5
elif question2 == "C":
    score += 10
else:
    print("your answer is not valid")
    exit()

question3 = input("Question 3: Are you lactose intelerant?\n"
                  "A- Yes\n"
                  "B- Sometimes?\n"
                  "C- NO\n"
                  "respose: ")
if question3 == "A":
    score += 0
elif question3 == "B":
    score += 5
elif question3 == "C":
    score += 10
else:
    print("your answer is not valid")
    exit()

if 0 <= score <= 14:
    print("\n" + "You don't like cheese")
elif 15 <= score <= 29:
    print("\n" + "You like cheese")
elif 30 <= score:
    print("\n" + "You love cheese")
else:
    print("an error occurred")
    exit()
