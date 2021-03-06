import cv2
from realsense_camera import *
import os
import csv
import numpy as np                        # fundamental package for scientific computing
import matplotlib.pyplot as plt  


rs = RealsenseCamera()
directory = r'D:\DataFromRealsense'
csvWriter = csv.writer(my_csv,delimiter=',')

os.chdir(directory)
# dec_filter = rs.decimation_filter ()   # Decimation - reduces depth frame density
# spat_filter = rs.spatial_filter()          # Spatial    - edge-preserving spatial smoothing
# temp_filter = rs.temporal_filter()    # Temporal   - reduces temporal noise
# hole_filter = rs.hole_filling_filter() #Hole filling

for x in range(30):
    ret, rgb_frame, depth_frame = rs.get_frame_stream()
    # filtered = dec_filter.process(depth_frame)
    # filtered = spat_filter.process(filtered)
    # filtered = temp_filter.process(filtered)
    cv2.imshow("iage", rgb_frame)
    cv2.imwrite(('ayyyyyyy' + str(x) + '.jpg'), rgb_frame)

    with open("depthcsv" + str(x) + ".csv","w+") as my_csv:
        
        csvWriter.writerows(depth_frame)
    
    # colorizer = rs.colorizer()
    # colorized_depth = np.asanyarray(colorizer.colorize(depth_frame).get_data())

    # plt.rcParams["axes.grid"] = False
    # plt.rcParams['figure.figsize'] = [8, 4]
    # plt.imshow(colorized_depth)

    cv2.waitKey(30)