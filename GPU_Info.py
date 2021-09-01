from subprocess import Popen, PIPE
from distutils import spawn

nvidia_smi = spawn.find_executable('nvidia-smi')

# Only works and tested on one windows PC, if multipule GPUS are detected then you must first parse the output
def getGPUInfo() -> list:
    try:
        p = Popen([nvidia_smi,
                   "--query-gpu=index,uuid,utilization.gpu,memory.total,memory.used,memory.free,driver_version,name,gpu_serial,display_active,display_mode,temperature.gpu",
                   "--format=csv,noheader,nounits"], stdout=PIPE)
        stdout, stderror = p.communicate()
    except:
        return[]
    output = stdout.decode('UTF-8')
    #removing the return and new line chars
    output = output[:-2]
    # print(output)
    # print("index,uuid,utilization.gpu,memory.total,memory.used,memory.free,driver_version,name,gpu_serial,display_active,display_mode,temperature")
    gpuData = output.split(", ")
    # Setting as a list delimited by ,
    result = []
    # Updating strings which can be numbers to float
    for each in gpuData:
        try:
            result.append(float(each))
        except ValueError:
            result.append(each)
    return(result)

def getGPUIndex( index: int):
    try:
        p = Popen([nvidia_smi,
                   "--query-gpu=index,uuid,utilization.gpu,memory.total,memory.used,memory.free,driver_version,name,gpu_serial,display_active,display_mode,temperature.gpu",
                   "--format=csv,noheader,nounits"], stdout=PIPE)
        stdout, stderror = p.communicate()
    except:
        return None
    output = stdout.decode('UTF-8')
    # removing the return and new line chars
    output = output[:-2]
    # print(output)
    # print("index,uuid,utilization.gpu,memory.total,memory.used,memory.free,driver_version,name,gpu_serial,display_active,display_mode,temperature")
    gpuData = output.split(", ")
    # Setting as a list delimited by ,
    result = gpuData[index]
    # Updating strings which can be numbers to float
    try:
        return(float(result))
    except ValueError:
            return result

def help():
    print("0  - index\n"
          "1  - uuid\n"
          "2  - utilization\n"
          "3  - memory total\n"
          "4  - memory used\n"
          "5  - memory.free\n"
          "6  - driver_version\n"
          "7  - name\n"
          "8  - gpu_serial\n"
          "9  - display_active\n"
          "10 - display_mode\n"
          "11 - temperature")
