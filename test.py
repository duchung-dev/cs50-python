score = int(input("Score: "))

if   score >= 85 and score <= 100:
    print("Grade: HD")
elif score >= 75 and score < 85:
    print("Grade: D")
elif score >= 65 and score < 75:
    print("Grade: C")
elif score >= 50 and score < 65:
    print("Grade: P")
elif score >= 30 and score < 50:
    print("Grade: F")
else:
    print("Grade: FF")