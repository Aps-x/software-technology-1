# Salary input
salary = float(input("Enter your salary:"))
# Salary check
if salary >= 30000:
    # Years input
    years_on_job = float(input("Enter your years of employment:"))
    # Years check
    if years_on_job >= 2:
        print("You qualify for the loan")
    else:
        print("You must have been on your current job for at least two years to qualify.")
else:
    print("You must earn at least $30,000 per year to qualify.")