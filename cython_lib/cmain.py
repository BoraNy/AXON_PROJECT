import camera
from multiprocessing import Process
import multiprocessing

print(f'CPU Cores: {multiprocessing.cpu_count()}')

if __name__ == '__main__':
    # Process(target=camera.color_extractor(0)).start()
    Process(target=camera.face_detection).start()
    # Process(target=camera.circle_detection).start()
    Process(target=camera.gui_control).start()
