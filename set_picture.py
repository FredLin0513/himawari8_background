#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
#

import win32api, win32con, win32gui
import NICT_Download
import os

dir  =  os.path.dirname(os.path.abspath(__file__))+"\\"   #os.getcwd()+"\""


def clear_dir(path):
	print("正在删除%s下的文件"%(path))
	dir_list = os.listdir(path)
	for my_file in dir_list:
		try:
			os.remove(path+my_file)
		except:
			print("删除%s错误!"%(my_file))
			
			
def set_desktop_windows(imagepath):
	k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
	win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "6")  # 2拉伸适应桌面，0桌面居中
	win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
	win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imagepath, 1 + 2)


if __name__ == '__main__':
	try:
		#clear_dir(dir+"__pycache__/")
		clear_dir(dir+"Download_Picture/")
		clear_dir(dir+"Wallpaper/")
		img_save_path = NICT_Download.dl_main(dir)
		set_desktop_windows(img_save_path)
	except Exception as e:
		print(e)
