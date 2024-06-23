#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  

from PIL import Image
import requests
import re
import datetime

			
def download_img(url, img_save_path):
	img = requests.get(url)
	with open(img_save_path, "wb") as fwi:
		fwi.write(img.content)
		print(img_save_path + "图片下载成功")


def fill_img(img_0,img_1,img_2,img_3,img_4,img_5,img_6,img_7,img_8,img_9,img_10,img_11,img_12,img_13,img_14,img_15,dir,img_save_path):
	#图片位置示意
	#0 4 8  12   
	#1 5 9  13
	#2 6 10 14
	#3 7 11 15
	width, height = 2560, 1600      # 电脑屏幕大小
	new_img = Image.new(img_1.mode, (width, height), color='black')
	new_img = Image.open(dir+"images/background.png")
	new_img = new_img.convert("RGBA")
	img_0=img_0.crop((0,0,550,550))
	img_1=img_1.crop((0,0,550,550))
	img_2=img_2.crop((0,0,550,550))
	img_3=img_3.crop((0,0,550,550))
	img_4=img_4.crop((0,0,550,550))
	img_5=img_5.crop((0,0,550,550))
	img_6=img_6.crop((0,0,550,550))
	img_7=img_7.crop((0,0,550,550))
	img_8=img_8.crop((0,0,550,550))
	img_9=img_9.crop((0,0,550,550))
	img_10=img_10.crop((0,0,550,550))
	img_11=img_11.crop((0,0,550,550))
	img_12=img_12.crop((0,0,550,550))
	img_13=img_13.crop((0,0,550,550))
	img_14=img_14.crop((0,0,550,550))
	img_15=img_15.crop((0,0,550,550))
	r,g,b,a = img_0.split()
	new_img.paste(img_0, (331,0),mask = a)#图片左上角的xy坐标
	r,g,b,a = img_1.split()
	new_img.paste(img_1, (331,550),mask = a)
	r,g,b,a = img_2.split()
	new_img.paste(img_2, (331,1100),mask = a)
	r,g,b,a = img_3.split()
	new_img.paste(img_3, (331,1650),mask = a)
	r,g,b,a = img_4.split()
	new_img.paste(img_4, (881,0),mask = a)
	r,g,b,a = img_5.split()
	new_img.paste(img_5, (881,550),mask = a)
	r,g,b,a = img_6.split()
	new_img.paste(img_6, (881,1100),mask = a)
	r,g,b,a = img_7.split()
	new_img.paste(img_7, (881,1650),mask = a)
	r,g,b,a = img_8.split()
	new_img.paste(img_8, (1431,0),mask = a)
	r,g,b,a = img_9.split()
	new_img.paste(img_9, (1431,550),mask = a)
	r,g,b,a = img_10.split()
	new_img.paste(img_10, (1431,1100),mask = a)
	r,g,b,a = img_11.split()
	new_img.paste(img_11, (1431,1650),mask = a)
	r,g,b,a = img_12.split()
	new_img.paste(img_12, (1981,0),mask = a)
	r,g,b,a = img_13.split()
	new_img.paste(img_13, (1981,550),mask = a)
	r,g,b,a = img_14.split()
	new_img.paste(img_14, (1981,1100),mask = a)
	r,g,b,a = img_15.split()
	new_img.paste(img_15, (1981,1650),mask = a)
	new_img.save(img_save_path)
	print(img_save_path + "图片合成成功")


def dl_main(dir):
	print("开始下载图片")
	# 获取当前系统时间
	utc_today = datetime.datetime.now(datetime.UTC) - datetime.timedelta(minutes=30)  # 获取GMT时间并减去20分钟
	delat_utc_today = utc_today.strftime("%Y/%m/%d/%H%M")  # 时间格式化
	# 分钟向下取整
	delat_utc_today_list = list(delat_utc_today)
	delat_utc_today_list[-1] = "0"
	delat_utc_today = "".join(delat_utc_today_list)
	
	# 整合为链接 格式为：http://himawari8-dl.nict.go.jp/himawari8/img/D531106/2d/550/2020/06/24/023000_0_0.png
	#                   https://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/2020/09/28/062000_0_0.png
	
	i=0
	for row in range(4):
		for col in range(4):
			img_url = "https://himawari8-dl.nict.go.jp/himawari8/img/D531106/4d/550/%s00_%d_%d.png"%(delat_utc_today,row,col)
			print(img_url)
			name = delat_utc_today.replace("/", "_") + "00_%d_%d.png"%(row,col)  # 获取图片名字
			# 图片保存路径
			img_save_path = dir+"Download_Picture/" + name
			# 下载图片
			download_img(img_url, img_save_path)
			# 合成图片
						
			img = Image.open(img_save_path)
			#print(img.mode)
			img = img.convert("RGBA")
			datas = img.getdata()
			newData = list()
			for item in datas:
				if item[0]<=10 and item[1]<=10  and item[2]<=10 :
					newData.append(( item[0], item[1], item[2], int(-17.0*(item[0]+item[1]+item[2])*(item[0]+item[1]+item[2])/60.0+17.0*(item[0]+item[1]+item[2]))))
				else:
					newData.append(item)
			img.putdata(newData)

			#print(img.mode)
			if i==0:
				img_0 = img
			elif i==1:
				img_1 = img
			elif i==2:
				img_2 = img
			elif i==3:
				img_3 = img
			elif i==4:
				img_4 = img
			elif i==5:
				img_5 = img
			elif i==6:
				img_6 = img
			elif i==7:
				img_7 = img
			elif i==8:
				img_8 = img
			elif i==9:
				img_9 = img
			elif i==10:
				img_10 = img
			elif i==11:
				img_11 = img
			elif i==12:
				img_12 = img
			elif i==13:
				img_13 = img
			elif i==14:
				img_14 = img
			elif i==15:
				img_15 = img
			i=i+1
	

	new_img_save_path = dir+"Wallpaper/" + delat_utc_today.replace("/", "_")+".png"
	#print(new_img_save_path)
	fill_img(img_0,img_1,img_2,img_3,img_4,img_5,img_6,img_7,img_8,img_9,img_10,img_11,img_12,img_13,img_14,img_15,dir,new_img_save_path)
	return new_img_save_path


if __name__ == '__main__':
	dl_main()
