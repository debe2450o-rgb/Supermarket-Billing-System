def main():
    print("=============================================")
    print("    SMARTBUY SUPERMARKET BILLING SYSTEM     ")
    print("=============================================\n")

    while True:
        # Array/List structures to handle dynamic parallel data
        product_names = []
        quantities = []
        unit_prices = []
        total_prices = []
        overall_total = 0.0

        print("--- Start New Customer Billing Session ---")
        
        # Inner loop to process multiple items for a single customer
        while True:
            name = input("Enter product name: ").strip()
            if not name:
                print("Product name cannot be blank. Please try again.")
                continue
            
            # Input validation block using try-except to trap data type errors
            try:
                quantity = int(input(f"Enter quantity for '{name}': "))
                price = float(input(f"Enter unit price for '{name}' (Le): "))
                
                # Check for zero or negative values
                if quantity <= 0 or price <= 0:
                    print("Quantity and price must be greater than zero.\n")
                    continue
            except ValueError:
                print("Invalid data format. Please input numerical characters for quantity and price.\n")
                continue

            # Core arithmetic operation
            item_total = quantity * price
            overall_total += item_total

            # Appending items safely into parallel lists
            product_names.append(name)
            quantities.append(quantity)
            unit_prices.append(price)
            total_prices.append(item_total)

            # Query the cashier to control loop scaling
            more_items = input("Add another item? (y/n): ").strip().lower()
            print()
            if more_items == 'n':
                break

        # Decision structure to apply promotional 10% discount if bill exceeds Le 500
        discount = 0.0
        if overall_total > 500:
            discount = overall_total * 0.10

        final_amount = overall_total - discount

        # Render structured, clean receipt format matching layout guidelines
        print("\n=============================================")
        print("             SMARTBUY SUPERMARKET            ")
        print("          Freetown, Sierra Leone             ")
        print("=============================================")
        print(f"{'Item Description':<18} {'Qty':<5} {'Unit (Le)':<10} {'Total (Le)':<10}")
        print("---------------------------------------------")
        
        # Iterating through parallel lists via loop indices
        for i in range(len(product_names)):
            print(f"{product_names[i]:<18} {quantities[i]:<5} {unit_prices[i]:<10.2f} {total_prices[i]:<10.2f}")
        
        print("---------------------------------------------")
        print(f"{'Subtotal:':<34} Le {overall_total:>8.2f}")
        print(f"{'Discount Applied (10%):':<34} Le {discount:>8.2f}")
        print("=============================================")
        print(f"{'FINAL TOTAL TO PAY:':<34} Le {final_amount:>8.2f}")
        print("=============================================")
        print("        Thank you for shopping with us!      ")
        print("=============================================\n")

        # Outer loop control for consecutive customer lines
        next_customer = input("Process billing for the next customer? (y/n): ").strip().lower()
        print("\n" + "="*45 + "\n")
        if next_customer != 'y':
            print("Terminal closed. System safely shutdown.")
            break

if __name__ == "__main__":
    main()
