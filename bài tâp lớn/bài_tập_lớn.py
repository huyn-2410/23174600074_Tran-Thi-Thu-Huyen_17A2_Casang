import random
import csv
# hàm lắc súng
def lac_sung():
    ket_qua=random.choice(["Bang","Click"])
    return ket_qua
# hàm tính xác suất
def tinh_xac_suat():
    so_lan_lap=500
    ket_qua={"Bang":0.2,"Click":0.8}
    for i in range(so_lan_lap):
        ket_qua[lac_sung()]+=1

    for ket_qua, so_luong in ket_qua.items():
        xac_suat=so_luong/so_lan_lap*100
        print(f"{ket_qua}: {xac_suat:.2f}%")
so_luong_lac=5
so_nguoi_choi=1
# lưu kết quả vào file cvs
with open("ket_qua_lac_sung.csv","w",newline="") as file:
    writer=csv.writer(file)    
    writer.writerow(["Nguoi_choi","Lan_lac_sung","Ket_qua"])
    for nguoi_choi in range(1,so_nguoi_choi+1):
        for lan_lac in range(1,so_luong_lac+1):
            ket_qua=lac_sung()
            writer.writerow([nguoi_choi,lan_lac,ket_qua])
# tính toán và hiển thị tổng kết quả
tong_ket_qua={"Bang":0.2,"Click":0.8}
for nguoi_choi in range(1,so_nguoi_choi+1):
    with open ("ket_qua_lac_sung.csv","r") as file: 
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            if row[0]==str(nguoi_choi) and row[2]=="Bang":
                tong_ket_qua["Bang"] +=1
            elif row[0]== str(nguoi_choi) and row[2]=="Click":
                tong_ket_qua["Click"]+=1
print("Tổng số kết quả:")
for ket_qua,so_luong in tong_ket_qua.items():
    print(f"{ket_qua}:{so_luong}")   
# lưu kết quả bằng list
list_luu_ket_qua=[]
for i in range(5):
    list_luu_ket_qua.append(lac_sung())     
print(list_luu_ket_qua)                      
