#pragma once
#include "objdetect.hpp"
#include "highgui.hpp"
#include "imgproc.hpp"

using namespace std;
using namespace cv;

//global variable
CascadeClassifier face_cascade;
String face_cascade_name = "haarcascade_frontalface_alt.xml";
Mat frame;
int IMG_WIDTH = 640;//by default
int IMG_HEIGHT = 480;//by default

//function statement
void capture_frame();
void face_detection(Mat frame);



