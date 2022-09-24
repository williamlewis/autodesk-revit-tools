import os 


############### lists out directory names in terminal ################ 
 
path = 'C:/Users/wlewis/Documents/_Desktop_/Checked_Revit_Users' # source directory containing subdirectories named for each Revit user
files = os.listdir(path) 
for f in files: 
    print(f)