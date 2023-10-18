import matplotlib.pyplot as plt
import roboticstoolbox as rtb
 
puma = rtb.models.DH.Puma560()
puma.q=puma.qz
puma.plot(puma.qz, block=False)