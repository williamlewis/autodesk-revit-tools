# autodesk-revit-tools
Assistive automations to accelerate workflow and facilitate user management for Revit.

Autodesk Revit is a widespread, 3D Building Information Modeling ("BIM") software used in the practice of architectural design & construction.

<br/>

---

## Revit Add-ins using pyRevit

*Created using the Revit API + IronPython language + pyRevit + Revit Python Wrapper*


<br/>

- **Remove Duplicate Titleblocks** - for subset of sheets, check for and purge duplicate titleblock classes, then overwrite shared parameter to ensure visibility of disclaimer note on remaining sheets
<br/>

- **Open Multiple Views** - check user selection in Project Browser, then open multiple views and sheets to perform tasks in batches and expedite daily workflow
<br/>

- **Dimension Multiple Lines** - create a dimension string with witness lines on multiple parallel line classes, to expedite repeated annotation process
<br/>

- **Categorize Views & Sheets** - overwrite a shared parameter value for view and sheet classes, to distinguish owner contents from future vendor contents within a shared file

<br/>

<u>Resources & Credits:</u>

[pyRevit](https://github.com/eirannejad/pyRevit) Rapid Application Development Environment for Autodesk Revit, by Ehsan Iran-Nejad

[Revit Python Wrapper](https://github.com/gtalarico/revitpythonwrapper) library of wrapper classes, by Gui Talarico

[Revit API](https://knowledge.autodesk.com/support/revit/learn-explore/caas/CloudHelp/cloudhelp/2014/ENU/Revit/files/GUID-F0A122E0-E556-4D0D-9D0F-7E72A9315A42-htm.html) for Autodesk Revit

[IronPython](https://ironpython.net/) implementation of Python language for compatibility with the .NET framework

<br/>

---

## Terminal Scripts for Revit User Managment
<br/>

- **Auto Reinstall Revit Add-In** - purge previous add-in files from all possible locations, replace with latest version, & run executable installation file from a Google shared drive location
<br/>

    --
<br/>

- **List Users from Filenames to Text** - convert set of filenames into a text file with linebreaks
<br/>

- **List Users from File & Folder Names to Text** - convert set of filenames and directory names into a text file with linebreaks
<br/>

- **List Users from Folder Names in Terminal** - list out all directory names with linebreaks, for copy/paste into a tracking document
