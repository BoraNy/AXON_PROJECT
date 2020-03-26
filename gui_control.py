# !/usr/bin/python3
import tkinter as tk
from tkinter import *
import cv2
import multiprocessing
from multiprocessing import cpu_count, Process

print(f'CPU Core: {cpu_count()}')

shared_memory_variable = []


def camera_control(passing_address):
	camera_id = 0
	cap = cv2.VideoCapture(camera_id)
	while True:
		_, img = cap.read()
		cv2.imshow('output', img)
		if cv2.waitKey(1) == 32:
			print(shared_memory_variable[:])
		if cv2.waitKey(1) == 27:
			break
	cap.release()
	cv2.destroyAllWindows()


def gui_control(passing_address):
	def get_all_value():
		shared_memory_variable[0] = (x_coordinate.get())
		shared_memory_variable[1] = (y_coordinate.get())
		shared_memory_variable[2] = (select_camera.get())
		label.config(text=f'x = {x_coordinate.get()}, y = {y_coordinate.get()}, camera = {select_camera.get()}')

	root = Tk()
	root.title('Control Panel')
	root.geometry('320x240')
	# root.resizable(width=False, height=False)

	select_camera = IntVar()

	x_label = Label(root, text='X-Axis')
	x_label.grid(row=0, column=0)
	x_coordinate = tk.Scale(root, length=150, from_=0, to=180, resolution=1, orient=HORIZONTAL)
	x_coordinate.grid(row=0, column=1)

	y_label = Label(root, text='Y-Axis')
	y_label.grid(row=1, column=0)
	y_coordinate = tk.Scale(root, length=150, from_=0, to=180, resolution=1, orient=HORIZONTAL)
	y_coordinate.grid(row=1, column=1)

	internal_camera = tk.Radiobutton(root, text='Built-in Camera', variable=select_camera, value=0)
	internal_camera.grid(row=2, column=0)
	external_camera = tk.Radiobutton(root, text='External Camera', variable=select_camera, value=1)
	external_camera.grid(row=2, column=1)

	get_val = Button(root, text='Get', command=get_all_value)
	get_val.place(x=265, y=210)

	label = Label(root, text='x = 0, y = 0, camera = 0')
	label.place(x=5, y=210)

	root.mainloop()


if __name__ == '__main__':
	shared_memory_variable = multiprocessing.Array('i', 3)  # 'i' as Integer, 3 is objects in array
	Process(target=camera_control, args=(shared_memory_variable,)).start()
	Process(target=gui_control, args=(shared_memory_variable,)).start()
