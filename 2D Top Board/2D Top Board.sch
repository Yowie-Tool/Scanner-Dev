EESchema Schematic File Version 4
LIBS:2D Top Board-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Camera Selection Board"
Date "2020-01-29"
Rev "1"
Comp "Beech Design Limited"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	2075 1500 1875 1500
Wire Wire Line
	2075 1600 1875 1600
$Comp
L power:GND #PWR02
U 1 1 580C1D11
P 1975 3550
F 0 "#PWR02" H 1975 3300 50  0001 C CNN
F 1 "GND" H 1975 3400 50  0000 C CNN
F 2 "" H 1975 3550 50  0000 C CNN
F 3 "" H 1975 3550 50  0000 C CNN
	1    1975 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	1975 1700 1975 2100
Wire Wire Line
	1975 3100 1875 3100
Wire Wire Line
	1975 2900 1875 2900
Connection ~ 1975 3100
Wire Wire Line
	1975 2400 1875 2400
Connection ~ 1975 2900
Wire Wire Line
	1975 2100 1875 2100
Connection ~ 1975 2400
$Comp
L power:GND #PWR03
U 1 1 580C1E01
P 1275 3550
F 0 "#PWR03" H 1275 3300 50  0001 C CNN
F 1 "GND" H 1275 3400 50  0000 C CNN
F 2 "" H 1275 3550 50  0000 C CNN
F 3 "" H 1275 3550 50  0000 C CNN
	1    1275 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	1275 3400 1375 3400
Wire Wire Line
	1275 1900 1275 2700
Wire Wire Line
	1275 2700 1375 2700
Connection ~ 1275 3400
Wire Wire Line
	1275 1900 1375 1900
Connection ~ 1275 2700
Wire Wire Line
	1975 1700 1875 1700
Connection ~ 1975 2100
$Comp
L Universal-Interface-Board-rescue:Mounting_Hole-Mechanical MK1
U 1 1 5834FB2E
P 650 7400
F 0 "MK1" H 750 7446 50  0000 L CNN
F 1 "M2.5" H 750 7355 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 650 7400 60  0001 C CNN
F 3 "" H 650 7400 60  0001 C CNN
	1    650  7400
	1    0    0    -1  
$EndComp
$Comp
L Universal-Interface-Board-rescue:Mounting_Hole-Mechanical MK3
U 1 1 5834FBEF
P 1100 7400
F 0 "MK3" H 1200 7446 50  0000 L CNN
F 1 "M2.5" H 1200 7355 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 1100 7400 60  0001 C CNN
F 3 "" H 1100 7400 60  0001 C CNN
	1    1100 7400
	1    0    0    -1  
$EndComp
$Comp
L Universal-Interface-Board-rescue:Mounting_Hole-Mechanical MK2
U 1 1 5834FC19
P 650 7600
F 0 "MK2" H 750 7646 50  0000 L CNN
F 1 "M2.5" H 750 7555 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 650 7600 60  0001 C CNN
F 3 "" H 650 7600 60  0001 C CNN
	1    650  7600
	1    0    0    -1  
$EndComp
$Comp
L Universal-Interface-Board-rescue:Mounting_Hole-Mechanical MK4
U 1 1 5834FC4F
P 1100 7600
F 0 "MK4" H 1200 7646 50  0000 L CNN
F 1 "M2.5" H 1200 7555 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 1100 7600 60  0001 C CNN
F 3 "" H 1100 7600 60  0001 C CNN
	1    1100 7600
	1    0    0    -1  
$EndComp
Text Notes 650  7250 0    50   ~ 10
Mounting Holes
Wire Wire Line
	2075 1500 2075 1600
Wire Wire Line
	1975 3100 1975 3550
Wire Wire Line
	1975 2900 1975 3100
Wire Wire Line
	1975 2400 1975 2900
Wire Wire Line
	1275 3400 1275 3550
Wire Wire Line
	1275 2700 1275 3400
Wire Wire Line
	1975 2100 1975 2400
Text Notes 775  1025 0    50   ~ 10
Pi Header (Extra Long pins)
Text GLabel 1100 2200 0    50   Output ~ 10
SEL
Wire Wire Line
	1375 1800 1100 1800
Text GLabel 1100 3200 0    50   Input ~ 10
REED
Wire Wire Line
	1100 3200 1375 3200
Text GLabel 1100 3300 0    50   Input ~ 10
SWITCH
Wire Wire Line
	1100 3300 1375 3300
Text GLabel 1100 3100 0    50   Input ~ 10
Uart5RX
Wire Wire Line
	1100 3100 1375 3100
Text GLabel 1175 2400 0    50   Output ~ 10
UartRESET
Wire Wire Line
	1375 2400 1175 2400
Text GLabel 2075 3000 2    50   Output ~ 10
Uart5TX
Wire Wire Line
	1875 3000 2075 3000
Text GLabel 1100 2100 0    50   Output ~ 10
LASER2
$Comp
L Connector_Generic:Conn_02x20_Odd_Even P1
U 1 1 59AD464A
P 1575 2400
F 0 "P1" H 1625 3517 50  0000 C CNN
F 1 "Conn_02x20_Odd_Even" H 1625 3426 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical" H -3275 1450 50  0001 C CNN
F 3 "" H -3275 1450 50  0001 C CNN
	1    1575 2400
	1    0    0    -1  
$EndComp
Text Notes 600  5700 0    50   ~ 10
Lasers
NoConn ~ 1375 1500
NoConn ~ 1875 2800
NoConn ~ 1375 2800
Text GLabel 1100 2000 0    50   Output ~ 10
LASER1
Wire Wire Line
	1175 2600 1375 2600
Text GLabel 1175 2600 0    50   Input ~ 10
SWITCHFAULT
Wire Wire Line
	1375 2100 1100 2100
Wire Wire Line
	1375 2000 1100 2000
NoConn ~ 1875 3400
Text GLabel 3275 1700 0    50   Input ~ 10
CAMERACP
Text GLabel 3275 1600 0    50   Input ~ 10
CAMERACN
Wire Wire Line
	3400 1400 3275 1400
Wire Wire Line
	3400 1300 3275 1300
Wire Wire Line
	3400 1100 3275 1100
Wire Wire Line
	3275 1000 3400 1000
Text GLabel 3275 1400 0    50   Input ~ 10
CAMERADP1
Text GLabel 3275 1300 0    50   Input ~ 10
CAMERADN1
Text GLabel 3275 1100 0    50   Input ~ 10
CAMERADP0
Text GLabel 3275 1000 0    50   Input ~ 10
CAMERADN0
Wire Wire Line
	3325 1200 3325 900 
Connection ~ 3325 1200
Wire Wire Line
	3400 1200 3325 1200
