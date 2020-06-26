EESchema Schematic File Version 4
LIBS:Top Board-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 2
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
L power:GND #PWR?
U 1 1 5E7B13D3
P 7050 5850
AR Path="/5E7B13D3" Ref="#PWR?"  Part="1" 
AR Path="/5E7671EB/5E7B13D3" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 7050 5600 50  0001 C CNN
F 1 "GND" V 7050 5625 50  0000 C CNN
F 2 "" H 7050 5850 50  0000 C CNN
F 3 "" H 7050 5850 50  0000 C CNN
	1    7050 5850
	1    0    0    -1  
$EndComp
Wire Wire Line
	7050 5850 7050 5775
Text GLabel 5375 4325 0    50   Input ~ 10
CAMERASDA
Text GLabel 5375 4425 0    50   Input ~ 10
CAMERASCL
$Comp
L dk_Logic-Signal-Switches-Multiplexers-Decoders:FSA642 U?
U 1 1 5E7B1443
P 10000 4675
AR Path="/5E7B1443" Ref="U?"  Part="1" 
AR Path="/5E7671EB/5E7B1443" Ref="U?"  Part="1" 
F 0 "U?" H 10228 4578 60  0000 L CNN
F 1 "FSA642" H 10228 4472 60  0000 L CNN
F 2 "digikey-footprints:QFN50P400X400X60-25N" H 10200 4975 60  0001 L CNN
F 3 "http://www.ti.com/general/docs/suppproductinfo.tsp?distId=10&gotoUrl=http%3A%2F%2Fwww.ti.com%2Flit%2Fgpn%2Ftca9548a" H 10200 5075 60  0001 L CNN
F 4 "FSA642" H 10200 5175 60  0001 L CNN "MPN"
F 5 "Integrated Circuits (ICs)" H 10200 5275 60  0001 L CNN "Category"
F 6 "Logic - Signal Switches, Multiplexers, Decoders" H 10200 5375 60  0001 L CNN "Family"
F 7 "Low power, three port high speed MIPI switch" H 10200 5475 60  0001 L CNN "Description"
F 8 "Fairchild" H 10200 5575 60  0001 L CNN "Manufacturer"
F 9 "Active" H 10200 5675 60  0001 L CNN "Status"
	1    10000 4675
	1    0    0    -1  
$EndComp
$Comp
L dk_Logic-Signal-Switches-Multiplexers-Decoders:FSA642 U?
U 1 1 5E7B144F
P 8350 4675
AR Path="/5E7B144F" Ref="U?"  Part="1" 
AR Path="/5E7671EB/5E7B144F" Ref="U?"  Part="1" 
F 0 "U?" H 8578 4578 60  0000 L CNN
F 1 "FSA642" H 8578 4472 60  0000 L CNN
F 2 "digikey-footprints:QFN50P400X400X60-25N" H 8550 4975 60  0001 L CNN
F 3 "http://www.ti.com/general/docs/suppproductinfo.tsp?distId=10&gotoUrl=http%3A%2F%2Fwww.ti.com%2Flit%2Fgpn%2Ftca9548a" H 8550 5075 60  0001 L CNN
F 4 "FSA642" H 8550 5175 60  0001 L CNN "MPN"
F 5 "Integrated Circuits (ICs)" H 8550 5275 60  0001 L CNN "Category"
F 6 "Logic - Signal Switches, Multiplexers, Decoders" H 8550 5375 60  0001 L CNN "Family"
F 7 "Low power, three port high speed MIPI switch" H 8550 5475 60  0001 L CNN "Description"
F 8 "Fairchild" H 8550 5575 60  0001 L CNN "Manufacturer"
F 9 "Active" H 8550 5675 60  0001 L CNN "Status"
	1    8350 4675
	1    0    0    -1  
