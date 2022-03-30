    # How large is the loan?

    # How good is your credit history?

    # How high is your income?

    # How large is your down payment?


# First, check if the loan size is at least 5. If it is, use the following rules:

# If the credit history and income are both at least 7, then the decision is "yes"

# If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no"

# Otherwise (if neither the credit history nor income is at least 7), the decision is "no"

# Otherwise (if the loan is not 5 or greater), use these rules:

# If the credit is less than 4, then the decision is "no"

# Otherwise, check the following:

# If either the income or the down payment is at least 7, the decision is "yes"

# If both the income and the down payment are at least 4, then the answer is "yes"

# Otherwise, the decision is "no"
print("Please give a rating from 1 to 10 on the following:")

loan_amount = float(input("How large is the loan? "))
credit_history = float(input("How good is your credit history? "))
income_amount = float(input("How high is your income? "))
downpayment_amount = float(input("How large is your down payment? "))

if loan_amount >= 5:
    if credit_history >= 7 and income_amount >= 7:
        decision = True
    elif credit_history >= 7 or income_amount >= 7:
        if downpayment_amount >= 5:
            decision = True
        else:
            decision = False
    else:
        decision = False
else:
    if loan_amount < 4:
        decision = False
    else:
        if income_amount >= 7 or downpayment_amount >= 7:
            decision = True
        elif income_amount >= 4 and downpayment_amount >= 4:
            decision = True
        else:
            decision = False
if decision:
    print("Congradulations! This checks out you can now loan from us!")
else:
    print("Sorry we wont be able to loan you anything right now.")



# Loan size: 8, Credit: 7, Income: 8, Down Payment: 1, Decision: "yes"

# Loan size: 5, Credit: 2, Income: 7, Down Payment: 5, Decision: "yes"

# Loan size: 8, Credit: 2, Income: 8, Down Payment: 3, Decision: "no"

# Loan size: 2, Credit: 4, Income: 1, Down Payment: 7, Decision: "yes"

# Loan size: 4, Credit: 5, Income: 5, Down Payment: 3, Decision: "no"