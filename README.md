# ssz-palette
Color palette for matplotlib

## Overview

Here is a list of all available colormaps in this module:

![Overview of available colormaps](https://user-images.githubusercontent.com/538415/114397915-7a5db900-9b9f-11eb-805c-b9976569859e.png)

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

![Scatter with harmonic6 colormap](https://user-images.githubusercontent.com/538415/114397996-919ca680-9b9f-11eb-956e-30799688d700.png)


To change the default colormap and set the color cycle (e.g. used for the colors of line charts), use the following snippet:

```python
plt.set_cmap('contrasting12') # or any other colormap
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.get_cmap().colors)
```


See the [Jupyter Notebook `SSZ Palette in Matplotlib.ipynb`](https://github.com/StatistikStadtZuerich/ssz-palette/blob/main/SSZ%20Palette%20in%20Matplotlib.ipynb) ([**HTML version**](https://statistikstadtzuerich.github.io/ssz-palette/example.html)) for a complete example.
