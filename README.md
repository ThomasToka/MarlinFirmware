# MarlinFirmware
Personal tweaks and builds of marlin 3d printer firmware repositories.

Source code is here: https://github.com/ThomasToka/MarlinbySynman/tree/bugfix-2.1.x-tweakedbyThomasToka

Update 08.02.2023 10:42 CET:

It seems there is bug when pushing touch display fast at initial z-offset configuration via touch screen.
I opened a bug with the builder of this wonderfull peace of software.
https://github.com/synman/Ender-3-S1-Pro-Firmware/issues/20

So my instructions for firmware installations are:

- level your bed with old firmware
- note your z-offset ex. -1.74mm
- flash new firmware
- connect with pronterface and issue

M502 ; factory reset
M851 Z-1.74 ; set your z-offset
M500 ; save configuration
M503 ; check if your z-offset matches
G28 ; home your printer
on the touch start autoleveling
after autoleveling your are ready to print.

Instructions: 

Please do the following two tests:

1.)
- best is to start with a leveled bed
- flash the firmware 
- reset to defaults via screen
- heat up nozzle and bed to your desired temerature
- g28
- got to leveling on the screen
- got to point 2
- set initial z-offset on this point that it has a around 2mm clearance (this is not final leveling
- go to points 3,4,5 an check if it nozzle to bed matches point 2, turn the wheels under bed to patch those 2 mm..
- go back to point 2, lower your z-offset to your desired height via screen (paper method, gauge, etc)
- go to points 3,4,5 and adjust those with the wheels to match point 2
- go around 2-3 times
- do not touch point 1
- go to leveling -> auto leveling, press start
- after this your are ready to print
- watch your g-code for the x position of your purge lines. your bad now starts exactly at x=0 and y=0

2.)
- best is to start with a leveled bed
- flash the firmware 
- reset to defaults via screen
- heat up nozzle and bed to your desired temerature
- g28
- got to leveling on the screen
- got to point 1
- set initial z-offset on this point that it has a around 2mm clearance (this is not final leveling
- go to points 2,3,4,5 an check if it nozzle to bed matches point 1, turn the wheels under bed to patch those position..
- go back to point 1, lower your z-offset to your desired height via screen (paper method, gauge, etc)
- go to points 2,3,4,5 and adjust those with the wheels to match point 2
- go around 2-3 times
- do not touch point 1 after your can go around 2,3,4,5 with same height
- go to leveling -> auto leveling, press start
- after this your are ready to print
- watch your g-code for the x position of your purge lines. your bad now starts exactly at x=0 and y=0

What is interessting in those two tests:

1) is your nozzle z-offset correct when the print starts on both?
2) are there any differences between those two tests in the resulting shown z-offsets?

Be carefully with your printer. Mine works fine. But this is a test. So have your fingers near the power button when lowering your z-axis.

Please open an issue if there is something wrong.
