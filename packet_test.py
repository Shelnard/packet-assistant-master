#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/12/6 16:44
#@Author  :Longyang Yao 
#@FileName: packet_test.py
#@Software: PyCharm

import pcapy
import binascii
import time

mac_srcAddress = [0x48,0x4D,0x7E,0xC9,0xE4,0x1A]
mac_desAddress_tl = [0xFC,0x0F,0x4B,0xAE,0x70,0x36]
mac_desAddress_inc = [0xC8,0xDF,0x84,0x7E,0x99,0x45]
protol_type = [0x08,0x06]
value = [0xEF]*50
data = bytes(mac_desAddress_tl+mac_srcAddress+protol_type+value)
dev = pcapy.open_live(str(pcapy.findalldevs()[2]), 100, 1, 1000)
#开始抓包
print("开始抓包...")
start_time = time.time()
pkt_cnt = 0
while time.time() - start_time < 10:
    (header, packet) = dev.next()
    if packet[0:6] == bytes(mac_srcAddress):
        print(f"{pkt_cnt:d}: Received {len(packet):d} bytes, packet type = 0x{bytes.hex(packet[12:14])}, "
              f"from source address  = 0x{bytes.hex(packet[0:6])}")
        pkt_cnt += 1
    # time.sleep(0.1)
print("抓包结束...")
print("开始发包...")
start_time = time.time()
#while time.time() - start_time < 10:
while True:
    print(data)
    dev.sendpacket(data)
    time.sleep(1)

