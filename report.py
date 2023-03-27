import csv
import matplotlib.pyplot as plt
from wordcloud import WordCloud

account_id_to_filter = '001j000000sDhBY'

file_names = [
    'accounts.csv',
    'contacts.csv',
    'opportunities.csv',
    'cases.csv'
]

def filter_and_print_rows(file_name, account_id_column_index, fields_to_print=None, values_to_find=None):
    with open(file_name, 'r', encoding='ISO-8859-1') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        print(f"{file_name} Information")

        for row in csv_reader:
            if row[account_id_column_index] == account_id_to_filter:
                print_filtered_data(row, header, fields_to_print, values_to_find)
        print("\n")

def print_filtered_data(row, header, fields_to_print, values_to_find):
    if fields_to_print is None:
        print(row)
    else:
        if values_to_find is not None:
            for column, value in values_to_find:
                if row[column] == value:
                    print_columns(row, header, fields_to_print)
        else:
            print_columns(row, header, fields_to_print)

def print_columns(row, header, columns_to_print):
    for i in columns_to_print:
        if row[i] != "":
            print(f"{header[i]}: {row[i]}")

def generate_word_cloud(file_name, account_id_column_index, subject_column):
    raw_data = ""
    with open(file_name, 'r', encoding='ISO-8859-1') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        for row in csv_reader:
            if row[account_id_column_index] == account_id_to_filter:
                raw_data = row[subject_column] + '\n'

    wordcloud = WordCloud(background_color='white', width=800, height=800).generate(raw_data)
    plot_word_cloud(wordcloud)

def plot_word_cloud(wordcloud):
    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(account_id_to_filter + '.png', dpi=300)
    plt.show()

def count_field_values(file_name, account_id_column_index, count_column_index, values):
    counter_data = {value: 0 for value in values}

    with open(file_name, 'r', encoding='ISO-8859-1') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        for row in csv_reader:
            if row[account_id_column_index] == account_id_to_filter:
                counter_data[row[count_column_index]] += 1
        print(counter_data)

for file_name in file_names:
    if file_name == 'accounts.csv':
        account_id_column_index = 19
        fields_to_print = [3, 1, 2, 4, 5, 6, 14, 15, 16, 17, 18]
        values_to_find = None
    elif file_name == 'contacts.csv':
        account_id_column_index = 5
        fields_to_print = [0, 1, 6]
        values_to_find = [(6, 'Champion'), (6, 'Economic Buyer')]
    elif file_name == 'opportunities.csv':
        account_id_column_index = 1  # Replace with the correct index of account_id in opportunities.csv
        fields_to_print = [3,4]
        values_to_find = None
    elif file_name == 'cases.csv':
        account_id_column_index = 6  # Replace with the correct index of account_id in cases.csv
        fields_to_print = [5,13,3]
        values_to_find = None
        count_field_values(file_name, account_id_column_index=6, count_column_index=3, values=["Priority 1 (Urgent)","Priority 2 (High)","Priority 3 (Normal)","Priority 4 (Low)"])
        generate_word_cloud(file_name,account_id_column_index=6,subject_column=13)
    filter_and_print_rows(file_name, account_id_column_index, fields_to_print, values_to_find)
