
from  controller.gfa_controller import gfa_controller

controller = gfa_controller(".")
status = controller.status()
print(status)
