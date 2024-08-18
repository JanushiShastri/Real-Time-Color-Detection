# Real-Time Color Detection with OpenCV and PIL
This project demonstrates real-time color detection using OpenCV and PIL (Python Imaging Library). The script captures video from the webcam, detects a specified color (yellow by default), and draws a bounding box around the detected color area in real-time.

## Features
#### Real-time video capture from the webcam.
#### Detection of a specific color (yellow by default) in the video feed.
#### Bounding box drawn around the area where the specified color is detected.
#### Easy-to-customize color detection using the get_limits function.

## Requirements
Python 3.6+

OpenCV

PIL (Pillow)

NumPy

## Installation
Clone the Repository:
```bash
git clone https://github.com/yourusername/ColorDetection.git
cd ColorDetection
```

Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv color-detection-venv
source color-detection-venv/bin/activate
```

Install the required dependencies:
```bash
pip install opencv-python pillow numpy 

```
## Usage
Run the Script:

```bash

 python main.py
 ```
The script will access the webcam, detect the specified color (yellow by default), and display a live video feed with a bounding box drawn around the detected color area.

Change the Color to Detect:

The color to detect is specified in BGR format in the yellow variable:
```bash 
python
yellow = [0, 255, 255]  # yellow in BGR
```

To detect a different color, modify this variable with the desired BGR values.
Quit the Video Feed:
Press the q key to exit the video feed and close the webcam.
