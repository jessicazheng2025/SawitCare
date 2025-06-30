from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import cv2
from datetime import datetime

app = Flask(__name__)

# Folder simpan file
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Load model
model = YOLO("best.pt")

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None

    if request.method == 'POST':
        nama_kebun = request.form['nama_kebun']
        blok_area = request.form['blok_area']
        tanggal_foto = request.form['tanggal_foto']
        file = request.files['gambar_kebun']

        if not file:
            return "Tidak ada file!"

        # Simpan gambar upload
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
        upload_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(upload_path)

        # YOLO infer
        results = model.predict(upload_path, conf=0.5, iou=0.5)


        # Baca gambar pakai OpenCV
        img = cv2.imread(upload_path)

        total_pohon = len(results[0].boxes)
        sehat = 0

        for box in results[0].boxes:
            xyxy = box.xyxy[0].cpu().numpy().astype(int)
            cls = int(box.cls)
            conf = float(box.conf)
            if cls == 0:
                color = (0, 255, 0)  # Hijau
                label = f"Sehat {conf:.2f}"
                sehat += 1  # ✅ INI HARUS ADA!
            else:
                color = (0, 0, 255)  # Merah
                label = f"Tidak Sehat {conf:.2f}"


            # Gambar kotak bounding box
            cv2.rectangle(img, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), color, 2)

            # Hitung ukuran teks
            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            # Kotak background di belakang teks
            cv2.rectangle(img, 
                        (xyxy[0], xyxy[1] - 20),
                        (xyxy[0] + w, xyxy[1]),
                        color, 
                        -1)  # -1 = fill

            # Tulis teks di atas kotak background
            cv2.putText(img, label, (xyxy[0], xyxy[1] - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)


        tidak_sehat = total_pohon - sehat

        result_filename = f"result_{filename}"
        result_path = os.path.join(RESULT_FOLDER, result_filename)
        cv2.imwrite(result_path, img)

        hasil = {
            'nama_kebun': nama_kebun,
            'blok_area': blok_area,
            'tanggal_foto': tanggal_foto,
            'total_pohon': total_pohon,
            'sehat': sehat,
            'tidak_sehat': tidak_sehat,
            'gambar_url': result_filename
        }

    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)