$EndComp
NoConn ~ 9700 5875
NoConn ~ 8050 5875
NoConn ~ 8050 4375
NoConn ~ 9700 4375
$Comp
L power:+3.3V #PWR?
U 1 1 5E7B1459
P 10150 3475
AR Path="/5E7B1459" Ref="#PWR?"  Part="1" 
AR Path="/5E7671EB/5E7B1459" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 10150 3325 50  0001 C CNN
F 1 "+3.3V" V 10150 3700 50  0000 C CNN
F 2 "" H 10150 3475 50  0001 C CNN
F 3 "" H 10150 3475 50  0001 C CNN
	1    10150 3475
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR?
U 1 1 5E7B145F
P 8500 3475
AR Path="/5E7B145F" Ref="#PWR?"  Part="1" 
AR Path="/5E7671EB/5E7B145F" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 8500 3325 50  0001 C CNN
F 1 "+3.3V" V 8500 3700 50  0000 C CNN
F 2 "" H 8500 3475 50  0001 C CNN
F 3 "" H 8500 3475 50  0001 C CNN
	1    8500 3475
	1    0    0    -1  
$EndComp
Wire Wire Line
	10150 3575 10150 3475
Wire Wire Line
	8500 3575 8500 3475
$Comp
L power:GND #PWR?
U 1 1 5E7B1467
P 8500 6175
AR Path="/5E7B1467" Ref="#PWR?"  Part="1" 
AR Path="/5E7671EB/5E7B1467" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 8500 5925 50  0001 C CNN
F 1 "GND" H 8500 6025 50  0000 C CNN
F 2 "" H 8500 6175 50  0000 C CNN
F 3 "" H 8500 6175 50  0000 C CNN
	1    8500 6175
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E7B146D
P 10150 6175
AR Path="/5E7B146D" Ref="#PWR?"  Part="1" 
AR Path="/5E7671EB/5E7B146D" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 10150 5925 50  0001 C CNN
F 1 "GND" H 10150 6025 50  0000 C CNN
F 2 "" H 10150 6175 50  0000 C CNN
F 3 "" H 10150 6175 50  0000 C CNN
	1    10150 6175
	1    0    0    -1  
$EndComp
Wire Wire Line
	10150 6175 10150 6075
Wire Wire Line
	8500 6175 8500 6075
Text GLabel 7900 4575 0    50   Input ~ 10
SEL
Text GLabel 9575 4575 0    50   Input ~ 10
SEL
Wire Wire Line
	7900 4575 8050 4575
Wire Wire Line
	9575 4575 9700 4575
Text GLabel 7900 4475 0    50   Input ~ 10
OE1
Text GLabel 9575 4475 0    50   Input ~ 10
OE2
Wire Wire Line
	9575 4475 9700 4475
Wire Wire Line
	7900 4475 8050 4475
$Comp
L dk_Logic-Signal-Switches-Multiplexers-Decoders:LTC4314 U?
U 1 1 5E7B1483
P 6750 4925
AR Path="/5E7B1483" Ref="U?"  Part="1" 
AR Path="/5E7671EB/5E7B1483" Ref="U?"  Part="1" 
F 0 "U?" H 7178 5103 60  0000 L CNN
F 1 "LTC4314" H 7178 4997 60  0000 L CNN
F 2 "digikey-footprints:SOP65P777X199-20N" H 7200 5225 60  0001 L CNN
F 3 "http://www.ti.com/general/docs/suppproductinfo.tsp?distId=10&gotoUrl=http%3A%2F%2Fwww.ti.com%2Flit%2Fgpn%2Ftca9548a" H 7200 5325 60  0001 L CNN
F 4 "LTC4314" H 7200 5425 60  0001 L CNN "MPN"
F 5 "Integrated Circuits (ICs)" H 7200 5525 60  0001 L CNN "Category"
F 6 "Logic - Signal Switches, Multiplexers, Decoders" H 7200 5625 60  0001 L CNN "Family"
F 7 "Pin Selectable, 4 Channel, 2 wire multiplexer" H 7200 5725 60  0001 L CNN "Description"
F 8 "Linear Technology" H 7200 5825 60  0001 L CNN "Manufacturer"
F 9 "Active" H 7200 5925 60  0001 L CNN "Status"
	1    6750 4925
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR?
U 1 1 5E7B1489
P 7100 3525
AR Path="/5E7B1489" Ref="#PWR?"  Part="1" 
AR Path="/5E7671EB/5E7B1489" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 7100 3375 50  0001 C CNN
F 1 "+3.3V" V 7100 3750 50  0000 C CNN
F 2 "" H 7100 3525 50  0001 C CNN
F 3 "" H 7100 3525 50  0001 C CNN
	1    7100 3525
	1    0    0    -1  
