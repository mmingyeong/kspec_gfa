from gfa_controller.gfa_controller.controller.legacy.gfa_controller import \
    gfa_controller

controller = gfa_controller(".")
status = controller.status()
print(status)
