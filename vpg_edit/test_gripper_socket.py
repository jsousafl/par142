from robot import Robot
import numpy as np

tcp_host_ip = '192.168.1.5' # IP and port to robot arm as TCP client (UR3)
tcp_port = 30002
rtc_host_ip = '100.127.7.223' # IP and port to robot arm as real-time client (UR3)
rtc_port = 30003
workspace_limits = np.asarray([[-0.112, 0.0], [0.35, 0.49], [0.05, 0.15]]) # Cols: min max, Rows: x y z (define workspace limits in robot coordinates)
checkerboard_offset_from_tool = [0,-0.13,0.04]
tool_orientation = [0.781997722248118, -1.72747311658691, -1.745019122048043]
tool_position = [workspace_limits[0][0],0.3168935073624113, 0.044575957549417684] #[0.05,0.35,0.05]
calib_grid_step = 0.05

robot = Robot(False, None, None, workspace_limits,
              tcp_host_ip, tcp_port, rtc_host_ip, rtc_port,
              False, None, None)

robot.open_gripper()
robot.close_gripper()
if robot.check_grasp():
    print('Object detected')
else:
    print('Object not detected')