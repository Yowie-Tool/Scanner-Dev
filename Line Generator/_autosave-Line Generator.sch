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
P 3175 4025
F 0 "J1" V 3139 3737 50  0000 R CNN
F 1 "Conn_01x04" V 3048 3737 50  0000 R CNN
F 2 "Connector_JST:JST_PH_B4B-PH-SM4-TB_1x04-1MP_P2.00mm_Vertical" H 3175 4025 50  0001 C CNN
F 3 "~" H 3175 4025 50  0001 C CNN
	1    3175 4025
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Schottky D1
U 1 1 5E540F29
P 4700 3950
F 0 "D1" V 4725 4025 50  0000 L CNN
F 1 "D_Schottky 7V" V 4800 4000 50  0000 L CNN
F 2 "Diode_SMD:D_SOD-323_HandSoldering" H 4700 3950 50  0001 C CNN
F 3 "https://docs.rs-online.com/2159/0900766b812e22b6.pdf" H 4700 3950 50  0001 C CNN
	1    4700 3950
	0    1    1    0   
$EndComp
$Comp
L power:+12V #PWR0101
U 1 1 5E54231E
P 3075 4375
F 0 "#PWR0101" H 3075 4225 50  0001 C CNN
F 1 "+12V" H 3090 4548 50  0000 C CNN
F 2 "" H 3075 4375 50  0001 C CNN
F 3 "" H 3075 4375 50  0001 C CNN
	1    3075 4375
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 5E542B5B
P 3175 4650
F 0 "#PWR0102" H 3175 4400 50  0001 C CNN
F 1 "GND" H 3180 4477 50  0000 C CNN
F 2 "" H 3175 4650 50  0001 C CNN
F 3 "" H 3175 4650 50  0001 C CNN
	1    3175 4650
	1    0    0    -1  
$EndComp
Text GLabel 3275 4375 3    50   Output ~ 0
Laser1
Text GLabel 3375 4375 3    50   Output ~ 0
Laser2
Wire Wire Line
	3075 4375 3075 4225
Wire Wire Line
	3175 4225 3175 4650
Wire Wire Line
	3275 4375 3275 4225
Wire Wire Line
	3375 4225 3375 4375
$Comp
L Device:R R3
U 1 1 5E54A307
P 4825 4600
F 0 "R3" H 4895 4646 50  0000 L CNN
F 1 "4K7" H 4895 4555 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 4755 4600 50  0001 C CNN
F 3 "~" H 4825 4600 50  0001 C CNN
	1    4825 4600
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 5E54B074
P 4450 3950
F 0 "R2" H 4275 4000 50  0000 L CNN
F 1 "100K" H 4200 3900 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 4380 3950 50  0001 C CNN
F 3 "~" H 4450 3950 50  0001 C CNN
	1    4450 3950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5E54EB98
P 4275 5075
F 0 "R1" V 4068 5075 50  0000 C CNN
F 1 "10K" V 4159 5075 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 4205 5075 50  0001 C CNN
F 3 "~" H 4275 5075 50  0001 C CNN
	1    4275 5075
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 5E54F1FD
P 5675 3750
F 0 "R4" H 5605 3704 50  0000 R CNN
F 1 "68R" H 5605 3795 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5605 3750 50  0001 C CNN
F 3 "~" H 5675 3750 50  0001 C CNN
	1    5675 3750
	-1   0    0    1   
$EndComp
Wire Wire Line
	4525 5075 4425 5075
Text GLabel 3950 5075 0    50   Output ~ 0
Laser2
Wire Wire Line
	3950 5075 4125 5075
$Comp
L power:GND #PWR0106
U 1 1 5E55789E
P 5425 5600
F 0 "#PWR0106" H 5425 5350 50  0001 C CNN
F 1 "GND" H 5430 5427 50  0000 C CNN
F 2 "" H 5425 5600 50  0001 C CNN
F 3 "" H 5425 5600 50  0001 C CNN
	1    5425 5600
	1    0    0    -1  
$EndComp
$Comp
L Device:LED_Dual_ACA D2
U 1 1 5E55C00C
P 5850 5000
F 0 "D2" V 5896 4790 50  0000 R CNN
F 1 "LED_Dual_ACA" V 5805 4790 50  0000 R CNN
F 2 "Connector_PinSocket_1.27mm:PinSocket_1x03_P1.27mm_Vertical" H 5850 5000 50  0001 C CNN
F 3 "~" H 5850 5000 50  0001 C CNN
	1    5850 5000
	0    -1   -1   0   
$EndComp
$Comp
L Transistor_FET:BS170F Q1
U 1 1 5E5613DE
P 4725 5075
F 0 "Q1" H 4931 5121 50  0000 L CNN
F 1 "BS170F" H 4931 5030 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 4925 5000 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/BS170F.pdf" H 4725 5075 50  0001 L CNN
	1    4725 5075
	1    0    0    -1  
