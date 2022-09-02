'''
Updates view parameters as "AoR--WW View:  WW".
Updates sheet parameters as "AoR--WW Sheet:  WW".
'''

import rpw
from rpw import doc

views = rpw.db.Collector(of_category="OST_Views", is_type=False).get_elements(wrapped=False)
sheets = rpw.db.Collector(of_category="OST_Sheets", is_type=False).get_elements(wrapped=False)

with rpw.db.Transaction('Categorize Views & Sheets'):
    for v in views:
        param = v.LookupParameter("AoR--WW View")
        try:
            param.Set("WW")
            '''
            if param.HasValue is False:
                try:
                    param.Set("WW")
                except:
                    pass
            elif param.Value != "WW":
                try:
                    param.Set("WW")
                except:
                    pass
                    '''
        except:
            pass
    
    for s in sheets:
        param = s.LookupParameter("AoR--WW Sheet")
        try:
            param.Set("WW")
            '''
            if s.LookupParameter("AoR--WW Sheet").HasValue is False:
                try:
                    s.LookupParameter("AoR--WW Sheet").Set("WW")
                except:
                    pass
                    '''
        except:
            pass

rpw.ui.forms.Alert('Views & Sheets categorized as "WW".\nCheck sorting in Project Browser.')