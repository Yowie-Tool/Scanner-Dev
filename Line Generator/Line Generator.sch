EESchema Schematic File Version 4
LIBS:Line Generator-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector_Generic:Conn_01x04 J1
U 1 1 5E454797
P 2175 1800
F 0 "J1" V 2139 1512 50  0000 R CNN
F 1 "Conn_01x04" V 2048 1512 50  0000 R CNN
F 2 "Connector_JST:JST_PH_B4B-PH-SM4-TB_1x04-1MP_P2.00mm_Vertical" H 2175 1800 50  0001 C CNN
F 3 "~" H 2175 1800 50  0001 C CNN
	1    2175 1800
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Schottky D1
U 1 1 5E540F29
P 4800 1925
F 0 "D1" V 4825 2000 50  0000 L CNN
F 1 "D_Schottky 7V" V 4900 1975 50  0000 L CNN
F 2 "Diode_SMD:D_SOD-323_HandSoldering" H 4800 1925 50  0001 C CNN
F 3 "https://docs.rs-online.com/2159/0900766b812e22b6.pdf" H 4800 1925 50  0001 C CNN
	1    4800 1925
	0    1    1    0   
$EndComp
$Comp
L power:+12V #PWR0101
U 1 1 5E54231E
P 2075 2150
F 0 "#PWR0101" H 2075 2000 50  0001 C CNN
F 1 "+12V" H 2090 2323 50  0000 C CNN
F 2 "" H 2075 2150 50  0001 C CNN
F 3 "" H 2075 2150 50  0001 C CNN
	1    2075 2150
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 5E542B5B
P 2175 2425
F 0 "#PWR0102" H 2175 2175 50  0001 C CNN
F 1 "GND" H 2180 2252 50  0000 C CNN
F 2 "" H 2175 2425 50  0001 C CNN
F 3 "" H 2175 2425 50  0001 C CNN
	1    2175 2425
	1    0    0    -1  
$EndComp
Text GLabel 2275 2150 3    50   Output ~ 0
Laser1
Text GLabel 2375 2150 3    50   Output ~ 0
Laser2
Wire Wire Line
	2075 2150 2075 2000
Wire Wire Line
	2175 2000 2175 2425
Wire Wire Line
	2275 2150 2275 2000
Wire Wire Line
	2375 2000 2375 2150
$Comp
L Device:R R3
U 1 1 5E54A307
P 4450 2275
F 0 "R3" H 4520 2321 50  0000 L CNN
F 1 "4K7" H 4520 2230 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 4380 2275 50  0001 C CNN
F 3 "~" H 4450 2275 50  0001 C CNN
	1    4450 2275
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 5E54B074
P 4450 1925
F 0 "R2" H 4275 1975 50  0000 L CNN
F 1 "100K" H 4200 1875 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 4380 1925 50  0001 C CNN
F 3 "~" H 4450 1925 50  0001 C CNN
	1    4450 1925
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5E54EB98
P 3900 2675
F 0 "R1" V 3693 2675 50  0000 C CNN
F 1 "10K" V 3784 2675 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3830 2675 50  0001 C CNN
F 3 "~" H 3900 2675 50  0001 C CNN
	1    3900 2675
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 5E54F1FD
P 4975 2525
F 0 "R4" H 4905 2479 50  0000 R CNN
F 1 "68R" H 4905 2570 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 4905 2525 50  0001 C CNN
F 3 "~" H 4975 2525 50  0001 C CNN
	1    4975 2525
	-1   0    0    1   
$EndComp
Wire Wire Line
	5400 2075 4800 2075
Wire Wire Line
	4450 2075 4450 2125
Connection ~ 4450 2075
Connection ~ 4800 2075
Wire Wire Line
	4800 2075 4450 2075
Wire Wire Line
	4450 2425 4450 2475
Wire Wire Line
	4150 2675 4050 2675
Wire Wire Line
	5200 2375 4975 2375
Wire Wire Line
	5600 2375 5600 2525
Wire Wire Line
	5800 2375 5800 2525
$Comp
L Device:R R5
U 1 1 5E55552F
P 5800 1700
F 0 "R5" H 5730 1654 50  0000 R CNN
F 1 "33R" H 5730 1745 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5730 1700 50  0001 C CNN
F 3 "~" H 5800 1700 50  0001 C CNN
	1    5800 1700
	-1   0    0    1   
$EndComp
Wire Wire Line
	5800 1975 5800 1850
Text GLabel 3575 2675 0    50   Output ~ 0
Laser2
Wire Wire Line
	3575 2675 3750 2675
Wire Wire Line
	4450 1775 4450 1625
Wire Wire Line
	4450 1625 4625 1625
Wire Wire Line
	4800 1625 4800 1775
$Comp
L power:+12V #PWR0103
U 1 1 5E556226
P 4625 1475
F 0 "#PWR0103" H 4625 1325 50  0001 C CNN
F 1 "+12V" H 4640 1648 50  0000 C CNN
F 2 "" H 4625 1475 50  0001 C CNN
F 3 "" H 4625 1475 50  0001 C CNN
	1    4625 1475
	1    0    0    -1  