$EndComp
Wire Wire Line
	7000 3825 7100 3825
Connection ~ 7100 3825
$Comp
L Device:R R?
U 1 1 5E7B1491
P 6050 3800
AR Path="/5E7B1491" Ref="R?"  Part="1" 
AR Path="/5E7671EB/5E7B1491" Ref="R?"  Part="1" 
F 0 "R?" H 5925 3850 50  0000 L CNN
F 1 "10K" V 6050 3725 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5980 3800 50  0001 C CNN
F 3 "~" H 6050 3800 50  0001 C CNN
	1    6050 3800
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E7B1497
P 6225 3800
AR Path="/5E7B1497" Ref="R?"  Part="1" 
AR Path="/5E7671EB/5E7B1497" Ref="R?"  Part="1" 
F 0 "R?" H 6100 3850 50  0000 L CNN
F 1 "10K" V 6225 3725 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 6155 3800 50  0001 C CNN
F 3 "~" H 6225 3800 50  0001 C CNN
	1    6225 3800
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E7B149D
P 6400 3800
AR Path="/5E7B149D" Ref="R?"  Part="1" 
AR Path="/5E7671EB/5E7B149D" Ref="R?"  Part="1" 
F 0 "R?" H 6275 3850 50  0000 L CNN
F 1 "10K" V 6400 3725 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 6330 3800 50  0001 C CNN
F 3 "~" H 6400 3800 50  0001 C CNN
	1    6400 3800
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E7B14A3
P 5875 3800
AR Path="/5E7B14A3" Ref="R?"  Part="1" 
AR Path="/5E7671EB/5E7B14A3" Ref="R?"  Part="1" 
F 0 "R?" H 5725 3850 50  0000 L CNN
F 1 "10K" V 5875 3725 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5805 3800 50  0001 C CNN
F 3 "~" H 5875 3800 50  0001 C CNN
	1    5875 3800
	1    0    0    -1  
$EndComp
Text GLabel 5375 4225 0    50   Input ~ 10
CAMERA0SDA
Text GLabel 5375 4125 0    50   Input ~ 10
CAMERA0SCL
Wire Wire Line
	5375 4125 6400 4125
Wire Wire Line
	6400 3950 6400 4125
Connection ~ 6400 4125
Wire Wire Line
	6400 4125 6450 4125
Wire Wire Line
	7100 3525 7100 3650
Wire Wire Line
	5375 4425 5875 4425
Wire Wire Line
	5375 4325 6050 4325
Wire Wire Line
	5375 4225 6225 4225
Wire Wire Line
	5875 3650 6050 3650
Connection ~ 7100 3650
Wire Wire Line
	7100 3650 7100 3825
Connection ~ 6050 3650
Wire Wire Line
	6050 3650 6225 3650
Connection ~ 6225 3650
Wire Wire Line
	6225 3650 6400 3650
Connection ~ 6400 3650
Wire Wire Line
	6400 3650 6475 3650
Wire Wire Line
	6225 3950 6225 4225
Connection ~ 6225 4225
Wire Wire Line
	6225 4225 6450 4225
Wire Wire Line
	6050 3950 6050 4325
Connection ~ 6050 4325
Wire Wire Line
	6050 4325 6450 4325
Wire Wire Line
	5875 3950 5875 4425
Connection ~ 5875 4425
Wire Wire Line
	5875 4425 6450 4425
