import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Step 1: Load your CSV file
df = pd.read_csv("cleaned_data.csv")

# Step 2: Specify which columns to encode
columns_to_encode = ["Item_Identifier", "Item_Fat_Content","Item_Type","Outlet_Identifier","Outlet_Size","Outlet_Location_Type","Outlet_Type"]  # replace with your column names

# Step 4: Encode each column
for col in columns_to_encode:
    le = LabelEncoder()
    df[col + "_Label"] = le.fit_transform(df[col])

# Step 5: Save the new encoded DataFrame
df.to_csv("multi_encoded_output.csv", index=False)
print("Multiple columns encoded and saved as 'multi_encoded_output.csv'")
