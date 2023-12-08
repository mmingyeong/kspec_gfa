from gfa_init import gfa_init

gfa_init = gfa_init()
gfa_init.gfa_init_connect_camera()
img_list = gfa_init.gfa_init_exposure(1000)
print(img_list)