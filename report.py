import csv

# Replace 'account_id_to_filter' with the account_id you want to filter the data by
account_id_to_filter = '001j000000sDhBY'

file_names = [
    'accounts.csv',
    'contacts.csv',
    'opportunities.csv',
    'cases.csv'
]

# Function to filter and print rows based on account_id
def filter_and_print_rows(file_name, account_id_column_index, fields_to_print=None, values_to_find=None):
    with open(file_name, 'r', encoding='ISO-8859-1') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        print(f"{file_name} Information")
        #print(header)
        for row in csv_reader:
            if row[account_id_column_index] == account_id_to_filter:
                
                if fields_to_print == None:
                    print(row)
                else:
                    if values_to_find != None:
                        for column, value in values_to_find:
                            if row[column] == value:
                                for i in fields_to_print:
                                    print(header[i]+': '+row[i])
                                    
                    else:
                        for i in fields_to_print:
                            if row[i] != "":
                                print(header[i]+': '+row[i])   

            
        print("\n")
def count_field(account_id_column_index, count_column_index, values):
    # 1. Get a unique list of the values found in a column
    
    """  
    values = ['a','b','c']
    counter_data = {}
    for value in values:
        counter_data[value] = 0
    rows = [['a',1],['a',0],['c',1]]
    for row in rows:
        counter_data[row[0]] += 1
    print(counter_data)
    """
    # 2. Iterate for each of the rows and count each of the values found

    counter_data = {}
    for value in values:
        counter_data[value] = 0
    
    with open(file_name, 'r', encoding='ISO-8859-1') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        for row in csv_reader:
            if row[account_id_column_index] == account_id_to_filter:
                counter_data[row[count_column_index]] += 1
        print(counter_data)

# Iterate over the CSV files and filter the data based on account_id
for file_name in file_names:
    if file_name == 'accounts.csv':
        account_id_column_index = 19  # Replace with the correct index of account_id in accounts.csv
        fields_to_print = [3,1,2,4,5,6,14,15,16,17,18]
        values_to_find = None
    elif file_name == 'contacts.csv':
        account_id_column_index = 5  # Replace with the correct index of account_id in contacts.csv
        fields_to_print = [0,1,6]
        values_to_find = [(6,'Champion'), (6,'Economic Buyer')]
    elif file_name == 'opportunities.csv':
        account_id_column_index = 1  # Replace with the correct index of account_id in opportunities.csv
        fields_to_print = [3,4]
        values_to_find = None
    elif file_name == 'cases.csv':
        account_id_column_index = 6  # Replace with the correct index of account_id in cases.csv
        fields_to_print = [5,13,3]
        values_to_find = None
        count_field(account_id_column_index=6, count_column_index=3, values=["Priority 1 (Urgent)","Priority 2 (High)","Priority 3 (Normal)","Priority 4 (Low)"])
    filter_and_print_rows(file_name, account_id_column_index, fields_to_print, values_to_find)
