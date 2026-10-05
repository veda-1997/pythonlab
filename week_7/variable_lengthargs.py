def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

print("3 marks:", total_marks(80, 75, 90))
print("5 marks:", total_marks(80, 75, 90, 85, 95))
print("1 mark:", total_marks(88))

# Output:
# 3 marks: (245, 81.66666666666667)
# 5 marks: (425, 85.0)
# 1 mark: (88, 88.0)
