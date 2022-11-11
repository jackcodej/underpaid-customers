melon_cost = 1.00

file = "customer-orders.txt"

def checkCustomerPayment(file):
    """
    Takes in customer orders and returns payment and calculated payment
    """
    #Initiate total debt value to track amount owed by all customers
    total_debt = 0
    #Open file to loop through
    current_file = open(file)
    #Process each line in list of customer orders
    for each_customer in current_file:
        #Default to customer does not owe money
        owe_money = "does not owe money"
        #Split the line by '|'
        words = each_customer.split('|')
        #Set customer id to first 'word'
        customer_id = words[0]
        #Set customer name to second 'word'
        customer_name = words[1]
        #Set melon count to third 'word'
        melon_count = int(words[2])
        #Set customer payment to fourth 'word'
        customer_payment = float(words[3])

        #Calculated expected payment
        expected_payment = melon_count * melon_cost
        #Check if customer payment is less than expected payment
        if customer_payment < expected_payment:
            #Calculate customer debt (rounding to 2 decimal places)
            customer_debt = round((expected_payment - customer_payment),2)
            total_debt = round((total_debt + customer_debt),2)
            #Change owe money string to reflect debt
            owe_money = f"owes the company ${customer_debt}"
        #Print all values per customer
        print(f"Customer ID {customer_id}: {customer_name} purchased {melon_count} for {customer_payment} expected payment was {expected_payment} and {owe_money}")
    #If debt exists, print total amount at the end of the function
    if total_debt > 0:
        print(f"Total debt of customers to melon company is: ${total_debt}")
    #Close file after done processing
    current_file.close()

checkCustomerPayment(file)