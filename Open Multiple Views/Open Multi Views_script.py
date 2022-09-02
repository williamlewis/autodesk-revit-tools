''' 
Opens multiple selected views & sheets, then tiles active windows. 
''' 

# read current user selection 
# for v in views (including both views & sheets), activate view 
# tile all activated views 

importrpw 
fromrpwimportui, db, doc 
frompyrevitimportrevit, DB, UI 
frompyrevitimportforms 
fromAutodesk.Revit.UIimportUIApplication, RevitCommandId, PostableCommand 

selection=revit.get_selection() 

forvinselection: 
	v_to_open=revit.doc.GetElement(v.Id) 
	revit.uidoc.ActiveView=v_to_open 

# activating views does NOT work in a transaction, but works fine kept OUTSIDE a transaction 


''' 
uiapp = UIApplication(doc.Application) ​ 

tile_windows = UI.RevitCommandId.LookupPostableCommandId(UI.PostableCommand.TileWindows) 
uiapp.PostCommand(tile_windows) 
''' 

​
''' 
zoom_extents = UI.RevitCommandId.LookupPostableCommandId(UI.PostableCommand.TileWindows) 
#uiapp = UIApplication(doc.Application) 
uiapp.PostCommand(zoom_extents) 
''' 

''' 
with rpw.db.Transaction('Multi Open Views & Sheets'): 
    try: 
        for v in selection: 
            v_to_open = revit.doc.GetElement(v.Id) 
            revit.uidoc.ActiveView = v_to_open 
        else: 
            pass 
    except: 
        pass 
''' 