Text GLabel 5725 5025 0    50   Input ~ 10
ENABLE1
Text GLabel 5725 4925 0    50   Input ~ 10
ENABLE2
Text GLabel 5725 4825 0    50   Input ~ 10
ENABLE3
Text GLabel 5725 4725 0    50   Input ~ 10
ENABLE4
Wire Wire Line
	6450 4725 5725 4725
Wire Wire Line
	6450 4825 5725 4825
Wire Wire Line
	6450 4925 5725 4925
Wire Wire Line
	6450 5025 5725 5025
$Comp
L Device:R R?
U 1 1 5E7B14D5
P 5525 3800
AR Path="/5E7B14D5" Ref="R?"  Part="1" 
AR Path="/5E7671EB/5E7B14D5" Ref="R?"  Part="1" 
F 0 "R?" H 5375 3850 50  0000 L CNN
F 1 "10K" V 5525 3725 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5455 3800 50  0001 C CNN
F 3 "~" H 5525 3800 50  0001 C CNN
	1    5525 3800
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E7B14DB
P 5700 3800
AR Path="/5E7B14DB" Ref="R?"  Part="1" 
AR Path="/5E7671EB/5E7B14DB" Ref="R?"  Part="1" 
F 0 "R?" H 5550 3850 50  0000 L CNN
F 1 "10K" V 5700 3725 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5630 3800 50  0001 C CNN
F 3 "~" H 5700 3800 50  0001 C CNN
	1    5700 3800
	1    0    0    -1  
$EndComp
Wire Wire Line
	5875 3650 5700 3650
Connection ~ 5875 3650
Connection ~ 5700 3650
Wire Wire Line
	5700 3650 5525 3650
Text GLabel 5375 4625 0    50   Input ~ 10
CAMERA1SDA
Text GLabel 5375 4525 0    50   Input ~ 10
CAMERA1SCL
Wire Wire Line
	5375 4525 5700 4525
Wire Wire Line
	5375 4625 5525 4625
Wire Wire Line
	5700 3950 5700 4525
Connection ~ 5700 4525
Wire Wire Line
	5700 4525 6450 4525
Wire Wire Line
	5525 3950 5525 4625
Connection ~ 5525 4625
Wire Wire Line
	5525 4625 6450 4625
Wire Wire Line
	6450 4025 6300 4025
Wire Wire Line
	6300 4025 6300 5625
Wire Wire Line
	6300 5625 6450 5625
$Comp
L power:+3.3V #PWR?
U 1 1 5E7B14F2
P 6250 6200
AR Path="/5E7B14F2" Ref="#PWR?"  Part="1" 
AR Path="/5E7671EB/5E7B14F2" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 6250 6050 50  0001 C CNN
F 1 "+3.3V" V 6250 6425 50  0000 C CNN
F 2 "" H 6250 6200 50  0001 C CNN
F 3 "" H 6250 6200 50  0001 C CNN
	1    6250 6200
	-1   0    0    1   
$EndComp
Connection ~ 6300 5625
Text GLabel 5375 5225 0    50   Input ~ 10
CAMERA2SDA
Text GLabel 5375 5125 0    50   Input ~ 10
CAMERA2SCL
Wire Wire Line
	6450 5125 5975 5125
Wire Wire Line
	6450 5225 5800 5225
Text GLabel 5375 5525 0    50   Input ~ 10
CAMERA3SDA
Text GLabel 5375 5425 0    50   Input ~ 10
CAMERA3SCL
Wire Wire Line
	6450 5425 5625 5425
$Comp
L Device:R R?
U 1 1 5E7B1500
P 5975 5950
AR Path="/5E7B1500" Ref="R?"  Part="1" 
AR Path="/5E7671EB/5E7B1500" Ref="R?"  Part="1" 
F 0 "R?" H 5850 6000 50  0000 L CNN
F 1 "10K" V 5975 5875 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5905 5950 50  0001 C CNN
F 3 "~" H 5975 5950 50  0001 C CNN
	1    5975 5950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E7B1506
