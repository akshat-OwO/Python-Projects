with open("mailMerge/Input/Names/invited_names.txt", "r") as fhand:
    names = fhand.read().split('\n')
    with open("mailMerge/Input/Letters/starting_letter.txt", "r") as fhand1:
        lines = fhand1.readlines()
        for name in names:
            with open("mailMerge/Output/ReadyToSend/" + name + ".txt", "a") as fhand2:
                for line in lines:
                    if line == lines[0]:
                        new_name = line.replace("[name]", name)
                        fhand2.write(new_name)
                    else:
                        fhand2.write(line)