Wire Wire Line
	3325 1500 3325 1200
Connection ~ 3325 1500
Connection ~ 3325 900 
Wire Wire Line
	3325 1800 3325 1500
Wire Wire Line
	3400 1800 3325 1800
NoConn ~ 3400 2000
Wire Wire Line
	3275 2300 3400 2300
$Comp
L power:+3.3V #PWR0104
U 1 1 5E690E50
P 3275 2300
F 0 "#PWR0104" H 3275 2150 50  0001 C CNN
F 1 "+3.3V" V 3275 2525 50  0000 C CNN
F 2 "" H 3275 2300 50  0001 C CNN
F 3 "" H 3275 2300 50  0001 C CNN
	1    3275 2300
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3275 2200 3400 2200
Wire Wire Line
	3400 2100 3275 2100
Text GLabel 3275 2100 0    50   Input ~ 10
CAMERASCL
Text GLabel 3275 2200 0    50   Input ~ 10
CAMERASDA
Wire Wire Line
	3325 900  3400 900 
$Comp
L power:GND #PWR0105
U 1 1 5E660F7E
P 3325 900
F 0 "#PWR0105" H 3325 650 50  0001 C CNN
F 1 "GND" V 3325 675 50  0000 C CNN
F 2 "" H 3325 900 50  0000 C CNN
F 3 "" H 3325 900 50  0000 C CNN
	1    3325 900 
	0    1    1    0   
$EndComp
Wire Wire Line
	8625 2500 8775 2500
Text GLabel 8625 2500 0    50   Input ~ 10
SEL
Wire Wire Line
	9225 4100 9225 4000
$Comp
L power:GND #PWR0111
U 1 1 5E3F2863
P 9225 4100
F 0 "#PWR0111" H 9225 3850 50  0001 C CNN
F 1 "GND" H 9225 3950 50  0000 C CNN
F 2 "" H 9225 4100 50  0000 C CNN
F 3 "" H 9225 4100 50  0000 C CNN
	1    9225 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	9225 1500 9225 1400
$Comp
L power:+3.3V #PWR0112
U 1 1 5E3EB157
P 9225 1400
F 0 "#PWR0112" H 9225 1250 50  0001 C CNN
F 1 "+3.3V" V 9225 1625 50  0000 C CNN
F 2 "" H 9225 1400 50  0001 C CNN
F 3 "" H 9225 1400 50  0001 C CNN
	1    9225 1400
	1    0    0    -1  
$EndComp
NoConn ~ 8775 2300
NoConn ~ 8775 3800
$Comp
L dk_Logic-Signal-Switches-Multiplexers-Decoders:FSA642 U1
U 1 1 5E3DCDB0
P 9075 2600
F 0 "U1" H 9303 2503 60  0000 L CNN
F 1 "FSA642" V 9200 2400 60  0000 L CNN
F 2 "digikey-footprints:QFN50P400X400X60-25N" H 9275 2900 60  0001 L CNN
F 3 "http://www.ti.com/general/docs/suppproductinfo.tsp?distId=10&gotoUrl=http%3A%2F%2Fwww.ti.com%2Flit%2Fgpn%2Ftca9548a" H 9275 3000 60  0001 L CNN
F 4 "FSA642" H 9275 3100 60  0001 L CNN "MPN"
F 5 "Integrated Circuits (ICs)" H 9275 3200 60  0001 L CNN "Category"
F 6 "Logic - Signal Switches, Multiplexers, Decoders" H 9275 3300 60  0001 L CNN "Family"
F 7 "Low power, three port high speed MIPI switch" H 9275 3400 60  0001 L CNN "Description"
F 8 "Fairchild" H 9275 3500 60  0001 L CNN "Manufacturer"
F 9 "Active" H 9275 3600 60  0001 L CNN "Status"
	1    9075 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	5525 4050 5525 3975
Wire Wire Line
	6600 4050 6600 3975
$Comp
L power:GND #PWR0114
U 1 1 5E6426D1
P 5525 3975
F 0 "#PWR0114" H 5525 3725 50  0001 C CNN
F 1 "GND" V 5525 3750 50  0000 C CNN
F 2 "" H 5525 3975 50  0000 C CNN
F 3 "" H 5525 3975 50  0000 C CNN
	1    5525 3975
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0115
U 1 1 5E6423DD
P 6600 3975
F 0 "#PWR0115" H 6600 3725 50  0001 C CNN
F 1 "GND" V 6600 3750 50  0000 C CNN
F 2 "" H 6600 3975 50  0000 C CNN
F 3 "" H 6600 3975 50  0000 C CNN
	1    6600 3975
	-1   0    0    1   
$EndComp
$Comp
L pspice:CAP C3
U 1 1 5E638678
P 5525 4300
F 0 "C3" H 5550 4400 50  0000 L CNN
F 1 "10nF" H 5600 4175 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 5525 4300 50  0001 C CNN
F 3 "~" H 5525 4300 50  0001 C CNN
	1    5525 4300
	-1   0    0    1   
$EndComp
$Comp
L pspice:CAP C5
U 1 1 5E638166
P 6600 4300
F 0 "C5" H 6625 4400 50  0000 L CNN
F 1 "10nF" H 6675 4175 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 6600 4300 50  0001 C CNN
F 3 "~" H 6600 4300 50  0001 C CNN
	1    6600 4300
	-1   0    0    1   
$EndComp
Wire Wire Line
	10200 5425 10025 5425
Text GLabel 10200 5425 2    50   Input ~ 10
SWITCHFAULT
Text GLabel 5600 5525 0    50   Input ~ 10
CAMERA1SCL
Text GLabel 5600 5625 0    50   Input ~ 10
CAMERA1SDA
Wire Wire Line
	9475 5525 10200 5525
Wire Wire Line
	9475 5625 10200 5625
Wire Wire Line
	6350 4850 6350 5125
Connection ~ 6350 5125
Wire Wire Line
	5600 5125 6350 5125
Text GLabel 5600 5125 0    50   Input ~ 10
CAMERA0SCL
Text GLabel 5600 5225 0    50   Input ~ 10
CAMERA0SDA
Wire Wire Line
	6525 4550 6600 4550
Connection ~ 6525 4550
$Comp
L Device:R R5
U 1 1 5E448982
P 6525 4700
F 0 "R5" H 6575 4775 50  0000 L CNN
F 1 "10K" V 6525 4625 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 6455 4700 50  0001 C CNN
F 3 "~" H 6525 4700 50  0001 C CNN
	1    6525 4700
	1    0    0    1   
$EndComp
Wire Wire Line
	6350 4550 6525 4550
