import cv2
from realsense_camera import *
import os
import numpy as np                        # fundamental package for scientific computing
from numpy import array
import pandas as pd 
import time

numberOfPics = 30

rs = RealsenseCamera()
directory = r'C:\Users\sotao\Desktop\Data\Test'

os.chdir(directory)
# dec_filter = rs.decimation_filter ()   # Decimation - reduces depth frame density
# spat_filter = rs.spatial_filter()          # Spatial    - edge-preserving spatial smoothing
# temp_filter = rs.temporal_filter()    # Temporal   - reduces temporal noise
# hole_filter = rs.hole_filling_filter() #Hole filling
# temporaryDepth = array([[0 for col in range(1280)]for row in range(720)])
# temporaryDepth = temporaryDepth.reshape((temporaryDepth.shape[0], temporaryDepth.shape[1], 1))

#720p
#sigma = [1, 1] #How big the blur is

start = time.time()
for x in range(numberOfPics):
    
    ret, rgb_frame, depth_frame = rs.get_frame_stream()
    
    cv2.imshow("image", depth_frame/9550.0) 

    #SAVE STUFF
    np.save('depth' + str(x) + '.npy', depth_frame)
    #cv2.imwrite(('Depth' + str(x) + '.png'), depth_frame/40)
    cv2.imwrite(('RGB' + str(x) + '.png'), rgb_frame)
    
    cv2.waitKey(10)
print("DONE!!!!!!")
print("it took milliseconds: " + str(time.time() - start))
