def solve(David):
    consonants = "bcdfghjklmnpqrstvwxyz"
    max_value = 0
    current_value = 0

    for consts in David:
        if consts in consonants:
            current_value += ord(consts) - ord("a") + 1
        else:
            max_value = max(max_value, current_value)
            current_value = 0

    return max(max_value, current_value)
 
 
