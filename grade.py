score = int(input("Score: "))

if   85 <= score <= 100:
    print("Grade: HD")
elif 75 <= score <= 84:
    print("Grade: D")
elif 65 <= score <= 74:
    print("Grade: C")
elif score >= 50 and score <= 64:
    print("Grade: P")
elif score >= 30 and score <= 49:
    print("Grade: F")
else:
    print("Grade: FF")