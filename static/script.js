const Item_Type = document.getElementById("Item_Type");
const Item_Identifier = document.getElementById("Item_Identifier");
const Item_Weight = document.getElementById("Item_Weight");
const Item_Fat_Content = document.getElementById("Item_Fat_Content");
const Item_Visibility = document.getElementById("Item_Visibility");
const Item_MRP = document.getElementById("Item_MRP");
const Outlet_Identifier = document.getElementById("Outlet_Identifier");
const Forecast_year = document.getElementById(
  "forecast_year"
);
const Outlet_Size = document.getElementById("Outlet_Size");
const Outlet_Location_Type = document.getElementById("Outlet_Location_Type");
const Outlet_Type = document.getElementById("Outlet_Type");
const Model = document.getElementById("model");

const item_identifiers_data_list = document.getElementById(
  "item_identifiers_data_list"
);
const items_fat_content_data_list = document.getElementById(
  "items_fat_content_data_list"
);
const outlet_identifiers_data_list = document.getElementById(
  "outlet_identifiers_data_list"
);
const outlet_sizes_data_list = document.getElementById(
  "outlet_sizes_data_list"
);
const outlet_location_types_data_list = document.getElementById(
  "outlet_location_types_data_list"
);
const outlet_types_data_list = document.getElementById(
  "outlet_types_data_list"
);
const models_name_data_list = document.getElementById("models_name_data_list");

const items_visibility_data_list=document.getElementById("items_visibility_data_list")

function check_item_identifiers_data_list() {
  if (item_identifiers_data_list.children.length !== 0) {
    item_identifiers_data_list.innerHTML = "";
    Item_Identifier.value = "";
    Item_Identifier.disabled = true;
    Item_Weight.value = "";
  }
}

function check_items_fat_content_data_list() {
  if (items_fat_content_data_list.children.length !== 0) {
    items_fat_content_data_list.innerHTML = "";
    Item_Fat_Content.value = "";
    Item_Fat_Content.disabled = true;
    Item_Visibility.value = "";
    Item_Visibility.disabled = true;
    items_visibility_data_list.innerHTML="";
    Item_MRP.value = "";
    Item_MRP.disabled = true;
  }
}

function check_outlet_identifiers_data_list() {
  if (outlet_identifiers_data_list.children.length !== 0) {
    outlet_identifiers_data_list.innerHTML = "";
    Outlet_Identifier.value = "";
    Outlet_Identifier.disabled = true;
    Forecast_year.value = "";
    Forecast_year.disabled = true;
  }
}

function check_outlet_sizes_data_list() {
  if (outlet_sizes_data_list.children.length !== 0) {
    outlet_sizes_data_list.innerHTML = "";
    Outlet_Size.value = "";
    Outlet_Size.disabled = true;
  }
}

function check_outlet_location_types_data_list() {
  if (outlet_location_types_data_list.children.length !== 0) {
    outlet_location_types_data_list.innerHTML = "";
    Outlet_Location_Type.value = "";
    Outlet_Location_Type.disabled = true;
  }
}

function check_outlet_types_data_list() {
  if (outlet_types_data_list.children.length !== 0) {
    outlet_types_data_list.innerHTML = "";
    Outlet_Type.value = "";
    Outlet_Type.disabled = true;
    Model.value = "";
    Model.disabled = true;
  }
}

async function userVerify() {
 try {
    const response = await fetch(`/verify`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ key: pageKey }) // Send key in request body
    });

    const result = await response.text();
    return result.trim() === "1";
} catch {
    alert("Network Error");
    return false;
}
}

Item_Type.addEventListener("change", async (e) => {
  if (!(await userVerify())) {
    alert("Page Reload Required");
    location.reload();
  } else {
    check_item_identifiers_data_list();
    check_items_fat_content_data_list();
    check_outlet_identifiers_data_list();
    check_outlet_sizes_data_list();
    check_outlet_location_types_data_list();
    check_outlet_types_data_list();
    if (Item_Type.value == "") return;
    fetch("/item_identifier", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        Item_Type: Item_Type.value,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        data.forEach((item_id) => {
          const option = document.createElement("option");
          option.value = item_id;
          item_identifiers_data_list.append(option);
        });
      })
      .catch((error) => {
        console.error("Fetch error:", error);
        alert("Fetch error:,error");
      });

    Item_Identifier.disabled = false;
  }
});

Item_Identifier.addEventListener("change", async (e) => {
  if (!(await userVerify())) {
    alert("Page Reload Required");
    location.reload();
  } else {
    check_items_fat_content_data_list();
    check_outlet_identifiers_data_list();
    check_outlet_sizes_data_list();
    check_outlet_location_types_data_list();
    check_outlet_types_data_list();
    if (Item_Identifier.value == "") return;
    fetch("/items_fat_content", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        Item_Identifier: Item_Identifier.value,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        data.item_fat_content.forEach((item_fat) => {
          const option = document.createElement("option");
          option.value = item_fat;
          items_fat_content_data_list.append(option);
        });
        Item_Weight.value=data.item_weight[0];
      })
      .catch((error) => {
        console.error("Fetch error:", error);
        alert("Fetch error");
      });
    Item_Fat_Content.disabled = false;
  }
});

