from fileinput import filename 
import os 


################ lists folder AND file names, saving to a TXT file ################ 
 
outputfile = "C:/Users/wlewis/Documents/_Desktop_/Checked_Revit_Users.txt" # file output where directory names have been converted to text, separated by line breaks
folder = 'C:/Users/wlewis/Documents/_Desktop_/Checked_Revit_Users' # source directory containing files and subdirectories named for each Revit user
exclude = [] 
pathsep = "\\" 
 
with open(outputfile, "w") as txtfile: 
    for path, dirs, files in os.walk(folder): 
        sep = "\n--------" + path.split(pathsep)[len(path.split(pathsep)) - 1] + "--------" 
        print(sep) 
        txtfile.write("%s\n" % sep) 
 
        for fn in sorted(files): 
            if not any(x in fn for x in exclude): 
                filename = os.path.splitext(fn)[0] 
 
                print(filename) 
                txtfile.write("%s\n" % filename) 
txtfile.close()