Connection ~ 6350 4550
$Comp
L Device:R R4
U 1 1 5E4486C2
P 6350 4700
F 0 "R4" H 6150 4775 50  0000 L CNN
F 1 "10K" V 6350 4625 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 6280 4700 50  0001 C CNN
F 3 "~" H 6350 4700 50  0001 C CNN
	1    6350 4700
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0120
U 1 1 5E43EC97
P 5800 3975
F 0 "#PWR0120" H 5800 3825 50  0001 C CNN
F 1 "+3.3V" V 5800 4200 50  0000 C CNN
F 2 "" H 5800 3975 50  0001 C CNN
F 3 "" H 5800 3975 50  0001 C CNN
	1    5800 3975
	1    0    0    -1  
$EndComp
Text GLabel 5600 5425 0    50   Input ~ 10
CAMERASCL
Text GLabel 5600 5325 0    50   Input ~ 10
CAMERASDA
Wire Wire Line
	2250 6375 2425 6375
Wire Wire Line
	2425 6275 2250 6275
Wire Wire Line
	2250 6175 2425 6175
Text GLabel 2250 6375 0    50   Input ~ 10
UartRESET
Text GLabel 2250 6275 0    50   Output ~ 10
Uart3RX
Text GLabel 2250 6175 0    50   Input ~ 10
Uart3TX
Text Notes 2150 5800 0    50   ~ 10
Stepper Control 1
Text GLabel 3275 1900 0    50   Input ~ 10
CAMERAGPIO
Wire Wire Line
	3275 1900 3400 1900
Text GLabel 5150 1800 0    50   Input ~ 10
CAMERA0CP
Text GLabel 5150 1700 0    50   Input ~ 10
CAMERA0CN
Wire Wire Line
	5275 1200 5150 1200
Wire Wire Line
	5150 1100 5275 1100
Text GLabel 5150 1500 0    50   Input ~ 10
CAMERA0DP1
Text GLabel 5150 1400 0    50   Input ~ 10
CAMERA0DN1
Text GLabel 5150 1200 0    50   Input ~ 10
CAMERA0DP0
Text GLabel 5150 1100 0    50   Input ~ 10
CAMERA0DN0
Wire Wire Line
	5200 1300 5200 1000
Connection ~ 5200 1300
Wire Wire Line
	5200 1600 5200 1300
Connection ~ 5200 1600
Connection ~ 5200 1000
Wire Wire Line
	5200 1900 5200 1600
NoConn ~ 5275 2100
Wire Wire Line
	5150 2400 5275 2400
$Comp
L power:+3.3V #PWR0122
U 1 1 5E7F9AD8
P 5150 2400
F 0 "#PWR0122" H 5150 2250 50  0001 C CNN
F 1 "+3.3V" V 5150 2625 50  0000 C CNN
F 2 "" H 5150 2400 50  0001 C CNN
F 3 "" H 5150 2400 50  0001 C CNN
	1    5150 2400
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5150 2300 5275 2300
Wire Wire Line
	5275 2200 5150 2200
Text GLabel 5150 2200 0    50   Input ~ 10
CAMERA0SCL
Text GLabel 5150 2300 0    50   Input ~ 10
CAMERA0SDA
Wire Wire Line
	5200 1000 5275 1000
$Comp
L power:GND #PWR0123
U 1 1 5E7F9AE3
P 5200 1000
F 0 "#PWR0123" H 5200 750 50  0001 C CNN
F 1 "GND" V 5200 775 50  0000 C CNN
F 2 "" H 5200 1000 50  0000 C CNN
F 3 "" H 5200 1000 50  0000 C CNN
	1    5200 1000
	0    1    1    0   
$EndComp
Text GLabel 5150 2000 0    50   Input ~ 10
CAMERAGPIO
Wire Wire Line
	5150 2000 5275 2000
Text Notes 2825 725  0    50   ~ 0
Camera Out
Text Notes 4650 800  0    50   ~ 0
Camera 0 in
Wire Wire Line
	7025 1800 6900 1800
Wire Wire Line
	6900 1700 7025 1700
Text GLabel 6900 1800 0    50   Input ~ 10
CAMERA1CP
Text GLabel 6900 1700 0    50   Input ~ 10
CAMERA1CN
Wire Wire Line
	7025 1500 6900 1500
Wire Wire Line
	7025 1400 6900 1400
Wire Wire Line
	7025 1200 6900 1200
Wire Wire Line
	6900 1100 7025 1100
Text GLabel 6900 1500 0    50   Input ~ 10
CAMERA1DP1
Text GLabel 6900 1400 0    50   Input ~ 10
CAMERA1DN1
Text GLabel 6900 1200 0    50   Input ~ 10
CAMERA1DP0
Text GLabel 6900 1100 0    50   Input ~ 10
CAMERA1DN0
Wire Wire Line
	6950 1300 6950 1000
Connection ~ 6950 1300
Wire Wire Line
	7025 1300 6950 1300
Wire Wire Line
	6950 1600 6950 1300
Connection ~ 6950 1600
Wire Wire Line
	7025 1600 6950 1600
Connection ~ 6950 1000
Wire Wire Line
	6950 1900 6950 1600
Wire Wire Line
	7025 1900 6950 1900
NoConn ~ 7025 2100
Wire Wire Line
	6900 2400 7025 2400
$Comp
L power:+3.3V #PWR0124
U 1 1 5E818C8E
P 6900 2400
F 0 "#PWR0124" H 6900 2250 50  0001 C CNN
F 1 "+3.3V" V 6900 2625 50  0000 C CNN
F 2 "" H 6900 2400 50  0001 C CNN
F 3 "" H 6900 2400 50  0001 C CNN
	1    6900 2400
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6900 2300 7025 2300
Wire Wire Line
	7025 2200 6900 2200
Text GLabel 6900 2200 0    50   Input ~ 10
CAMERA1SCL
Text GLabel 6900 2300 0    50   Input ~ 10
CAMERA1SDA
Wire Wire Line
	6950 1000 7025 1000
$Comp
L power:GND #PWR0125
U 1 1 5E818C99
P 6950 1000
F 0 "#PWR0125" H 6950 750 50  0001 C CNN
F 1 "GND" V 6950 775 50  0000 C CNN
F 2 "" H 6950 1000 50  0000 C CNN
F 3 "" H 6950 1000 50  0000 C CNN
	1    6950 1000
	0    1    1    0   
$EndComp
Text GLabel 6900 2000 0    50   Input ~ 10
CAMERAGPIO
Wire Wire Line
	6900 2000 7025 2000
Text Notes 6400 825  0    50   ~ 0
Camera 1 in
Text GLabel 8650 1700 0    50   Input ~ 10
CAMERACP
Text GLabel 8650 1800 0    50   Input ~ 10
CAMERACN
Wire Wire Line
	8650 1700 8775 1700
