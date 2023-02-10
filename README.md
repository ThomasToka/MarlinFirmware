# MarlinFirmware
Personal tweaks and builds of marlin 3d printer firmware repositories.

Source code is here: https://github.com/ThomasToka/MarlinbySynman/tree/bugfix-2.1.x-tweakedbyThomasToka

-------------------------------------------------------------------------------------------------------------------
My instructions for firmware installations are:

- level your bed with old firmware
- note your z-offset ex. -1.74mm
- flash new firmware
- connect with pronterface or other terminal to your printer and issue:
- M502 ; factory reset
- M851 Z-1.74 ; set your z-offset
- M500 ; save configuration
- M503 ; check if your z-offset matches
- G28 ; home your printer
- on the touch start autoleveling (there is no need to do the points if your bed was level before..)
- after autoleveling your are ready to print.
-------------------------------------------------------------------------------------------------------------------
Update 08.02.2023 10:42 CET:

It seems there is bug when pushing touch display fast at initial z-offset configuration via touch screen.
I opened a bug with the builder of this wonderfull peace of software.
https://github.com/synman/Ender-3-S1-Pro-Firmware/issues/20

Update 09.02.2023 10:11 CET:

The touch screen babystepping fast pushing bug has been adressed and (hopefully) fixed. Updated binaries have been uploaded.
Feedback welcome.

-------------------------------------------------------------------------------------------------------------------
Update 10.02.2023 10:59 CET:

Updated binaries have been released. Its just a small Fix:
The bed is 235x235, standard lcd_rts.cpp, the class managing lcd display only supports integer ex 170. But the bed middle is 235/2=117.5 .
So i had to hardcode it to respect the .5 decimal.
Works perfectly. 

Now my firmware is technically complete, besides laser functionality which is not functional in upstream Marlin-2.1.x-pro-s1 source.
So i will have to wait with this till upstream is functional.
-------------------------------------------------------------------------------------------------------------------

Be carefully with your printer. Mine works fine. But this is a new build. So have your fingers near the power button when lowering your z-axis and starting print for the first time.

Please open an issue if there is something wrong.
