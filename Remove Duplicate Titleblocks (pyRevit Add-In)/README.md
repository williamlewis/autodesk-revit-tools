# Remove Duplicate Titleblocks

### Use Case:

A series of Revit files (~500) was found to contain identical titleblock instances, in the same position on sheets.

In addition to duplicated titleblocks, a critical text note controlled by a visibility yes/no parameter was not consistenty enabled to display correctly.

The `Remove Duplicate Titleblocks` tool filter selects the relevant sheets, removes duplicate titleblock instances from those, and overwrites the related visibility parameter value to ensure the correct presence of the text note.
