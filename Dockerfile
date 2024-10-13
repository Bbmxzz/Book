# ใช้ base image ที่เหมาะสม
FROM python:3.9-slim

# ตั้ง working directory
WORKDIR /app

# คัดลอก requirements.txt
COPY requirements.txt .

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดแอปพลิเคชัน
COPY . .

# กำหนดพอร์ตที่แอปพลิเคชันจะฟัง
EXPOSE 5000

# สั่งให้รันแอปพลิเคชัน
CMD ["python", "app.py"]
