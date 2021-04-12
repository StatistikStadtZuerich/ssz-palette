import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors


 __version__ = "0.1.0"


palettes = {
    # gray scales
    'gray10': ['#2a2a2a', '#404040', '#606060', '#7c7c7c', '#989898', '#aaaaaa', '#c2c2c2', '#d2d2d2', '#e8e8e8', '#f4f4f4'],
    'gray10cool': ["#001215", "#082429", "#223a41", "#3d575e", "#5c7781", "#79949f", "#8dafbc", "#b2ccd7", "#dfe9ef", "#f4f7f9"],
    'gray10warm': ["#131111", "#252323", "#3b3737", "#545050", "#726f6e", "#8f8b8b", "#aca8a8", "#c9c5c4", "#e4e0df", "#f6f3f2"],
    
    # harmonic scales
    'harmonic6': ['#0f05a0', '#2ac7c7' ,'#0a8df6', '#a2e5b0', '#3d575e', '#23c3f1'],
    'harmonic12': ['#0f05a0', '#94b7f8', '#009f9d', '#2ac7c7', '#0a8df6', '#88cfff', '#009755', '#a2e5b0', '#3d575e', '#8dafbc', '#0076aa', '#23c3f1'],
    'harmonic6hell': ['#94b7f8', '#7ee7e3', '#88cfff', '#a2e5b0', '#b2ccd7', '#bbeefe'],
  
    # contrasting scales
    'contrasting12': ['#0f05a0', '#65cd8c', '#960055', '#0098c6', '#fbcb97', '#53831b', '#fb737e', '#351459', '#2ac7c7', '#b9d55c', '#46b2ff', '#5c7781'],
    'contrasting12hell': ['#94b7f8', '#a2e5b0', '#f18785', '#7bdcf9', '#fbcb97', '#b9d55c', '#f99ec8', '#bc92ff', '#8ecf69', '#b5f4f4', '#8dafbc', '#c5e7ff'],

    # sequential scales
    'sequential9blau': ['#030033', '#080490', '#1e1fc1', '#3e46dd', '#606dee', '#8391f7', '#a6b2fc', '#c8d0fe', '#e9ecff'],
    'sequential5blau': ['#080490', '#3e46dd', '#8391f7', '#c8d0fe', '#e9ecff'],
    'sequential9rot': ['#1a0207', '#450612', '#720b1f', '#9d142e', '#c22340', '#df3b57', '#f26178', '#fc99a8', '#ffe0e4'],
    'sequential5rot': ['#720b1f', '#9d142e', '#df3b57', '#fc99a8', '#ffe0e4'],
    'sequential9ocker': ['#1a1000', '#452b00', '#724600', '#9d6100', '#c27800', '#df9114', '#f2ac3c', '#fccb7b', '#ffebcc'],
    'sequential5ocker': ['#724600', '#9d6100', '#df9114', '#fccb7b', '#ffebcc'],
    'sequential9petrol': ['#001414', '#00312f', '#004d4b', '#006a68', '#008685', '#18a2a1', '#48bfbe', '#86dbdb', '#d0f7f7'],
    'sequential5petrol': ['#004d4b', '#008685', '#18a2a1', '#86dbdb', '#d0f7f7'],
    
    # diverginig scales
    #### 5 Farben rot zu grün
    'diverging5rotgruen': ['#EA4F61', '#F6AFA0', '#F4F7F9', '#B5F4F4', '#2AC7C7'],
    'diverging5rotblau': ['#EA4F61', '#F6AFA0', '#F4F7F9', '#94B7F8', '#0F05A0'],
    
    # special scales
    'gender4': ['#0F05A0', '#94B7F8', '#EA4F61', '#F6AFA0'],
    'nation4': ['#0F05A0', '#94B7F8', '#2AC7C7', '#B5F4F4'],
}


def register():
    registered_colormaps = []
    for name, colors in palettes.items():
        cmap = matplotlib.colors.ListedColormap(colors=colors, name=name)
        boundaries = np.linspace(0, 1, len(colors))
        plt.register_cmap(cmap=cmap)
        registered_colormaps.append(name)
    return registered_colormaps