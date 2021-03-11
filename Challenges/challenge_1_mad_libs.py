# Write a story with some words missing


# Ask the user to provide the missing words
colour = input("Type a colour ")
colour2 = input("Type a colour2 ")
adjective = input("Type an adjective ")

story = f"""
Roses are {colour}
Violets are {colour2}
Sugar is {adjective}
And so are you
"""
# Display the final story
#print(story.format(colour=colour, colour2=colour2, adjective=adjective))

print(story)