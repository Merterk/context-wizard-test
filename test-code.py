# test_code.py

def calculate_discount(price, quantity):
    total = price * quantity
    
    # ISSUE 1: Ambiguous logic/style issue
    if total > 100:
        return total * 0.90 # 10% discount
    
def apply_tax(amount):
    TAX_RATE = 0.05
    return amount * (1 + TAX_RATE)

def main():
    price_1, quantity_1 = 50, 3
    
    # Reviewer's Comment could target this line:
    final_price_1 = calculate_discount(price_1, quantity_1)
    
    # ISSUE 2: Syntax Error (Indentation Issue)
    final_price_1 = apply_tax(final_price_1) # This line is intentionally misindented below

    print(f"Final price for item 1: {final_price_1}")


# This line is indented incorrectly for Python
    if __name__ == "__main__":
        main()