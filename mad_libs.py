# Mad Libs Game
# This is a fun word game where players input different words to create a silly story

print("Welcome to Mad Libs!")
print("Please enter the following words to create your story:\n")

# Get user input for different words
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb (past tense): ")
adverb = input("Enter an adverb: ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
noun3 = input("Enter a third noun: ")
adjective3 = input("Enter a third adjective: ")
verb2 = input("Enter another verb: ")
exclamation = input("Enter an exclamation: ")
verb3 = input("Enter a third verb: ")
adjective4 = input("Enter a fourth adjective: ")

# Create the story using f-strings
story = f"""
The other day, I was really in trouble. It all started when I saw a very {adjective1} {noun1} {verb1} {adverb} down the hallway. "{exclamation}!" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before trying to {verb3} right in front of my family.

Now I have a {adjective2} {noun2} and a {adjective3} {noun3} in my room. I'm not sure what to do with them, but they make me feel {adjective4}!
"""

# Print the completed story
print("\nHere's your Mad Libs story:")
print(story) 