$EndComp
$Comp
L Device:Q_PNP_Darlington_BEC Q2
U 1 1 5E552935
P 5575 4200
F 0 "Q2" V 5525 3975 50  0000 C CNN
F 1 "BCV46" V 5600 3950 50  0000 C CNN
F 2 "digikey-footprints:SOT-23-3" H 5775 4300 50  0001 C CNN
F 3 "~" H 5575 4200 50  0001 C CNN
	1    5575 4200
	1    0    0    1   
$EndComp
$Comp
L Jumper:SolderJumper_2_Open JP1
U 1 1 5E556D51
P 5150 4475
F 0 "JP1" H 5150 4680 50  0000 C CNN
F 1 "SolderJumper_2_Open" H 5150 4589 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm" H 5150 4475 50  0001 C CNN
F 3 "~" H 5150 4475 50  0001 C CNN
	1    5150 4475
	1    0    0    -1  
$EndComp
$Comp
L Device:R_POT RV1
U 1 1 5E5819FB
P 5000 4200
F 0 "RV1" H 4931 4246 50  0000 R CNN
F 1 "22K" H 4931 4155 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3006P_Horizontal" H 5000 4200 50  0001 C CNN
F 3 "~" H 5000 4200 50  0001 C CNN
	1    5000 4200
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR0103
U 1 1 5E625F82
P 5100 3325
F 0 "#PWR0103" H 5100 3175 50  0001 C CNN
F 1 "+12V" H 5115 3498 50  0000 C CNN
F 2 "" H 5100 3325 50  0001 C CNN
F 3 "" H 5100 3325 50  0001 C CNN
	1    5100 3325
	1    0    0    -1  
$EndComp
Wire Wire Line
	5100 3325 5100 3500
Wire Wire Line
	5675 3900 5675 4000
Wire Wire Line
	5675 3600 5675 3500
Connection ~ 5675 3500
Wire Wire Line
	5675 3500 6025 3500
$Comp
L Device:C C1
U 1 1 5E5844FF
P 5225 3800
F 0 "C1" V 5100 3925 50  0000 C CNN
F 1 "0.1uF" V 5175 3975 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 5263 3650 50  0001 C CNN
F 3 "~" H 5225 3800 50  0001 C CNN
	1    5225 3800
	-1   0    0    1   
$EndComp
Wire Wire Line
	4450 3800 4450 3500
Wire Wire Line
	4450 3500 4700 3500
Connection ~ 5100 3500
Wire Wire Line
	4700 3800 4700 3500
Connection ~ 4700 3500
Wire Wire Line
	4700 3500 5000 3500
Wire Wire Line
	5000 4050 5000 3500
Connection ~ 5000 3500
Wire Wire Line
	5000 3500 5100 3500
Wire Wire Line
	4825 4750 4825 4875
Wire Wire Line
	4825 4450 4825 4350
Wire Wire Line
	4825 4350 5000 4350
Wire Wire Line
	5100 3500 5225 3500
Wire Wire Line
	5150 4200 5225 4200
Wire Wire Line
	5225 3650 5225 3500
Connection ~ 5225 3500
Wire Wire Line
	5225 3500 5675 3500
Wire Wire Line
	5225 3950 5225 4200
Connection ~ 5225 4200
Wire Wire Line
	5225 4200 5300 4200
Wire Wire Line
	5000 4350 5000 4475
Connection ~ 5000 4350
Wire Wire Line
	5300 4475 5300 4200
Connection ~ 5300 4200
Wire Wire Line
	5300 4200 5375 4200
Wire Wire Line
	4825 5275 4825 5450
Wire Wire Line
	5850 5300 5850 5450
Connection ~ 5850 5450
Wire Wire Line
	5425 5600 5425 5450
Connection ~ 5425 5450
Wire Wire Line
	5425 5450 5850 5450
$Comp
L Device:D_Schottky D3
U 1 1 5E74F35F
P 7000 3925
F 0 "D3" V 7025 4000 50  0000 L CNN
F 1 "D_Schottky 7V" V 7100 3975 50  0000 L CNN
F 2 "Diode_SMD:D_SOD-323_HandSoldering" H 7000 3925 50  0001 C CNN
F 3 "https://docs.rs-online.com/2159/0900766b812e22b6.pdf" H 7000 3925 50  0001 C CNN
	1    7000 3925
	0    -1   1    0   
$EndComp
$Comp
L Device:R R6
U 1 1 5E74F365
P 6875 4600
F 0 "R6" H 6945 4646 50  0000 L CNN
F 1 "4K7" H 6945 4555 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 6805 4600 50  0001 C CNN
F 3 "~" H 6875 4600 50  0001 C CNN
	1    6875 4600
	-1   0    0    -1  
$EndComp
$Comp
L Device:R R7
U 1 1 5E74F36B
P 7250 3925
F 0 "R7" H 7075 3975 50  0000 L CNN
F 1 "100K" H 7000 3875 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 7180 3925 50  0001 C CNN
F 3 "~" H 7250 3925 50  0001 C CNN
	1    7250 3925
	-1   0    0    -1  
$EndComp
$Comp
L Device:R R8
U 1 1 5E74F371
P 7425 5075
F 0 "R8" V 7218 5075 50  0000 C CNN
F 1 "10K" V 7309 5075 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 7355 5075 50  0001 C CNN
F 3 "~" H 7425 5075 50  0001 C CNN
	1    7425 5075
	0    -1   1    0   
