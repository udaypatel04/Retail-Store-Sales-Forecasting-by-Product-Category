from flask import Flask, request, render_template,jsonify,session
import process as pc
import secrets
import webbrowser
from threading import Timer

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def home():
    if "page_key" not in session:
        session["page_key"] = secrets.token_urlsafe(16)
    item_types,models_name=pc.selectionItemTypeAndModelName()
    return render_template('index.html',item_types=item_types,models_name=models_name,page_key=session["page_key"])

@app.route("/verify",methods=["POST"])
def verify_key():
    data=request.get_json('key')
    if data and data.get('key') == session.get("page_key"):
        return "1"
    else:
        return "0"

@app.route('/item_identifier', methods=['POST'])
def itemIdentifier():
    data=request.get_json()
    item_type=data.get('Item_Type')
    return jsonify(pc.get_item_identifiers(item_type=item_type))

@app.route('/items_fat_content', methods=['POST'])
def itemWeightAndFatContent():
    data=request.get_json()
    item_identifier=data.get('Item_Identifier').split('-')[0]
    item_weight,item_fat_content=pc.get_item_weight_item_Fat_Content(item_identifier=item_identifier)
    return jsonify({"item_weight":item_weight,"item_fat_content":item_fat_content})

@app.route('/outlet_identifier', methods=['POST'])
def itemVisibilityAndoutletIdentifierAndItemMRP():
     data=request.get_json()
     item_type=data.get('Item_Type')
     item_identifier=data.get('Item_Identifier').split('-')[0]
     item_visibility,oulet_identifier,item_mrp=pc.get_item_Visibility_outlet_Identifier_AND_MinMRP(item_type=item_type,item_identifier=item_identifier)
     return jsonify({"item_visibility":item_visibility,"oulet_identifier":oulet_identifier,"item_mrp":item_mrp})

@app.route('/outlet_sizes', methods=['POST'])
def outletSizeAndMinYear():
    data=request.get_json()
    item_type=data.get('Item_Type')
    item_identifier=data.get('Item_Identifier').split('-')[0]
    outlet_identifier=data.get('Outlet_Identifier')
    oulet_size_list,min_year=pc.get_outlet_Size(item_type=item_type,item_identifier=item_identifier,outlet_identifier=outlet_identifier)
    return jsonify({"outlet_size_list": oulet_size_list, "min_year": min_year})

@app.route('/outlet_location', methods=['POST'])
def outletLocation():
    data=request.get_json()
    item_type=data.get('Item_Type')
    item_identifier=data.get('Item_Identifier').split('-')[0]
    return jsonify(pc.get_outlet_Location(item_type=item_type,item_identifier=item_identifier))

@app.route('/outlet_type', methods=['POST'])
def outletType():
    data=request.get_json()
    item_type=data.get('Item_Type')
    item_identifier=data.get('Item_Identifier').split('-')[0]
    outlet_size=data.get('Outlet_Size');
    print(outlet_size)
    return jsonify(pc.get_outlet_Type(item_type=item_type,item_identifier=item_identifier,outlet_size=outlet_size))

@app.route('/predict', methods=['POST'])
def predict():
    modelName=request.form['model']
    input_process_data = pc.preprocessInput(request)
    prediction = pc.selectedModelPrediction(input_data=input_process_data,modelName=modelName)
    
    if prediction:
        output = f'{prediction:.2f}'
        return jsonify({'prediction': output})
    else:
        return jsonify({'prediction': 'Error'})

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")
        
if __name__ == '__main__':    
    Timer(1, open_browser).start()
    app.run(port=5000, debug=False)