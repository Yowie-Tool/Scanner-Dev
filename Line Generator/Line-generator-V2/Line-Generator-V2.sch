EESchema Schematic File Version 4
EELAYER 30 0
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
P 925 1150
F 0 "J1" V 889 862 50  0000 R CNN
F 1 "Conn_01x04" V 798 862 50  0000 R CNN
F 2 "Connector_JST:JST_PH_B4B-PH-SM4-TB_1x04-1MP_P2.00mm_Vertical" H 925 1150 50  0001 C CNN
F 3 "~" H 925 1150 50  0001 C CNN
	1    925  1150
	0    -1   -1   0   
$EndComp
$Comp
L power:+12V #PWR0101
U 1 1 5E54231E
P 825 1500
F 0 "#PWR0101" H 825 1350 50  0001 C CNN
F 1 "+12V" H 840 1673 50  0000 C CNN
F 2 "" H 825 1500 50  0001 C CNN
F 3 "" H 825 1500 50  0001 C CNN
	1    825  1500
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 5E542B5B
P 925 1775
F 0 "#PWR0102" H 925 1525 50  0001 C CNN
F 1 "GND" H 930 1602 50  0000 C CNN
F 2 "" H 925 1775 50  0001 C CNN
F 3 "" H 925 1775 50  0001 C CNN
	1    925  1775
	1    0    0    -1  
$EndComp
Text GLabel 1025 1500 3    50   Output ~ 0
Laser1
Text GLabel 1125 1500 3    50   Output ~ 0
Laser2
Wire Wire Line
	825  1500 825  1350
Wire Wire Line
	925  1350 925  1775
Wire Wire Line
	1025 1500 1025 1350
Wire Wire Line
	1125 1350 1125 1500
$Comp
L Device:R R1
U 1 1 5E54EB98
P 2900 2125
F 0 "R1" V 2693 2125 50  0000 C CNN
F 1 "10K" V 2784 2125 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 2830 2125 50  0001 C CNN
F 3 "~" H 2900 2125 50  0001 C CNN
	1    2900 2125
	0    1    1    0   
$EndComp
Wire Wire Line
	2575 2125 2750 2125
$Comp
L Device:LED_Dual_ACA D?
U 1 1 6000B750
P 5275 2175
F 0 "D?" V 5321 1965 50  0000 R CNN
F 1 "LED_Dual_ACA" V 5230 1965 50  0000 R CNN
F 2 "Connector_PinSocket_1.27mm:PinSocket_1x03_P1.27mm_Vertical" H 5275 2175 50  0001 C CNN
F 3 "~" H 5275 2175 50  0001 C CNN
	1    5275 2175
	0    -1   -1   0   
$EndComp
Text Notes 5500 1975 0    50   ~ 0
120mA
Text Notes 4825 1950 0    50   ~ 0
200mA
Text Notes 4925 2325 0    50   ~ 0
2V5\nboth
$Comp
L Device:R R?
U 1 1 6000D306
P 4775 1075
F 0 "R?" H 4705 1029 50  0000 R CNN
F 1 "10R" H 4705 1120 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 4705 1075 50  0001 C CNN
F 3 "~" H 4775 1075 50  0001 C CNN
	1    4775 1075
	-1   0    0    1   
$EndComp
Text Notes 4975 1550 0    50   ~ 0
1.5W\n7V5
$Comp
L Device:D_Schottky D?
U 1 1 6001883B
P 3425 1325
F 0 "D?" V 3450 1400 50  0000 L CNN
F 1 "D_Schottky 2V" V 3225 1350 50  0000 L CNN
F 2 "Diode_SMD:D_SOD-323_HandSoldering" H 3425 1325 50  0001 C CNN
F 3 "https://docs.rs-online.com/2159/0900766b812e22b6.pdf" H 3425 1325 50  0001 C CNN
	1    3425 1325
	0    1    1    0   
$EndComp
$Comp
L Transistor_BJT:BCP51 Q?
U 1 1 60019DE0
P 4675 1575
F 0 "Q?" H 4865 1621 50  0000 L CNN
F 1 "BCP5310" H 4865 1530 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223-3_TabPin2" H 4875 1500 50  0001 L CIN
F 3 "" H 4675 1575 50  0001 L CNN
	1    4675 1575
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:TLC272 U?
U 1 1 6001B1FB
P 4175 1575
F 0 "U?" H 4200 1825 50  0000 C CNN
F 1 "TLC272" H 4225 1750 50  0000 C CNN
F 2 "" H 4175 1575 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tlc272.pdf" H 4175 1575 50  0001 C CNN
	1    4175 1575
	1    0    0    -1  
$EndComp
Wire Wire Line
	3775 1225 3775 1675
