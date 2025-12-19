# Sales Forecasting by Product Category

This project focuses on predicting retail sales at the **product category level** using machine learning techniques.  
It provides an automated workflow where the user can train a model and launch a web application to view forecasting results.

The project is designed to simplify setup by automatically creating a virtual environment, installing required libraries, and launching Jupyter Notebook and a Flask web app.

---

## Project Overview

Accurate sales forecasting helps retail businesses plan inventory, manage supply chains, and improve decision-making.  
This project uses historical sales data to train a machine learning model that predicts future sales based on product categories.

---

## Features

- Product category-wise sales forecasting
- Automated virtual environment creation
- Automatic dependency installation
- Model training using Jupyter Notebook
- Flask-based web interface to view results
- Simple and beginner-friendly workflow

---

## Requirements

- **Python** (any recent version installed on the system)

All required Python libraries are installed automatically when the project starts.

---

## How to Run the Project

### 1. Clone the repository

git clone https://github.com/udaypatel04/Retail-Store-Sales-Forecasting-by-Product-Category.git

cd Retail-Store-Sales-Forecasting-by-Product-Category

---

### 2. Start the project

python LaunchApp.py

This command will:
- Create a virtual environment named `projectVirtualEnv`
- Install all required dependencies
- Launch Jupyter Notebook automatically

---

### 3. Train the model in Jupyter Notebook

- Change the kernel to **projectVirtualEnv**
- Run all notebook cells in sequence
- Wait until the model is trained and saved successfully

---

### 4. Launch the web application

After training is completed:
- `app.py` will run automatically inside the virtual environment
- A Flask web application will start

Open your browser and visit:

http://localhost:5000

to use the application.

---

## Project Structure

project/
│
├── files/ # Dataset and supporting files
├── model_train/ # Model training scripts and notebooks
├── models/ # Trained and saved models
├── projectVirtualEnv/ # Auto-created virtual environment
├── static/ # Static files (CSS, JS, images)
├── templates/ # HTML templates for Flask
├── app.py # Flask web application
├── column_to_encode.py # Categorical column encoding logic
├── LaunchApp.py # Entry point for setup and execution
├── process.py # Data preprocessing logic
└── README.md # Project documentation

---

## Use Case

This project is suitable for:
- Machine learning academic projects
- Retail analytics learning
- Demonstrating end-to-end ML workflow
- Portfolio and GitHub showcase

---

## Future Enhancements

- Add more advanced forecasting models
- Improve UI and visualizations
- Support real-time data input
- Add performance metrics dashboard
- Deploy the application on cloud

---

## License

This project is created for educational and academic purposes.  
You are free to use and modify it for learning and non-commercial use.

---

## Author

**Uday Patel**  
