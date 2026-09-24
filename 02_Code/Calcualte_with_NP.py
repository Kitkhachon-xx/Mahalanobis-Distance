import numpy as np

# 1. จำลองกลุ่มข้อมูล (Data Matrix) ขนาด 5 ตัวอย่าง, 3 ฟีเจอร์
data_1 = np.array([[1,0,2]])
data_2 = np.array([[2, -1, -3]])
data_3 = np.array([[3, 1, 0]])
data = np.vstack((data_1, data_2, data_3))
test_data = np.array([[0, 1, 1]])
data_mean = np.mean(data, axis=0)
print("Mean of each feature:", data_mean)

data_center = data - data_mean
print("Centered Data:\n", data_center)

data_center_T = data_center.T
print("Transposed Centered Data:\n", data_center_T)

varaince = np.dot(data_center_T, data_center)
print("Variance-Covariance Matrix:\n", varaince)

s = varaince / (data_center.shape[0] - 1)
print("Variance-Covariance Matrix (Normalized):\n", s)

# s เป็น Singular Matrix (n=3 ตัวอย่าง <= 3 ฟีเจอร์ ทำให้ det(s) = 0)
# จึงใช้ Pseudo-inverse (Moore-Penrose, ผ่าน SVD) แทน np.linalg.inv
s_inv = np.linalg.pinv(s)
print("Pseudo-inverse of Variance-Covariance Matrix:\n", s_inv)

