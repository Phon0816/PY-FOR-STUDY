# Nhập đâu vào dài rộng cao
Dai = float(input('Nhập Chiều Dài : '))
Rong = float(input('Nhập Chiều Rộng : '))
Cao = float(input('Nhập chiều Cao : '))

# Nhập số lượng chữ số sau dấu phẩy muốn hiển thị
SoLe = int(input('Nhập số lượng số lẻ cần hiển thị: '))

# Diện tích đáy hình hộp chữ nhật là
DienTichDay = Dai * Rong # diện tích đáy lấy dài nhân rộng

#Thể tích hình hộp chữ nhật
TheTichHCN = Dai * Cao * Rong   #thể tích dài nhân cao nhân rộng

#in dòng lệnh ra terminal
print(f'Dien tich day = {DienTichDay:.{SoLe}f} cm\u00b2')
print(f'The tich hinh khoi = {TheTichHCN:.{SoLe}f} cm\u00b3')