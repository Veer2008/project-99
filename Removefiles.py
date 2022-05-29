import time
import os
import shutil

def main():
    folders_count=0
    files_count=0
    path="/pathtodelete"
    days=30
    seconds=time.time()-(days*24*60*60)
    
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds>=file_or_folder_age(root_folder):
                remove_folder(root_folder)
                folders_count+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if seconds>=file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        folders_count+=1
                
                for file in files:
                    file_path=os.path.join(root_folder,file)
                    if seconds>=file_or_folder_age(file_path):
                        remove_file(file_path)
                        files_count+=1
        
        else:
            if seconds>=file_or_folder_age(path):
                remove_file(path)
                files_count+=1
    else:
        print("Path not found")
    
    print(f"Total folders deleted:{folders_count}")
    print(f"Total files deleted:{files_count}")

def file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

def remove_folder(path):
    if not shutil.rmtree(path):
        print("Path removed successfully")
    else :
        print("Unable to delete the path")
        
def remove_file(path):
    if not os.remove(path):
        print("Path removed successfully")
    else :
        print("Unable to delete the path")

main()
                
            
