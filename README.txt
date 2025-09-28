Project Name: Sales Forecasting by Product Category

This project focuses on predicting sales by product category using machine learning. It provides a simple interface where you can train the model and launch a web app to view results.

Requirements

* Python (any recent version installed on your computer)

All other dependencies are automatically handled.

How to Run

1. Clone the repository:

   
   git clone https://github.com/udaypatel04/Retail-Store-Sales-Forecasting-by-Product-Category.git
   cd Retail-Store-Sales-Forecasting-by-Product-Category
   

2. Start the project:

   
   python LaunchApp.py
   

   * This will create a virtual environment.
   * It will also install all necessary libraries.
   * Jupyter Notebook will launch automatically.

3. In Jupyter Notebook:

   * Change the kernel to the one named **projectVirtualEnv**.
   * Run all cells in order.
   * Wait until the model is trained and saved.

4. After training:

   * The file `app.py` will run automatically inside the virtual environment.
   * A Flask web app will be created.
   * Open your browser and go to:

     
     http://localhost:5000
     

     to use the application.

Project Structure

│project/
│── files/                # Data and supporting files
│── model_train/          # Scripts and notebooks for training
│── models/               # Saved models
│── projectVirtualEnv/    # Auto-created virtual environment
│── static/               # Static assets (CSS, JS, images)
│── templates/            # HTML templates for Flask
│── app.py                # Flask web application
│── column_to_encode.py   # Handles encoding of categorical columns
│── LaunchApp.py          # Entry point: sets up environment and workflow
│── process.py            # Data processing logic
│── README.md             # Project documentation


