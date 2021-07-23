import cv2
from realsense_camera import *
import os
import csv
import numpy as np                        # fundamental package for scientific computing
from numpy import array
import matplotlib.pyplot as plt  
import pandas as pd 
import time
import scipy as sp
import scipy.ndimage

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
    #temporaryRGB[x] = rgb_frame
    #print("type : " + str(type(temporaryDepth)) + " shape: " + str(temporaryDepth.shape))
    
    #temporaryDepth = np.concatenate( ( temporaryDepth, depth_frame.reshape(depth_frame.shape[0], depth_frame.shape[1], 1) ) , axis=-1) #np.concatenate((temporaryDepth, depth_frame.reshape(depth_frame.shape[0], depth_frame.shape[1], 1)), 2) #np.dstack((temporaryDepth, depth_frame))
    # temporaryDepth[x] = depth_frame

    #FILTERS
    # filtered = dec_filter.process(depth_frame)
    # filtered = spat_filter.process(filtered)
    # filtered = temp_filter.process(filtered)
    # depth_frame = sp.ndimage.filters.gaussian_filter(depth_frame, sigma, mode='constant')

    #DISPLAY STUFF
    # print(str(len(temporaryRGB[x][x])) + " x: " + str(x) + "contents: " + str(temporaryRGB[x]))
    # print(str(len(temporaryDepth[x])) + " x: " + str(x) + "contents: ")
    # cv2.imshow("iage", temporaryDepth[:, :,x]/4000.0) 
    cv2.imshow("iage", depth_frame/9550.0) 

    #SAVE STUFF
    # if(np.amax(depth_frame) > max):
    #     max = np.amax(depth_frame)
    cv2.imwrite('fname' + str(x) + '.jpg', depth_frame/40.0)
    cv2.imwrite(('ayyyyyyy' + str(x) + '.jpg'), rgb_frame)
    # pd.DataFrame(depth_frame).to_csv("Depth" + str(x) + ".csv", header=None, index=None)
    


    # colorizer = rs.colorizer()
    # colorized_depth = np.asanyarray(colorizer.colorize(depth_frame).get_data())

    # plt.rcParams["axes.grid"] = False
    # plt.rcParams['figure.figsize'] = [8, 4]
    # plt.imshow(colorized_depth)
    
    cv2.waitKey(10)
print("DONE!!!!!!")
print("it took milliseconds: " + str(time.time() - start))
# print(str(temporaryDepth.shape[2]))

# #save the depth files. The first one is empty so skiup over that
# for i in range(temporaryDepth.shape[2]):
#     print(str(i))
#     if(i != 0):
#         pd.DataFrame(temporaryDepth[:, :, i]).to_csv("Depth" + str(i - 1) + ".csv", header=None, index=None)
# print("shape: " + str(temporaryDepth[:,:,1].shape))