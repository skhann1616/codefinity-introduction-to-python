# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

shelf1_update_tuple = tuple(shelf1_update)
#Concatenate shelf1_update_tuple with the existing tuple shelf1 to create a new tuple called shelf1_concat.
shelf1_concat = shelf1 + shelf1_update_tuple
#Count how many times the string "celery" appears in shelf1_concat and store this number in a variable called celery_count.
celery_count = shelf1_concat.count("celery")
#Find the index of the first occurrence of "celery" in shelf1_concat and store it in a variable called celery_index.
celery_index = shelf1_concat.index("celery")

print("Updated Shelf #1:", shelf1_concat)
print("Number of Celery:", celery_count)
print("Celery Index:", celery_index)