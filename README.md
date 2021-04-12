# ssz-palette
Color palette for matplotlib

## Overview

Here is a list of all available colormaps in this module:



## Installation

To install ssz-palette from GitHub run the following command:

```
pip install git+https://github.com/StatistikStadtZuerich/ssz-palette.git#egg=sszpalette
```

## Usage

To use one of the defined colormaps with matplotlib, simply import this module, register the colormaps and start using them:

```python
import numpy as np
import matplotlib.pyplot as plt
import sszpalette

# register the ssz color palette
colorsmaps = sszpalette.register()
```

`register()` returns the names of all added colormaps (e.g. `harmonic6`).
To then use this colormap, simply provide it's name to the plot:

```python
# create mock data
x,y,c = zip(*np.random.rand(30,3)*4-2)
norm = plt.Normalize(-2,2)

# scatter plot with harmonic6 colormap
plt.scatter(x,y,c=c, cmap='harmonic6', norm=norm)
plt.colorbar()
plt.show()
```

Result:



See the Jupyter Notebook `SSZ Palette in Matplotlib.ipynb` for a complete example.