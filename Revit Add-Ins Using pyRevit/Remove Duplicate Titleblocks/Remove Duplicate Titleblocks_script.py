# Automation to check Revit models for duplicate titleblock instances, purging duplicates and updating visibility parameter settings to display a legal disclaimer note

# import modules from Revit API, pyRevit, & python pretty printer
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction
from pyrevit import revit, script
import pprint

# set up resource for current Revit file & final output to print
doc = __revit__.ActiveUIDocument.Document
output = script.get_output()


#############################
#### GET RELEVANT SHEETS ####
#############################

# get all sheets in document
sheets = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_Sheets)
    .WhereElementIsNotElementType()
    .ToElements()
)

# filter sheets to get relevant 'DWG' category sheets, then store in dictionary
dwgSheets = {}
for sheet in sheets:
    if "DWG Plan Export" in sheet.Name:
        dwgSheets[sheet] = [
            sheet.SheetNumber,
            sheet.Name,
        ]
    else:
        pass


###########################################
#### FIND & SORT DUPLICATE TITLEBLOCKS ####
###########################################

# get & count titleblocks on DWG sheets, to determine if there are duplicate instances
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
        ):  # relies on the fact that element IDs are chronological (i.e. latest is probably correct), and that they were appended into a list ordered by element IDs
            listOfTBsToKeep.append(i)
        else:
            listOfTbsToDelete.append(i)


#####################################################
#### DELETE DUPLICATES & MAKE LEGAL TEXT VISIBLE ####
#####################################################

# open a transaction to commit changes to elements within the active document
t = Transaction(doc)
try:
    # delete duplicate titleblocks in the "to-delete" list
    t.Start("Purge Duplicate Titleblocks")
    for i in listOfTbsToDelete:
        doc.Delete(i.Id)
    
    # make legal note visible on titleblocks in the "to-keep" list
    for i in listOfTBsToKeep:
        i.LookupParameter("DWG Waiver On").Set( # parameter name as defined in file template
            1
        )  # integer 1 indicates that checkbox value is checked (i.e. Yes for Y/N)
    t.Commit()
except:
    t.RollBack()
    print("transaction had to roll back")


################################
#### PRINT RESULTS FOR USER ####
################################

# print latest results for visual confirmation to user, without needing to open or check individual sheet views
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
