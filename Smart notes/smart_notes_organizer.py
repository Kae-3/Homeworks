
sample_notes = """IMPORTANT: Finish Python project by midnight.
Junk line: Random thoughts 123...
TODO: Buy milk and bread.
Just a random note without priority prefix.
IMPORTANT: Call client regarding project update.
TODO: Review pull request on GitHub.
Junk line: Ignore this text.
"""

with open("notes.txt", "w") as f:
    f.write(sample_notes)

print("--- 1. Demonstrating read(n) ---")
with open("notes.txt", "r") as file:
    # Skill 1: Read the first 25 characters of the file
    first_chunk = file.read(25)
    print(f"First 25 characters:\n{first_chunk}\n")

print("--- 2. Demonstrating readlines() ---")
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines read into list: {len(lines)}\n")

print("--- 3. Filtering and Writing to New File ---")
clean_lines = []


for line in lines:
    line_trimmed = line.strip()

    if line_trimmed.startswith("IMPORTANT:") or line_trimmed.startswith("TODO:"):
        clean_lines.append(line)
    
with open("clean_notes.txt", "w") as clean_file:
    clean_file.writelines(clean_lines)

print("Clean notes written to 'clean_notes.txt':\n")
with open("clean_notes.txt", "r") as clean_file:
    print(clean_file.read())