Wire Wire Line
	8775 1800 8650 1800
Text GLabel 8650 1900 0    50   Input ~ 10
CAMERADP0
Text GLabel 8650 2000 0    50   Input ~ 10
CAMERADN0
Wire Wire Line
	8650 1900 8775 1900
Wire Wire Line
	8775 2000 8650 2000
Text GLabel 8650 2100 0    50   Input ~ 10
CAMERADP1
Text GLabel 8650 2200 0    50   Input ~ 10
CAMERADN1
Wire Wire Line
	8775 2100 8650 2100
Wire Wire Line
	8775 2200 8650 2200
Text GLabel 8625 3100 0    50   Input ~ 10
CAMERA0CP
Text GLabel 8625 3000 0    50   Input ~ 10
CAMERA0CN
Text GLabel 8625 2700 0    50   Input ~ 10
CAMERA0DP1
Text GLabel 8625 2600 0    50   Input ~ 10
CAMERA0DN1
Text GLabel 8625 2900 0    50   Input ~ 10
CAMERA0DP0
Text GLabel 8625 2800 0    50   Input ~ 10
CAMERA0DN0
Wire Wire Line
	8625 3000 8775 3000
Wire Wire Line
	8775 3100 8625 3100
Wire Wire Line
	8625 2600 8775 2600
Wire Wire Line
	8625 2700 8775 2700
Wire Wire Line
	8775 2800 8625 2800
Wire Wire Line
	8625 2900 8775 2900
Text GLabel 8650 3600 0    50   Input ~ 10
CAMERA1CP
Text GLabel 8650 3700 0    50   Input ~ 10
CAMERA1CN
Text GLabel 8650 3300 0    50   Input ~ 10
CAMERA1DP1
Text GLabel 8650 3200 0    50   Input ~ 10
CAMERA1DN1
Text GLabel 8650 3400 0    50   Input ~ 10
CAMERA1DP0
Text GLabel 8650 3500 0    50   Input ~ 10
CAMERA1DN0
Wire Wire Line
	8650 3200 8775 3200
Wire Wire Line
	8775 3300 8650 3300
Wire Wire Line
	8775 3400 8650 3400
Wire Wire Line
	8650 3500 8775 3500
Wire Wire Line
	8775 3600 8650 3600
Wire Wire Line
	8650 3700 8775 3700
$Comp
L Connector_Generic:Conn_01x02 J4
U 1 1 5ED9669C
P 4075 2900
F 0 "J4" H 4155 2892 50  0000 L CNN
F 1 "Conn_01x02" H 4155 2801 50  0000 L CNN
F 2 "Connector_JST:JST_PH_B2B-PH-SM4-TB_1x02-1MP_P2.00mm_Vertical" H 4075 2900 50  0001 C CNN
F 3 "~" H 4075 2900 50  0001 C CNN
	1    4075 2900
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J5
U 1 1 5ED97F8F
P 4075 3400
F 0 "J5" H 4155 3392 50  0000 L CNN
F 1 "Conn_01x02" H 4155 3301 50  0000 L CNN
F 2 "Connector_JST:JST_PH_B2B-PH-SM4-TB_1x02-1MP_P2.00mm_Vertical" H 4075 3400 50  0001 C CNN
F 3 "~" H 4075 3400 50  0001 C CNN
	1    4075 3400
	1    0    0    -1  
$EndComp
Text GLabel 3675 2900 0    50   Input ~ 10
REED
Wire Wire Line
	3675 2900 3875 2900
Text GLabel 3675 3400 0    50   Input ~ 10
SWITCH
Wire Wire Line
	3675 3400 3875 3400
Wire Wire Line
	3675 3500 3875 3500
Wire Wire Line
	3675 3000 3875 3000
Text Notes 3375 2750 0    50   ~ 0
Reed Switch
Text Notes 3375 3275 0    50   ~ 0
Power Switch
$Comp
L Device:R_Pack04 RN1
U 1 1 5F09F1F3
P 6000 4850
F 0 "RN1" H 5575 4900 50  0000 L CNN
F 1 "10K" H 5575 4825 50  0000 L CNN
F 2 "Resistor_SMD:R_Array_Convex_4x1206" V 6275 4850 50  0001 C CNN
F 3 "~" H 6000 4850 50  0001 C CNN
	1    6000 4850
	1    0    0    -1  
$EndComp
Wire Wire Line
	1375 2200 1100 2200
Text GLabel 1100 1800 0    50   Output ~ 10
Uart3TX
Text GLabel 1100 2900 0    50   Output ~ 10
Uart3TX
Wire Wire Line
	1375 2900 1100 2900
Wire Wire Line
	3900 6200 3725 6200
Wire Wire Line
	3725 6100 3900 6100
Text GLabel 3725 6200 0    50   Output ~ 10
Uart5RX
Text GLabel 3725 6100 0    50   Input ~ 10
Uart5TX
Text Notes 3475 5875 0    50   ~ 10
Additional UART control (GPS)
NoConn ~ 1375 1600
NoConn ~ 1375 1700
NoConn ~ 1875 2500
$Comp
L Connector_Generic:Conn_01x04 J10
U 1 1 5E6EFA2A
P 4100 6100
F 0 "J10" H 4180 6092 50  0000 L CNN
F 1 "Conn_01x04" H 4180 6001 50  0000 L CNN
F 2 "Connector_JST:JST_PH_B4B-PH-SM4-TB_1x04-1MP_P2.00mm_Vertical" H 4100 6100 50  0001 C CNN
F 3 "~" H 4100 6100 50  0001 C CNN
	1    4100 6100
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0101
U 1 1 5E70A5CD
P 3725 6000
F 0 "#PWR0101" H 3725 5850 50  0001 C CNN
F 1 "+3.3V" V 3725 6225 50  0000 C CNN
F 2 "" H 3725 6000 50  0001 C CNN
F 3 "" H 3725 6000 50  0001 C CNN
	1    3725 6000
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3900 6000 3725 6000
$Comp
L power:GND #PWR0102
U 1 1 5E725DDF
P 3725 6300
F 0 "#PWR0102" H 3725 6050 50  0001 C CNN
F 1 "GND" V 3725 6075 50  0000 C CNN
F 2 "" H 3725 6300 50  0000 C CNN
F 3 "" H 3725 6300 50  0000 C CNN
	1    3725 6300
	0    1    1    0   
$EndComp
Wire Wire Line
	3900 6300 3725 6300
