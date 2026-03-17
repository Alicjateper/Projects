# age = 23
age = 28

if age >= 18:
    print("Jestes dorosły")
else:
    print("Jesteś za młody")

isDrunk = False # zmienna logiczna, czy osoba jest trzeźwa

if age >= 18 and not isDrunk:
    print("Jesteś trzeżwy i dorosły")
else:
    print("Jesteś nietrzeźwy")

isRestriction = False

if age >= 18 and not isDrunk and not isRestriction:
    print("Jesteś trzeżwy i dorosły")
else:
    print("Jesteś nietrzeźwy")