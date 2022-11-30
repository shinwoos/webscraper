def get_yearly_revenue(monthly_revenue):
    return monthly_revenue * 12 

def get_yearly_expenses(monthly_expenses):
    return monthly_expenses * 12

def get_tax_amount(profit):
    if( profit > 100000):
        return profit * 0.25
    else:
        return profit * 0.15
        
def apply_tax_credits(tax_amount, tax_credits):

    return tax_amount * tax_credits



profit = get_yearly_revenue(100) - get_yearly_expenses(10)
get_tax_amount(profit)
tax_amount = get_tax_amount(profit)
tax_credits = 0.01
final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")
