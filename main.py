from ControlCAN import *
import msvcrt
import configparser


def main():
    cf = configparser.ConfigParser()
    cf.read('config.ini')
    can_devtype = cf.getint("can", "devicetype")
    can_devindex = cf.getint("can", "deviceindex")
    can_canindex = cf.getint("can", "canindex")
    can_baudrate = cf.getint("can", "baudrate")
    can_acccode = int(cf.get("can", "acceptcode"), 16)
    can_accmask = int(cf.get("can", "acceptmask"), 16)
    print('读取配置成功')


    can = ControlCAN(can_devtype, can_devindex, can_canindex, can_baudrate, can_acccode, can_accmask)
    can.opendevice()
    can.initcan()
    can.startcan()
    while 1:
        if kbq(): break
        can.receive()
    del can



def kbq():
    if msvcrt.kbhit():
        ret = ord(msvcrt.getch())
        if ret == 113 or ret == 81:  # q or Q
            return 1


if __name__ == "__main__":
    main()
