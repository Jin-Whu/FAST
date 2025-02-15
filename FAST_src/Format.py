#!/usr/bin/python3
# CDD_Sub        : Format conversion subroutine
# Author         : Chang Chuntao
# Copyright(C)   : The GNSS Center, Wuhan University & Chinese Academy of Surveying and mapping
# Latest Version : 1.21
# Creation Date  : 2022.03.27 - Version 1.00
# Date           : 2022.09.16 - Version 1.21

import os
import platform
import sys
import time
from FAST_Print import PrintGDD

from GNSS_Timestran import gnssTime2datetime, datetime2GnssTime


def isinpath(file):  # 判断相关文件是否存在
    """
    2022-03-27 : 判断文件在本地是否存在 by Chang Chuntao -> Version : 1.00
    2022-09-09 : > 修正广播星历文件判定
                 by Chang Chuntao  -> Version : 1.20
    """
    orifile = str(file).split(".")[0]
    if len(orifile) > 9:
        filelowo = file.lower()[0:4] + file.lower()[16:20] + "." + file.lower()[14:16] + "o"
        filelowd = file.lower()[0:4] + file.lower()[16:20] + "." + file.lower()[14:16] + "d"
        filelowp = file.lower()[0:4] + file.lower()[16:20] + "." + file.lower()[14:16] + "p"
        fileprolow = file.lower()[0:4] + file.lower()[16:20] + ".bia"
        sp3filelow = filelowo
        filelown = filelowo
    elif orifile.split(".")[-1] == "SP3":
        year = file.lower()[11:15]
        doy = file.lower()[15:18]
        specTime = gnssTime2datetime(year + " " + doy, "YearDoy")
        [YearMonthDay, GPSWeekDay, YearDoy, MjdSod] = datetime2GnssTime(specTime)
        sp3filelow = file.lower()[0:3] + str(GPSWeekDay[0]) + str(GPSWeekDay[1]) + ".sp3"
        filelowo = sp3filelow
        filelowd = sp3filelow
        filelowp = sp3filelow
        filelown = sp3filelow
        fileprolow = filelown
    else:
        filelowo = file.lower()[0:11] + "o"
        filelowd = file.lower()[0:11] + "d"
        filelowp = file.lower()[0:11] + "p"
        filelown = file.lower()[0:11] + "n"
        fileprolow = file.lower()[0:12]
        sp3filelow = filelown
    gzdfile = filelowd + ".gz"
    zdfile = filelowd + ".Z"
    gzofile = filelowo + ".gz"
    zofile = filelowo + ".Z"
    filebialowZ = fileprolow + ".Z"
    filebialowgz = fileprolow + ".gz"
    if os.path.exists(file[0:-2]) or os.path.exists(file[0:-3]) \
            or os.path.exists(filelowo) or os.path.exists(filelowd) \
            or os.path.exists(gzdfile) or os.path.exists(zdfile) \
            or os.path.exists(gzofile) or os.path.exists(zofile) \
            or os.path.exists(filelowp) or os.path.exists(filelown) \
            or os.path.exists(filebialowgz) or os.path.exists(filebialowZ) \
            or os.path.exists(sp3filelow) or os.path.exists(file):
        return True
    else:
        return False


"""
2022-03-27 : 判断操作平台，获取bin下格式转换程序      by Chang Chuntao -> Version : 1.00
2022-09-16 : 更新索引                            by Chang Chuntao -> Version : 1.21
"""
if platform.system() == 'Windows':
    if getattr(sys, 'frozen', False):
        dirname = os.path.dirname(sys.executable)
    else:
        dirname = os.path.dirname(os.path.abspath(__file__))
    unzip = os.path.join(dirname, 'bin', 'gzip.exe')
    unzip += " -d "
    crx2rnx = os.path.join(dirname, 'bin', 'crx2rnx.exe')
    crx2rnx += " "
else:
    if getattr(sys, 'frozen', False):
        dirname = os.path.dirname(sys.executable)
    else:
        dirname = os.path.dirname(os.path.abspath(__file__))
    crx2rnx = os.path.join(dirname, 'bin', 'crx2rnx')
    crx2rnx += ' '
    unzip = 'uncompress '


