import tensorflow as tf
import os
import numpy as np
import math
class detect_result(object):

    def __init__(self,out_boxes,image):
        self.threshold = 3
        self.out_boxes = out_boxes
        self.width = image.size[0]
        self.height = image.size[1]
        self.left = 190
        self.right = 605
        self.top = 470
        self.bottom = 461
       # self.prepoints = prepoints
        self.detectthreshold = 15



    def return_center(self):
        centers= []
        for i in range(len(self.out_boxes)):
            box = self.out_boxes[i]
            top, left, bottom, right = box
            top = max(0, np.floor(top + 0.5).astype('int32'))
            left = max(0, np.floor(left + 0.5).astype('int32'))
            bottom = min(self.height, np.floor(bottom + 0.5).astype('int32'))
            right = min(self.width, np.floor(right + 0.5).astype('int32'))

            x = int((left+right)/2)
            y = int((top+bottom)/2)
            center = [x,y]
            centers.append(center)
        return np.array(centers,dtype=np.int32)

    def detect_inline(self):
        centers = self.return_center()
        final_points = []
        for c in centers:
            if self.left<=c[0]<=self.right:
                distance = self.line_distance(c)
                if (distance<=self.threshold):
                    final_points.append(c)

            else:
                continue
        return np.array(final_points)


    def line_distance(self,point):
        A = self.bottom - self.top
        B = self.left - self.right
        C = self.right*self.top - self.left*self.bottom
        distance = abs(A*point[0]+B*point[1]+C)/math.sqrt(A**2+B**2)
        return distance


    def point_distance(self,pointA,pointB):

        x = pointA[0]-pointB[0]
        y = pointA[1]-pointB[1]

        return math.sqrt(x**2+y**2)

    def detect_preson(self,prepoints,final_points):
        keys=0

        #final_points = self.detect_inline()
        # print(final_points)
        return_points =[]
        # points = []
    #    else:
        for fp in final_points:
            points = []

            for pp in prepoints:

                dis = self.point_distance(pp,fp)
                points.append(dis)
                # print(pp)
                # print(dis)
                # if(dis<distance):
                #     distance = dis
            points = np.array(points)
            if (np.min(points)>=self.detectthreshold):
                print(np.min(points))
                keys+=1
            return_points.append(fp)




        return return_points,keys







