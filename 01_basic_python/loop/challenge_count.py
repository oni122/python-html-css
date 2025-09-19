
def chek_is_balance(text:str):
    text = text.upper()

    count_r = text.count("R")
    count_j = text.count("J")

    print(f"count_r : {count_r}, count_j : {count_j}")

    return count_r == count_j

print(chek_is_balance("RJRJ"))
print(chek_is_balance("RJRJrjrjrjrj"))