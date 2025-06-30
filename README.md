# 🌴SawitCare
SawitCare is a web application to detect healthy/unhealthy oil palm trees from aerial images using AI (YOLOv11 model)

## 🚀 Features

- Upload plantation images easily via drag & drop or file picker.
- Automatic detection of healthy and unhealthy oil palm trees.
- Visualized detection results with bounding boxes and labels.
- Statistics: total trees, number of healthy vs unhealthy trees, and percentage bars.

## 🧰 Technologies Used
- Python & Flask (Backend)
- YOLO (Object Detection)
- OpenCV (Image Processing)
- HTML, CSS, Bootstrap (Frontend)


## 📦 Installation & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/jessicazheng2025/SawitCare.git
   cd SawitCare

  Install the required Python packages:

bash
Salin
Edit
pip install -r requirements.txt
(You need Python 3.7+ installed.)

Add your trained YOLO model file best.pt to the project root.

Run the application:

bash
Salin
Edit
python app.py
Open your browser and go to:

cpp
Salin
Edit
http://127.0.0.1:5000/
📸 Screenshot

2. Install the required Python packages
   ```bash
   pip install -r requirements.txt


3. Add your trained YOLO model
Place your best.pt YOLO model file in the project root.

4. Run the application
   ```bash
   python app.py

5. Open your browser and go to
   ```bash
   http://127.0.0.1:5000/


## 📂 Project Structure
SawitCare/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── uploads/
│   ├── results/
└── best.pt

## 📸 Screenshot
![image](https://github.com/user-attachments/assets/0e58b962-99f3-4990-ba34-f9340a7fa2b7)


## ✏️ License
This project is open source and available under the MIT License.

🙌 Author
Jessica Zheng
