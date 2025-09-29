import subprocess,os
import venv
import time,signal

def checkVirtualEnviromnet(venv_python):
    if os.path.exists(venv_python):
        return 1
    else:
        return 0

def train_model(notebook_path,signal_file_path):
    process = subprocess.Popen(["jupyter", "notebook", notebook_path])
    print("Jupyter Notebook started. Waiting for model file...")
    while not os.path.exists(signal_file_path):
      time.sleep(10)  # check every 5 seconds
    os.remove(signal_file_path)
    print("Model file created. Shutting down notebook server...")
    process.terminate()
    process.wait()
    print("Jupyter Notebook stopped.")
    
def startApp(venv_python,venv_dir,notebook_path,signal_file_path):
      
      if checkVirtualEnviromnet(venv_python):
          if not os.listdir("models"):
             print("Please train the model first.(Open Jupyter Notebook)")
             train_model(notebook_path,signal_file_path)
         
          print("Launching App")
          subprocess.run([venv_python, "app.py"])
          
      else: 
          print("Creating virtual environment...")
          venv.create(venv_dir,with_pip=True)
          print(f"Virtual environment '{venv_dir}' created successfully.")
          
          print("Please wait while library installation completes...")
          subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"])
          
          libraries = ["flask==3.1.2",
                       "pandas==2.3.2",
                       "joblib==1.5.2",
                       "matplotlib==3.10.6",
                       "seaborn==0.13.2",
                       "scikit-learn==1.7.1",
                       "ipykernel==6.30.1",
                       "notebook==7.2.2"
                       ]  
          subprocess.run([venv_python, "-m", "pip", "install"] + libraries)
          print("Virtual environment setup complete!")
          
          
          print("Adding virtual environment to Jupyter kernels...")
          subprocess.run([venv_python, "-m", "ipykernel", "install", "--user", "--name", venv_dir, "--display-name", venv_dir])
          
          print("Virtual environment setup complete!")
          
          if not os.listdir("models"):
             print("Please train the model first.(Open Jupyter Notebook)")
             train_model(notebook_path,signal_file_path)
          
          print("Launching App")
          subprocess.run([venv_python, "app.py"])
          
if __name__=='__main__':
    venv_dir="projectVirtualEnv"
    venv_python = f"{venv_dir}/Scripts/python.exe"
    notebook_path="model_train/Sales_Prediction_Random_Forest.ipynb"
    signal_file_path="models/signal.flag"
    startApp(venv_python,venv_dir,notebook_path,signal_file_path)
