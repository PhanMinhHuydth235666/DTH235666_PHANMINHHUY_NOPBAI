t = int(input("Nhập số giây: "))

hour = (t // 3600) % 24
minute = (t % 3600) // 60
second = (t % 3600) % 60

print(hour, ": - bai2c2.py:7", minute, ":", second)
