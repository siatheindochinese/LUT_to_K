import numpy as np

def get_LF():
	with open('LUT/VLC LF_lut.bin', mode='rb') as depth_file:
		lut = np.frombuffer(depth_file.read(), dtype="f")
		lut = lut.reshape(480,640,3)
	return lut

def get_RF():
	with open('LUT/VLC RF_lut.bin', mode='rb') as depth_file:
		lut = np.frombuffer(depth_file.read(), dtype="f")
		lut = lut.reshape(480,640,3)
	return lut
    
def get_AHaT():
	with open('LUT/Depth AHaT_lut.bin', mode='rb') as depth_file:
		lut = np.frombuffer(depth_file.read(), dtype="f")
		lut = lut.reshape(512,512,3)
	return lut
    
def GT():
	return None
