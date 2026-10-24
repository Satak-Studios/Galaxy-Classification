import h5py
import numpy as np

with h5py.File('models/Galaxy10.h5', 'r') as F:
    print("Keys in HDF5:", list(F.keys()))
    
    raw_images = np.array(F['images'])  # Shape: (21785, 69, 69, 3)
    raw_labels = np.array(F['ans'])     # Shape: (21785,), values: 0 to 9

    print(raw_images.shape)