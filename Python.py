# import os

# project_structure = {
#     'Programowanie Python': ['Cwiczenia', 'Zadania domowe'],
#     'NumPy': ['NumPy I', 'NumPy II'],
#     'Pandas': ['Pandas I', 'Pandas II'],
#     'Project': ['tekst1', 'tekst2']
# }
# def create_project_structure(Data_Science, structure):
# # Tworzenie głównego folderu
#     os.makedirs(Data_Science, exist_ok=True)
#     print(f"Utworzono projekt: {Data_Science}/")
# # Tworzenie podfolderów
# for folder, subfolders in structure.items():
#     folder_path = os.path.join(Data_Science, folder)
#     os.makedirs(folder_path, exist_ok=True)
#     print(f" ├── {folder}/")
    
# create_project_structure("Data_Science", project_structure)

import os

project_structure = {
    'Programowanie Python': ['Cwiczenia', 'Zadania domowe'],
    'NumPy': ['NumPy I', 'NumPy II'],
    'Pandas': ['Pandas I', 'Pandas II'],
    'Project': ['tekst1', 'tekst2']
}

def create_project_structure(Data_Science, structure):
    # główny folder
    os.makedirs(Data_Science, exist_ok=True)

    # podfoldery
    for folder, subfolders in structure.items():
        folder_path = os.path.join(Data_Science, folder)
        os.makedirs(folder_path, exist_ok=True)

        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)

create_project_structure("Data_Science", project_structure)

print("Gotowe!")