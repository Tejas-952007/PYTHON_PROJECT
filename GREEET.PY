import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))
if(4<timestamp<12):
    print("morning")
elif(12<timestamp<18):
    print("afternoon")
elif(18<timestamp<23):
    print("evening")
else:
    print("night")