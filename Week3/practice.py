# Demonstrates (unintended) concatenation strings  
# Hiển thị việc nối chuỗi (không mong muốn)

# Promt user for two inputs
# Yêu cầu người dùng nhập hai giá trị
x = float(input("What's x? "))
y = float(input("What's y? "))

# Print sum
# In ra tổng
z = (x + y)
# Format to 2 decimal places
# In và định dạng đến 2 chữ số thập phân
print(f"{z:.2f}")  