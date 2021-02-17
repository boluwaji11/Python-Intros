def main():   
    
    found = False  
    coffee_file = open('coffee.txt', 'r')
    record = coffee_file.readline()
    search = input('Enter the coffee description to search for: ')
    while record != '':
        record = record.rstrip('\n')
        split_record = record.split('\t')   # Split each field in the record into lists      
        if search in split_record:
            print()
            print('Record Found....')
            print('Description\t', 'Quantity')
            print('--------------------------')
            print(record)
            found = True  
        record = coffee_file.readline()
    if not found:
            print()
            print('The record', search, 'was not found in the file.')     
    coffee_file.close()   
    print()
    print('Thanks for using the Program!')

# Call the main function.
main()
