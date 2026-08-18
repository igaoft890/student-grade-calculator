print("=== Student Grade Calculator ===")

n1 = float(input("Enter the AV1 grade: "))
n2 = float(input("Enter the AV2 grade: "))
n3 = float(input("Enter the AV3 grade: "))
n4 = float(input("Enter the AV4 grade: "))

average = (n1 + n2 + n3 + n4) / 4

print("\n=== Student Report ===")
print(f"Average grade: {average:.2f}")

if average >= 6:
    print("Status: Approved")
else:
    print("Status: Failed")
