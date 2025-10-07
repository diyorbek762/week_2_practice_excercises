
name = input("Enter your name: ")
gpa = float(input("Enter your GPA: "))

credit_hours = float(input("Enter the total credit hours: "))

print(f"\n{'=' * 40}")
print(f'\nStudent Information: {name}')
print(f"Whether Eligible for Dean's List: {"Yes" if gpa >= 3.5 and credit_hours >= 12 else "No"}")
print(f'GPA points needed: {3.5- gpa:.1f} points' if gpa < 3.5 else "")
print(f'Credit Hours needed: {12 - credit_hours:.1f} ' if credit_hours < 12 else "" )
print(f"\n{'=' * 40}")
      