Wire Wire Line
	3775 1675 3875 1675
Wire Wire Line
	3775 1225 4775 1225
Wire Wire Line
	4775 1225 4775 1375
Connection ~ 4775 1225
Wire Wire Line
	4775 1775 4775 1875
Wire Wire Line
	3875 1475 3425 1475
Wire Wire Line
	4775 925  4000 925 
Wire Wire Line
	3425 925  3425 1175
$Comp
L power:+12V #PWR?
U 1 1 6003C71C
P 4000 825
F 0 "#PWR?" H 4000 675 50  0001 C CNN
F 1 "+12V" H 4015 998 50  0000 C CNN
F 2 "" H 4000 825 50  0001 C CNN
F 3 "" H 4000 825 50  0001 C CNN
	1    4000 825 
	1    0    0    -1  
$EndComp
Connection ~ 4000 925 
Wire Wire Line
	4000 925  3425 925 
$Comp
L Amplifier_Operational:TLC272 U?
U 3 1 6003EE56
P 1950 1450
F 0 "U?" H 1975 1700 50  0000 C CNN
F 1 "TLC272" H 2000 1625 50  0000 C CNN
F 2 "" H 1950 1450 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tlc272.pdf" H 1950 1450 50  0001 C CNN
	3    1950 1450
	1    0    0    -1  
$EndComp
Wire Wire Line
	4000 825  4000 925 
$Comp
L power:+12V #PWR?
U 1 1 60043F18
P 1850 1075
F 0 "#PWR?" H 1850 925 50  0001 C CNN
F 1 "+12V" H 1865 1248 50  0000 C CNN
F 2 "" H 1850 1075 50  0001 C CNN
F 3 "" H 1850 1075 50  0001 C CNN
	1    1850 1075
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 6004478D
P 4575 2475
F 0 "#PWR?" H 4575 2225 50  0001 C CNN
F 1 "GND" H 4580 2302 50  0000 C CNN
F 2 "" H 4575 2475 50  0001 C CNN
F 3 "" H 4575 2475 50  0001 C CNN
	1    4575 2475
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 60044FEB
P 1850 1825
F 0 "#PWR?" H 1850 1575 50  0001 C CNN
F 1 "GND" H 1855 1652 50  0000 C CNN
F 2 "" H 1850 1825 50  0001 C CNN
F 3 "" H 1850 1825 50  0001 C CNN
	1    1850 1825
	1    0    0    -1  
$EndComp
Wire Wire Line
	1850 1750 1850 1825
$Comp
L Transistor_FET:BS170F Q?
U 1 1 60049EAB
P 3325 2125
F 0 "Q?" H 3531 2171 50  0000 L CNN
F 1 "BS170F" H 3531 2080 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 3525 2050 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/BS170F.pdf" H 3325 2125 50  0001 L CNN
	1    3325 2125
	1    0    0    -1  
$EndComp
Connection ~ 4575 2475
$Comp
L Device:R R?
U 1 1 6006FB1E
P 3175 1175
F 0 "R?" H 3000 1225 50  0000 L CNN
F 1 "100K" H 2925 1125 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3105 1175 50  0001 C CNN
F 3 "~" H 3175 1175 50  0001 C CNN
	1    3175 1175
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 6007059A
P 3425 1700
F 0 "R?" H 3495 1746 50  0000 L CNN
F 1 "4K7" H 3495 1655 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3355 1700 50  0001 C CNN
F 3 "~" H 3425 1700 50  0001 C CNN
	1    3425 1700
	1    0    0    -1  
$EndComp
Wire Wire Line
	3425 1550 3425 1475
Connection ~ 3425 1475
Wire Wire Line
	3425 1925 3425 1850
Wire Wire Line
	3425 2325 3425 2475
Wire Wire Line
	3425 2475 4575 2475
Wire Wire Line
	3175 1025 3175 925 
Wire Wire Line
	3175 925  3425 925 
Connection ~ 3425 925 
Wire Wire Line
	3425 1475 3175 1475
Wire Wire Line
	3175 1475 3175 1325
Wire Wire Line
	3125 2125 3050 2125
Text Notes 5000 1125 0    50   ~ 0
0.5W\n2V
Text Notes 5575 1125 2    50   ~ 0
0.25W\n2V
Wire Wire Line
	7450 2125 7525 2125
Wire Wire Line
	7400 1475 7400 1325
Wire Wire Line
	7150 1475 7400 1475
Connection ~ 7150 925 
Wire Wire Line
	7400 925  7150 925 
Wire Wire Line
	7400 1025 7400 925 
Wire Wire Line
	7150 2325 7150 2475
Wire Wire Line
	7150 1925 7150 1850
Connection ~ 7150 1475
Wire Wire Line
	7150 1550 7150 1475
