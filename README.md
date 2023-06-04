### ATTENTION: Binaries moved to https://github.com/ThomasToka/MarlinFirmware/releases ###

# MarlinFirmware fork MARLIN-E3S1PRO-FORK-BYTT

Source code is here: [https://github.com/ThomasToka/Marlin/tree/MARLIN-E3S1PRO-FORK-BYTT]

Source code release will be on the 9th of june 2023.

This firmware is for the Creality Ender 3 S1 Pro and Ender 3 S1 Plus.

It has its own screen firmware for DWIN and Dacai displays. This firmware is backward compatible with the stock
screen display firmware. Naturally then only the stock features are available.

Expect updates of other non patched firmwares with this fixes then.. lol

But hej. I will release the fixes. :-)


-------------------------------------------------------------------------------------------------------------------
My instructions for firmware installations are:

- check your chip inside your printer (look at the about page, usually you will see F4 in the number FW/Ver field)
- for F4 printer create a folder STM32F4_UPDATE on your 4096 formated SD card and put my firmware bin file inside
- for F1 printer it is sufficient to put the firmware bin file inside the root of your 4096 formated SD card
- reboot printer

Note:
Touch display firmware 1.0.2 or 1.0.3 is required. Look at your about page "Screen VER"
But if you have the recent vendor firmware running you should have already one of this touch firmware versions installed and be fine.

Please check your machines start gcode.
Your bed starts now at x=0. Some Slicer default to a negative purge line start point ex x=-2 or very close to the bededge ex x=0.1.
Put it on x=5 or something reasonable beeing good placed on your bed..

Example old:

G1 X-2.1 Y20 Z0.28 F5000.0 ;Move to start position

G1 X-2.1 Y200.0 Z0.28 F1500.0 E15 ;Draw the first line

G1 X-2.4 Y200.0 Z0.28 F5000.0 ;Move to side a little

G1 X-2.4 Y20 Z0.28 F1500.0 E30 ;Draw the second line


Example new:

G1 X5.1 Y20 Z0.28 F5000.0 ;Move to start position

G1 X5.1 Y200.0 Z0.28 F1500.0 E15 ;Draw the first line

G1 X5.4 Y200.0 Z0.28 F5000.0 ;Move to side a little

G1 X5.4 Y20 Z0.28 F1500.0 E30 ;Draw the second line

Check also the set dimensions of the buildplate in your slicer. Most slicers have 220mm x 220 mm (Pro) or 300mm x 300mm (Plus) cause of the not
matching firmware. The bed has 235mm x 235mm on the Pro. On the Plus we have a special situation: The nozzle can´t reach the last 5mm on y max.
So we capped here 5mm. The configured printarea for the Plus is 310mm x 310mm.
Please set this values as your printarea in you slicer.

-------------------------------------------------------------------------------------------------------------------

My instructions for Z-Offset quick setting and installation:
- level your bed with old firmware
- note your z-offset ex. -1.74mm
- flash new firmware
- connect with pronterface or other terminal to your printer and issue:
- M502 ; factory reset
- M851 Z-1.74 ; set your z-offset
- M500 ; save configuration
- M503 ; check if your z-offset matches
- G28 ; home your printer
- heat up nozzle and/or bed like usually do before bedleveling
- on the touch start autoleveling (there is no need to do the points if your bed was level before..)
- after autoleveling your are ready to print.

Alternative method for Z-Offset setting:

Do it your way as usual. You can set your z-offset by gcode, by touch display, by other terminal. However you do it.
This firmware is installable as every other firmware.

-------------------------------------------------------------------------------------------------------------------

Be carefully with your printer. Mine works fine. But this is a new build. So have your fingers near the power button when lowering your z-axis and starting print for the first time.

Please open an issue if there is something wrong.

-------------------------------------------------------------------------------------------------------------------

The changelog has been rebased to: https://github.com/ThomasToka/MarlinFirmware/blob/Firmware-Binaries/CHANGELOG.md

-------------------------------------------------------------------------------------------------------------------
