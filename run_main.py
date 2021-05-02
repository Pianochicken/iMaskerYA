import os
import threading
import time

# 子執行緒的工作函數
def quasar():
	os.system('quasar dev -m electron')

# # 建立第一個子執行緒
first = threading.Thread(target = quasar)
first.start() # 執行該子執行緒

# 子執行緒的工作函數
time.sleep(10)
def yolov4():
	os.chdir('darknet/build/darknet/x64')
	# 執行Yolov4模型
	os.system('darknet.exe detector demo obj_imaskerya.data yolov4-tiny_imaskerya.cfg yolov4-tiny_imaskerya.weights -c 0 -json_port 8070 -mjpeg_port 8090 -thresh 0.6 -dont_show')


# # 建立第一個子執行緒
second = threading.Thread(target = yolov4)
second.start() # 執行該子執行緒

# 等待子執行緒結束
first.join()
second.join()

print("done!")
os.system('pause')