$Comp
L Device:R R?
U 1 1 600D0224
P 7150 1700
F 0 "R?" H 7220 1746 50  0000 L CNN
F 1 "4K7" H 7220 1655 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 7080 1700 50  0001 C CNN
F 3 "~" H 7150 1700 50  0001 C CNN
	1    7150 1700
	-1   0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 600D021E
P 7400 1175
F 0 "R?" H 7225 1225 50  0000 L CNN
F 1 "100K" H 7150 1125 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 7330 1175 50  0001 C CNN
F 3 "~" H 7400 1175 50  0001 C CNN
	1    7400 1175
	-1   0    0    -1  
$EndComp
$Comp
L Transistor_FET:BS170F Q?
U 1 1 600D0217
P 7250 2125
F 0 "Q?" H 7456 2171 50  0000 L CNN
F 1 "BS170F" H 7456 2080 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 7450 2050 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/BS170F.pdf" H 7250 2125 50  0001 L CNN
	1    7250 2125
	-1   0    0    -1  
$EndComp
Wire Wire Line
	7150 925  7150 1175
Wire Wire Line
	6700 1475 7150 1475
Wire Wire Line
	5800 1775 5800 1875
Connection ~ 5800 1225
Wire Wire Line
	5800 1225 5800 1375
Wire Wire Line
	6800 1225 5800 1225
Wire Wire Line
	6800 1675 6700 1675
Wire Wire Line
	6800 1225 6800 1675
$Comp
L Amplifier_Operational:TLC272 U?
U 2 1 600D01F8
P 6400 1575
F 0 "U?" H 6425 1825 50  0000 C CNN
F 1 "TLC272" H 6450 1750 50  0000 C CNN
F 2 "" H 6400 1575 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tlc272.pdf" H 6400 1575 50  0001 C CNN
	2    6400 1575
	-1   0    0    -1  
$EndComp
$Comp
L Transistor_BJT:BCP51 Q?
U 1 1 600D01F2
P 5900 1575
F 0 "Q?" H 6090 1621 50  0000 L CNN
F 1 "BCP5310" H 6090 1530 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223-3_TabPin2" H 6100 1500 50  0001 L CIN
F 3 "" H 5900 1575 50  0001 L CNN
	1    5900 1575
	-1   0    0    -1  
$EndComp
$Comp
L Device:D_Schottky D?
U 1 1 600D01EC
P 7150 1325
F 0 "D?" V 7175 1400 50  0000 L CNN
F 1 "D_Schottky 2V" V 6950 1350 50  0000 L CNN
F 2 "Diode_SMD:D_SOD-323_HandSoldering" H 7150 1325 50  0001 C CNN
F 3 "https://docs.rs-online.com/2159/0900766b812e22b6.pdf" H 7150 1325 50  0001 C CNN
	1    7150 1325
	0    -1   1    0   
$EndComp
Text Notes 5600 1550 2    50   ~ 0
1.5W\n7V5
$Comp
L Device:R R?
U 1 1 600D01E5
P 5800 1075
F 0 "R?" H 5730 1029 50  0000 R CNN
F 1 "18R" H 5730 1120 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5730 1075 50  0001 C CNN
F 3 "~" H 5800 1075 50  0001 C CNN
	1    5800 1075
	1    0    0    1   
$EndComp
Wire Wire Line
	8000 2125 7825 2125
Text GLabel 8000 2125 2    50   Output ~ 0
Laser2
$Comp
L Device:R R?
U 1 1 600D01D4
P 7675 2125
F 0 "R?" V 7468 2125 50  0000 C CNN
F 1 "10K" V 7559 2125 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 7605 2125 50  0001 C CNN
F 3 "~" H 7675 2125 50  0001 C CNN
	1    7675 2125
	0    -1   1    0   
$EndComp
Wire Wire Line
	4575 2475 5275 2475
Wire Wire Line
	5175 1875 4775 1875
Wire Wire Line
	5375 1875 5800 1875
Connection ~ 5275 2475
Text GLabel 2575 2125 0    50   Output ~ 0
Laser1
Wire Wire Line
	1850 1075 1850 1150
Wire Bus Line
	4500 775  6025 775 
Wire Bus Line
	6025 775  6025 2400
Wire Bus Line
	6025 2400 4500 2400
Wire Bus Line
	4500 2400 4500 775 
Text Notes 4525 2350 0    50   ~ 0
All this\nwill get\nhot
Wire Wire Line
	5275 2475 7150 2475
Wire Wire Line
	5800 925  7150 925 
Wire Wire Line
	5800 925  4775 925 
Connection ~ 5800 925 
Connection ~ 4775 925 
$EndSCHEMATC
