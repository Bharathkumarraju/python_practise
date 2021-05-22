try:
    print(1/0)
except:
    print("Wrong denominator")
finally:
    print("Always printed")