NoConn ~ 1375 3000
$Comp
L LTC4312IMSPBF:LTC4312IMSPBF U3
U 1 1 5E71D777
P 6675 4925
F 0 "U3" H 8075 5290 50  0000 C CNN
F 1 "LTC4312IMSPBF" H 8075 5199 50  0000 C CNN
F 2 "Package_SO:MSOP-16_3x4mm_P0.5mm" H 6675 4925 50  0001 L BNN
F 3 "" H 6675 4925 50  0001 L BNN
F 4 "Buffer, Multiplexer 1 x 1:2 Channel 400kHz 16-MSOP" H 6675 4925 50  0001 L BNN "Field4"
F 5 "Linear Technology" H 6675 4925 50  0001 L BNN "Field5"
F 6 "None" H 6675 4925 50  0001 L BNN "Field6"
F 7 "LTC4312IMS#PBF" H 6675 4925 50  0001 L BNN "Field7"
F 8 "Unavailable" H 6675 4925 50  0001 L BNN "Field8"
	1    6675 4925
	1    0    0    -1  
$EndComp
Wire Wire Line
	6350 5125 6675 5125
Wire Wire Line
	5525 4550 5800 4550
Wire Wire Line
	6675 5425 6000 5425
Wire Wire Line
	6100 4650 6100 4550
Connection ~ 6100 4550
Wire Wire Line
	6100 4550 6175 4550
Wire Wire Line
	6000 4650 6000 4550
Connection ~ 6000 4550
Wire Wire Line
	6000 4550 6100 4550
Wire Wire Line
	5900 4650 5900 4550
Connection ~ 5900 4550
Wire Wire Line
	5900 4550 6000 4550
Wire Wire Line
	5800 4650 5800 4550
Connection ~ 5800 4550
Wire Wire Line
	5800 4550 5900 4550
Wire Wire Line
	5600 5225 6525 5225
Wire Wire Line
	6525 4850 6525 5225
Connection ~ 6525 5225
Wire Wire Line
	6525 5225 6675 5225
$Comp
L Device:R R6
U 1 1 5E8D628D
P 10025 5275
F 0 "R6" H 9825 5350 50  0000 L CNN
F 1 "10K" V 10025 5200 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 9955 5275 50  0001 C CNN
F 3 "~" H 10025 5275 50  0001 C CNN
	1    10025 5275
	1    0    0    -1  
$EndComp
Connection ~ 10025 5425
Wire Wire Line
	10025 5425 9475 5425
Wire Wire Line
	9475 5325 9800 5325
Wire Wire Line
	9800 5325 9800 5125
Wire Wire Line
	9800 5125 10025 5125
Wire Wire Line
	10025 5125 10025 4925
Wire Wire Line
	10025 4925 9475 4925
Connection ~ 10025 5125
$Comp
L power:+3.3V #PWR0103
U 1 1 5E90DB24
P 10025 4925
F 0 "#PWR0103" H 10025 4775 50  0001 C CNN
F 1 "+3.3V" V 10025 5150 50  0000 C CNN
F 2 "" H 10025 4925 50  0001 C CNN
F 3 "" H 10025 4925 50  0001 C CNN
	1    10025 4925
	1    0    0    -1  
$EndComp
Connection ~ 10025 4925
$Comp
L power:GND #PWR0106
U 1 1 5E90E2DF
P 9600 5025
F 0 "#PWR0106" H 9600 4775 50  0001 C CNN
F 1 "GND" V 9600 4800 50  0000 C CNN
F 2 "" H 9600 5025 50  0000 C CNN
F 3 "" H 9600 5025 50  0000 C CNN
	1    9600 5025
	0    -1   -1   0   
$EndComp
Wire Wire Line
	9600 5025 9475 5025
Wire Wire Line
	6175 4050 6175 3975
$Comp
L power:GND #PWR0107
U 1 1 5E9714C9
P 6175 3975
F 0 "#PWR0107" H 6175 3725 50  0001 C CNN
F 1 "GND" V 6175 3750 50  0000 C CNN
F 2 "" H 6175 3975 50  0000 C CNN
F 3 "" H 6175 3975 50  0000 C CNN
	1    6175 3975
	-1   0    0    1   
$EndComp
$Comp
L pspice:CAP C4
U 1 1 5E9714CF
P 6175 4300
F 0 "C4" H 6200 4400 50  0000 L CNN
F 1 "10nF" H 6250 4175 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 6175 4300 50  0001 C CNN
F 3 "~" H 6175 4300 50  0001 C CNN
	1    6175 4300
	-1   0    0    1   
$EndComp
Connection ~ 6175 4550
Wire Wire Line
	6175 4550 6350 4550
Wire Wire Line
	6675 5025 6675 4925
Wire Wire Line
	6675 4550 6600 4550
Connection ~ 6675 4925
Wire Wire Line
	6675 4925 6675 4550
Connection ~ 6600 4550
$Comp
L power:GND #PWR0108
U 1 1 5E9CCBC5
P 8625 2400
F 0 "#PWR0108" H 8625 2150 50  0001 C CNN
F 1 "GND" V 8625 2200 50  0000 C CNN
F 2 "" H 8625 2400 50  0000 C CNN
F 3 "" H 8625 2400 50  0000 C CNN
	1    8625 2400
	0    1    1    0   
$EndComp
Wire Wire Line
	8775 2400 8625 2400
Text GLabel 10200 5525 2    50   Input ~ 10
SEL
Text GLabel 10200 5625 2    50   Input ~ 10
NOTSEL
Wire Wire Line
	5800 3975 5800 4550
$Comp
L Connector_Generic:Conn_01x04 J8
U 1 1 5E9FF565
P 975 6125
F 0 "J8" H 1055 6117 50  0000 L CNN
F 1 "Conn_01x04" H 1055 6026 50  0000 L CNN
F 2 "Connector_JST:JST_PH_B4B-PH-SM4-TB_1x04-1MP_P2.00mm_Vertical" H 975 6125 50  0001 C CNN
F 3 "~" H 975 6125 50  0001 C CNN
	1    975  6125
	0    -1   -1   0   
$EndComp
$Comp
L dk_Transistors-FETs-MOSFETs-Single:BS170 Q1
U 1 1 5EA00C5C
P 10500 2900
F 0 "Q1" H 10608 2953 60  0000 L CNN
F 1 "BS170" H 10608 2847 60  0000 L CNN
F 2 "digikey-footprints:SOT-23-3" H 10700 3100 60  0001 L CNN
F 3 "https://www.onsemi.com/pub/Collateral/BS170-D.PDF" H 10700 3200 60  0001 L CNN
F 4 "BS170-ND" H 10700 3300 60  0001 L CNN "Digi-Key_PN"
F 5 "BS170" H 10700 3400 60  0001 L CNN "MPN"
F 6 "Discrete Semiconductor Products" H 10700 3500 60  0001 L CNN "Category"
F 7 "Transistors - FETs, MOSFETs - Single" H 10700 3600 60  0001 L CNN "Family"
F 8 "https://www.onsemi.com/pub/Collateral/BS170-D.PDF" H 10700 3700 60  0001 L CNN "DK_Datasheet_Link"
F 9 "/product-detail/en/on-semiconductor/BS170/BS170-ND/244280" H 10700 3800 60  0001 L CNN "DK_Detail_Page"
F 10 "MOSFET N-CH 60V 500MA TO-92" H 10700 3900 60  0001 L CNN "Description"
F 11 "ON Semiconductor" H 10700 4000 60  0001 L CNN "Manufacturer"
F 12 "Active" H 10700 4100 60  0001 L CNN "Status"
	1    10500 2900
	1    0    0    -1  
