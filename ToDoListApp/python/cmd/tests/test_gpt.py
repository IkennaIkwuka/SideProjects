raw_data = [
    "\n",
    "1.\tTitle: book\n",
    "\tDescription: web\n",
    "\n",
    "2.\tTitle: life and shit\n",
    "\tDescription: porn\n",
    "\n",
    "3.\tTitle: goat\n",
    "\tDescription: goal soccer shit\n",
    "\n",
    "1.\tTitle: fuck balls dick\n",
    "\tDescription: twat groove grape\n",
    "2.\tTitle: gun-violin\n",
    "\tDescription: Gun Violence",
]

# Clean and structure the data
structured_data = []
current_entry = {}

for line in raw_data:
    line = line.strip()
    if line.startswith("Title:"):
        if current_entry:  # Save the previous entry if it exists
            structured_data.append(current_entry)
            current_entry = {}
        current_entry["Title"] = line.split("Title:", 1)[1].strip()
    elif line.startswith("Description:"):
        current_entry["Description"] = line.split("Description:", 1)[1].strip()

# Append the last entry if it exists
if current_entry:
    structured_data.append(current_entry)

# Print the cleaned and structured data
for i, entry in enumerate(structured_data, start=1):
    print(f"{i}. Title: {entry.get('Title')}")
    print(f"   Description: {entry.get('Description')}")
