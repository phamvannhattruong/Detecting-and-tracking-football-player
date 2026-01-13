## You can get the video demo in folder output_data/

## ⚽ Football Player Detection & Tracking with YOLO 

This project utilizes the YOLO deep learning model combined with object tracking algorithms to detect and monitor players, referees, and the ball in football match videos.

## 📊 Dataset
You can download the dataset used for this project (including annotated videos and images) from the link below:

* **Google Drive**: [Download Football Dataset Here](https://drive.google.com/drive/folders/1uJZlKBTXR3avqk6DmeW53d8LaTxUyIdj?usp=drive_link)

> **Note:** Please place the downloaded files into the `input_data/` folder before running the project.

## 📁 Directory Structure 

Based on the current project organization:

- main.py: The entry point of the application. It handles the video processing pipeline and integrates detection with tracking.

- tracker/: Contains the logic and classes for object tracking across video frames.

- utils/: Helper functions for reading/saving videos and general image processing tasks.

- input_data/: Directory for storing raw input video files.

- data/: This is place that you will put the dataset which dowdloads from my google drive link or any dataset.

- models/: You will save your model file here.

## 🚀 Key Features

- Real-time Detection: High-accuracy detection of football players, referees, and the ball using YOLO.

- Persistent Tracking: Assigns unique IDs to each player to track their movement throughout the match.

- Team Classification: (Optional) Analyzes jersey colors to distinguish between teams.


## 🛠 Installation & Setup

- Clone the Repository:

    - git clone https://github.com/phamvannhattruong/Detecting-and-tracking-football-player.git

- Install Dependencies:

    - pip install ultralytics supervision opencv-python numpy pandas

- Prepare the Model: Place your YOLO weights (e.g., yolov8x.pt) in the root directory or a models/ folder.


## 💻 Usage

- To run the detection and tracking on a video: python main.py


## 📊 Expected Results

- The system generates an output video with:

- Bounding boxes and unique IDs for every person on the pitch.

- Movement trajectories for both the players and the ball.
