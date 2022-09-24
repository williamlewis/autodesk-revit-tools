from fileinput import filename 
import os 


################ lists file names only (not folder names), saving to a TXT file ################ 
 
outputfile = "C:/Users/wlewis/Documents/_Desktop_/Checked_Revit_Users.txt" # file output where directory names have been converted to text, separated by line breaks
folder = 'C:/Users/wlewis/Documents/_Desktop_/Checked_Revit_Users' # source directory containing files named for each Revit user
exclude = [] 
pathsep = "\\" 
 
 
with open(outputfile, "w") as txtfile: 
    for dirs in os.listdir(folder): 
        prefix = "ScanWin-" 
        if dirs.startswith(prefix): 
            dirs = dirs.strip(prefix) 
 
        sep = "\n" 
        #print(sep + dirs) 
        print(dirs) 
        #txtfile.write("%s\n" % sep + dirs) 
        txtfile.write(sep+dirs) 
 
txtfile.close()