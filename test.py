
import controller

gfa_init = controller.gfa_init()
gfa_init.gfa_init_connect_camera()
img_list = gfa_init.gfa_init_exposure(1000)
print(len(img_list))
