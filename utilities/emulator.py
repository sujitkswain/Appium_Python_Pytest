# import threading
# import subprocess
# import psutil
# import time
# from utilities.customexceptions import EmulatorNotFoundError
# import subprocess
#
# def check_emulator_device():
#     result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE)
#     if "emulator-5554" in str(result.stdout):
#         return True
#     else:
#         return False
#
# def wait_until(predicate, timeout, period=0.25):
#     mustend = time.time() + timeout
#     while time.time() < mustend:
#         if (globals()[predicate]()):
#             return True
#         time.sleep(period)
#     raise TimeoutError
#
# def validate_adb():
#     if wait_until('check_emulator_device',120)==False:
#         raise(EmulatorNotFoundError)
#     else:
#         print("got it")
#
# def validate():
#     if wait_until('check_emulator_window',60)==False:
#         raise(EmulatorNotFoundError)
#     else:
#         print("got it")
#
# def check_emulator_window():
#     li = []
#     for proc in psutil.process_iter(): li.append(proc.name())
#     print(li)
#     if 'qemu-system-i386.exe' in li:
#         print(li)
#         return True
#     else:
#         return False
#
# class Emulator(threading.Thread):
#     def __init__(self,threadID, name, counter):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         subprocess.call(["emulator", "-avd", "Pixel_2_API_25"], shell=True, close_fds=True)
#
# def launch():
#     thread1 = Emulator(1, "Thread-1", 1)
#     thread1.start()
#     #validate()