import numpy as np
import os
import cv2
import random
import matplotlib.pyplot as plt
import pickle

DIRECTORY = r"C:\Users\adria\Downloads\train"
CATEGORIES = ['cat', 'dog']

for category in CATEGORIES:
    folder = os.path.join(DIRECTORY, category)
    print(folder)