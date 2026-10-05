def build_profile(**details):
    print("----- Profile -----")
    for key, value in details.items():
        print(key.title() + ":", value)
    print("-------------------")

build_profile(name="Veda", age=19, city="Hyderabad", hobby="Reading")

build_profile(name="Meghana", branch="CSE", hobby="Drawing")

# Output:
# ----- Profile -----
# Name: Veda
# Age: 19
# City: Hyderabad
# Hobby: Reading
# -------------------
# ----- Profile -----
# Name: Meghana
# Branch: CSE
# Hobby: Drawing
# -------------------
