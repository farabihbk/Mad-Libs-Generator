def mad_libs():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")

    story = f"The {adjective} {noun} loves to {verb} at the {place}."
    print(story)

mad_libs()