$EndComp
$Comp
L Device:R R3
U 1 1 5EA02B50
P 10500 2375
F 0 "R3" H 10300 2450 50  0000 L CNN
F 1 "10K" V 10500 2300 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 10430 2375 50  0001 C CNN
F 3 "~" H 10500 2375 50  0001 C CNN
	1    10500 2375
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0109
U 1 1 5EA033C4
P 10500 2125
F 0 "#PWR0109" H 10500 1975 50  0001 C CNN
F 1 "+3.3V" V 10500 2350 50  0000 C CNN
F 2 "" H 10500 2125 50  0001 C CNN
F 3 "" H 10500 2125 50  0001 C CNN
	1    10500 2125
	1    0    0    -1  
$EndComp
Wire Wire Line
	10500 2125 10500 2225
Wire Wire Line
	10500 2525 10500 2625
$Comp
L power:GND #PWR0110
U 1 1 5EA16E66
P 10500 3225
F 0 "#PWR0110" H 10500 2975 50  0001 C CNN
F 1 "GND" H 10500 3075 50  0000 C CNN
F 2 "" H 10500 3225 50  0000 C CNN
F 3 "" H 10500 3225 50  0000 C CNN
	1    10500 3225
	-1   0    0    -1  
$EndComp
Wire Wire Line
	10500 3100 10500 3225
Text GLabel 10075 3000 0    50   Input ~ 10
SEL
Wire Wire Line
	10075 3000 10200 3000
Text GLabel 10675 2625 2    50   Input ~ 10
NOTSEL
Wire Wire Line
	10675 2625 10500 2625
Connection ~ 10500 2625
Wire Wire Line
	10500 2625 10500 2700
$Comp
L 647676-2:647676-2 J6
U 1 1 5EA8B371
P 1000 4575
F 0 "J6" H 893 4308 50  0000 C CNN
F 1 "647676-2" H 893 4399 50  0000 C CNN
F 2 "TE_647676-2" H 1000 4575 50  0001 L BNN
F 3 "" H 1000 4575 50  0001 L BNN
F 4 "3.96 mm[.156 in]" H 1000 4575 50  0001 L BNN "Field4"
F 5 "https://www.te.com/usa-en/product-647676-2.html?te_bu=Cor&te_type=disp&te_campaign=seda_glo_cor-seda-global-disp-prtnr-fy19-seda-model-bom-cta_sma-317_1&elqCampaignId=32493" H 1000 4575 50  0001 L BNN "Field5"
F 6 "Header" H 1000 4575 50  0001 L BNN "Field6"
F 7 "2" H 1000 4575 50  0001 L BNN "Field7"
F 8 "647676-2" H 1000 4575 50  0001 L BNN "Field8"
	1    1000 4575
	-1   0    0    1   
$EndComp
$Comp
L power:+12V #PWR0113
U 1 1 5EA8C2C5
P 1650 4575
F 0 "#PWR0113" H 1650 4425 50  0001 C CNN
F 1 "+12V" V 1650 4700 50  0000 L CNN
F 2 "" H 1650 4575 50  0001 C CNN
F 3 "" H 1650 4575 50  0001 C CNN
	1    1650 4575
	0    1    1    0   
$EndComp
Wire Wire Line
	1650 4575 1400 4575
$Comp
L power:GND #PWR0116
U 1 1 5EA9745A
P 1675 4675
F 0 "#PWR0116" H 1675 4425 50  0001 C CNN
F 1 "GND" V 1675 4475 50  0000 C CNN
F 2 "" H 1675 4675 50  0000 C CNN
F 3 "" H 1675 4675 50  0000 C CNN
	1    1675 4675
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1400 4675 1675 4675
$Comp
L Regulator_Linear:NCP1117-3.3_SOT223 U2
U 1 1 5EAB689A
P 10150 1250
F 0 "U2" H 10150 1492 50  0000 C CNN
F 1 "NCP1117-3.3_SOT223" H 10150 1401 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-223-3_TabPin2" H 10150 1450 50  0001 C CNN
F 3 "http://www.onsemi.com/pub_link/Collateral/NCP1117-D.PDF" H 10250 1000 50  0001 C CNN
	1    10150 1250
	1    0    0    -1  
$EndComp
$Comp
L Device:CP C1
U 1 1 5EAB8B6F
P 9725 1400
F 0 "C1" H 9607 1446 50  0000 R CNN
F 1 "10uf" H 9607 1355 50  0000 R CNN
F 2 "digikey-footprints:T491-3.5x2.8" H 9763 1250 50  0001 C CNN
F 3 "~" H 9725 1400 50  0001 C CNN
	1    9725 1400
	-1   0    0    -1  
$EndComp
$Comp
L Device:CP C2
U 1 1 5EAC3440
P 10650 1400
F 0 "C2" H 10532 1446 50  0000 R CNN
F 1 "100uf" H 10532 1355 50  0000 R CNN
F 2 "digikey-footprints:T491-3.5x2.8" H 10688 1250 50  0001 C CNN
F 3 "~" H 10650 1400 50  0001 C CNN
	1    10650 1400
	-1   0    0    -1  
$EndComp
Wire Wire Line
	9625 1250 9725 1250
Connection ~ 9725 1250
Wire Wire Line
	9725 1250 9850 1250
Wire Wire Line
	9725 1550 10150 1550
Connection ~ 10150 1550
Wire Wire Line
	10450 1250 10650 1250
$Comp
L power:GND #PWR0117
U 1 1 5EB2AAB9
P 10150 1650
F 0 "#PWR0117" H 10150 1400 50  0001 C CNN
F 1 "GND" H 10150 1500 50  0000 C CNN
F 2 "" H 10150 1650 50  0000 C CNN
F 3 "" H 10150 1650 50  0000 C CNN
	1    10150 1650
	-1   0    0    -1  
$EndComp
Wire Wire Line
	10150 1650 10150 1550
