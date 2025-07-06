"""L1T16 - Data Structures - The List - Optional Task"""

# Resubmission - Corrected the {i+1} in the final output to print from
# 1 instead of index 0.

# Method 1 - Enumeration courtesy of geeksforgeeks.

movies = ["Interstellar", "Romulus", "Event Horizon", "Mars", "Star Wars"]

# Provides both the index (i) and the linked element for i for each loop. 
for i, movie in enumerate(movies):
    print(f"Movie: {i+1} {movie}")

# Method 2. Please uncomment below - Pretty much the same process but a 
# longer, round about way of defining i and creating a new list 

# movies = ["Interstellar", "Romulus", "Event Horizon", "Mars", "Star Wars"]
# i = 1
# movie_list = []

# for i in range(len(movies)):
#     movie_list = movies[i]
#     print(f"Movie {i+1}: {movie_list}")
