import cv2
from realsense_camera import *
import os
import csv



rs = RealsenseCamera()
directory = r'C:\Users\sotao\Desktop\IntelRealsense'

os.chdir(directory)
for x in range(300):
    ret, rgb_frame, depth_frame = rs.get_frame_stream()
    cv2.imwrite(('test' + str(x) + '.jpg'), rgb_frame)

    with open("depthcsv" + str(x) + ".csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(depth_frame)

    #cv2.waitKey(1)