Item_Fat_Content.addEventListener("change", async (e) => {
  if (!(await userVerify())) {
    alert("Page Reload Required");
    location.reload();
  } else {
    check_outlet_identifiers_data_list();
    check_outlet_sizes_data_list();
    check_outlet_location_types_data_list();
    check_outlet_types_data_list();
    if (Item_Fat_Content.value == "") return;
    fetch("/outlet_identifier", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        Item_Type: Item_Type.value,
        Item_Identifier: Item_Identifier.value,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        data.oulet_identifier.forEach((outlet_id) => {
          const option = document.createElement("option");
          option.value = outlet_id;
          outlet_identifiers_data_list.append(option);
        });
        data.item_visibility.forEach((visibility) => {
          const option = document.createElement("option");
          option.value = visibility;
          items_visibility_data_list.append(option);
        });
        Item_MRP.min=data.item_mrp;
        Item_MRP.placeholder="e.g. "+data.item_mrp;
      })
      .catch((error) => alert("Fetch:", error));
    Item_Visibility.disabled = false;
    Item_MRP.disabled = false;
    Outlet_Identifier.disabled = false;
  }
});

Outlet_Identifier.addEventListener("change", async (e) => {
  if (!(await userVerify())) {
    alert("Page Reload Required");
    location.reload();
  } else {
    check_outlet_sizes_data_list();
    check_outlet_location_types_data_list();
    check_outlet_types_data_list();
    if (Outlet_Identifier.value == "") return;
    fetch("/outlet_sizes", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        Item_Type: Item_Type.value,
        Item_Identifier: Item_Identifier.value,
        Outlet_Identifier:Outlet_Identifier.value
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        data.outlet_size_list.forEach((outlet_sizes) => {

          const option = document.createElement("option");
          option.value = outlet_sizes;
          outlet_sizes_data_list.append(option);
        });
        Forecast_year.min=data.min_year;
      })
      .catch((error) => alert("Fetch:", error));
    Forecast_year.disabled = false;
    Outlet_Size.disabled = false;
  }
});

Outlet_Size.addEventListener("change", async (e) => {
  if (!(await userVerify())) {
    alert("Page Reload Required");
    location.reload();
  } else {
    check_outlet_location_types_data_list();
    check_outlet_types_data_list();
    if (Outlet_Size.value == "") return;
    fetch("/outlet_location", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        Item_Type: Item_Type.value,
        Item_Identifier: Item_Identifier.value,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        data.forEach((outlet_location) => {
          const option = document.createElement("option");
          option.value = outlet_location;
          outlet_location_types_data_list.append(option);
        });
      })
      .catch((error) => alert("Fetch:", error));

    Outlet_Location_Type.disabled = false;
  }
});

Outlet_Location_Type.addEventListener("change", async (e) => {
  if (!(await userVerify())) {
    alert("Page Reload Required");
    location.reload();
  } else {
    check_outlet_types_data_list();
    if (Outlet_Location_Type.value == "") return;
    fetch("/outlet_type", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        Item_Type: Item_Type.value,
        Item_Identifier: Item_Identifier.value,
        Outlet_Size:Outlet_Size.value
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        data.forEach((outlet_type) => {
          const option = document.createElement("option");
          option.value = outlet_type;
          outlet_types_data_list.append(option);
        });
      })
      .catch((error) => alert("Fetch:", error));

    Outlet_Type.disabled = false;
    Model.disabled = false;
  }
});

function showResult(result) {
  const box = document.getElementById("resultBox");
  const text = document.getElementById("predictionText");
  text.textContent = "Predicted Sales: ₹" + result;
  box.style.display = "block";
}

document
  .getElementById("predictionForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();
    document.getElementById("submitButton").disabled=true;
    const formData = new FormData(this);

    fetch("/predict", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        showResult(data.prediction); // show the result
        document.getElementById("submitButton").disabled=false;
      })
      .catch((error) => console.error("Prediction error:", error));
  });

Forecast_year.addEventListener("blur",()=>{
    const enteredYear = parseInt(Forecast_year.value);
    const minYear=parseInt(Forecast_year.min);
    if (enteredYear < minYear) {
       
        alert(`The year must be ${minYear} or later.`);
        Forecast_year.value='';
    }
  });

Item_MRP.addEventListener("blur",()=>{
    const enteredMRP = parseFloat(Item_MRP.value);
    const minMRP=parseFloat(Item_MRP.min);
    if (enteredMRP < minMRP) {
       
        alert(`The Item MRP must be ${minMRP} or more.`);
        Item_MRP.value='';
    }
  });