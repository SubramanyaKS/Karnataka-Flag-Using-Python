# -*- coding: utf-8 -*-
"""KarnatakaFlag.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13QJygde5qhQIUXMnnnp-YS3vWvMkhfSs

# Karnataka Flag

Karnataka Flag using Python
"""

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch

red=patch.Rectangle((0,1), width=8, height=2,facecolor='red', edgecolor='grey')
yellow=patch.Rectangle((0,3), width=8, height=2,facecolor='yellow', edgecolor='grey')
mm,n= plt.subplots()
n.add_patch(red)
n.add_patch(yellow)
plt.axis('equal')
plt.title("Karnataka Flag")
plt.show();
print("ಜೈ ಕರ್ನಾಟಕ ಮಾತೆ")
print("ಸಿರಿಗನ್ನಡಂ ಗೆಲ್ಗೆ ಸಿರಿಗನ್ನಡಂ ಬಾಳ್ಗೆ")

