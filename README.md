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
- heat up nozzle and/or bed like usually do before bedleveling
- on the touch start autoleveling (there is no need to do the points if your bed was level before..)
- after autoleveling your are ready to print.

Alternative method:

Do it your way as usual. You can set your z-offset by gcode, by touch display, by other terminal. However you do it.
This firmware is installable as every other firmware.

Note:
Touch display firmware 1.0.2 or 1.0.3 is required.
But if you have the recent vendor firmware running you should have already one of this touch firmware versions installed and be fine.

The folder for the F4 installation on the sdcard is STM32F4_UPDATE .
Put the firmware inside this folder on a 4096kb formated sdcard.

Reboot your printer.

-------------------------------------------------------------------------------------------------------------------
Update 23.02.2023 19:47 CET:

Todays update is that there is no update needed. lol
Today i helped some testers, among there was on Ender S1 plus user wanting my firmware to use 300°C.
No problem.. So i gethered measurements from the printer and sent him a version.
He was not able to set 300°C.. My directly thought and after code review verified: "hm thats fishy af. haha, it will be the touch screen firmware!".
We then installed the Ender 3 S1 Pro touch firmware version to break this barrier. double lol.

It works. All other parameters seem also match.

Again one happy person..

I will release a version for the Ender 3 S1 Plus with touch display and the Ender 3 S1 with knob display soon.
I am just gathering some informations and needed measurements. The firmware base is ready to rock also those machines.
-------------------------------------------------------------------------------------------------------------------
Update 21.02.2023 22:11 CET:

Pushed a new update called "performance and quality" update.
- increased buffers as we have enough ram for better sd card and octoprint performance
- rebased on upstream fixes and again manually fixed upstream babystepping that is still not functional with 0.01 mm babysteps
- increased min_segementtime
- increased feedrates for faster printing with "reasonable" barriers
-------------------------------------------------------------------------------------------------------------------
Update 16.02.2023 21:31 CET:

Todays release is mainly a service and quality release.
I fixed babystepping while printing as it is broken upstream.
Enjoy :)
-------------------------------------------------------------------------------------------------------------------
Update 13.02.2023 0:13 CET:

Today i ported all my config tweaks back and released a version of Marlin 2.0.8 with the Ender 3 S1 Pro upstream implementations.
Version 2.0.8 supports also the laser!
I also rebuild my 2.1.2 release and implemented all upstream fixes.
And by the way: I recalibrated my own printers belts which were way to loose :-)
Had wobbles today.. But also with the stock firmware.. Belts tightend. Wobbles way better :-)
Will check deeper tomorrow.
-------------------------------------------------------------------------------------------------------------------
Update 10.02.2023 10:59 CET:

Updated binaries have been released. Its just a small Fix:
The bed is 235x235, standard lcd_rts.cpp, the class managing lcd display only supports integer ex 117. But the bed middle is 235/2=117.5 .
So i had to hardcode it to respect the .5 decimal.
Works perfectly. 

Now my firmware is technically complete, besides laser functionality which is not functional in upstream Marlin-2.1.x-pro-s1 source.
So i will have to wait with this till upstream is functional.
-------------------------------------------------------------------------------------------------------------------
Update 08.02.2023 10:42 CET:

It seems there is bug when pushing touch display fast at initial z-offset configuration via touch screen.
I opened a bug with the builder of this wonderfull peace of software.
https://github.com/synman/Ender-3-S1-Pro-Firmware/issues/20

Update 09.02.2023 10:11 CET:

The touch screen babystepping fast pushing bug has been adressed and (hopefully) fixed. Updated binaries have been uploaded.
Feedback welcome.

-------------------------------------------------------------------------------------------------------------------

Be carefully with your printer. Mine works fine. But this is a new build. So have your fingers near the power button when lowering your z-axis and starting print for the first time.

Please open an issue if there is something wrong.
