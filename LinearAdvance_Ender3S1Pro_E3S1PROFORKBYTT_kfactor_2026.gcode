; ### Marlin K-Factor Calibration Pattern ###
; -------------------------------------------
;
; Printer: Ender 3 S1 Pro
; Filament: filament name
; Created: Wed Feb 04 2026 12:50:00 GMT+0100 (Mitteleuropäische Normalzeit)
;
; Settings Printer:
; Filament Diameter = 1.75 mm
; Nozzle Diameter = 0.4 mm
; Nozzle Temperature = 205 °C
; Bed Temperature = 60 °C
; Retraction Distance = 0.8 mm
; Layer Height = 0.28 mm
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
; Factor Stepping = 0.005
; Test Line Spacing = 5 mm
; Test Line Length Slow = 40 mm
; Test Line Length Fast = 100 mm
; Print Pattern = Standard
; Print Frame = false
; Number Lines = true
; Print Size X = 198 mm
; Print Size Y = 125 mm
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

G1 Z0.28 F1800 ; Move to layer height
;
; prime nozzle
;
G1 X18.5 Y55 F12000 ; move to start
G1 X18.5 Y180 E17.4616 F1800 ; print line
G1 X19.22 Y180 F12000 ; move to start
G1 X19.22 Y55 E17.4616 F1800 ; print line
G1 E-0.8 F2400 ; retract
;
; start the Test pattern
;
G4 P2000 ; Pause (dwell) for 2 seconds
G1 X28.5 Y55 F12000 ; move to start
M900 K0 ; set K-factor
M117 K0 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y55 E2.2351 F1800 ; print line
G1 X168.5 Y55 E5.5877 F7200 ; print line
G1 X208.5 Y55 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y60 F12000 ; move to start
M900 K0.005 ; set K-factor
M117 K0.005 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y60 E2.2351 F1800 ; print line
G1 X168.5 Y60 E5.5877 F7200 ; print line
G1 X208.5 Y60 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y65 F12000 ; move to start
M900 K0.01 ; set K-factor
M117 K0.01 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y65 E2.2351 F1800 ; print line
G1 X168.5 Y65 E5.5877 F7200 ; print line
G1 X208.5 Y65 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y70 F12000 ; move to start
M900 K0.015 ; set K-factor
M117 K0.015 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y70 E2.2351 F1800 ; print line
G1 X168.5 Y70 E5.5877 F7200 ; print line
G1 X208.5 Y70 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y75 F12000 ; move to start
M900 K0.02 ; set K-factor
M117 K0.02 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y75 E2.2351 F1800 ; print line
G1 X168.5 Y75 E5.5877 F7200 ; print line
G1 X208.5 Y75 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y80 F12000 ; move to start
M900 K0.025 ; set K-factor
M117 K0.025 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y80 E2.2351 F1800 ; print line
G1 X168.5 Y80 E5.5877 F7200 ; print line
G1 X208.5 Y80 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y85 F12000 ; move to start
M900 K0.03 ; set K-factor
M117 K0.03 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y85 E2.2351 F1800 ; print line
G1 X168.5 Y85 E5.5877 F7200 ; print line
G1 X208.5 Y85 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y90 F12000 ; move to start
M900 K0.035 ; set K-factor
M117 K0.035 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y90 E2.2351 F1800 ; print line
G1 X168.5 Y90 E5.5877 F7200 ; print line
G1 X208.5 Y90 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y95 F12000 ; move to start
M900 K0.04 ; set K-factor
M117 K0.04 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y95 E2.2351 F1800 ; print line
G1 X168.5 Y95 E5.5877 F7200 ; print line
G1 X208.5 Y95 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y100 F12000 ; move to start
M900 K0.045 ; set K-factor
M117 K0.045 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y100 E2.2351 F1800 ; print line
G1 X168.5 Y100 E5.5877 F7200 ; print line
G1 X208.5 Y100 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y105 F12000 ; move to start
M900 K0.05 ; set K-factor
M117 K0.05 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y105 E2.2351 F1800 ; print line
G1 X168.5 Y105 E5.5877 F7200 ; print line
G1 X208.5 Y105 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y110 F12000 ; move to start
M900 K0.055 ; set K-factor
M117 K0.055 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y110 E2.2351 F1800 ; print line
G1 X168.5 Y110 E5.5877 F7200 ; print line
G1 X208.5 Y110 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y115 F12000 ; move to start
M900 K0.06 ; set K-factor
M117 K0.06 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y115 E2.2351 F1800 ; print line
G1 X168.5 Y115 E5.5877 F7200 ; print line
G1 X208.5 Y115 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y120 F12000 ; move to start
M900 K0.065 ; set K-factor
M117 K0.065 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y120 E2.2351 F1800 ; print line
G1 X168.5 Y120 E5.5877 F7200 ; print line
G1 X208.5 Y120 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y125 F12000 ; move to start
M900 K0.07 ; set K-factor
M117 K0.07 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y125 E2.2351 F1800 ; print line
G1 X168.5 Y125 E5.5877 F7200 ; print line
G1 X208.5 Y125 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y130 F12000 ; move to start
M900 K0.075 ; set K-factor
M117 K0.075 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y130 E2.2351 F1800 ; print line
G1 X168.5 Y130 E5.5877 F7200 ; print line
G1 X208.5 Y130 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y135 F12000 ; move to start
M900 K0.08 ; set K-factor
M117 K0.08 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y135 E2.2351 F1800 ; print line
G1 X168.5 Y135 E5.5877 F7200 ; print line
G1 X208.5 Y135 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y140 F12000 ; move to start
M900 K0.085 ; set K-factor
M117 K0.085 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y140 E2.2351 F1800 ; print line
G1 X168.5 Y140 E5.5877 F7200 ; print line
G1 X208.5 Y140 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y145 F12000 ; move to start
M900 K0.09 ; set K-factor
M117 K0.09 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y145 E2.2351 F1800 ; print line
G1 X168.5 Y145 E5.5877 F7200 ; print line
G1 X208.5 Y145 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y150 F12000 ; move to start
M900 K0.095 ; set K-factor
M117 K0.095 ; 
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y150 E2.2351 F1800 ; print line
G1 X168.5 Y150 E5.5877 F7200 ; print line
G1 X208.5 Y150 E2.2351 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X28.5 Y155 F12000 ; move to start
;
; Mark the test area for reference
M117 K0
M900 K0 ; Set K-factor 0
G1 X68.5 Y160 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X68.5 Y180 E1.1175 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 X168.5 Y160 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X168.5 Y180 E1.1175 F1800 ; print line
G1 E-0.8 F2400 ; retract
G1 Z0.38 F1800 ; zHop
;
; print K-values
;
G1 X210.5 Y53 F12000 ; move to start
G1 Z0.28 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X212.5 Y53 E0.1118 F1800 ; 0
G1 X212.5 Y55 E0.1118 F1800 ; 0
G1 X212.5 Y57 E0.1118 F1800 ; 0
G1 X210.5 Y57 E0.1118 F1800 ; 0
G1 X210.5 Y55 E0.1118 F1800 ; 0
G1 X210.5 Y53 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 Z0.38 F1800 ; zHop
G1 X210.5 Y63 F12000 ; move to start
G1 Z0.28 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X212.5 Y63 E0.1118 F1800 ; 0
G1 X212.5 Y65 E0.1118 F1800 ; 0
G1 X212.5 Y67 E0.1118 F1800 ; 0
G1 X210.5 Y67 E0.1118 F1800 ; 0
G1 X210.5 Y65 E0.1118 F1800 ; 0
G1 X210.5 Y63 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X213.5 Y63 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X213.5 Y63.4 E0.0224 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X214.5 Y63 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X216.5 Y63 E0.1118 F1800 ; 0
G1 X216.5 Y65 E0.1118 F1800 ; 0
G1 X216.5 Y67 E0.1118 F1800 ; 0
G1 X214.5 Y67 E0.1118 F1800 ; 0
G1 X214.5 Y65 E0.1118 F1800 ; 0
G1 X214.5 Y63 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X217.5 Y63 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X217.5 Y65 E0.1118 F1800 ; 1
G1 X217.5 Y67 E0.1118 F1800 ; 1
G1 E-0.8 F2400 ; retract
G1 Z0.38 F1800 ; zHop
G1 X210.5 Y73 F12000 ; move to start
G1 Z0.28 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X212.5 Y73 E0.1118 F1800 ; 0
G1 X212.5 Y75 E0.1118 F1800 ; 0
G1 X212.5 Y77 E0.1118 F1800 ; 0
G1 X210.5 Y77 E0.1118 F1800 ; 0
G1 X210.5 Y75 E0.1118 F1800 ; 0
G1 X210.5 Y73 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X213.5 Y73 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X213.5 Y73.4 E0.0224 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X214.5 Y73 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X216.5 Y73 E0.1118 F1800 ; 0
G1 X216.5 Y75 E0.1118 F1800 ; 0
G1 X216.5 Y77 E0.1118 F1800 ; 0
G1 X214.5 Y77 E0.1118 F1800 ; 0
G1 X214.5 Y75 E0.1118 F1800 ; 0
G1 X214.5 Y73 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X217.5 Y73 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X217.5 Y75 F12000 ; move to start
G1 X217.5 Y77 F12000 ; move to start
G1 X219.5 Y77 E0.1118 F1800 ; 2
G1 X219.5 Y75 E0.1118 F1800 ; 2
G1 X217.5 Y75 E0.1118 F1800 ; 2
G1 X217.5 Y73 E0.1118 F1800 ; 2
G1 X219.5 Y73 E0.1118 F1800 ; 2
G1 E-0.8 F2400 ; retract
G1 Z0.38 F1800 ; zHop
G1 X210.5 Y83 F12000 ; move to start
G1 Z0.28 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X212.5 Y83 E0.1118 F1800 ; 0
G1 X212.5 Y85 E0.1118 F1800 ; 0
G1 X212.5 Y87 E0.1118 F1800 ; 0
G1 X210.5 Y87 E0.1118 F1800 ; 0
G1 X210.5 Y85 E0.1118 F1800 ; 0
G1 X210.5 Y83 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X213.5 Y83 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X213.5 Y83.4 E0.0224 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X214.5 Y83 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X216.5 Y83 E0.1118 F1800 ; 0
G1 X216.5 Y85 E0.1118 F1800 ; 0
G1 X216.5 Y87 E0.1118 F1800 ; 0
G1 X214.5 Y87 E0.1118 F1800 ; 0
G1 X214.5 Y85 E0.1118 F1800 ; 0
G1 X214.5 Y83 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X217.5 Y83 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X217.5 Y85 F12000 ; move to start
G1 X217.5 Y87 F12000 ; move to start
G1 X219.5 Y87 E0.1118 F1800 ; 3
G1 X219.5 Y85 E0.1118 F1800 ; 3
G1 X219.5 Y83 E0.1118 F1800 ; 3
G1 X217.5 Y83 E0.1118 F1800 ; 3
G1 X217.5 Y85 F12000 ; move to start
G1 X219.5 Y85 E0.1118 F1800 ; 3
G1 E-0.8 F2400 ; retract
G1 Z0.38 F1800 ; zHop
G1 X210.5 Y93 F12000 ; move to start
G1 Z0.28 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X212.5 Y93 E0.1118 F1800 ; 0
G1 X212.5 Y95 E0.1118 F1800 ; 0
G1 X212.5 Y97 E0.1118 F1800 ; 0
G1 X210.5 Y97 E0.1118 F1800 ; 0
G1 X210.5 Y95 E0.1118 F1800 ; 0
G1 X210.5 Y93 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X213.5 Y93 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X213.5 Y93.4 E0.0224 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X214.5 Y93 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X216.5 Y93 E0.1118 F1800 ; 0
G1 X216.5 Y95 E0.1118 F1800 ; 0
G1 X216.5 Y97 E0.1118 F1800 ; 0
G1 X214.5 Y97 E0.1118 F1800 ; 0
G1 X214.5 Y95 E0.1118 F1800 ; 0
G1 X214.5 Y93 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X217.5 Y93 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X217.5 Y95 F12000 ; move to start
G1 X217.5 Y97 F12000 ; move to start
G1 X217.5 Y95 E0.1118 F1800 ; 4
G1 X219.5 Y95 E0.1118 F1800 ; 4
G1 X219.5 Y97 F12000 ; move to start
G1 X219.5 Y95 E0.1118 F1800 ; 4
G1 X219.5 Y93 E0.1118 F1800 ; 4
G1 E-0.8 F2400 ; retract
G1 Z0.38 F1800 ; zHop
G1 X210.5 Y103 F12000 ; move to start
G1 Z0.28 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X212.5 Y103 E0.1118 F1800 ; 0
G1 X212.5 Y105 E0.1118 F1800 ; 0
G1 X212.5 Y107 E0.1118 F1800 ; 0
G1 X210.5 Y107 E0.1118 F1800 ; 0
G1 X210.5 Y105 E0.1118 F1800 ; 0
G1 X210.5 Y103 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X213.5 Y103 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X213.5 Y103.4 E0.0224 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X214.5 Y103 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X216.5 Y103 E0.1118 F1800 ; 0
G1 X216.5 Y105 E0.1118 F1800 ; 0
G1 X216.5 Y107 E0.1118 F1800 ; 0
G1 X214.5 Y107 E0.1118 F1800 ; 0
G1 X214.5 Y105 E0.1118 F1800 ; 0
G1 X214.5 Y103 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X217.5 Y103 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X219.5 Y103 E0.1118 F1800 ; 5
G1 X219.5 Y105 E0.1118 F1800 ; 5
G1 X217.5 Y105 E0.1118 F1800 ; 5
G1 X217.5 Y107 E0.1118 F1800 ; 5
G1 X219.5 Y107 E0.1118 F1800 ; 5
G1 E-0.8 F2400 ; retract
G1 Z0.38 F1800 ; zHop
G1 X210.5 Y113 F12000 ; move to start
G1 Z0.28 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X212.5 Y113 E0.1118 F1800 ; 0
G1 X212.5 Y115 E0.1118 F1800 ; 0
G1 X212.5 Y117 E0.1118 F1800 ; 0
G1 X210.5 Y117 E0.1118 F1800 ; 0
G1 X210.5 Y115 E0.1118 F1800 ; 0
G1 X210.5 Y113 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X213.5 Y113 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X213.5 Y113.4 E0.0224 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X214.5 Y113 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X216.5 Y113 E0.1118 F1800 ; 0
G1 X216.5 Y115 E0.1118 F1800 ; 0
G1 X216.5 Y117 E0.1118 F1800 ; 0
G1 X214.5 Y117 E0.1118 F1800 ; 0
G1 X214.5 Y115 E0.1118 F1800 ; 0
G1 X214.5 Y113 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X217.5 Y113 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X217.5 Y115 F12000 ; move to start
G1 X219.5 Y115 E0.1118 F1800 ; 6
G1 X219.5 Y113 E0.1118 F1800 ; 6
G1 X217.5 Y113 E0.1118 F1800 ; 6
G1 X217.5 Y115 E0.1118 F1800 ; 6
G1 X217.5 Y117 E0.1118 F1800 ; 6
G1 X219.5 Y117 E0.1118 F1800 ; 6
G1 E-0.8 F2400 ; retract
G1 Z0.38 F1800 ; zHop
G1 X210.5 Y123 F12000 ; move to start
G1 Z0.28 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X212.5 Y123 E0.1118 F1800 ; 0
G1 X212.5 Y125 E0.1118 F1800 ; 0
G1 X212.5 Y127 E0.1118 F1800 ; 0
G1 X210.5 Y127 E0.1118 F1800 ; 0
G1 X210.5 Y125 E0.1118 F1800 ; 0
G1 X210.5 Y123 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X213.5 Y123 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X213.5 Y123.4 E0.0224 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X214.5 Y123 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X216.5 Y123 E0.1118 F1800 ; 0
G1 X216.5 Y125 E0.1118 F1800 ; 0
G1 X216.5 Y127 E0.1118 F1800 ; 0
G1 X214.5 Y127 E0.1118 F1800 ; 0
G1 X214.5 Y125 E0.1118 F1800 ; 0
G1 X214.5 Y123 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X217.5 Y123 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X217.5 Y125 F12000 ; move to start
G1 X217.5 Y127 F12000 ; move to start
G1 X219.5 Y127 E0.1118 F1800 ; 7
G1 X219.5 Y125 E0.1118 F1800 ; 7
G1 X219.5 Y123 E0.1118 F1800 ; 7
G1 E-0.8 F2400 ; retract
G1 Z0.38 F1800 ; zHop
G1 X210.5 Y133 F12000 ; move to start
G1 Z0.28 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X212.5 Y133 E0.1118 F1800 ; 0
G1 X212.5 Y135 E0.1118 F1800 ; 0
G1 X212.5 Y137 E0.1118 F1800 ; 0
G1 X210.5 Y137 E0.1118 F1800 ; 0
G1 X210.5 Y135 E0.1118 F1800 ; 0
G1 X210.5 Y133 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X213.5 Y133 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X213.5 Y133.4 E0.0224 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X214.5 Y133 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X216.5 Y133 E0.1118 F1800 ; 0
G1 X216.5 Y135 E0.1118 F1800 ; 0
G1 X216.5 Y137 E0.1118 F1800 ; 0
G1 X214.5 Y137 E0.1118 F1800 ; 0
G1 X214.5 Y135 E0.1118 F1800 ; 0
G1 X214.5 Y133 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X217.5 Y133 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X217.5 Y135 F12000 ; move to start
G1 X219.5 Y135 E0.1118 F1800 ; 8
G1 X219.5 Y133 E0.1118 F1800 ; 8
G1 X217.5 Y133 E0.1118 F1800 ; 8
G1 X217.5 Y135 E0.1118 F1800 ; 8
G1 X217.5 Y137 E0.1118 F1800 ; 8
G1 X219.5 Y137 E0.1118 F1800 ; 8
G1 X219.5 Y135 E0.1118 F1800 ; 8
G1 E-0.8 F2400 ; retract
G1 Z0.38 F1800 ; zHop
G1 X210.5 Y143 F12000 ; move to start
G1 Z0.28 F1800 ; zHop
G1 E0.8 F2400 ; un-retract
G1 X212.5 Y143 E0.1118 F1800 ; 0
G1 X212.5 Y145 E0.1118 F1800 ; 0
G1 X212.5 Y147 E0.1118 F1800 ; 0
G1 X210.5 Y147 E0.1118 F1800 ; 0
G1 X210.5 Y145 E0.1118 F1800 ; 0
G1 X210.5 Y143 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X213.5 Y143 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X213.5 Y143.4 E0.0224 F1800 ; dot
G1 E-0.8 F2400 ; retract
G1 X214.5 Y143 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X216.5 Y143 E0.1118 F1800 ; 0
G1 X216.5 Y145 E0.1118 F1800 ; 0
G1 X216.5 Y147 E0.1118 F1800 ; 0
G1 X214.5 Y147 E0.1118 F1800 ; 0
G1 X214.5 Y145 E0.1118 F1800 ; 0
G1 X214.5 Y143 E0.1118 F1800 ; 0
G1 E-0.8 F2400 ; retract
G1 X217.5 Y143 F12000 ; move to start
G1 E0.8 F2400 ; un-retract
G1 X219.5 Y143 E0.1118 F1800 ; 9
G1 X219.5 Y145 E0.1118 F1800 ; 9
G1 X217.5 Y145 E0.1118 F1800 ; 9
G1 X217.5 Y147 E0.1118 F1800 ; 9
G1 X219.5 Y147 E0.1118 F1800 ; 9
G1 X219.5 Y145 E0.1118 F1800 ; 9
G1 E-0.8 F2400 ; retract
G1 Z0.38 F1800 ; zHop
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