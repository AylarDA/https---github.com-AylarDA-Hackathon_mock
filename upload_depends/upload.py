import sys
import os
import uuid
import shutil


def upload_image(directory, file):
    BASE_PATH = f"/uploads/{directory}/"
    path = sys.path[0] + BASE_PATH
    print(sys.path)
    if not os.path.exists(path):
        os.makedirs(path)
            
    
    sp = file.filename.split(".")
    extension = sp[-1]
    unique_id = str(uuid.uuid4())
    new_name = unique_id + "." + extension
    upload_file_path_for_save_static = path + f"{new_name}"
    upload_file_path_for_db = BASE_PATH + f"{new_name}"
    
    
    with open(upload_file_path_for_save_static, "wb") as file_object:
        shutil.copyfileobj(file.file, file_object)
    if upload_file_path_for_db:
        return upload_file_path_for_db
    else:
        return False