EESchema Schematic File Version 4
LIBS:Camera Adapter-cache
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
L MC33269D-3.3G:MC33269D-3.3G U1
U 1 1 5E85F90B
P 2875 4175
F 0 "U1" H 2875 4645 50  0000 C CNN
F 1 "MC33269D-3.3G" H 2875 4554 50  0000 C CNN
F 2 "SOIC127P600X175-8N" H 2875 4175 50  0001 L BNN
F 3 "" H 2875 4175 50  0001 C CNN
	1    2875 4175
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 5E8601F7
P 3725 4175
F 0 "C2" H 3840 4221 50  0000 L CNN
F 1 "10uF" H 3840 4130 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 3763 4025 50  0001 C CNN
F 3 "~" H 3725 4175 50  0001 C CNN
	1    3725 4175
	1    0    0    -1  
$EndComp
Wire Wire Line
	3575 3975 3725 3975
Wire Wire Line
	3725 3975 3725 4025
Wire Wire Line
	3725 4325 3725 4375
Wire Wire Line
	3725 4375 3575 4375
$Comp
L Device:C C1
U 1 1 5E860F9A
P 1825 4125
F 0 "C1" H 1940 4171 50  0000 L CNN
F 1 "10uF" H 1940 4080 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 1863 3975 50  0001 C CNN
F 3 "~" H 1825 4125 50  0001 C CNN
	1    1825 4125
	1    0    0    -1  
$EndComp
Wire Wire Line
	3725 4375 3725 4575
Wire Wire Line
	3725 4575 2875 4575
Wire Wire Line
	1825 4575 1825 4275
Connection ~ 3725 4375
$Comp
L power:+12V #PWR0101
U 1 1 5E8619F5
P 1750 3975
F 0 "#PWR0101" H 1750 3825 50  0001 C CNN
F 1 "+12V" V 1765 4103 50  0000 L CNN
F 2 "" H 1750 3975 50  0001 C CNN
F 3 "" H 1750 3975 50  0001 C CNN
	1    1750 3975
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2175 3975 1825 3975
Connection ~ 1825 3975
Wire Wire Line
	1825 3975 1750 3975
$Comp
L power:+3.3V #PWR0102
U 1 1 5E8622BF
P 3900 3975
F 0 "#PWR0102" H 3900 3825 50  0001 C CNN
F 1 "+3.3V" V 3915 4103 50  0000 L CNN
F 2 "" H 3900 3975 50  0001 C CNN
F 3 "" H 3900 3975 50  0001 C CNN
	1    3900 3975
	0    1    1    0   
$EndComp
Wire Wire Line
	3900 3975 3825 3975
Connection ~ 3725 3975
$Comp
L power:GND #PWR0103
U 1 1 5E862F20
P 2875 4575
F 0 "#PWR0103" H 2875 4325 50  0001 C CNN
F 1 "GND" H 2880 4402 50  0000 C CNN
F 2 "" H 2875 4575 50  0001 C CNN
F 3 "" H 2875 4575 50  0001 C CNN
	1    2875 4575
	1    0    0    -1  
$EndComp
Connection ~ 2875 4575
Wire Wire Line
	2875 4575 1825 4575
$Comp
L 634108150321:634108150321 J6
U 1 1 5E8639B3
P 7750 2100
F 0 "J6" H 8030 2171 50  0000 L CNN
F 1 "634108150321" H 8030 2080 50  0000 L CNN
F 2 "WURTH_634108150321" H 7750 2100 50  0001 L BNN
F 3 "" H 7750 2100 50  0001 L BNN
F 4 "8.85mm" H 7750 2100 50  0001 L BNN "Field4"
F 5 "Wurth Electronik" H 7750 2100 50  0001 L BNN "Field5"
F 6 "Manufacturer recommendations" H 7750 2100 50  0001 L BNN "Field6"
	1    7750 2100
	1    0    0    -1  
