# Pedestrian-traffic-detection
## Introduction
This is a applicaiton for detection pedestrian traffic based on YOLOv3 framework by YifengChen ([yfchen@stu.suda.edu.cn](yfchen@stu.suda.edu.cn)).
The repository is based on the python tensorflow/keras implementation of yolo avaiable [here](https://pjreddie.com/darknet/yolo/).
The testing detecting result is shown below:

<img src="https://github.com/YifengChen94/Pedestrian-traffic-detection/blob/master/test.gif" width="550" height="400" alt="test.gif"/>

## Quick start
Specially, the project is based on tensorflow/keras. If you haven't install tensorflow/keras, you should follow the installation of [Tensorflow](https://github.com/tensorflow/tensorflow). 
[OpenCV](https://pypi.org/project/opencv-python/) is also required before trying the demo.
1. Clone the repository
```
  git clone https://github.com/YifengChen94/Pedestrian-traffic-detection
```
2. Download the YOLOv3 weights from YOLO website
```
  cd Pedestrian-traffic-detection
  wget https://pjreddie.com/media/files/yolov3.weights
```
3. Convert the Darknet YOLO model to a Keras model.
```
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
```
4. Run pedestrain traffic detection. The testing video is avaiable [here](https://pan.baidu.com/s/1op1FJCcEuHe2pXdgDoZgqw)
```python
python yolo_video.py [video_path] [output_path (optional)]
```
Tips, for Tiny YOLOv3, just follow the similar command and specify model path and anchor path in yolo.py
```
 wget https://pjreddie.com/media/files/yolov3-tiny.weights
 python convert.py yolov3-tiny.cfg yolov3-tiny.weights model_data/yolo-tiny.h5
```
## Some issues to know
1.The test environment is

- Python 3.5.2

- Keras 2.2.2

- tensorflow-gpu 1.9.0

2.Default anchors are used. If you use your own anchors, probably some changes are needed.

3.For detecting pedestrain, you can modify the threshold value in order to fit your practical application. Spectific information is listed below:
```python
  self.threshold = 3    # detecting whether person in
  self.out_boxes = out_boxes
  self.width = image.size[0]
  self.height = image.size[1]
  self.left = 190       # The starting point of the detection line, default (190,470)
  self.right = 605
  self.top = 470        # The ending point of the detection line, default (605,461)
  self.bottom = 461
  self.detectthreshold = 15   # Threshold for detecting if the same person
```

