# Mahalanobis Distance

คลังสรุปเนื้อหาและตัวอย่างการคำนวณ **Mahalanobis Distance** ซึ่งเป็นวิธีการวัดระยะห่างของข้อมูลทางสถิติที่คำนึงถึงความแปรปรวนและความสัมพันธ์ (Covariance) ของแต่ละตัวแปร เหมาะสำหรับข้อมูลที่มีการกระจายตัวแบบวงรี (Elliptical) มากกว่าการวัดระยะทางเส้นตรงแบบปกติ (Euclidean Distance)

---

## โครงสร้าง Repository

```text
Mahalanobis-Distance/
├── 01_Lecture/
│   └── Detail.md      # สรุปทฤษฎีและขั้นตอนการคำนวณ Mahalanobis Distance แบบละเอียด
├── 02_Code/            # โค้ดตัวอย่าง (Python) — จะทยอยเพิ่มในภายหลัง
└── README.md
```

## เนื้อหาใน `01_Lecture/Detail.md`

- สูตรทางคณิตศาสตร์ของ Mahalanobis Distance
- ขั้นตอนการคำนวณ Covariance Matrix ทีละ Step
- เหตุผลที่ต้องใช้ Covariance Matrix ในการคำนวณ
- ตัวอย่างการคำนวณ (เปรียบเทียบ Identity Matrix vs Custom Covariance)
- กรณีศึกษา: ทำนายค่า Target ด้วย Mahalanobis Distance ร่วมกับ K-Nearest Neighbors (KNN) และ Pseudo-inverse (SVD)
- การประยุกต์ใช้งานในการเตรียมข้อมูล (Outlier Detection, Data Whitening, Data Imputation, Handling Imbalanced Data)

## อ้างอิง

- บทสนทนา Gemini ต้นฉบับที่ใช้อ้างอิงขั้นตอนการคำนวณ: `https://gemini.google.com/app/60e2824d84ecc442`
