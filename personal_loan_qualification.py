# variables for set limits and valid data
available_repayment_months = (12, 24, 36, 48, 60)
min_age = 18
max_age = 75
min_monthly_income = 5000.00
max_loan_request = 35000.00
tier1_loan_max = 15000.00
tier2_loan_max = 30000.00
tier1_min_monthly_income = 15000.00
tier2_min_monthly_income = 10000.00
cheap_interest_rate = 0.1
med_interest_rate = 0.2
high_interest_rate = 0.3
repayment_pct_limit = 0.3
# user input
applicant_name = input('Enter your name: ').strip()
applicant_age = int(input('Enter your age: '))
monthly_income = float(input('Enter your monthly income: '))
monthly_expenses = float(input('Enter your monthly expenses: '))
loan_request = float(input('Enter your requested loan amount: '))
repayment_months = int(input(f'Select a repayment period in months {available_repayment_months}: '))
currently_employed = input('Are you currently employed? (yes/no): ').lower().strip() == 'yes'
# input validation
if len(applicant_name) < 2:
    print('Error: Name cannot be shorter than 2 characters.')

elif applicant_age <= 0:
    print('Error: Age cannot be zero or negative.')

elif monthly_income < 0:
    print('Error: Monthly income cannot be negative.')

elif monthly_expenses < 0:
    print('Error: Monthly expenses cannot be negative.')

elif loan_request <= 0:
    print('Error: Loan requested cannot be 0 or negative.')

elif repayment_months not in available_repayment_months:
    print(f'Error: Please select a repayment period in months within the available options. Available options: {available_repayment_months}')

else:
    # interest tiers
    if monthly_income >= tier1_min_monthly_income and loan_request <= tier1_loan_max:
        yearly_interest_rate = cheap_interest_rate
        tier_name = 'Prime Rate'

    elif monthly_income >= tier2_min_monthly_income and loan_request <= tier2_loan_max:
        yearly_interest_rate = med_interest_rate
        tier_name = 'Standard Rate'

    else: # lower income = higher risk
        yearly_interest_rate = high_interest_rate
        tier_name = 'High-Risk Rate'

    # arithmetic
    disposable_income = monthly_income - monthly_expenses
    repayment_months_in_years = repayment_months / 12
    total_interest_decimal = repayment_months_in_years * yearly_interest_rate
    total_interest_amount = loan_request * total_interest_decimal
    total_payback = loan_request + total_interest_amount
    monthly_repayment = total_payback / repayment_months
    max_monthly_repayment = disposable_income * repayment_pct_limit

    # applicant declination
    declination_count = 0
    if not currently_employed:
        declination_count += 1
        print('Loan application declined: You are not employed.')

    if disposable_income <= 0:
        declination_count += 1
        print('Loan application declined: Your disposable income is 0 or negative.')

    if not min_age <= applicant_age <= max_age:
        declination_count += 1
        print(f'Loan application declined: You are not within the {min_age}-{max_age} age requirements.')

    if monthly_income < min_monthly_income:
        declination_count += 1
        print(f'Loan application declined: Your monthly income does not meet the R{min_monthly_income:.2f} minimum.')

    if loan_request > max_loan_request:
        declination_count += 1
        print(f'Loan application declined: Loan request is above R{max_loan_request:.2f} maximum.')

    if disposable_income > 0 and monthly_repayment > max_monthly_repayment:
        declination_count += 1
        print(f'Loan application declined: Your R{monthly_repayment:.2f} monthly repayment amount exceeds the R{max_monthly_repayment:.2f} monthly limit.')

    if declination_count > 0:
        print(f'Loan application has been blocked by {declination_count} issue(s).')

    else:
        # formatted summary
        print(f'The loan for {applicant_name} has been approved.')
        print(f'Tier: {tier_name}')
        print(f'Your yearly interest rate: {yearly_interest_rate * 100:.2f}%')
        print(f'Total repayable amount: R{total_payback:.2f}')
        print(f'Your monthly repayment amount: R{monthly_repayment:.2f}')