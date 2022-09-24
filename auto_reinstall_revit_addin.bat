Rem This batch script is for uninstalling previous versions of the [Proprietary 'Data Extractor'] Addin for Revit, then reinstalling the latest version from the [Department] google shared drive (managed by Design Technology team). 
@echo off 
echo -------- Starting Installation Process --------  
 

:: -------- ALERT USER IF REVIT IS NOT CLOSED -------- 
tasklist /fi "ImageName eq Revit.exe" /fo csv 2>NUL | find /I "Revit.exe">NUL 
 
if "%ERRORLEVEL%"=="0" echo Please close all instances of Revit, then rerun install_Harvester.bat 
if "%ERRORLEVEL%"=="0" pause 
if "%ERRORLEVEL%"=="0" exit 
 
 
:: -------- PURGE OUTDATED FILES FROM ALL POSSIBLE PREVIOUS VERSIONS OF [DATA EXTRACTOR ADDIN] -------- 
:: --------     from AppData - main .addin file
del "%AppData%\Autodesk\Revit\Addins\2015\ModelRepSync.addin" /s /q 
del "%AppData%\Autodesk\Revit\Addins\2016\ModelRepSync.addin" /s /q 
del "%AppData%\Autodesk\Revit\Addins\2017\ModelRepSync.addin" /s /q 
del "%AppData%\Autodesk\Revit\Addins\2018\ModelRepSync.addin" /s /q 
del "%AppData%\Autodesk\Revit\Addins\2019\ModelRepSync.addin" /s /q 
del "%AppData%\Autodesk\Revit\Addins\2020\ModelRepSync.addin" /s /q 
del "%AppData%\Autodesk\Revit\Addins\2021\ModelRepSync.addin" /s /q 
del "%AppData%\Autodesk\Revit\Addins\2022\ModelRepSync.addin" /s /q 
:: --------     from AppData - directory of libraries & DLLs
rd "%AppData%\Autodesk\Revit\Addins\2015\ModelRepSync" /s /q 
rd "%AppData%\Autodesk\Revit\Addins\2016\ModelRepSync" /s /q 
rd "%AppData%\Autodesk\Revit\Addins\2017\ModelRepSync" /s /q 
rd "%AppData%\Autodesk\Revit\Addins\2018\ModelRepSync" /s /q 
rd "%AppData%\Autodesk\Revit\Addins\2019\ModelRepSync" /s /q 
rd "%AppData%\Autodesk\Revit\Addins\2020\ModelRepSync" /s /q 
rd "%AppData%\Autodesk\Revit\Addins\2021\ModelRepSync" /s /q 
rd "%AppData%\Autodesk\Revit\Addins\2022\ModelRepSync" /s /q 
:: --------     from ProgramData - main .addin file
del "C:\ProgramData\Autodesk\Revit\Addins\2015\ModelRepSync.addin" /s /q 
del "C:\ProgramData\Autodesk\Revit\Addins\2016\ModelRepSync.addin" /s /q 
del "C:\ProgramData\Autodesk\Revit\Addins\2017\ModelRepSync.addin" /s /q 
del "C:\ProgramData\Autodesk\Revit\Addins\2018\ModelRepSync.addin" /s /q 
del "C:\ProgramData\Autodesk\Revit\Addins\2019\ModelRepSync.addin" /s /q 
del "C:\ProgramData\Autodesk\Revit\Addins\2020\ModelRepSync.addin" /s /q 
del "C:\ProgramData\Autodesk\Revit\Addins\2021\ModelRepSync.addin" /s /q 
del "C:\ProgramData\Autodesk\Revit\Addins\2022\ModelRepSync.addin" /s /q 
:: --------     from ProgramData - directory of libraries & DLLs
rd "C:\ProgramData\Autodesk\Revit\Addins\2015\ModelRepSync" /s /q 
rd "C:\ProgramData\Autodesk\Revit\Addins\2016\ModelRepSync" /s /q 
rd "C:\ProgramData\Autodesk\Revit\Addins\2017\ModelRepSync" /s /q 
rd "C:\ProgramData\Autodesk\Revit\Addins\2018\ModelRepSync" /s /q 
rd "C:\ProgramData\Autodesk\Revit\Addins\2019\ModelRepSync" /s /q 
rd "C:\ProgramData\Autodesk\Revit\Addins\2020\ModelRepSync" /s /q 
rd "C:\ProgramData\Autodesk\Revit\Addins\2021\ModelRepSync" /s /q 
rd "C:\ProgramData\Autodesk\Revit\Addins\2022\ModelRepSync" /s /q 
 
 
:: -------- PLACE LATEST [DATA EXTRACTOR ADDIN] FILES IN CORRESPONDING APPDATA FOLDERS -------- 
Xcopy "G:\Shared drives\Prod-Global Project Content\Tooling & Services\Harvester\Version 1-3-15\2017" "%AppData%\Autodesk\Revit\Addins\2017" /s /e /y 
Xcopy "G:\Shared drives\Prod-Global Project Content\Tooling & Services\Harvester\Version 1-3-15\2018" "%AppData%\Autodesk\Revit\Addins\2018" /s /e /y 
Xcopy "G:\Shared drives\Prod-Global Project Content\Tooling & Services\Harvester\Version 1-3-15\2019" "%AppData%\Autodesk\Revit\Addins\2019" /s /e /y 
Xcopy "G:\Shared drives\Prod-Global Project Content\Tooling & Services\Harvester\Version 1-3-15\2020" "%AppData%\Autodesk\Revit\Addins\2020" /s /e /y 
 
 
:: -------- RUN EXECUTABLE FILE TO PERFORM INSTALLATION -------- 
start /d "G:\Shared drives\Prod-Global Project Content\Tooling & Services\Harvester\Version 1-3-15" cp-srs-mmi.exe 
 
echo -------- Installation Process Complete -------- 
 
 
:: Future Updates: 
:: check that Google Drive for Desktop is installed and connected 
::    if not, provide warning to check that Google Drive for Desktop is installed and connected? 
 
 
@REM exit