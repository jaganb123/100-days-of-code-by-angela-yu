with open("./Input/Names/invited_names.txt") as names:
    for i in names.readlines():

        with open("./Input/Letters/starting_letter.txt") as letter:
            write_this = letter.read().replace("[name]", i.strip("\n"))
            print(write_this)
            with open(f"./Output/send_to_{i}.txt", "w") as out_letter:
                out_letter.write(write_this)