P 5800 5950
AR Path="/5E7B1506" Ref="R?"  Part="1" 
AR Path="/5E7671EB/5E7B1506" Ref="R?"  Part="1" 
F 0 "R?" H 5650 6000 50  0000 L CNN
F 1 "10K" V 5800 5875 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5730 5950 50  0001 C CNN
F 3 "~" H 5800 5950 50  0001 C CNN
	1    5800 5950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E7B150C
P 5450 5950
AR Path="/5E7B150C" Ref="R?"  Part="1" 
AR Path="/5E7671EB/5E7B150C" Ref="R?"  Part="1" 
F 0 "R?" H 5300 6000 50  0000 L CNN
F 1 "10K" V 5450 5875 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5380 5950 50  0001 C CNN
F 3 "~" H 5450 5950 50  0001 C CNN
	1    5450 5950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E7B1512
P 5625 5950
AR Path="/5E7B1512" Ref="R?"  Part="1" 
AR Path="/5E7671EB/5E7B1512" Ref="R?"  Part="1" 
F 0 "R?" H 5475 6000 50  0000 L CNN
F 1 "10K" V 5625 5875 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5555 5950 50  0001 C CNN
F 3 "~" H 5625 5950 50  0001 C CNN
	1    5625 5950
	1    0    0    -1  
$EndComp
Wire Wire Line
	6250 6200 6250 6100
Wire Wire Line
	6250 5625 6300 5625
Wire Wire Line
	6250 6100 6150 6100
Connection ~ 6250 6100
Connection ~ 5625 6100
Wire Wire Line
	5625 6100 5450 6100
Connection ~ 5800 6100
Wire Wire Line
	5800 6100 5625 6100
Connection ~ 5975 6100
Wire Wire Line
	5975 6100 5800 6100
Wire Wire Line
	5450 5800 5450 5525
Connection ~ 5450 5525
Wire Wire Line
	5450 5525 5375 5525
Wire Wire Line
	5625 5800 5625 5425
Connection ~ 5625 5425
Wire Wire Line
	5625 5425 5375 5425
Wire Wire Line
	5800 5800 5800 5225
Connection ~ 5800 5225
Wire Wire Line
	5800 5225 5375 5225
Wire Wire Line
	5975 5800 5975 5125
Connection ~ 5975 5125
Wire Wire Line
	5975 5125 5375 5125
Text GLabel 5375 5325 0    50   Input ~ 10
SWITCHFAULT
Wire Wire Line
	6250 5625 6250 6100
$Comp
L Device:R R?
U 1 1 5E7B1530
P 6150 5950
AR Path="/5E7B1530" Ref="R?"  Part="1" 
AR Path="/5E7671EB/5E7B1530" Ref="R?"  Part="1" 
F 0 "R?" H 6025 6000 50  0000 L CNN
F 1 "10K" V 6150 5875 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 6080 5950 50  0001 C CNN
F 3 "~" H 6150 5950 50  0001 C CNN
	1    6150 5950
	1    0    0    -1  
$EndComp
Connection ~ 6150 6100
Wire Wire Line
	6150 6100 5975 6100
Wire Wire Line
	5450 5525 6450 5525
Wire Wire Line
	5375 5325 6150 5325
Wire Wire Line
	6150 5800 6150 5325
Connection ~ 6150 5325
Wire Wire Line
	6150 5325 6450 5325
$Comp
L pspice:CAP C?
U 1 1 5E7B153D
P 5375 6350
AR Path="/5E7B153D" Ref="C?"  Part="1" 
AR Path="/5E7671EB/5E7B153D" Ref="C?"  Part="1" 
F 0 "C?" H 5400 6450 50  0000 L CNN
F 1 "10nF" H 5425 6225 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 5375 6350 50  0001 C CNN
F 3 "~" H 5375 6350 50  0001 C CNN
	1    5375 6350
	1    0    0    -1  
