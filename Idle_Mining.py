import GPU_Info as GI
import numpy as np
import time
import subprocess as sp
import os

# GI.help()
avg = np.zeros((50,), dtype=float)
avg = np.append(avg, 1000000.0)


while(1):
    avg = np.delete(avg,0)
    new_Value = GI.getGPUIndex(2)
    avg = np.append(avg,new_Value)
    print(np.mean(avg))
    time.sleep(30)

    if(np.mean(avg) < 60.0):

        os.chdir("C:\\Program Files (x86)\\MSI Afterburner")
        sp.run("C:\\Program Files (x86)\\MSI Afterburner\\MSIAfterburner.exe" + " -Profile2")
        os.chdir('C:\\Users\\Justin\\Downloads\\Mining\\NBMiner_39.1_Win\\NBMiner_Win')
        sp.Popen('C:\\Users\\Justin\\Downloads\\Mining\\NBMiner_39.1_Win\\NBMiner_Win\\start_eth.bat')
        while(1):
            pass


