the_loai=str(input("nhập thể loại phim muốn xem: "))
thoi_gian=str(input("nhập thời gian xem: "))
if the_loai=="Hành động" or the_loai=="Kinh dị":
    if thoi_gian=="sáng" or thoi_gian=="trưa" or thoi_gian=="chiều" or thoi_gian=="tối":
        print(f"Phim {the_loai} được chiếu vào buổi {thoi_gian}")
    else:
        print("Không có suất chiếu") 
elif the_loai=="Tình cảm" or the_loai=="Hoạt hình":
    if thoi_gian=="tối" :
        print(f"Phim {the_loai} được chiếu vào buổi {thoi_gian}") 
    else:
        print("Không có suất chiếu") 
elif the_loai=="Hài hước" :
    if thoi_gian=="sáng" or thoi_gian=="trưa":
        print(f"Phim {the_loai} được chiếu vào buổi {thoi_gian}")
    else:
        print("Không có suất chiếu")  
else:
    print("Thể loại không hợp lệ")          
                     