$EndComp
$Comp
L pspice:CAP C?
U 1 1 5E7B1543
P 5025 6350
AR Path="/5E7B1543" Ref="C?"  Part="1" 
AR Path="/5E7671EB/5E7B1543" Ref="C?"  Part="1" 
F 0 "C?" H 5050 6450 50  0000 L CNN
F 1 "10nF" H 5050 6225 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 5025 6350 50  0001 C CNN
F 3 "~" H 5025 6350 50  0001 C CNN
	1    5025 6350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E7B1549
P 5375 6675
AR Path="/5E7B1549" Ref="#PWR?"  Part="1" 
AR Path="/5E7671EB/5E7B1549" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 5375 6425 50  0001 C CNN
F 1 "GND" V 5375 6450 50  0000 C CNN
F 2 "" H 5375 6675 50  0000 C CNN
F 3 "" H 5375 6675 50  0000 C CNN
	1    5375 6675
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E7B154F
P 5025 6675
AR Path="/5E7B154F" Ref="#PWR?"  Part="1" 
AR Path="/5E7671EB/5E7B154F" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 5025 6425 50  0001 C CNN
F 1 "GND" V 5025 6450 50  0000 C CNN
F 2 "" H 5025 6675 50  0000 C CNN
F 3 "" H 5025 6675 50  0000 C CNN
	1    5025 6675
	1    0    0    -1  
$EndComp
Wire Wire Line
	5450 6100 5375 6100
Connection ~ 5450 6100
Connection ~ 5375 6100
Wire Wire Line
	5375 6100 5025 6100
Wire Wire Line
	5025 6600 5025 6675
Wire Wire Line
	5375 6675 5375 6600
$Comp
L pspice:CAP C?
U 1 1 5E7B155B
P 6825 3400
AR Path="/5E7B155B" Ref="C?"  Part="1" 
AR Path="/5E7671EB/5E7B155B" Ref="C?"  Part="1" 
F 0 "C?" H 6850 3500 50  0000 L CNN
F 1 "10nF" H 6900 3275 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 6825 3400 50  0001 C CNN
F 3 "~" H 6825 3400 50  0001 C CNN
	1    6825 3400
	-1   0    0    1   
$EndComp
Connection ~ 6825 3650
Wire Wire Line
	6825 3650 7100 3650
$Comp
L pspice:CAP C?
U 1 1 5E7B1563
P 6475 3400
AR Path="/5E7B1563" Ref="C?"  Part="1" 
AR Path="/5E7671EB/5E7B1563" Ref="C?"  Part="1" 
F 0 "C?" H 6500 3500 50  0000 L CNN
F 1 "10nF" H 6550 3275 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 6475 3400 50  0001 C CNN
F 3 "~" H 6475 3400 50  0001 C CNN
	1    6475 3400
	-1   0    0    1   
$EndComp
Connection ~ 6475 3650
Wire Wire Line
	6475 3650 6825 3650
$Comp
L pspice:CAP C?
U 1 1 5E7B156B
P 5400 3400
AR Path="/5E7B156B" Ref="C?"  Part="1" 
AR Path="/5E7671EB/5E7B156B" Ref="C?"  Part="1" 
F 0 "C?" H 5425 3500 50  0000 L CNN
F 1 "10nF" H 5475 3275 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 5400 3400 50  0001 C CNN
F 3 "~" H 5400 3400 50  0001 C CNN
	1    5400 3400
	-1   0    0    1   
$EndComp
Wire Wire Line
	5525 3650 5400 3650
