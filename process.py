import pandas as pd
import joblib

df=None
mapping_df=None
item_name_mapping_df=None
model=None
previousModel=None
def read_files():
    global df
    global mapping_df
    global item_name_mapping_df
    df=pd.read_csv("files/cleaned_data.csv")
    mapping_df=pd.read_csv("files/multi_encoded_output.csv")
    item_name_mapping_df=pd.read_csv("files/product_names.csv")
   
def get_item_identifiers(item_type):
    unique_item_identifier=sorted(df[df["Item_Type"] == item_type]["Item_Identifier"].unique().tolist())
    filtered_names = item_name_mapping_df[item_name_mapping_df["Item_Identifier"].isin(unique_item_identifier)]
    name_map = filtered_names.set_index("Item_Identifier")["Item_Name"].to_dict()
    combined_list = [f"{iid}-{name_map.get(iid, '')}" for iid in unique_item_identifier]
    return combined_list

def get_item_weight_item_Fat_Content(item_identifier):
    item_weight=df[df['Item_Identifier']==item_identifier]['Item_Weight'].unique().tolist()
    item_fat_content=sorted(df[df["Item_Identifier"] == item_identifier]["Item_Fat_Content"].unique().tolist())
    return item_weight,item_fat_content

def get_item_Visibility_outlet_Identifier_AND_MinMRP(item_type,item_identifier):
    item_visibility=df[df['Item_Identifier']==item_identifier]['Item_Visibility'].unique().tolist()
    item_mrp=df[df['Item_Identifier']==item_identifier]['Item_MRP'].min()
    oulet_identifier=sorted(df[(df["Item_Type"] == item_type)&(df["Item_Identifier"] == item_identifier)]["Outlet_Identifier"].unique().tolist())
    return item_visibility,oulet_identifier,item_mrp

def get_outlet_Size(item_type,item_identifier,outlet_identifier):
    min_year=int(df[df["Outlet_Identifier"]==outlet_identifier]['Outlet_Establishment_Year'].unique())
    return sorted(df[(df["Item_Type"] == item_type)&(df["Item_Identifier"] == item_identifier)]["Outlet_Size"].unique().tolist()),min_year

def get_outlet_Location(item_type,item_identifier):
    return sorted(df[(df["Item_Type"] == item_type)&(df["Item_Identifier"] == item_identifier)]["Outlet_Location_Type"].unique().tolist())

def get_outlet_Type(item_type,item_identifier,outlet_size):
    return sorted(df[(df["Item_Type"] == item_type)&(df["Item_Identifier"] == item_identifier)&(df["Outlet_Size"]==outlet_size)]["Outlet_Type"].unique().tolist())

def selectionItemTypeAndModelName():
    read_files()
    item_types=sorted(df["Item_Type"].unique().tolist())
    models_name=["Random Forest"]
    return item_types,models_name

# Define a function to preprocess the input data
def get_label(mapping_df, column, label_column, value):
    
    result = mapping_df[mapping_df[column] == value][label_column]
    if not result.empty:
        return result.values[0]
    else:
        raise ValueError(f"[Error] Value '{value}' not found in column '{column}'")

def preprocessInput(request):
    try:
        # Ensure data is loaded
        if df is None or mapping_df is None:
            read_files()
            
        print("[Info] Starting input preprocessing...", flush=True)
        
        # Extract form data
        form_data = request.form
        outletEstablishmentYear=df[df["Outlet_Type"] == form_data['Outlet_Type']]['Outlet_Establishment_Year'].unique().min()
        outletAge=int(form_data['forecast_year'])-int(outletEstablishmentYear)
        features = {
            "Item_Identifier": [get_label(mapping_df, 'Item_Identifier', 'Item_Identifier_Label', form_data['Item_Identifier'].split('-')[0])],
            "Item_Weight": [float(form_data['Item_Weight'])],
            "Item_Fat_Content": [get_label(mapping_df, 'Item_Fat_Content', 'Item_Fat_Content_Label', form_data['Item_Fat_Content'])],
            "Item_Visibility": [float(form_data['Item_Visibility'])],
            "Item_Type": [get_label(mapping_df, 'Item_Type', 'Item_Type_Label', form_data['Item_Type'])],
            "Item_MRP": [float(form_data['Item_MRP'])],
            "Outlet_Identifier": [get_label(mapping_df, 'Outlet_Identifier', 'Outlet_Identifier_Label', form_data['Outlet_Identifier'])],
            "Outlet_Establishment_Year":[int(outletEstablishmentYear)],
            "Outlet_Size": [get_label(mapping_df, 'Outlet_Size', 'Outlet_Size_Label', form_data['Outlet_Size'])],
            "Outlet_Location_Type": [get_label(mapping_df, 'Outlet_Location_Type', 'Outlet_Location_Type_Label', form_data['Outlet_Location_Type'])],
            "Outlet_Type": [get_label(mapping_df, 'Outlet_Type', 'Outlet_Type_Label', form_data['Outlet_Type'])],
            "Outlet_Age": [outletAge]
        }
       
        input_df = pd.DataFrame(features)
        
        # Check for any NaNs after conversion
        if input_df.isnull().values.any():
            print("[Abort] Missing or invalid data in input:")
            print(input_df)
            return None
        
        return input_df

    except (KeyError, ValueError, TypeError, Exception) as e:
        import traceback
        print("[Preprocessing Error]:", str(e))
        traceback.print_exc()
        
        print("[Preprocessing Error]:", e)
        return None
        

def selectedModelPrediction(input_data,modelName):
    global model
    global previousModel
    if input_data is None:
        print("[Error] input_data is None")
        return None

    try:
        if modelName == previousModel and model is not None:
            pass
                
        elif modelName == 'Random Forest':
            try:
                with open('models/randomForestModel.joblib', 'rb') as file:
                    model = joblib.load(file)
                    previousModel=modelName
            except FileNotFoundError:
                print("[Error] Model not found. Please train the model first.(Open Jupyter Notebook)")
                return None
        else:
            print(f"[Error] Unknown model name: {modelName}")
            return None

        prediction = model.predict(input_data)
        return prediction[0] if prediction is not None else None
    
    except Exception as e:
        print("[Model Prediction Error]:", e)
        return None
