import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

# Define a dictionary to map numerical choices to keys
key_mapping = {
    1: "Occupation",
    2: "Name",
    3: "Location",
    4: "Age"
}

# Display the menu and get user input
print("Select the key to extract the value:")
print("1. Occupation")
print("2. Name")
print("3. Location")
print("4. Age")
choice = int(input("Enter your choice (1-4): "))

# Validate the choice
if choice in key_mapping:
    key = key_mapping[choice]

    # Use a regular expression to find the value for the given key
    pattern = rf"{key}:\s*([^;]+)"
    match = re.search(pattern, text)

    if match:
        value = match.group(1)
        print(f"The value for '{key}' is: {value}")
    else:
        print(f"The key '{key}' was not found in the text.")
else:
    print("Invalid choice. Please select a number between 1 and 4.")
