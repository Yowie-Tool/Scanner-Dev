; pcb2gcode 2.0.0 
; Software-independent Gcode 

G94 ; Millimeters per minute feed rate. 
G21 ; Units == Millimeters. 

G90 ; Absolute coordinates. 
;G1 F3000 S10000 ; RPM spindle speed. 
G1 F300 F600.00000 ; Feedrate. 


G1 F3000 Z3.00000 ;Retract to tool change height
;T0
;M5      ;Spindle stop.
;G04 P1.00000 ;Wait for spindle to stop
;MSG, Change tool bit to cutter diameter 0.12000mm
;M6      ;Tool change.
;M0      ;Temporary machine stop.
;M3 ; Spindle on clockwise. 
;G04 P1.00000 ;Wait for spindle to get up to speed
;G04 P0 ; dwell for no time -- G64 should not smooth over this point 
G1 F3000 Z3.00000 ; retract 

G1 F3000 X-0.10996 Y3.17001 ; rapid move to begin. 
G1 F300 Z-0.07000 F300.00000 ; plunge. 
;G04 P0 ; dwell for no time -- G64 should not smooth over this point 
G1 F300 F600.00000
G1 F300 X-0.10996 Y59.09100
G1 F300 X-0.17021 Y59.69370
G1 F300 X-0.34542 Y60.26735
G1 F300 X-0.62919 Y60.79580
G1 F300 X-1.01059 Y61.25874
G1 F300 X-1.47498 Y61.63834
G1 F300 X-2.00452 Y61.92008
G1 F300 X-2.57882 Y62.09308
G1 F300 X-3.16995 Y62.15104
G1 F300 X-62.82157 Y62.15803
G1 F300 X-63.28497 Y62.11152
G1 F300 X-63.72467 Y61.97693
G1 F300 X-64.12967 Y61.75915
G1 F300 X-64.48441 Y61.46654
G1 F300 X-64.77524 Y61.11033
G1 F300 X-64.99098 Y60.70426
G1 F300 X-65.12334 Y60.26387
G1 F300 X-65.16759 Y59.81201
G1 F300 X-65.16759 Y2.45601
G1 F300 X-65.12106 Y1.99264
G1 F300 X-64.98649 Y1.55292
G1 F300 X-64.76871 Y1.14794
G1 F300 X-64.47608 Y0.79318
G1 F300 X-64.11989 Y0.50237
G1 F300 X-63.71380 Y0.28663
G1 F300 X-63.27344 Y0.15424
G1 F300 X-62.82160 Y0.11002
G1 F300 X-3.16998 Y0.11002
G1 F300 X-2.57882 Y0.16796
G1 F300 X-2.00452 Y0.34098
G1 F300 X-1.47498 Y0.62269
G1 F300 X-1.01059 Y1.00235
G1 F300 X-0.62919 Y1.46526
G1 F300 X-0.34542 Y1.99368
G1 F300 X-0.17021 Y2.56734
G1 F300 X-0.10996 Y3.17001
;G04 P0 ; dwell for no time -- G64 should not smooth over this point 
G1 F3000 Z3.00000 ; retract 

G1 F3000 X-13.77958 Y15.90399 ; rapid move to begin. 
G1 F300 Z-0.07000 F300.00000 ; plunge. 
;G04 P0 ; dwell for no time -- G64 should not smooth over this point 
G1 F300 F600.00000
G1 F300 X-13.77958 Y45.39812
G1 F300 X-13.81336 Y45.56929
G1 F300 X-13.90866 Y45.71194
G1 F300 X-14.05131 Y45.80729
G1 F300 X-14.22253 Y45.84102
G1 F300 X-43.71660 Y45.84102
G1 F300 X-43.88785 Y45.80729
G1 F300 X-44.03050 Y45.71196
G1 F300 X-44.12582 Y45.56929
G1 F300 X-44.15956 Y45.39804
G1 F300 X-44.15956 Y15.90399
G1 F300 X-44.12582 Y15.73275
G1 F300 X-44.03050 Y15.59010
G1 F300 X-43.88785 Y15.49477
G1 F300 X-43.71660 Y15.46104
G1 F300 X-14.22256 Y15.46104
G1 F300 X-14.05131 Y15.49477
G1 F300 X-13.90864 Y15.59010
G1 F300 X-13.81336 Y15.73275
G1 F300 X-13.77958 Y15.90399

;G04 P0 ; dwell for no time -- G64 should not smooth over this point 
G1 F3000 Z3.000 ; retract 

;M5 ; Spindle off. 
;G04 P1.000000
;M9 ; Coolant off. 
M0 ; Program end. 
