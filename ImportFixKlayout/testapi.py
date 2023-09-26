import os
print(os.getcwd())

import klayout.db as db
import klayout.lib

lm = db.LayerMap()
lm.map("1/0-255 : ONE (1/0)")
lm.map("2/0-255 : TWO (2/0)")
lm.map("3/0-255 : THREE (3/0)")

lo = db.LoadLayoutOptions()
lo.layer_map = lm
ly = db.Layout()
ly.read("ImportFixKlayout\contours.gds", lo)

all_polygons = []

# Iterate through all cells
for cell in ly.each_cell():
    for layer_index in ly.layer_indices():
        for shape in cell.shapes(layer_index).each():
            if shape.is_polygon():
                all_polygons.append(shape.polygon)

new_layout = db.Layout()
new_layout.dbu = ly.dbu  # Use the same database unit

# Define a layer (you can customize the layer number and datatype)
layer_info = db.LayerInfo(1, 0)
new_layer_index = new_layout.layer(layer_info)

# Create a cell
new_cell = new_layout.create_cell("PolygonCell")

# Insert the last polygon into the cell
"""new_cell.shapes(new_layer_index).insert(all_polygons[8])
new_cell.shapes(new_layer_index).insert(all_polygons[0])"""

# Create an empty region for each polygon
region1 = db.Region(all_polygons[0])
region2 = db.Region(all_polygons[8])

# Check if poly1 is inside poly2
# This is done by subtracting region2 from region1. If poly1 is entirely inside poly2, 
# the result will be an empty region.

# Assuming region1 and region2 are two Region objects
result = region1^region2
# Write the new layout to a GDS file
new_cell.shapes(new_layer_index).insert(result)
new_layout.write("ImportFixKlayout/output2.gds")

"""print(ly)

output_file = "ImportFixKlayout\output.gds"
ly.write(output_file)"""