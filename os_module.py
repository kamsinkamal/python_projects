import os

directory = r"C:\Users\kamal\Desktop\python_projects"
files = os.listdir(directory)
print(files) 
file_path = "example.jpg"
if os.path.exists(file_path):
    print("File exists!")
  