$Comp
L power:+3.3V #PWR0118
U 1 1 5EB3602B
P 10775 1250
F 0 "#PWR0118" H 10775 1100 50  0001 C CNN
F 1 "+3.3V" V 10775 1475 50  0000 C CNN
F 2 "" H 10775 1250 50  0001 C CNN
F 3 "" H 10775 1250 50  0001 C CNN
	1    10775 1250
	0    1    1    0   
$EndComp
Wire Wire Line
	10775 1250 10650 1250
Wire Wire Line
	10150 1550 10650 1550
Connection ~ 10650 1250
$Comp
L power:+12V #PWR0119
U 1 1 5E68A307
P 875 6475
F 0 "#PWR0119" H 875 6325 50  0001 C CNN
F 1 "+12V" V 875 6600 50  0000 L CNN
F 2 "" H 875 6475 50  0001 C CNN
F 3 "" H 875 6475 50  0001 C CNN
	1    875  6475
	1    0    0    1   
$EndComp
$Comp
L power:GND #PWR0121
U 1 1 5E68A90A
P 975 6475
F 0 "#PWR0121" H 975 6225 50  0001 C CNN
F 1 "GND" V 975 6275 50  0000 C CNN
F 2 "" H 975 6475 50  0000 C CNN
F 3 "" H 975 6475 50  0000 C CNN
	1    975  6475
	1    0    0    -1  
$EndComp
Wire Wire Line
	875  6475 875  6325
Wire Wire Line
	975  6475 975  6325
Text GLabel 1075 6525 3    50   Output ~ 10
LASER1
Text GLabel 1175 6525 3    50   Output ~ 10
LASER2
Wire Wire Line
	1075 6525 1075 6325
Wire Wire Line
	1175 6325 1175 6525
$Comp
L Connector_Generic:Conn_01x05 J9
U 1 1 5E6C2D82
P 2625 6175
F 0 "J9" H 2705 6217 50  0000 L CNN
F 1 "Conn_01x05" H 2705 6126 50  0000 L CNN
F 2 "Connector_JST:JST_PH_B5B-PH-SM4-TB_1x05-1MP_P2.00mm_Vertical" H 2625 6175 50  0001 C CNN
F 3 "~" H 2625 6175 50  0001 C CNN
	1    2625 6175
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR0126
U 1 1 5E7376F4
P 2250 5975
F 0 "#PWR0126" H 2250 5825 50  0001 C CNN
F 1 "+12V" V 2250 6100 50  0000 L CNN
F 2 "" H 2250 5975 50  0001 C CNN
F 3 "" H 2250 5975 50  0001 C CNN
	1    2250 5975
	0    -1   1    0   
$EndComp
$Comp
L power:GND #PWR0127
U 1 1 5E737EC1
P 2250 6075
F 0 "#PWR0127" H 2250 5825 50  0001 C CNN
F 1 "GND" V 2250 5875 50  0000 C CNN
F 2 "" H 2250 6075 50  0000 C CNN
F 3 "" H 2250 6075 50  0000 C CNN
	1    2250 6075
	0    1    1    0   
$EndComp
Wire Wire Line
	2425 5975 2250 5975
Wire Wire Line
	2250 6075 2425 6075
Text Notes 850  4225 0    50   ~ 10
12v power connector
$Comp
L Connector_Generic:Conn_01x06 J7
U 1 1 5E7908A2
P 2825 4525
F 0 "J7" V 2789 4137 50  0000 R CNN
F 1 "Conn_01x06" V 2698 4137 50  0000 R CNN
F 2 "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" H 2825 4525 50  0001 C CNN
F 3 "~" H 2825 4525 50  0001 C CNN
	1    2825 4525
	0    -1   -1   0   
$EndComp
Text Notes 2500 4225 0    50   ~ 10
Temporary power connector\n(for use with external regulator)\n
$Comp
L power:+12V #PWR0128
U 1 1 5E79154E
P 2625 4850
F 0 "#PWR0128" H 2625 4700 50  0001 C CNN
F 1 "+12V" V 2625 4975 50  0000 L CNN
F 2 "" H 2625 4850 50  0001 C CNN
F 3 "" H 2625 4850 50  0001 C CNN
	1    2625 4850
	-1   0    0    1   
$EndComp
$Comp
L power:+12V #PWR0129
U 1 1 5E791AB6
P 2725 4850
F 0 "#PWR0129" H 2725 4700 50  0001 C CNN
F 1 "+12V" V 2725 4975 50  0000 L CNN
F 2 "" H 2725 4850 50  0001 C CNN
F 3 "" H 2725 4850 50  0001 C CNN
	1    2725 4850
	-1   0    0    1   
$EndComp
Wire Wire Line
	2625 4850 2625 4725
Wire Wire Line
	2725 4850 2725 4725
$Comp
L power:GND #PWR0132
U 1 1 5E7AA41C
P 3125 4850
F 0 "#PWR0132" H 3125 4600 50  0001 C CNN
F 1 "GND" V 3125 4650 50  0000 C CNN
F 2 "" H 3125 4850 50  0000 C CNN
F 3 "" H 3125 4850 50  0000 C CNN
	1    3125 4850
	1    0    0    -1  
$EndComp
Wire Wire Line
	3125 4850 3125 4725
$Comp
L power:GND #PWR0133
U 1 1 5E7B6F3E
P 3025 4850
F 0 "#PWR0133" H 3025 4600 50  0001 C CNN
F 1 "GND" V 3025 4650 50  0000 C CNN
F 2 "" H 3025 4850 50  0000 C CNN
F 3 "" H 3025 4850 50  0000 C CNN
	1    3025 4850
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0134
U 1 1 5E7B70B9
P 2925 4850
F 0 "#PWR0134" H 2925 4600 50  0001 C CNN
F 1 "GND" V 2925 4650 50  0000 C CNN
F 2 "" H 2925 4850 50  0000 C CNN
F 3 "" H 2925 4850 50  0000 C CNN
	1    2925 4850
	1    0    0    -1  
$EndComp
Wire Wire Line
	2925 4850 2925 4725
Wire Wire Line
	3025 4725 3025 4850
$Comp
L power:+5V #PWR0135
U 1 1 5E7CFFA4
P 2175 1500
F 0 "#PWR0135" H 2175 1350 50  0001 C CNN
F 1 "+5V" V 2190 1628 50  0000 L CNN
F 2 "" H 2175 1500 50  0001 C CNN
F 3 "" H 2175 1500 50  0001 C CNN
	1    2175 1500
	0    1    1    0   
$EndComp
Wire Wire Line
	2175 1500 2075 1500
