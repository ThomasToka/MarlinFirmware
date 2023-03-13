# MarlinFirmware
Personal tweaks and builds of marlin 3d printer firmware repositories.

Source code is here: https://github.com/ThomasToka/MarlinbySynman/tree/bugfix-2.1.x-tweakedbyThomasToka

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
Update 13.03.2023 20:21 CET:

Today i have finalized the laser module integration. Basic workflow works. So it should work if there are no bugs in the code provided by creality.
Additionally i today scripted my build environment to be able to faster build the maintained versions.
Tomorrow i will backport new upstream code fixes into my fork and release new binarys with laser functionality enabled.
Also i will release UBL builds with 5x5, 7x7, 10x10 meeshes.
Many testers gave feedback so i could make this firmware as good as possible.
With the next release the nameing cheme will change:
Like firmware-XXXXXX-YYYY-E3S1Pro-abl5x5-LA-F1.bin or firmware-XXXXXXX-YYYY-E3S1Plus-ubl10x10-LA-F4.bin 

XXXXXX will represent the build day.

YYYYYY will represent the build time.

abl5x5 bilinear bed leveling with 5x5 square mesh

ubl5x5 ubl with 5x5 mesh

ubl7x7 ubl with 7x7 mesh

ubl10x10 ubl with 10x10 mesh

All versions will support laser functionality!

-------------------------------------------------------------------------------------------------------------------
Update 08.03.2023 14:02 CET:

Today i released new builds with some fixes for Linear Advance.
Additionally i added a build for the Ender 3 S1 non Pro with the knob encoder display.
I also uploaded the needed files for the DWIN display and instructions what to do.
-------------------------------------------------------------------------------------------------------------------
Update 27.02.2023 16:40 CET:

Thanks to the testers we have found another bug while sd printing in upstream sources.
So i fixed today:
- fixed filament runount sensor resume not functional
- fixed sd print pause resume not functional

New binarys have been released.

And a good day for Ender 3 S1 Plus users: Also thanks to the testers i am now able to support Ender 3 S1 Plus with 310x315 heatbed.
Just pushed first Release for it!

Happy printing and filament changeing!
------------------------------------------------------------------------------------------------------------------
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
