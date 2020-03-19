


output = '''Radio power mode = online
LTE Rx Channel Number =  2050
LTE Tx Channel Number =  20050
LTE Band =  4
LTE Bandwidth = 20 MHz
Current RSSI = -80 dBm
Current RSRP = -110 dBm
Current RSRQ = -10 dB
Current SNR = 4.4  dB
Physical Cell Id = 0x55
Number of nearby cells = 4
Idx      PCI (Physical Cell Id)
--------------------------------
1              85
2              285
3              87
4              86
Radio Access Technology(RAT) Preference = AUTO
Radio Access Technology(RAT) Selected = LTE
'''

# Carve it up
for line in output.splitlines():
    print("Line is =", line)
    if "RSSI" in line:
        rssi = line.split('=')[1].split()[0]
        print(rssi)
    if "RSRP" in line:
        rsrp = line.split('=')[1].split()[0]
        print(rsrp)
    if "RSRQ" in line:
        rsrq = line.split('=')[1].split()[0]
        print(rsrq)
    if "SNR" in line:
        snr = line.split('=')[1].split()[0]
        print(snr)