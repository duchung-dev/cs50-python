# This program asks the user a question and responds based on their answer.
# Translated to Vietnamese: Chương trình này hỏi người dùng một câu hỏi và phản hồi dựa trên câu trả lời của họ.
answer = input("Do you agree? ").strip().lower()
if answer.startswith("y"):
    print ("Agreed")
else:
    print("Not agreed")