budget = {
"food":500,
"transportation":300,
"entertainment":200,
"utilities":150,
"rent":375,
"savings":400
}
expense = {
"food": 0,
"transportation": 0,
"entertainment": 0,
"utilities": 0,
"rent": 0,
"savings": 0
}
print("Personal Budget Tracker")
print("Your budget for each category is:")
for category, amount in budget.items():
    print(f"{category.capitalize()}: ${amount}")
print() 
print("Enter your expenses (press Enter with no amount to finish):")
while True:
    category = input("Category (Food/Transportation/Entertainment/Utilities/Rent/Savings): ").strip()
    if category == "":
        break
    if category not in budget:
        print("Invalid category. Please try again.")
        continue
    try:
        amount = float(input(f"Amount spent on {category}: $"))
        expense [category] += amount
        print(f"Added ${amount} to {category}")
        print()
    except ValueError:
        print("Please enter a valid number!")
        continue
print("\n=== BUDGET ANALYSIS ===")
total_budget = 0
total_spent = 0
total_remaining = 0
for category in budget:
    budgeted = budget[category]
    spent = expense[category]
    remaining = budgeted - spent
    total_budget += budgeted
    total_spent += spent
    total_remaining += remaining
print(f"\n{category}:")
print(f"Budgeted: ${budget[category]}")
print(f"Spent: ${expense[category]}")
print(f"Remaining: ${budget[category] - expense[category]}")

if remaining<0:
    print(f" OVER BUDGET by ${abs(remaining)}")
elif remaining>0:
    print(f" Under budget by ${remaining}")
else:
    print(" EXACTLY ON BUDGET!")

print(f"\n=== OVERALL SUMMARY ===")
print(f"Total Budget: ${total_budget}")
print(f"Total Spent: ${total_spent}")
print(f"Total Remaining: ${total_remaining}")
if total_remaining < 0:
    print("🚨 You're over budget! Consider reducing expenses.")
elif total_remaining > total_budget * 0.2:
    print("💰 Great job! You have significant savings this month.")
else:
    print("👍 You're on track with your budget. Keep it up!")

print(f"\n=== CATEGORY INSIGHTS ===")
biggest_overspend = 0
overspend_category = ""
for category in expense:
    overspend = expense[category] - budget[category]
    if overspend > biggest_overspend:
        biggest_overspend = overspend
        overspend_category = category
if biggest_overspend > 0:
    print(f"You overspent the most on {overspend_category.capitalize()} by ${biggest_overspend}.")
else:
    print("No overspending detected in any category.")
    
print("\nThank you for using the Personal Budget Tracker! Remember to review your budget regularly.")

