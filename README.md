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
- M502 ; factory reset
- M851 Z-1.74 ; set your z-offset
- M500 ; save configuration
- M503 ; check if your z-offset matches
- G28 ; home your printer
- on the touch start autoleveling
- after autoleveling your are ready to print.

Be carefully with your printer. Mine works fine. But this is a new build. So have your fingers near the power button when lowering your z-axis and starting print for the first time.

Please open an issue if there is something wrong.
