# Places a dimension string object with witness lines attached to multiple parallel lines


# Import pyRevit libraries & DB namepsace from Revit API assemblies
from revitutils import doc
from Autodesk.Revit import DB


# Store user selection of lines objects with element collector class
collector = DB.FilteredElementCollector(doc)
lines = collector.OfCategory(DB.BuiltInCategory.OST_HiddenLines)


# Retrieve first line object & its endpoint location
line1 = lines[0]
point1 = line1.GeometryCurve.GetEndPoint(0)
ref1 = line1.GeometryCurve.GetEndPointReference(0)


# Retrieve last line object & its endpoint location
line2 = lines[1]
point2 = line2.GeometryCurve.GetEndPoint(0)
ref2 = line2.GeometryCurve.GetEndPointReference(0)




#---------------------
# Define arguments to be used in NewDimension method

view = doc.ActiveView

line = DB.Line.CreateBound(point1, point2)

reference = ReferenceArray()
reference.Append(ref1)
reference.Append(ref2)




#---------------------
# Create new dimension string within a transaction

transaction = DB.Transaction(doc)
transaction.Start()

doc.Create.NewDimension(view, line, reference)

transaction.Commit()