$EndComp
$Comp
L 634108150321:634108150321 J2
U 1 1 5E865ACA
P 3975 2000
F 0 "J2" H 4255 2071 50  0000 L CNN
F 1 "634108150321" H 4255 1980 50  0000 L CNN
F 2 "WURTH_634108150321" H 3975 2000 50  0001 L BNN
F 3 "" H 3975 2000 50  0001 L BNN
F 4 "8.85mm" H 3975 2000 50  0001 L BNN "Field4"
F 5 "Wurth Electronik" H 3975 2000 50  0001 L BNN "Field5"
F 6 "Manufacturer recommendations" H 3975 2000 50  0001 L BNN "Field6"
	1    3975 2000
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J4
U 1 1 5E867193
P 5825 4250
F 0 "J4" H 5905 4292 50  0000 L CNN
F 1 "Conn_01x03" H 5905 4201 50  0000 L CNN
F 2 "Connector_JST:JST_PH_S3B-PH-SM4-TB_1x03-1MP_P2.00mm_Horizontal" H 5825 4250 50  0001 C CNN
F 3 "~" H 5825 4250 50  0001 C CNN
	1    5825 4250
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR0104
U 1 1 5E867751
P 5475 4150
F 0 "#PWR0104" H 5475 4000 50  0001 C CNN
F 1 "+12V" V 5490 4278 50  0000 L CNN
F 2 "" H 5475 4150 50  0001 C CNN
F 3 "" H 5475 4150 50  0001 C CNN
	1    5475 4150
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0105
U 1 1 5E867DDE
P 5475 4350
F 0 "#PWR0105" H 5475 4100 50  0001 C CNN
F 1 "GND" V 5480 4222 50  0000 R CNN
F 2 "" H 5475 4350 50  0001 C CNN
F 3 "" H 5475 4350 50  0001 C CNN
	1    5475 4350
	0    1    1    0   
$EndComp
Text GLabel 5475 4250 0    50   Input ~ 0
CAMERAGPIO
Wire Wire Line
	5475 4150 5625 4150
Wire Wire Line
	5625 4250 5475 4250
Wire Wire Line
	5475 4350 5625 4350
$Comp
L power:GND #PWR0106
U 1 1 5E869037
P 1775 1450
F 0 "#PWR0106" H 1775 1200 50  0001 C CNN
F 1 "GND" V 1780 1322 50  0000 R CNN
F 2 "" H 1775 1450 50  0001 C CNN
F 3 "" H 1775 1450 50  0001 C CNN
	1    1775 1450
	0    1    1    0   
$EndComp
Wire Wire Line
	1775 1450 1800 1450
Wire Wire Line
	1925 1750 1800 1750
Wire Wire Line
	1800 1750 1800 1450
Connection ~ 1800 1450
Wire Wire Line
	1800 1450 1925 1450
Wire Wire Line
	1800 1750 1800 2050
Wire Wire Line
	1800 2050 1925 2050
Connection ~ 1800 1750
Wire Wire Line
	1800 2050 1800 2350
Wire Wire Line
	1800 2350 1925 2350
Connection ~ 1800 2050
NoConn ~ 1925 2550
NoConn ~ 5875 2550
$Comp
L power:+3.3V #PWR0107
U 1 1 5E86B0F9
P 1825 2850
F 0 "#PWR0107" H 1825 2700 50  0001 C CNN
F 1 "+3.3V" V 1840 2978 50  0000 L CNN
F 2 "" H 1825 2850 50  0001 C CNN
F 3 "" H 1825 2850 50  0001 C CNN
	1    1825 2850
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1825 2850 1925 2850
Text GLabel 1675 2450 0    50   Input ~ 0
CAMERAGPIO
Wire Wire Line
	1925 2450 1675 2450
Text GLabel 1675 1550 0    50   Input ~ 0
CAMERA0DN0
Text GLabel 1675 1650 0    50   Input ~ 0
CAMERA0DP0
Text GLabel 1675 1850 0    50   Input ~ 0
CAMERA0DN1
Text GLabel 1675 1950 0    50   Input ~ 0
CAMERA0DP1
Text GLabel 1675 2150 0    50   Input ~ 0
CAMERA0CN
Text GLabel 1675 2250 0    50   Input ~ 0
CAMERA0CP
Text GLabel 1675 2650 0    50   Input ~ 0
CAMERA0SCL
Text GLabel 1675 2750 0    50   Input ~ 0
CAMERA0SDA
Wire Wire Line
	1675 1550 1925 1550
Wire Wire Line
	1925 1650 1675 1650
Wire Wire Line
	1675 2150 1925 2150
Wire Wire Line
	1925 2250 1675 2250
Wire Wire Line
	1675 2650 1925 2650
Wire Wire Line
	1925 2750 1675 2750
Text GLabel 3400 1800 0    50   Input ~ 0
CAMERA0DN0
Text GLabel 3400 1900 0    50   Input ~ 0
CAMERA0DP0
Text GLabel 3400 1600 0    50   Input ~ 0
CAMERA0DN1
Text GLabel 3400 1700 0    50   Input ~ 0
CAMERA0DP1
Text GLabel 3400 2000 0    50   Input ~ 0
CAMERA0CN
Text GLabel 3400 2100 0    50   Input ~ 0
CAMERA0CP
Text GLabel 3400 2200 0    50   Input ~ 0
CAMERA0SCL
Text GLabel 3400 2300 0    50   Input ~ 0
CAMERA0SDA
$Comp
L power:GND #PWR0108
U 1 1 5E872410
P 3375 2500
F 0 "#PWR0108" H 3375 2250 50  0001 C CNN
F 1 "GND" V 3380 2372 50  0000 R CNN
F 2 "" H 3375 2500 50  0001 C CNN
F 3 "" H 3375 2500 50  0001 C CNN
	1    3375 2500
	0    1    1    0   
