# Step 1: Take user input and write to output.txt
user_input = input("Enter the initial content to write in the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data
additional_data = input("Enter additional data to append: ")
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")

# Step 3: Read and display the final content
with open("output.txt", "r") as file:
    content = file.read()

print("Final content of output.txt:")
print(content)