$EndComp
$Comp
L Device:R R5
U 1 1 5E74F377
P 6025 3750
F 0 "R5" H 5956 3704 50  0000 R CNN
F 1 "33R" H 5956 3795 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5955 3750 50  0001 C CNN
F 3 "~" H 6025 3750 50  0001 C CNN
	1    6025 3750
	1    0    0    1   
$EndComp
Wire Wire Line
	7175 5075 7275 5075
Text GLabel 7750 5075 2    50   Output ~ 0
Laser1
Wire Wire Line
	7750 5075 7575 5075
$Comp
L Transistor_FET:BS170F Q4
U 1 1 5E74F38C
P 6975 5075
F 0 "Q4" H 7181 5121 50  0000 L CNN
F 1 "BS170F" H 7181 5030 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 7175 5000 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/BS170F.pdf" H 6975 5075 50  0001 L CNN
	1    6975 5075
	-1   0    0    -1  
$EndComp
$Comp
L Device:Q_PNP_Darlington_BEC Q3
U 1 1 5E74F392
P 6125 4200
F 0 "Q3" V 6075 3975 50  0000 C CNN
F 1 "BCV46" V 6150 3950 50  0000 C CNN
F 2 "digikey-footprints:SOT-23-3" H 6325 4300 50  0001 C CNN
F 3 "~" H 6125 4200 50  0001 C CNN
	1    6125 4200
	-1   0    0    1   
$EndComp
$Comp
L Jumper:SolderJumper_2_Open JP2
U 1 1 5E74F398
P 6550 4475
F 0 "JP2" H 6550 4680 50  0000 C CNN
F 1 "SolderJumper_2_Open" H 6550 4589 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm" H 6550 4475 50  0001 C CNN
F 3 "~" H 6550 4475 50  0001 C CNN
	1    6550 4475
	-1   0    0    -1  
$EndComp
$Comp
L Device:R_POT RV2
U 1 1 5E74F39E
P 6700 4200
F 0 "RV2" H 6631 4246 50  0000 R CNN
F 1 "22K" H 6631 4155 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3006P_Horizontal" H 6700 4200 50  0001 C CNN
F 3 "~" H 6700 4200 50  0001 C CNN
	1    6700 4200
	-1   0    0    -1  
$EndComp
Wire Wire Line
	6025 3900 6025 4000
Wire Wire Line
	6025 3600 6025 3500
$Comp
L Device:C C2
U 1 1 5E74F3A6
P 6475 3800
F 0 "C2" V 6350 3925 50  0000 C CNN
F 1 "0.1uF" V 6425 3975 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 6513 3650 50  0001 C CNN
F 3 "~" H 6475 3800 50  0001 C CNN
	1    6475 3800
	1    0    0    1   
$EndComp
Wire Wire Line
	7250 3775 7250 3500
Wire Wire Line
	7000 3775 7000 3500
Wire Wire Line
	6700 4050 6700 3500
Wire Wire Line
	6875 4750 6875 4875
Wire Wire Line
	6875 4450 6875 4350
Wire Wire Line
	6875 4350 6700 4350
Wire Wire Line
	6550 4200 6475 4200
Wire Wire Line
	6475 3650 6475 3500
Wire Wire Line
	6475 3950 6475 4200
Connection ~ 6475 4200
Wire Wire Line
	6475 4200 6400 4200
Wire Wire Line
	6700 4350 6700 4475
Connection ~ 6700 4350
Wire Wire Line
	6400 4475 6400 4200
Connection ~ 6400 4200
Wire Wire Line
	6400 4200 6325 4200
Wire Wire Line
	6025 4400 6025 4700
Wire Wire Line
	6875 5275 6875 5450
Connection ~ 6025 3500
Wire Wire Line
	6025 3500 6475 3500
Connection ~ 6475 3500
Wire Wire Line
	6475 3500 6700 3500
Connection ~ 6700 3500
Wire Wire Line
	6700 3500 7000 3500
Connection ~ 7000 3500
Wire Wire Line
	7000 3500 7250 3500
Wire Wire Line
	5850 5450 6875 5450
Wire Wire Line
	6025 4700 5950 4700
Wire Wire Line
	5675 4400 5675 4700
Wire Wire Line
	5675 4700 5750 4700
Wire Wire Line
	6875 4350 7000 4350
Wire Wire Line
	7250 4350 7250 4075
Connection ~ 6875 4350
Wire Wire Line
	7000 4075 7000 4350
Connection ~ 7000 4350
Wire Wire Line
	7000 4350 7250 4350
Wire Wire Line
	4450 4100 4450 4350
Wire Wire Line
	4450 4350 4700 4350
Connection ~ 4825 4350
Wire Wire Line
	4700 4100 4700 4350
Connection ~ 4700 4350
Wire Wire Line
	4700 4350 4825 4350
Connection ~ 5300 5450
Wire Wire Line
	5300 5450 5425 5450
Wire Wire Line
	4825 5450 5425 5450
$EndSCHEMATC
