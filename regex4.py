import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

# Define keywords for each category
keywords = {
    "Electronics": ["smartphone", "screen", "memory"],
    "Apparel": ["t-shirt", "cotton", "size"],
    "Home & Kitchen": ["kitchen", "knife", "stainless steel"]
}

# Function to tag a product based on its description
def tag_product(description):
    for category, keys in keywords.items():
        for key in keys:
            if re.search(r'\b' + re.escape(key) + r'\b', description, re.IGNORECASE):
                return category
    return "Unknown"

# Tag each product in the descriptions list
tagged_products = [(description, tag_product(description)) for description in descriptions]

# Print the results
for description, tag in tagged_products:
    print(f"Description: {description}\nTag: {tag}\n")
