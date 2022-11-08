# Opens multiple selected views & sheets in a batch 

import rpw 
from rpw import ui, db, doc 
from pyrevit import revit, DB, UI 
from pyrevit import forms 
from Autodesk.Revit.UI import UIApplication, RevitCommandId, PostableCommand 

# Read current user selection (views and sheets from Revit Project Browser)
selection = revit.get_selection() 

# Loop through selection and activate each view
# Note:  view activation does NOT work within a Revit transaction, but works fine outside of a transaction
for v in selection:
    v_to_open = revit.doc.GetElement(v.Id) 
	revit.uidoc.ActiveView = v_to_open