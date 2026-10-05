grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks = [85, 32, 67, 39, 45, 20]

for mark in marks:
    print(mark, ":", grade(mark))

# Output:
# 85 : Pass
# 32 : Fail
# 67 : Pass
# 39 : Fail
# 45 : Pass
# 20 : Fail
