# Updates VIEW parameters as "AoR--Owner View:  Owner"
# Updates SHEET parameters as "AoR--Owner Sheet:  Owner"

# Import "Revit Python Wrapper" library to simplify calls to Revit API
import rpw
from rpw import doc


# Collect view and sheet objects throughout document (Revit 3D model file)
views = rpw.db.Collector(of_category="OST_Views", is_type=False).get_elements(wrapped=False)
sheets = rpw.db.Collector(of_category="OST_Sheets", is_type=False).get_elements(wrapped=False)


# Open Revit "transaction" to modify elements within file (closes automatically)
with rpw.db.Transaction('Categorize Views & Sheets'):
    # Populate / overwrite view parameter values
    for v in views:
        param = v.LookupParameter("AoR--WW View")
        try:
            param.Set("WW")
        except:
            pass
    
    # Populate / overwrite sheet parameter values
    for s in sheets:
        param = s.LookupParameter("AoR--WW Sheet")
        try:
            param.Set("WW")
        except:
            pass

# Notify user with pop-up message
rpw.ui.forms.Alert('Views & Sheets categorized as "WW".\nCheck sorting in Project Browser.')