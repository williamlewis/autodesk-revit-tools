from Autodesk.Revit.DB import FilteredElementCollector 
from Autodesk.Revit.DB import BuiltInCategory 
from Autodesk.Revit.DB import Transaction 
from pyrevit import revit 
from pyrevit import script 
import pprint 
 
doc = __revit__.ActiveUIDocument.Document 
 
output = script.get_output() 
 
 
# get all sheets in document 
sheets = ( 
    FilteredElementCollector(doc) 
    .OfCategory(BuiltInCategory.OST_Sheets) 
    .WhereElementIsNotElementType() 
    .ToElements() 
) 
 
# get list of DWG sheets 
dwgSheets = {} 
for sheet in sheets:
    if "DWG Plan Export" in sheet.Name: 
        dwgSheets[sheet] = [ 
            sheet.SheetNumber, 
            sheet.Name, 
        ]  # would prefer to use sheet Id for key, but only getting extended version instead of 8-digit number 
    else: 
        pass 
 
 
# get & count titleblocks on DWG sheets 
allDwgTbs = [] 
for sheet in dwgSheets: 
    tbCount = 0 
    sheetTbs = [] 
 
    tblocks = revit.query.get_sheet_tblocks(sheet) 
    for tblock in tblocks: 
        allDwgTbs.append(tblock) 
 
        tbCount += 1 
        sheetTbs.append(tblock) 
 
    dwgSheets[sheet].append(tbCount) 
    dwgSheets[sheet].append(sheetTbs) 
 
 
# sort DWG sheet titleblocks into those to keep (latest) vs. those to delete (all others) 
listOfTbsToDelete = [] 
listOfTBsToKeep = [] 
 
for sheet in dwgSheets: 
    listOfSheetTbs=dwgSheets.get(sheet)[3] 
 
    for i in listOfSheetTbs: 
        if( 
            i == listOfSheetTbs[-1] 
        ):  # relies on the fact that element IDs are chronological (i.e. latest is probably correct), and that they were appended into a list in that order by element ID 
            listOfTBsToKeep.append(i) 
        else: 
            listOfTbsToDelete.append(i) 
 
 
# within a transaction, delete duplicate DWG sheet titleblocks & set DWG waiver as visible in remaining DWG sheet titleblocks 
t = Transaction(doc) 
try: 
    t.Start("Purge Duplicate Titleblocks") 
    for i in listOfTbsToDelete: 
        doc.Delete(i.Id) 
    for i in listOfTBsToKeep: 
        i.LookupParameter("DWG Waiver On").Set( 
            1 
        )  # use integer 1 as value to make checkbox checked 
    t.Commit() 
except: 
    t.RollBack() 
    print("transaction had to roll back") 
 
 
# print latest results for visual confirmation 
updatedDwgTbs = [] 
for sheet in dwgSheets: 
    tblocks = revit.query.get_sheet_tblocks(sheet) 
    updatedDwgTbs.extend([x.Id for x in tblocks]) 
    for tblock in tblocks: 
        print( 
            sheet.SheetNumber, 
            sheet.Name, 
            "DWG Waiver Visible? > " 
            + tblock.LookupParameter("DWG Waiver On").AsValueString(), 
            output.linkify(tblock.Id), 
        ) 
 
 
def main(): 
    doc = __revit__.ActiveUIDocument.Document 
 
 
if __name__ == "__main__": 
    main() 