def uncompresss(file):
    """
    2022-03-27 : 解压单个文件 by Chang Chuntao -> Version : 1.00
    """
    if file.split(".")[-1] == "Z" or file.split(".")[-1] == "gz":
        cmd = unzip + file
        os.system(cmd)
    elif file.endswith(".tgz"):
        if platform.system() == 'Windows':
            cmd = "7z x -tgzip -so {} | 7z x -si -ttar".format(file)
            os.system(cmd)
        else:
            cmd = "tar xzvf {}".format(file)
            os.system(cmd)


def crx2rnxs(file):
    """
    2022-03-27 : crx2rnx by Chang Chuntao -> Version : 1.00
    """
    if (file[-3:-1].isdigit() and file[-1] == "d") or file.endswith("crx"):
        cmd = crx2rnx + file
        os.system(cmd)


def crx2d(file):
    """
    2022-03-27 : crx更名为d by Chang Chuntao -> Version : 1.00
    """
    if file.split(".")[-1] == "crx":
        if "15M_01S" in file:
            filelow = file.lower()[0:4] + file.lower()[16:23] + "." + file.lower()[14:16] + "d"
        else:
            filelow = file.lower()[0:4] + file.lower()[16:20] + "." + file.lower()[14:16] + "d"
        os.rename(file, filelow)


def renamebrdm(file):
    """
    2022-03-27 : BRDM长名更名为brdm短名 by Chang Chuntao -> Version : 1.00
    """
    if file.split(".")[-1] == "rnx" and file[0:4] == "BRDM":
        filelow = file.lower()[0:4] + file.lower()[16:20] + "." + file.lower()[14:16] + "p"
        os.rename(file, filelow)
    if file.split(".")[-1] == "rnx" and file[0:4] == "BRDC":
        filelow = "brdm" + file.lower()[16:20] + "." + file.lower()[14:16] + "p"
        os.rename(file, filelow)


def unzip_vlbi(path, ftpsite):
    """
    2022-03-27 : 解压vlbi文件 by Chang Chuntao -> Version : 1.00
    """
    nowdir = os.getcwd()
    if len(path) == 0:
        path = os.getcwd()
    os.chdir(path)
    PrintGDD("开始解压文件!", "normal")
    dirs = os.listdir(path)
    for filename in dirs:
        if ftpsite[83:88] == filename[0:5] and filename.split(".")[-1] == "gz":
            uncompresss(filename)


def unzipfile(path, ftpsite):
    """
    2022.04.12 : 通过下载列表解压相应文件 by Chang Chuntao -> Version : 1.10
    """
    nowdir = os.getcwd()
    if len(path) == 0:
        path = os.getcwd()
    os.chdir(path)
    PrintGDD("开始解压文件!", "normal")
    for ftp in ftpsite:
        zipfilename = str(ftp).split("/")[-1]
        if os.path.exists(zipfilename):
            uncompresss(zipfilename)
    dirs = os.listdir(path)
    for filename in dirs:
        if filename[-3:-1].isdigit() or filename.split(".")[-1] == "crx":
            if filename.split(".")[-1] == "crx" or filename[-1] == "d":
                PrintGDD("目录内含有crx文件，正在进行格式转换！", "normal")
                break
    for filename in dirs:
        if filename.split(".")[-1] == "crx":
            crx2d(filename)

    dirs = os.listdir(path)
    for filename in dirs:
        if filename[-1] == "d" and filename[-3:-1].isdigit():
            crx2rnxs(filename)
            time.sleep(0.1)
            os.remove(filename)

    dirs = os.listdir(path)
    for filename in dirs:
        if filename.split(".")[-1] == "rnx" and filename[0:4] == "BRDM":
            renamebrdm(filename)
        if filename.split(".")[-1] == "rnx" and filename[0:4] == "BRDC":
            renamebrdm(filename)
    os.chdir(nowdir)