$EndComp
Wire Wire Line
	3375 2500 3475 2500
Wire Wire Line
	3400 2300 3475 2300
Wire Wire Line
	3475 2200 3400 2200
Wire Wire Line
	3400 2100 3475 2100
Wire Wire Line
	3475 2000 3400 2000
Wire Wire Line
	3475 1900 3400 1900
Wire Wire Line
	3400 1800 3475 1800
Wire Wire Line
	3475 1700 3400 1700
Wire Wire Line
	3475 1600 3400 1600
Text GLabel 7175 1900 0    50   Input ~ 0
CAMERA1DN0
Text GLabel 7175 2000 0    50   Input ~ 0
CAMERA1DP0
Text GLabel 7175 1700 0    50   Input ~ 0
CAMERA1DN1
Text GLabel 7175 1800 0    50   Input ~ 0
CAMERA1DP1
Text GLabel 7175 2100 0    50   Input ~ 0
CAMERA1CN
Text GLabel 7175 2200 0    50   Input ~ 0
CAMERA1CP
Text GLabel 7175 2300 0    50   Input ~ 0
CAMERA1SCL
Text GLabel 7175 2400 0    50   Input ~ 0
CAMERA1SDA
Wire Wire Line
	7175 2400 7250 2400
Wire Wire Line
	7250 2300 7175 2300
Wire Wire Line
	7175 2200 7250 2200
Wire Wire Line
	7250 2100 7175 2100
Wire Wire Line
	7250 2000 7175 2000
Wire Wire Line
	7175 1900 7250 1900
Wire Wire Line
	7250 1800 7175 1800
Wire Wire Line
	7250 1700 7175 1700
$Comp
L power:GND #PWR0109
U 1 1 5E87CD41
P 5725 1450
F 0 "#PWR0109" H 5725 1200 50  0001 C CNN
F 1 "GND" V 5730 1322 50  0000 R CNN
F 2 "" H 5725 1450 50  0001 C CNN
F 3 "" H 5725 1450 50  0001 C CNN
	1    5725 1450
	0    1    1    0   
$EndComp
Wire Wire Line
	5725 1450 5750 1450
Wire Wire Line
	5875 1750 5750 1750
Wire Wire Line
	5750 1750 5750 1450
Connection ~ 5750 1450
Wire Wire Line
	5750 1450 5875 1450
Wire Wire Line
	5750 1750 5750 2050
Wire Wire Line
	5750 2050 5875 2050
Connection ~ 5750 1750
Wire Wire Line
	5750 2050 5750 2350
Wire Wire Line
	5750 2350 5875 2350
Connection ~ 5750 2050
$Comp
L power:+3.3V #PWR0110
U 1 1 5E87CD52
P 5775 2850
F 0 "#PWR0110" H 5775 2700 50  0001 C CNN
F 1 "+3.3V" V 5790 2978 50  0000 L CNN
F 2 "" H 5775 2850 50  0001 C CNN
F 3 "" H 5775 2850 50  0001 C CNN
	1    5775 2850
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5775 2850 5875 2850
Text GLabel 5625 2450 0    50   Input ~ 0
CAMERAGPIO
Wire Wire Line
	5875 2450 5625 2450
Text GLabel 5625 1550 0    50   Input ~ 0
CAMERA1DN0
Text GLabel 5625 1650 0    50   Input ~ 0
CAMERA1DP0
Text GLabel 5625 1850 0    50   Input ~ 0
CAMERA1DN1
Text GLabel 5625 1950 0    50   Input ~ 0
CAMERA1DP1
Text GLabel 5625 2150 0    50   Input ~ 0
CAMERA1CN
Text GLabel 5625 2250 0    50   Input ~ 0
CAMERA1CP
Text GLabel 5625 2650 0    50   Input ~ 0
CAMERA1SCL
Text GLabel 5625 2750 0    50   Input ~ 0
CAMERA1SDA
Wire Wire Line
	5625 1550 5875 1550
Wire Wire Line
	5875 1650 5625 1650
Wire Wire Line
	5625 2150 5875 2150
Wire Wire Line
	5875 2250 5625 2250
Wire Wire Line
	5625 2650 5875 2650
Wire Wire Line
	5875 2750 5625 2750
