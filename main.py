from DifferentialDriveSimulatedRobot import *
from DR_3DOFDifferentialDrive import *

if __name__ == "__main__":

     # feature map. Position of 2 point features in the world frame.
    M2D = [np.array([[-40, 5]]).T,
           np.array([[-5, 40]]).T,
           np.array([[-5, 25]]).T,
           np.array([[-3, 50]]).T,
           np.array([[-20, 3]]).T,
           np.array([[40,-40]]).T]
    xs0 = np.zeros((6,1))   # initial simulated robot pose
    robot = DifferentialDriveSimulatedRobot(xs0, M2D) # instantiate the simulated robot object

    kSteps = 5000 # number of simulation steps
    xsk_1 = xs0 = np.zeros((6, 1))  # initial simulated robot pose
    # index = [IndexStruct("x", 0, None), IndexStruct("y", 1, None), IndexStruct("yaw", 2, 1)] # index of the state vector used for plotting

    # x0=Pose3D(np.zeros((3,1)))
    # dr_robot=DR_3DOFDifferentialDrive(index,kSteps,robot,x0)
    # dr_robot.LocalizationLoop(x0, np.array([[0.5, 0.03]]).T)
    
    vd = np.array([[0.8 , 0.05 ]]).T #Input velocity [u,v,r]
    ch_1 = np.array([[1, 0 ],
                     [0, -1]])
    for i in range(1,kSteps):
       xsk = robot.fs(xsk_1,vd)
       xsk_1 = xsk
       """ #Uncomment for 8 trayectory
       if -0.2 < xsk[0] < 0.2 and -0.2 < xsk[1] < 0.2 :
           vd = ch_1 @ vd """
    
    # print(current_state)
    # exit(0)
