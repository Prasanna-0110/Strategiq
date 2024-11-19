import csv
import json
 
def csv_to_json(csv_file_path, json_file_path):
    # Open the CSV file for reading
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(csv_file)
        # Convert the CSV rows into a list of dictionaries (each row becomes a dictionary)
        data = [row for row in csv_reader]
    # Write the JSON data to the output file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        # Convert the list of dictionaries into JSON and write it to the file
        json.dump(data, json_file, indent=4)
 
# Example usage:
csv_file_path = 'Financial Statements.csv'  # Path to the CSV file you want to convert
json_file_path = 'testdata_financial.json'  # Path to save the JSON output
 
csv_to_json(csv_file_path, json_file_path)