Connection ~ 2075 1500
$Comp
L power:+5V #PWR0136
U 1 1 5E7DD466
P 2825 4850
F 0 "#PWR0136" H 2825 4700 50  0001 C CNN
F 1 "+5V" H 2840 5023 50  0000 C CNN
F 2 "" H 2825 4850 50  0001 C CNN
F 3 "" H 2825 4850 50  0001 C CNN
	1    2825 4850
	-1   0    0    1   
$EndComp
Wire Wire Line
	2825 4850 2825 4725
$Comp
L power:+5V #PWR0137
U 1 1 5E7EB1A2
P 9625 1250
F 0 "#PWR0137" H 9625 1100 50  0001 C CNN
F 1 "+5V" V 9640 1378 50  0000 L CNN
F 2 "" H 9625 1250 50  0001 C CNN
F 3 "" H 9625 1250 50  0001 C CNN
	1    9625 1250
	0    -1   -1   0   
$EndComp
NoConn ~ 1875 3200
NoConn ~ 1375 2500
NoConn ~ 1375 2300
NoConn ~ 1875 1800
NoConn ~ 1875 1900
$Comp
L Connector_Generic:Conn_02x15_Top_Bottom J3
U 1 1 5E931A31
P 7225 1700
F 0 "J3" H 7275 2617 50  0000 C CNN
F 1 "Conn_02x15_Top_Bottom" H 7275 2526 50  0000 C CNN
F 2 "digikey-footprints:117342485" H 7225 1700 50  0001 C CNN
F 3 "~" H 7225 1700 50  0001 C CNN
	1    7225 1700
	1    0    0    -1  
$EndComp
NoConn ~ 7525 1000
NoConn ~ 7525 1100
NoConn ~ 7525 1200
NoConn ~ 7525 2000
NoConn ~ 7525 2100
NoConn ~ 7525 2200
NoConn ~ 7525 2300
NoConn ~ 7525 2400
NoConn ~ 5775 1000
NoConn ~ 5775 1100
NoConn ~ 5775 1200
NoConn ~ 5775 2000
NoConn ~ 5775 2100
NoConn ~ 5775 2200
NoConn ~ 5775 2300
NoConn ~ 5775 2400
NoConn ~ 3900 900 
NoConn ~ 3900 1000
NoConn ~ 3900 1100
NoConn ~ 3900 1900
NoConn ~ 3900 2000
NoConn ~ 3900 2100
NoConn ~ 3900 2200
NoConn ~ 3900 2300
NoConn ~ 7525 1300
NoConn ~ 7525 1900
Wire Wire Line
	5275 1800 5150 1800
Wire Wire Line
	5150 1700 5275 1700
Wire Wire Line
	5275 1600 5200 1600
Wire Wire Line
	5275 1500 5150 1500
Wire Wire Line
	5275 1400 5150 1400
Wire Wire Line
	5275 1300 5200 1300
Wire Wire Line
	5275 1900 5200 1900
$Comp
L Connector_Generic:Conn_02x15_Top_Bottom J2
U 1 1 5E9F7DC7
P 5475 1700
F 0 "J2" H 5525 2617 50  0000 C CNN
F 1 "Conn_02x15_Top_Bottom" H 5525 2526 50  0000 C CNN
F 2 "digikey-footprints:117342485" H 5475 1700 50  0001 C CNN
F 3 "~" H 5475 1700 50  0001 C CNN
	1    5475 1700
	1    0    0    -1  
$EndComp
NoConn ~ 5775 1300
NoConn ~ 5775 1900
NoConn ~ 3900 1200
NoConn ~ 3900 1800
NoConn ~ 7525 1600
NoConn ~ 7525 1400
NoConn ~ 7525 1500
Text GLabel 7575 1800 2    50   Input ~ 10
CAMERA1CP
Text GLabel 7575 1700 2    50   Input ~ 10
CAMERA1CN
Wire Wire Line
	7575 1700 7525 1700
Wire Wire Line
	7575 1800 7525 1800
Text GLabel 5825 1800 2    50   Input ~ 10
CAMERA0CP
Text GLabel 5825 1700 2    50   Input ~ 10
CAMERA0CN
Wire Wire Line
	5825 1800 5775 1800
Wire Wire Line
	5775 1700 5825 1700
NoConn ~ 5775 1600
NoConn ~ 5775 1500
NoConn ~ 5775 1400
Wire Wire Line
	3400 1700 3275 1700
Wire Wire Line
	3275 1600 3400 1600
Wire Wire Line
	3400 1500 3325 1500
$Comp
L Connector_Generic:Conn_02x15_Top_Bottom J1
U 1 1 5EAE442F
P 3600 1600
F 0 "J1" H 3650 2517 50  0000 C CNN
F 1 "Conn_02x15_Top_Bottom" H 3650 2426 50  0000 C CNN
F 2 "digikey-footprints:117342485" H 3600 1600 50  0001 C CNN
F 3 "~" H 3600 1600 50  0001 C CNN
	1    3600 1600
	1    0    0    -1  
$EndComp
Text GLabel 3950 1600 2    50   Input ~ 10
CAMERACN
Text GLabel 3950 1700 2    50   Input ~ 10
CAMERACP
Wire Wire Line
	3950 1600 3900 1600
Wire Wire Line
	3900 1700 3950 1700
NoConn ~ 3900 1500
NoConn ~ 3900 1400
NoConn ~ 3900 1300
Wire Wire Line
	5600 5625 5800 5625
Wire Wire Line
	6100 5050 6100 5325
Connection ~ 6100 5325
Wire Wire Line
	6100 5325 6675 5325
Wire Wire Line
	5600 5525 5900 5525
Wire Wire Line
	6000 5050 6000 5425
Connection ~ 6000 5425
Wire Wire Line
	5600 5425 6000 5425
Wire Wire Line
	5900 5050 5900 5525
Connection ~ 5900 5525
Wire Wire Line
	5900 5525 6675 5525
Wire Wire Line
	5600 5325 6100 5325
Wire Wire Line
	5800 5050 5800 5625
Connection ~ 5800 5625
Wire Wire Line
	5800 5625 6675 5625
$Comp
L power:GND #PWR0130
U 1 1 5E6B1D9F
P 3675 3000
F 0 "#PWR0130" H 3675 2750 50  0001 C CNN
F 1 "GND" V 3675 2775 50  0000 C CNN
F 2 "" H 3675 3000 50  0000 C CNN
F 3 "" H 3675 3000 50  0000 C CNN
	1    3675 3000
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0131
U 1 1 5E6BDA82
P 3675 3500
F 0 "#PWR0131" H 3675 3250 50  0001 C CNN
F 1 "GND" V 3675 3275 50  0000 C CNN
F 2 "" H 3675 3500 50  0000 C CNN
F 3 "" H 3675 3500 50  0000 C CNN
	1    3675 3500
	0    1    1    0   
$EndComp
$EndSCHEMATC
