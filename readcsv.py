import csv

def read_csv_to_dict(filename, key_index=0):
  """
  Reads data from a CSV file and stores it in a dictionary.

  Args:
    filename: The path to the CSV file.
    key_index: The index of the column to use as the dictionary key 
               (default: 0 for the first column).

  Returns:
    A dictionary where keys are taken from the specified column 
    and values are lists of the remaining columns for each row.
  """

  data_dict = {}
  with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      key = row[key_index]
      data_dict[key] = row[:key_index] + row[key_index + 1:] 
  return data_dict

# Example usage:
csv_file = 'options/spy/spy.csv'  # Replace with the actual filename
data_dict = read_csv_to_dict(csv_file) 

print(data_dict)