Connection ~ 5525 3650
$Comp
L power:GND #PWR?
U 1 1 5E7B1573
P 6825 3075
AR Path="/5E7B1573" Ref="#PWR?"  Part="1" 
AR Path="/5E7671EB/5E7B1573" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 6825 2825 50  0001 C CNN
F 1 "GND" V 6825 2850 50  0000 C CNN
F 2 "" H 6825 3075 50  0000 C CNN
F 3 "" H 6825 3075 50  0000 C CNN
	1    6825 3075
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E7B1579
P 6475 3075
AR Path="/5E7B1579" Ref="#PWR?"  Part="1" 
AR Path="/5E7671EB/5E7B1579" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 6475 2825 50  0001 C CNN
F 1 "GND" V 6475 2850 50  0000 C CNN
F 2 "" H 6475 3075 50  0000 C CNN
F 3 "" H 6475 3075 50  0000 C CNN
	1    6475 3075
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E7B157F
P 5400 3075
AR Path="/5E7B157F" Ref="#PWR?"  Part="1" 
AR Path="/5E7671EB/5E7B157F" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 5400 2825 50  0001 C CNN
F 1 "GND" V 5400 2850 50  0000 C CNN
F 2 "" H 5400 3075 50  0000 C CNN
F 3 "" H 5400 3075 50  0000 C CNN
	1    5400 3075
	-1   0    0    1   
$EndComp
Wire Wire Line
	6825 3150 6825 3075
Wire Wire Line
	6475 3150 6475 3075
Wire Wire Line
	5400 3150 5400 3075
$Comp
L Connector_Generic:Conn_01x15 J?
U 1 1 5E7E1B47
P 1950 1700
F 0 "J?" H 2030 1742 50  0000 L CNN
F 1 "Conn_01x15" H 2030 1651 50  0000 L CNN
F 2 "" H 1950 1700 50  0001 C CNN
F 3 "~" H 1950 1700 50  0001 C CNN
	1    1950 1700
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E7E1B4D
P 1675 1000
F 0 "#PWR?" H 1675 750 50  0001 C CNN
F 1 "GND" V 1675 775 50  0000 C CNN
F 2 "" H 1675 1000 50  0000 C CNN
F 3 "" H 1675 1000 50  0000 C CNN
	1    1675 1000
	0    1    1    0   
$EndComp
Wire Wire Line
	1675 1000 1750 1000
Text GLabel 1625 2300 0    50   Input ~ 10
CAMERASDA
Text GLabel 1625 2200 0    50   Input ~ 10
CAMERASCL
Wire Wire Line
	1750 2200 1625 2200
Wire Wire Line
	1625 2300 1750 2300
$Comp
L power:+3.3V #PWR?
U 1 1 5E7E1B58
P 1625 2400
F 0 "#PWR?" H 1625 2250 50  0001 C CNN
F 1 "+3.3V" V 1625 2625 50  0000 C CNN
F 2 "" H 1625 2400 50  0001 C CNN
F 3 "" H 1625 2400 50  0001 C CNN
	1    1625 2400
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1625 2400 1750 2400
NoConn ~ 1750 2100
Wire Wire Line
	1750 1900 1675 1900
Wire Wire Line
	1675 1900 1675 1600
Connection ~ 1675 1000
Wire Wire Line
	1750 1600 1675 1600
Connection ~ 1675 1600
Wire Wire Line
	1675 1600 1675 1300
Wire Wire Line
	1750 1300 1675 1300
Connection ~ 1675 1300
Wire Wire Line
	1675 1300 1675 1000
Text GLabel 1625 1100 0    50   Input ~ 10
CAMERADN0
Text GLabel 1625 1200 0    50   Input ~ 10
CAMERADP0
Text GLabel 1625 1400 0    50   Input ~ 10
CAMERADN1
Text GLabel 1625 1500 0    50   Input ~ 10
CAMERADP1
Wire Wire Line
	1625 1100 1750 1100
Wire Wire Line
	1750 1200 1625 1200
Wire Wire Line
	1750 1400 1625 1400
Wire Wire Line
	1750 1500 1625 1500
Text GLabel 1625 1700 0    50   Input ~ 10
CAMERACN
Text GLabel 1625 1800 0    50   Input ~ 10
CAMERACP
Wire Wire Line
	1625 1700 1750 1700
Wire Wire Line
	1750 1800 1625 1800
Text GLabel 1625 2000 0    50   Input ~ 10
CAMERAGPIO
Wire Wire Line
	1625 2000 1750 2000
$EndSCHEMATC