$EndComp
Wire Wire Line
	4625 1475 4625 1625
Connection ~ 4625 1625
Wire Wire Line
	4625 1625 4800 1625
$Comp
L power:+12V #PWR0104
U 1 1 5E556A2D
P 4975 2875
F 0 "#PWR0104" H 4975 2725 50  0001 C CNN
F 1 "+12V" H 4990 3048 50  0000 C CNN
F 2 "" H 4975 2875 50  0001 C CNN
F 3 "" H 4975 2875 50  0001 C CNN
	1    4975 2875
	-1   0    0    1   
$EndComp
Wire Wire Line
	4975 2675 4975 2875
$Comp
L power:GND #PWR0105
U 1 1 5E5573F2
P 4450 2975
F 0 "#PWR0105" H 4450 2725 50  0001 C CNN
F 1 "GND" H 4455 2802 50  0000 C CNN
F 2 "" H 4450 2975 50  0001 C CNN
F 3 "" H 4450 2975 50  0001 C CNN
	1    4450 2975
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0106
U 1 1 5E55789E
P 5700 3200
F 0 "#PWR0106" H 5700 2950 50  0001 C CNN
F 1 "GND" H 5705 3027 50  0000 C CNN
F 2 "" H 5700 3200 50  0001 C CNN
F 3 "" H 5700 3200 50  0001 C CNN
	1    5700 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 3200 5700 3125
Wire Wire Line
	4450 2975 4450 2875
$Comp
L Device:LED_Dual_ACA D2
U 1 1 5E55C00C
P 5700 2825
F 0 "D2" V 5746 2615 50  0000 R CNN
F 1 "LED_Dual_ACA" V 5655 2615 50  0000 R CNN
F 2 "Connector_PinSocket_1.27mm:PinSocket_1x03_P1.27mm_Vertical" H 5700 2825 50  0001 C CNN
F 3 "~" H 5700 2825 50  0001 C CNN
	1    5700 2825
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Schottky D3
U 1 1 5E55CFF5
P 6550 2025
F 0 "D3" V 6504 2104 50  0000 L CNN
F 1 "D_Schottky 7V" V 6595 2104 50  0000 L CNN
F 2 "Diode_SMD:D_SOD-323_HandSoldering" H 6550 2025 50  0001 C CNN
F 3 "https://docs.rs-online.com/2159/0900766b812e22b6.pdf" H 6550 2025 50  0001 C CNN
	1    6550 2025
	0    1    1    0   
$EndComp
$Comp
L Device:R R6
U 1 1 5E55D5BE
P 7475 2025
F 0 "R6" H 7300 2075 50  0000 L CNN
F 1 "100K" H 7225 1975 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 7405 2025 50  0001 C CNN
F 3 "~" H 7475 2025 50  0001 C CNN
	1    7475 2025
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR0107
U 1 1 5E560299
P 6900 1300
F 0 "#PWR0107" H 6900 1150 50  0001 C CNN
F 1 "+12V" V 6915 1428 50  0000 L CNN
F 2 "" H 6900 1300 50  0001 C CNN
F 3 "" H 6900 1300 50  0001 C CNN
	1    6900 1300
	0    1    1    0   
$EndComp
$Comp
L Device:R R7
U 1 1 5E560C71
P 6550 2375
F 0 "R7" H 6620 2421 50  0000 L CNN
F 1 "4K7" H 6620 2330 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 6480 2375 50  0001 C CNN
F 3 "~" H 6550 2375 50  0001 C CNN
	1    6550 2375
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:BS170F Q1
U 1 1 5E5613DE
P 4350 2675
F 0 "Q1" H 4556 2721 50  0000 L CNN
F 1 "BS170F" H 4556 2630 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 4550 2600 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/BS170F.pdf" H 4350 2675 50  0001 L CNN
	1    4350 2675
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:BS170F Q4
U 1 1 5E563A34
P 7025 2625
F 0 "Q4" V 7368 2625 50  0000 C CNN
F 1 "BS170F" V 7277 2625 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 7225 2550 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/BS170F.pdf" H 7025 2625 50  0001 L CNN
	1    7025 2625
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6825 2525 6550 2525
Wire Wire Line
	6550 2225 6550 2175
Connection ~ 6550 2175
$Comp
L Device:R R8
U 1 1 5E56AF84
P 7025 3050
F 0 "R8" H 6955 3004 50  0000 R CNN
F 1 "10K" H 6955 3095 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 6955 3050 50  0001 C CNN
F 3 "~" H 7025 3050 50  0001 C CNN
	1    7025 3050
	-1   0    0    1   
$EndComp
Text GLabel 7025 3275 3    50   Output ~ 0
Laser1
Wire Wire Line
	7025 3200 7025 3275
Wire Wire Line
	7025 2900 7025 2825
$Comp
L power:GND #PWR0108
U 1 1 5E56C3C6
P 7300 2525
F 0 "#PWR0108" H 7300 2275 50  0001 C CNN
F 1 "GND" V 7305 2397 50  0000 R CNN
F 2 "" H 7300 2525 50  0001 C CNN
F 3 "" H 7300 2525 50  0001 C CNN
	1    7300 2525
	0    -1   -1   0   
