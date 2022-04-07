PLACEHOLDER = "[name]"

# Open the file "Invited_names" and put the names in a list.
with open('./Input/Names/Invited_names.txt') as names_file:
    names = names_file.readlines()

# Open the file "starting_letter" at once.
with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    # Put each name in a separate "starting letter" after replacing each "[Name]"
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # Rename each new letter then send to "ReadyToSend" folder after renaming each new letter.
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as completed_letter:
            completed_letter.write(new_letter)
