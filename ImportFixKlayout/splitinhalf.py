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
ly.read("GDSExport\exported.gds", lo)

all_polygons = []

result = db.Region()

# Iterate through all cells
for cell in ly.each_cell():
    for layer_index in ly.layer_indices():
        for shape in cell.shapes(layer_index).each():
            if shape.is_polygon():
                region = db.Region(shape.polygon)
                result = result ^ region

new_layout = db.Layout()
new_layout.dbu = ly.dbu  # Use the same database unit

# Define a layer (you can customize the layer number and datatype)
layer_info = db.LayerInfo(1, 0)
new_layer_index = new_layout.layer(layer_info)

# Create a cell
new_cell = new_layout.create_cell("TOP")

rect = db.Box(-20000, 0, 30000, -50000)  # Rectangle from (0,0) to (1000,500)

rect_region = db.Region(rect)

result = result - rect_region

# Write the new layout to a GDS file
new_cell.shapes(new_layer_index).insert(result)
new_layout.write("GDSExport/exportedfixed.gds")
