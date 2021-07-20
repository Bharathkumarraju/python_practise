score = int(input("Enter your score: "))

if score > 100 or score < 0:
    print("score is invalid!!!")

elif score >= 50:
    print("You have passed your exam!!!")
    print("Congratulations!!!")
else:
    print("Unfortunately you have failed this time please try again later!!!")