$Comp
L Connector_Generic:Conn_01x02 J3
U 1 1 5E88631B
P 5800 3775
F 0 "J3" H 5880 3767 50  0000 L CNN
F 1 "Conn_01x02" H 5880 3676 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 5800 3775 50  0001 C CNN
F 3 "~" H 5800 3775 50  0001 C CNN
	1    5800 3775
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0111
U 1 1 5E886A04
P 5475 3875
F 0 "#PWR0111" H 5475 3625 50  0001 C CNN
F 1 "GND" V 5480 3747 50  0000 R CNN
F 2 "" H 5475 3875 50  0001 C CNN
F 3 "" H 5475 3875 50  0001 C CNN
	1    5475 3875
	0    1    1    0   
$EndComp
Wire Wire Line
	5600 3875 5475 3875
$Comp
L power:+3.3V #PWR0112
U 1 1 5E888D4B
P 5475 3775
F 0 "#PWR0112" H 5475 3625 50  0001 C CNN
F 1 "+3.3V" V 5490 3903 50  0000 L CNN
F 2 "" H 5475 3775 50  0001 C CNN
F 3 "" H 5475 3775 50  0001 C CNN
	1    5475 3775
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5600 3775 5475 3775
$Comp
L Device:R R1
U 1 1 5E88B7FD
P 3825 3825
F 0 "R1" H 3895 3871 50  0000 L CNN
F 1 "220" H 3895 3780 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3755 3825 50  0001 C CNN
F 3 "~" H 3825 3825 50  0001 C CNN
	1    3825 3825
	1    0    0    -1  
$EndComp
Connection ~ 3825 3975
Wire Wire Line
	3825 3975 3725 3975
$Comp
L Device:LED D1
U 1 1 5E88C3F2
P 3825 3450
F 0 "D1" V 3772 3528 50  0000 L CNN
F 1 "LED" V 3863 3528 50  0000 L CNN
F 2 "LED_SMD:LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 3825 3450 50  0001 C CNN
F 3 "~" H 3825 3450 50  0001 C CNN
	1    3825 3450
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0113
U 1 1 5E88CA09
P 3825 3225
F 0 "#PWR0113" H 3825 2975 50  0001 C CNN
F 1 "GND" H 3830 3052 50  0000 C CNN
F 2 "" H 3825 3225 50  0001 C CNN
F 3 "" H 3825 3225 50  0001 C CNN
	1    3825 3225
	-1   0    0    1   
$EndComp
Wire Wire Line
	3825 3225 3825 3300
Wire Wire Line
	3825 3600 3825 3675
Wire Wire Line
	1925 1850 1675 1850
Wire Wire Line
	1675 1950 1925 1950
$Comp
L 68611514122:68611514122 J1
U 1 1 6366E004
P 2125 2150
F 0 "J1" H 2089 2190 50  0000 L CNN
F 1 "68611514122" H 2089 2099 50  0000 L CNN
F 2 "digikey-footprints:68611514122" H 2125 2150 50  0001 L BNN
F 3 "" H 2125 2150 50  0001 L BNN
F 4 "68611514122" H 2125 2150 50  0001 L BNN "Field4"
F 5 "None" H 2125 2150 50  0001 L BNN "Field5"
F 6 "Unavailable" H 2125 2150 50  0001 L BNN "Field6"
F 7 "Connector [Würth Elektronik] 68611514122 Connector" H 2125 2150 50  0001 L BNN "Field7"
F 8 "Würth Elektronik" H 2125 2150 50  0001 L BNN "Field8"
	1    2125 2150
	1    0    0    -1  
$EndComp
$Comp
L 68611514122:68611514122 J5
U 1 1 6367193C
P 6075 2150
F 0 "J5" H 6039 2190 50  0000 L CNN
F 1 "68611514122" H 6039 2099 50  0000 L CNN
F 2 "digikey-footprints:68611514122" H 6075 2150 50  0001 L BNN
F 3 "" H 6075 2150 50  0001 L BNN
F 4 "68611514122" H 6075 2150 50  0001 L BNN "Field4"
F 5 "None" H 6075 2150 50  0001 L BNN "Field5"
F 6 "Unavailable" H 6075 2150 50  0001 L BNN "Field6"
F 7 "Connector [Würth Elektronik] 68611514122 Connector" H 6075 2150 50  0001 L BNN "Field7"
F 8 "Würth Elektronik" H 6075 2150 50  0001 L BNN "Field8"
	1    6075 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	5625 1850 5875 1850
Wire Wire Line
	5875 1950 5625 1950
$Comp
L power:GND #PWR0114
U 1 1 64014CD3
P 7200 2600
F 0 "#PWR0114" H 7200 2350 50  0001 C CNN
F 1 "GND" V 7205 2472 50  0000 R CNN
F 2 "" H 7200 2600 50  0001 C CNN
F 3 "" H 7200 2600 50  0001 C CNN
	1    7200 2600
	0    1    1    0   
$EndComp
Wire Wire Line
	7200 2600 7250 2600
$EndSCHEMATC