; pcb2gcode 2.0.0 
; Software-independent Gcode 

; This file uses only one drill bit. Forced by 'onedrill' option 

G94       ;Millimeters per minute feed rate.
G21       ;Units == Millimeters.
G90       ;Absolute coordinates.
;G1 F3000 S10000     ;RPM spindle speed.

G1 F3000 Z3.00000 ;Retract
;T1
;M5      ;Spindle stop.
;G04 P1.00000
;MSG, Change tool bit to drill size 0.75 mm
;M6      ;Tool change.
;M0      ;Temporary machine stop.
;M3      ;Spindle on clockwise.
G1 F3000 Z3.00000
;G04 P1.00000

;F1000.00000
G1 F3000 X-61.96960 Y22.90100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-58.46960 Y22.90100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-50.71960 Y29.65100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-47.76960 Y31.07900
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-50.71960 Y27.65100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-50.71960 Y25.65100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-49.46960 Y20.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-49.46960 Y18.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-49.46960 Y16.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-49.46960 Y14.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-61.66960 Y3.59100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-55.89460 Y4.82600
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-53.35460 Y4.82600
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-48.69460 Y4.82600
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-46.15460 Y4.82600
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-18.71960 Y5.07100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-18.71960 Y7.61100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-18.71960 Y10.15100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-11.71960 Y6.65100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-11.71960 Y10.15100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-3.66960 Y3.59100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-3.57360 Y11.26700
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-8.65360 Y17.36300
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-4.46960 Y23.90100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-4.46960 Y25.90100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-4.46960 Y27.90100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-4.46960 Y29.90100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-4.46960 Y31.90100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-4.21960 Y41.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-4.21960 Y46.48100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-3.66960 Y52.59100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-8.53960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-11.07960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-8.53960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-11.07960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-13.61960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-16.15960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-13.61960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-16.15960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-18.69960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-18.69960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-22.46960 Y58.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-24.46960 Y58.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-26.46960 Y58.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-28.46960 Y58.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-30.46960 Y58.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-31.39960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-28.85960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-26.31960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-23.77960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-21.23960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-21.23960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-23.77960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-26.31960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-28.85960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-31.39960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-33.93960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-36.47960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-33.93960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-36.47960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-41.92760 Y47.58900
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-39.01960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-39.01960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-41.55960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-41.55960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-44.09960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-44.09960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-46.63960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-46.63960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-49.17960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-51.71960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-49.17960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-51.71960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-54.25960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-54.25960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-59.45360 Y60.54300
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-59.45360 Y56.22500
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-61.66960 Y52.59100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-56.79960 Y53.86100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-56.79960 Y51.32100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-62.46960 Y46.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-60.46960 Y46.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-55.21960 Y45.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-53.21960 Y45.40100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-49.03960 Y43.77900
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-49.29360 Y36.41300
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-58.96960 Y35.15100
G1 F300 Z-2.50000
G1 F300 Z3.00000
G1 F3000 X-61.46960 Y35.15100
G1 F300 Z-2.50000
G1 F300 Z3.00000

G1 F3000 Z3.000 ; All done -- retract 

;M5      ;Spindle off.
;G04 P1.000000
;M9      ;Coolant off.
M0      ;Program end.
