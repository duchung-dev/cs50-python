# Demonstrates str functions
# Hiển thị các hàm xử lý chuỗi trong Python

name = input("What's your name? ").strip().title()

first, last = name.split(" ")
print(f"Hello, {first} {last}!")