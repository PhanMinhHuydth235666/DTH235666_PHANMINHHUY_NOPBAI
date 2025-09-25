# randrange(0, 100) sẽ sinh ra số NGUYÊN trong khoảng [0, 100)
# tức là từ 0 đến 99

# Các giá trị cần kiểm tra: 4.5, 34, -1, 100, 0, 99

# 4.5 ->  không thể, vì randrange chỉ trả số nguyên
# 34  ->  có thể, vì nằm trong khoảng 0–99
# -1  ->  không thể, vì nhỏ hơn 0
# 100 ->  không thể, vì 100 bị loại trừ
# 0   ->  có thể, vì 0 là số đầu tiên trong khoảng
# 99  ->  có thể, vì 99 là số cuối cùng trong khoảng

# Kết luận: các giá trị có thể xuất hiện là 34, 0, 99