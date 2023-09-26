import lumapi

# Create a handle to an FDTD Solutions session
fdtd = lumapi.FDTD()

# Load the GDS file
fdtd.load('y_branch_3D_Final.lms')