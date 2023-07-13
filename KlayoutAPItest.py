import pya

# Create a new layout
layout = pya.Layout()

# Create a new layer (with layer index 1, datatype index 0)
layer = layout.layer(1, 0)

# Create a new cell
cell = layout.create_cell("MyCell")

# Create a box on the layer
box = pya.Box(0, 0, 1000, 2000)
cell.shapes(layer).insert(box)

# Write the layout to a file
layout.write("my_layout.gds")