// face_detection_debug_2.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include "head.h"

int main(int argc, const char** argv)
{
	if (!face_cascade.load(face_cascade_name))
	{
		printf("Error loading face cascade\n");
		return -1;
	}
	else
	{
		while (true)
		{
			capture_frame();
			if (frame.empty())
			{
				printf("Empty frame!\n");
				continue;
			}
			if (waitKey(5) == 27)
				break; // esc to quit
			face_detection(frame);
		}
	}
	return 0;
}

//function definition
void capture_frame()
{
	VideoCapture cap;
	cap=VideoCapture("http://183.172.49.42:8080/shot.jpg");//ip address
	if (!cap.isOpened())
	{
		printf("Error capturing frame from net!\n");
		return;
	}
	cap>>frame;
	cap.release();
	IMG_WIDTH = frame.rows;
	IMG_HEIGHT= frame.cols;
}

void face_detection(Mat frame)
{
	std::vector<Rect> faces;
	Mat frame_gray;
	cvtColor(frame, frame_gray, COLOR_BGR2GRAY);
	equalizeHist(frame_gray, frame_gray);

	//face detection
	face_cascade.detectMultiScale(frame_gray, faces,1.1, 3,0, Size(40, 40));
	//face number
	size_t num = faces.size();
	if (num == 0)
		return;

	//find largest face
	std::vector<int> faces_area;
	for (size_t i = 0; i < num; i++)
		faces_area.push_back(faces[i].width*faces[i].height);
	auto maxPosition = max_element(faces_area.begin(), faces_area.end());
	__int64 index = maxPosition - faces_area.begin();
	Point center(faces[index].x + faces[index].width / 2, faces[index].y + faces[index].height / 2);
	//bluetooth

	//display section: draw rectangle(optional)
	Point original(faces[index].x, faces[index].y);
	Point diagonal(faces[index].x + faces[index].width, faces[index].y + faces[index].height);
	rectangle(frame, original, diagonal, Scalar(255, 0, 0), 3, 6, 0);
	imshow("Capture - Face detection", frame);
	waitKey(500);
	printf("success!\n");
}