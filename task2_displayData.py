import json
import re

# load the the json file
with open('products.json', 'r', encoding='utf-8') as file:
    products_data = json.load(file)

# the important specs that I chose
important_specs = {
    "Diameter φD": "Diameter φ",
    "Focal length f": "Focal length",
    "Edge thickness te": "Edge thickness",
    "Center thickness tc": "Center thickness",
    "Back focal length fb": "Back focal length",
    "Radius of curvature  r": "Radius of curvature"
}


# this is the approach with pandas library

# import pandas as pd
# rows = []
# for product_id, details in products_data.items(): 
#     row = {"Product_code": product_id}
#     for json_spec, table_col in important_specs.items():
#         row[table_col] = details["details"].get(json_spec)
#         rows.append(row)
# myTable = pd.DataFrame(rows)
# # Print the table
# print(myTable)

# this is the approach with prettytable library
from prettytable import PrettyTable

myTable = PrettyTable()
# initializing the field name with product_id and the specs that I chose
myTable.field_names = ["Product Code"] + list(important_specs.values()) 

for product_id, details in products_data.items():
    rows = [product_id]
    # add each important spec that I chose to the row with the format values
    for original_spec,values in important_specs.items():
        spec_value = details["details"].get(original_spec, "Missing")
        # I put a space between 1 or more digits in row and any upper or lower letter by splitting them in 2 groups \1 and \2
        spec_value = re.sub(r"(\d+)([a-zA-Z]+)", r"\1 \2", spec_value)
        # I remove φ character from Diameter column
        if "φ" in spec_value:
            spec_value = re.sub(r"φ", "", spec_value)   
        rows.append(spec_value)
    myTable.add_row(rows)

# print the table
print(myTable)