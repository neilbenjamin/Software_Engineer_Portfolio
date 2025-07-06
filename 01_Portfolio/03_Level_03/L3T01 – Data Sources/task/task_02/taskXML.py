
""" Task 01_Module 3- Task 1 & 2 - Data Sources

I found the json section quite clear, but the xml sextion was very confusing
and I needed quite a bit of help from the documents and google to manage the
basics of the task. This could be a section for am entire chapter considering
the depth of the xml manual and the various methods.
"""

import xml.etree.ElementTree as ET
tree = ET.parse('movie.xml')
root = tree.getroot()

# Loop first element
print("")
print("DISPLAY TAGS OF MOVIE ELEMENTS")
for movie in root.iter('movie'):
    print(f"This is the {movie.tag} element")
    for child_tag in movie:
        display_tag = child_tag.tag
        print(f"Child tags of the movie element: {display_tag}")

# Print description

print("")
print("MOVIE DESCRIPTIONS")
for description_element in root.iter('description'):
    text_output = description_element.itertext()
    print("".join(text_output).strip())


# Favorite Display

# Set counters

favorite_count = 0
not_favourite_count = 0
unknown_favorite = 0

# Map movie elements in the tree

for movie_element in root.iter('movie'):
    # Get the status attribute in each movie
    favorite_status = movie_element.get('favorite')
    if favorite_status == 'True':
        favorite_count += 1
    if favorite_status == 'False':
        not_favourite_count += 1
    else:
        unknown_favorite += 1
print("")
print("FAVORITE COUNTS")
print(f"The favorite count total is: {favorite_count}")
print(f"The least favorite count is: {not_favourite_count}")
print(f"The uncategorised count is: {unknown_favorite}")
