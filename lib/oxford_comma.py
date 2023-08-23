# convert string into a list use .split()
# convert a list to a string use .join()
# oxford.comma ---function designed to format items in the list as gramatically correct and readable sentence

def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    # above check if there is one item
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    # above checks if there are two items
    else:
        return ', '.join(items[:-1]) + f", and {items[-1]}"
    # above checks if there are 3 or more items