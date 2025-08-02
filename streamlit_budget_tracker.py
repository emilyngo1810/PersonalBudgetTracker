import streamlit as st

st.title("Personal Budget Tracker")

budget = {
    "food": 500,
    "transportation": 300,
    "entertainment": 200,
    "utilities": 150,
    "rent": 375,
    "savings": 400
}
expense = {cat: 0 for cat in budget}

st.header("Your budget for each category is:")
for category, amount in budget.items():
    st.write(f"{category.capitalize()}: ${amount}")

st.header("Enter your expenses:")
categories = list(budget.keys())
for category in categories:
    amount = st.number_input(f"Amount spent on {category.capitalize()}", min_value=0.0, step=1.0, key=category)
    expense[category] = amount

if st.button("Analyze Budget"):
    st.subheader("=== BUDGET ANALYSIS ===")
    total_budget = sum(budget.values())
    total_spent = sum(expense.values())
    total_remaining = total_budget - total_spent

    for category in budget:
        budgeted = budget[category]
        spent = expense[category]
        remaining = budgeted - spent

        st.write(f"{category.capitalize()}:")
        st.write(f"Budgeted: ${budgeted}")
        st.write(f"Spent: ${spent}")
        st.write(f"Remaining: ${remaining}")

        if remaining < 0:
            st.error(f"OVER BUDGET by ${abs(remaining)}")
        elif remaining > 0:
            st.success(f"Under budget by ${remaining}")
        else:
            st.info("EXACTLY ON BUDGET!")

    st.subheader("=== OVERALL SUMMARY ===")
    st.write(f"Total Budget: ${total_budget}")
    st.write(f"Total Spent: ${total_spent}")
    st.write(f"Total Remaining: ${total_remaining}")

    if total_remaining < 0:
        st.error("🚨 You're over budget! Consider reducing expenses.")
    elif total_remaining > total_budget * 0.2:
        st.success("💰 Great job! You have significant savings this month.")
    else:
        st.info("👍 You're on track with your budget. Keep it up!")

    st.subheader("=== CATEGORY INSIGHTS ===")
    biggest_overspend = 0
    overspend_category = ""
    for category in expense:
        overspend = expense[category] - budget[category]
        if overspend > biggest_overspend:
            biggest_overspend = overspend
            overspend_category = category
    if biggest_overspend > 0:
        st.warning(f"You overspent the most on {overspend_category.capitalize()} by ${biggest_overspend}.")
    else:
        st.success("No overspending detected in any category.")

    st.write("Thank you for using the Personal Budget Tracker! Remember to review your budget regularly.")
