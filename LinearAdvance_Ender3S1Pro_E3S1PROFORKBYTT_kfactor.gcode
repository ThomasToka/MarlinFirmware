; ### Marlin K-Factor Calibration Pattern ###
; -------------------------------------------
;
; Printer: Ender 3 S1 Pro
; Filament: filament name
; Created: Sun Nov 19 2023 11:45:10 GMT+0100 (Mitteleuropäische Normalzeit)
;
; Settings Printer:
; Filament Diameter = 1.75 mm
; Nozzle Diameter = 0.4 mm
; Nozzle Temperature = 205 °C
; Bed Temperature = 60 °C
; Retraction Distance = 0.8 mm
; Layer Height = 0.2 mm
; Extruder = 0 
; Fan Speed = 0 %
; Z-axis Offset = 0 mm
;
; Settings Print Bed:
; Bed Shape = Rect
; Bed Size X = 235 mm
; Bed Size Y = 235 mm
; Origin Bed Center = false
;
; Settings Speed:
; Slow Printing Speed = 1800 mm/min
; Fast Printing Speed = 7200 mm/min
; Movement Speed = 12000 mm/min
; Retract Speed = 2400 mm/min
; Unretract Speed = 2400 mm/min
; Printing Acceleration = 1000 mm/s^2
; Jerk X-axis =  firmware default
; Jerk Y-axis =  firmware default
; Jerk Z-axis =  firmware default
; Jerk Extruder =  firmware default
;
; Settings Pattern:
; Linear Advance Version = 1.5
; Starting Value Factor = 0
; Ending Value Factor = 0.1
; Factor Stepping = 0.01
; Test Line Spacing = 5 mm
; Test Line Length Slow = 40 mm
; Test Line Length Fast = 80 mm
; Print Pattern = Standard
; Print Frame = false
; Number Lines = true
; Print Size X = 178 mm
; Print Size Y = 75 mm
; Print Rotation = 0 degree
;
; Settings Advance:
; Nozzle / Line Ratio = 1.2
; Bed leveling = 0
; Use FWRETRACT = false
; Extrusion Multiplier = 1
; Prime Nozzle = true
; Prime Extrusion Multiplier = 2.5
; Prime Speed = 1800
; Dwell Time = 2 s
;
; prepare printing
;
G21 ; Millimeter units
G90 ; Absolute XYZ
M83 ; Relative E
G28 ; Home all axes
T0 ; Switch to tool 0
G1 Z10 F100 ; Z raise
M104 S205 ; Set nozzle temperature (no wait)
M190 S60 ; Set bed temperature (wait)
M109 S205 ; Wait for nozzle temp
M204 P1000 ; Acceleration
G92 E0 ; Reset extruder distance
M106 P0 S0
G1 X117.5 Y117.5 F12000 ; move to start
G1 Z0.2 F1800 ; Move to layer height
;
; prime nozzle
;
G1 X28.5 Y80 F12000 ; move to start
G1 X28.5 Y155 E7.4835 F1800 ; print line
G1 X29.22 Y155 F12000 ; move to start
G1 X29.22 Y80 E7.4835 F1800 ; print line
G1 E-0.8 F2400 ; retract
;
; start the Test pattern
;
G4 P2000 ; Pause (dwell) for 2 seconds
G1 X38.5 Y80 F12000 ; move to start
M900 K0 ; set K-factor
M117 K0 ; 
G1 E0.8 F2400 ; un-retract
G1 X78.5 Y80 E1.5965 F1800 ; print line
G1 X158.5 Y80 E3.193 F7200 ; print line
G1 X198.5 Y80 E1.5965 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X38.5 Y85 F12000 ; move to start
M900 K0.01 ; set K-factor
M117 K0.01 ; 
G1 E0.8 F2400 ; un-retract
G1 X78.5 Y85 E1.5965 F1800 ; print line
G1 X158.5 Y85 E3.193 F7200 ; print line
G1 X198.5 Y85 E1.5965 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X38.5 Y90 F12000 ; move to start
M900 K0.02 ; set K-factor
M117 K0.02 ; 
G1 E0.8 F2400 ; un-retract
G1 X78.5 Y90 E1.5965 F1800 ; print line
G1 X158.5 Y90 E3.193 F7200 ; print line
G1 X198.5 Y90 E1.5965 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X38.5 Y95 F12000 ; move to start
M900 K0.03 ; set K-factor
M117 K0.03 ; 
G1 E0.8 F2400 ; un-retract
G1 X78.5 Y95 E1.5965 F1800 ; print line
G1 X158.5 Y95 E3.193 F7200 ; print line
G1 X198.5 Y95 E1.5965 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X38.5 Y100 F12000 ; move to start
M900 K0.04 ; set K-factor
M117 K0.04 ; 
G1 E0.8 F2400 ; un-retract
G1 X78.5 Y100 E1.5965 F1800 ; print line
G1 X158.5 Y100 E3.193 F7200 ; print line
G1 X198.5 Y100 E1.5965 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X38.5 Y105 F12000 ; move to start
M900 K0.05 ; set K-factor
M117 K0.05 ; 
G1 E0.8 F2400 ; un-retract
G1 X78.5 Y105 E1.5965 F1800 ; print line
G1 X158.5 Y105 E3.193 F7200 ; print line
G1 X198.5 Y105 E1.5965 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X38.5 Y110 F12000 ; move to start
M900 K0.06 ; set K-factor
M117 K0.06 ; 
G1 E0.8 F2400 ; un-retract
G1 X78.5 Y110 E1.5965 F1800 ; print line
G1 X158.5 Y110 E3.193 F7200 ; print line
G1 X198.5 Y110 E1.5965 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X38.5 Y115 F12000 ; move to start
M900 K0.07 ; set K-factor
M117 K0.07 ; 
G1 E0.8 F2400 ; un-retract
G1 X78.5 Y115 E1.5965 F1800 ; print line
G1 X158.5 Y115 E3.193 F7200 ; print line
G1 X198.5 Y115 E1.5965 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X38.5 Y120 F12000 ; move to start
M900 K0.08 ; set K-factor
M117 K0.08 ; 
G1 E0.8 F2400 ; un-retract
G1 X78.5 Y120 E1.5965 F1800 ; print line
G1 X158.5 Y120 E3.193 F7200 ; print line
G1 X198.5 Y120 E1.5965 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X38.5 Y125 F12000 ; move to start
M900 K0.09 ; set K-factor
M117 K0.09 ; 
G1 E0.8 F2400 ; un-retract
G1 X78.5 Y125 E1.5965 F1800 ; print line
G1 X158.5 Y125 E3.193 F7200 ; print line
G1 X198.5 Y125 E1.5965 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X38.5 Y130 F12000 ; move to start
M900 K0.1 ; set K-factor
M117 K0.1 ; 
G1 E0.8 F2400 ; un-retract
G1 X78.5 Y130 E1.5965 F1800 ; print line
G1 X158.5 Y130 E3.193 F7200 ; print line
G1 X198.5 Y130 E1.5965 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X38.5 Y135 F12000 ; move to start
;
; Mark the test area for reference
M117 K0
M900 K0 ; Set K-factor 0
G1 X78.5 Y135 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X78.5 Y155 E0.7982 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X158.5 Y135 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X158.5 Y155 E0.7982 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 Z0.3 F1800 ; zHop
;
; print K-values
;
G1 X200.5 Y78 F12000 ; move to start
G1 Z0.2 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X202.5 Y78 E0.0798 F1800 ; 0
G1 X202.5 Y80 E0.0798 F1800 ; 0
G1 X202.5 Y82 E0.0798 F1800 ; 0
G1 X200.5 Y82 E0.0798 F1800 ; 0
G1 X200.5 Y80 E0.0798 F1800 ; 0
G1 X200.5 Y78 E0.0798 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 Z0.3 F1800 ; zHop
G1 X200.5 Y88 F12000 ; move to start
G1 Z0.2 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X202.5 Y88 E0.0798 F1800 ; 0
G1 X202.5 Y90 E0.0798 F1800 ; 0
G1 X202.5 Y92 E0.0798 F1800 ; 0
G1 X200.5 Y92 E0.0798 F1800 ; 0
G1 X200.5 Y90 E0.0798 F1800 ; 0
G1 X200.5 Y88 E0.0798 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X203.5 Y88 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X203.5 Y88.4 E0.016 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X204.5 Y88 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X206.5 Y88 E0.0798 F1800 ; 0
G1 X206.5 Y90 E0.0798 F1800 ; 0
G1 X206.5 Y92 E0.0798 F1800 ; 0
G1 X204.5 Y92 E0.0798 F1800 ; 0
G1 X204.5 Y90 E0.0798 F1800 ; 0
G1 X204.5 Y88 E0.0798 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X207.5 Y88 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X207.5 Y90 F12000 ; move to start
G1 X207.5 Y92 F12000 ; move to start
G1 X209.5 Y92 E0.0798 F1800 ; 2
G1 X209.5 Y90 E0.0798 F1800 ; 2
G1 X207.5 Y90 E0.0798 F1800 ; 2
G1 X207.5 Y88 E0.0798 F1800 ; 2
G1 X209.5 Y88 E0.0798 F1800 ; 2
G1 E-0.8 F2400 ; retract
G1 Z0.3 F1800 ; zHop
G1 X200.5 Y98 F12000 ; move to start
G1 Z0.2 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X202.5 Y98 E0.0798 F1800 ; 0
G1 X202.5 Y100 E0.0798 F1800 ; 0
G1 X202.5 Y102 E0.0798 F1800 ; 0
G1 X200.5 Y102 E0.0798 F1800 ; 0
G1 X200.5 Y100 E0.0798 F1800 ; 0
G1 X200.5 Y98 E0.0798 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X203.5 Y98 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X203.5 Y98.4 E0.016 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X204.5 Y98 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X206.5 Y98 E0.0798 F1800 ; 0
G1 X206.5 Y100 E0.0798 F1800 ; 0
G1 X206.5 Y102 E0.0798 F1800 ; 0
G1 X204.5 Y102 E0.0798 F1800 ; 0
G1 X204.5 Y100 E0.0798 F1800 ; 0
G1 X204.5 Y98 E0.0798 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X207.5 Y98 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X207.5 Y100 F12000 ; move to start
G1 X207.5 Y102 F12000 ; move to start
G1 X207.5 Y100 E0.0798 F1800 ; 4
G1 X209.5 Y100 E0.0798 F1800 ; 4
G1 X209.5 Y102 F12000 ; move to start
G1 X209.5 Y100 E0.0798 F1800 ; 4
G1 X209.5 Y98 E0.0798 F1800 ; 4
G1 E-0.8 F2400 ; retract
G1 Z0.3 F1800 ; zHop
G1 X200.5 Y108 F12000 ; move to start
G1 Z0.2 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X202.5 Y108 E0.0798 F1800 ; 0
G1 X202.5 Y110 E0.0798 F1800 ; 0
G1 X202.5 Y112 E0.0798 F1800 ; 0
G1 X200.5 Y112 E0.0798 F1800 ; 0
G1 X200.5 Y110 E0.0798 F1800 ; 0
G1 X200.5 Y108 E0.0798 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X203.5 Y108 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X203.5 Y108.4 E0.016 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X204.5 Y108 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X206.5 Y108 E0.0798 F1800 ; 0
G1 X206.5 Y110 E0.0798 F1800 ; 0
G1 X206.5 Y112 E0.0798 F1800 ; 0
G1 X204.5 Y112 E0.0798 F1800 ; 0
G1 X204.5 Y110 E0.0798 F1800 ; 0
G1 X204.5 Y108 E0.0798 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X207.5 Y108 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X207.5 Y110 F12000 ; move to start
G1 X209.5 Y110 E0.0798 F1800 ; 6
G1 X209.5 Y108 E0.0798 F1800 ; 6
G1 X207.5 Y108 E0.0798 F1800 ; 6
G1 X207.5 Y110 E0.0798 F1800 ; 6
G1 X207.5 Y112 E0.0798 F1800 ; 6
G1 X209.5 Y112 E0.0798 F1800 ; 6
G1 E-0.8 F2400 ; retract
G1 Z0.3 F1800 ; zHop
G1 X200.5 Y118 F12000 ; move to start
G1 Z0.2 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X202.5 Y118 E0.0798 F1800 ; 0
G1 X202.5 Y120 E0.0798 F1800 ; 0
G1 X202.5 Y122 E0.0798 F1800 ; 0
G1 X200.5 Y122 E0.0798 F1800 ; 0
G1 X200.5 Y120 E0.0798 F1800 ; 0
G1 X200.5 Y118 E0.0798 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X203.5 Y118 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X203.5 Y118.4 E0.016 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X204.5 Y118 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X206.5 Y118 E0.0798 F1800 ; 0
G1 X206.5 Y120 E0.0798 F1800 ; 0
G1 X206.5 Y122 E0.0798 F1800 ; 0
G1 X204.5 Y122 E0.0798 F1800 ; 0
G1 X204.5 Y120 E0.0798 F1800 ; 0
G1 X204.5 Y118 E0.0798 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X207.5 Y118 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X207.5 Y120 F12000 ; move to start
G1 X209.5 Y120 E0.0798 F1800 ; 8
G1 X209.5 Y118 E0.0798 F1800 ; 8
G1 X207.5 Y118 E0.0798 F1800 ; 8
G1 X207.5 Y120 E0.0798 F1800 ; 8
G1 X207.5 Y122 E0.0798 F1800 ; 8
G1 X209.5 Y122 E0.0798 F1800 ; 8
G1 X209.5 Y120 E0.0798 F1800 ; 8
G1 E-0.8 F2400 ; retract
G1 Z0.3 F1800 ; zHop
G1 X200.5 Y128 F12000 ; move to start
G1 Z0.2 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X202.5 Y128 E0.0798 F1800 ; 0
G1 X202.5 Y130 E0.0798 F1800 ; 0
G1 X202.5 Y132 E0.0798 F1800 ; 0
G1 X200.5 Y132 E0.0798 F1800 ; 0
G1 X200.5 Y130 E0.0798 F1800 ; 0
G1 X200.5 Y128 E0.0798 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X203.5 Y128 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X203.5 Y128.4 E0.016 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X204.5 Y128 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X204.5 Y130 E0.0798 F1800 ; 1
G1 X204.5 Y132 E0.0798 F1800 ; 1
G1 E-0.8 F2400 ; retract
G1 Z0.3 F1800 ; zHop
;
; FINISH
;
M107 ; Turn off fan
M400 ; Finish moving
M104 S0 ; Turn off hotend
M140 S0 ; Turn off bed
G1 Z30 X235 Y235 F12000 ; Move away from the print
M84 ; Disable motors
M501 ; Load settings from EEPROM
;