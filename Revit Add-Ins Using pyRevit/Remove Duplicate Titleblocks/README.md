# Remove Duplicate Titleblocks

### Use Case:

A series of Revit files (~500) was found to contain identical titleblock instances, in the same position on sheets.

In addition to duplicated titleblocks, a critical legal disclaimer note, controlled by a yes/no visibility parameter, was not consistenty enabled to display the text correctly.

The `Remove Duplicate Titleblocks` tool:
1. Filter selects the relevant sheets
2. Removes duplicate titleblock instances from those sheets
3. Overwrites the related visibility parameter value to ensure visibility of the legal text note
4. Prints a table of remaining titleblocks as a visual confirmation of results to the user