$EndComp
Wire Wire Line
	7225 2525 7300 2525
$Comp
L Device:Q_PNP_Darlington_BEC Q2
U 1 1 5E552935
P 5400 2275
F 0 "Q2" V 5350 2050 50  0000 C CNN
F 1 "BCV46" V 5425 2025 50  0000 C CNN
F 2 "digikey-footprints:SOT-23-3" H 5600 2375 50  0001 C CNN
F 3 "~" H 5400 2275 50  0001 C CNN
	1    5400 2275
	0    1    1    0   
$EndComp
$Comp
L Device:Q_PNP_Darlington_BEC Q3
U 1 1 5E553329
P 5900 2175
F 0 "Q3" H 5800 2350 50  0000 L CNN
F 1 "BCV46" H 5700 2425 50  0000 L CNN
F 2 "digikey-footprints:SOT-23-3" H 6100 2275 50  0001 C CNN
F 3 "~" H 5900 2175 50  0001 C CNN
	1    5900 2175
	-1   0    0    1   
$EndComp
$Comp
L Jumper:SolderJumper_2_Open JP1
U 1 1 5E556D51
P 4950 1525
F 0 "JP1" V 4904 1593 50  0000 L CNN
F 1 "SolderJumper_2_Open" V 4995 1593 50  0000 L CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm" H 4950 1525 50  0001 C CNN
F 3 "~" H 4950 1525 50  0001 C CNN
	1    4950 1525
	1    0    0    -1  
$EndComp
$Comp
L Device:R_POT RV1
U 1 1 5E5819FB
P 5125 1775
F 0 "RV1" H 5056 1821 50  0000 R CNN
F 1 "22K" H 5056 1730 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3006P_Horizontal" H 5125 1775 50  0001 C CNN
F 3 "~" H 5125 1775 50  0001 C CNN
	1    5125 1775
	1    0    0    -1  
$EndComp
Wire Wire Line
	5275 1775 5400 1775
Wire Wire Line
	5400 1775 5400 2075
Connection ~ 5400 2075
$Comp
L Device:C C1
U 1 1 5E5844FF
P 5275 1525
F 0 "C1" V 5150 1650 50  0000 C CNN
F 1 "0.1uF" V 5225 1700 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 5313 1375 50  0001 C CNN
F 3 "~" H 5275 1525 50  0001 C CNN
	1    5275 1525
	0    1    1    0   
$EndComp
Wire Wire Line
	5425 1525 5425 1775
Wire Wire Line
	5425 1775 5400 1775
Connection ~ 5400 1775
Wire Wire Line
	7475 2175 6550 2175
Wire Wire Line
	6550 1875 6700 1875
Wire Wire Line
	6700 1300 6700 1875
Wire Wire Line
	6700 1300 6900 1300
Connection ~ 6700 1875
Wire Wire Line
	6700 1875 7475 1875
Connection ~ 4800 1625
Wire Wire Line
	4800 1625 4800 1525
Wire Wire Line
	5100 1525 5125 1525
Wire Wire Line
	5125 1525 5125 1625
Connection ~ 5125 1525
$Comp
L Jumper:SolderJumper_2_Open JP2
U 1 1 5E599476
P 6225 1450
F 0 "JP2" V 6179 1518 50  0000 L CNN
F 1 "SolderJumper_2_Open" V 6270 1518 50  0000 L CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm" H 6225 1450 50  0001 C CNN
F 3 "~" H 6225 1450 50  0001 C CNN
	1    6225 1450
	0    1    1    0   
$EndComp
$Comp
L Device:R_POT RV2
U 1 1 5E59947C
P 6225 1900
F 0 "RV2" H 6156 1946 50  0000 R CNN
F 1 "22K" H 6156 1855 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3006P_Horizontal" H 6225 1900 50  0001 C CNN
F 3 "~" H 6225 1900 50  0001 C CNN
	1    6225 1900
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 5E599482
P 6425 1750
F 0 "C2" V 6300 1875 50  0000 C CNN
F 1 "0.1uF" V 6375 1925 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 6463 1600 50  0001 C CNN
F 3 "~" H 6425 1750 50  0001 C CNN
	1    6425 1750
	-1   0    0    1   
$EndComp
Wire Wire Line
	6225 1600 6225 1750
Wire Wire Line
	6100 2175 6425 2175
Wire Wire Line
	6225 1600 6425 1600
Wire Wire Line
	6375 1900 6425 1900
Wire Wire Line
	6425 1900 6425 2175
Connection ~ 6425 1900
Connection ~ 6425 2175
Wire Wire Line
	6425 2175 6550 2175
Connection ~ 6225 1600
Wire Wire Line
	6700 1300 6225 1300
Wire Wire Line
	5800 1300 5800 1550
Connection ~ 6700 1300
Connection ~ 6225 1300
Wire Wire Line
	6225 1300 5800 1300
$EndSCHEMATC
