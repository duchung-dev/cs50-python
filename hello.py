# Ask user for their name and greet them
name = input("what's your name? ").strip().title()

# Split the name into parts (first and last)
first, last = name.split(" ")
# Greet the user
print(f"hello, {first}")

