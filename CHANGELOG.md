# Changelog of [MARLIN-E3S1PROFORK-BYTT] based on Marlin bugfix-2.1.x
# for Ender 3 S1 Pro/Plus/noneProPlus

This is a fork of Marlin bugfix-2.1.x and the Creality Ender 3 S1 Pro source code.

As of the release of [MARLIN-E3S1PROFORK-BYTT-4] this port is made by me.

All notable changes to this project will be documented in this file.

I hope you like my work.

I have created a discord server for faster communication https://discord.gg/Fh4jsUJWe6 .

## [MARLIN-E3S1PROFORK-BYTT-9] - 2023-05-10

This release is the prerelease for the screen firmware release. Development features are already in the firmware but not visible yet.
I will deliver the new stable screen firmware in the next 14days.

Users of the beta screen firmware can also install this build. My new developments are transparent and not interfering with the stock screen firmware. So if you use the stock screen you dont see my new developments. 

I had to disable the LASER FEATURE temporary. We are running out of memory and most users dont use it. Maybe it will come back later..

In this release i also fixed the M600 repeating bug. Now it is possible to do multiple M600 as the variables are reset correctly.

### Added
- [MARLIN-E3S1PROFORK-BYTT-add7] I included all marlin upstream commits since the last release.
- [MARLIN-E3S1PROFORK-BYTT-add8] New features added in the backgroud for the upcomming screen release.

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change15] Laser feature deactivated due to low memory.
- [MARLIN-E3S1PROFORK-BYTT-change16] Unifing beta phase code and last release code. 

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix7] M600 can now be used multiple times. 


## [MARLIN-E3S1PROFORK-BYTT-8] - 2023-05-05 Service Release

This is a short service release covering only one problem as i am mid development of the new touchscreen and mainboard firmware.

In this release i fixed zoffset setting on the auxl. lvl. page. It was damaged due to a new introduced logic depending on internal signals. But those signals were not consistent in all ranges. So i reverted to my earlier logic.
 
### Added
- nothing

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change11] CHANGE PENDING! WAITING FOR CONFIRMATION FROM UPSTREAM! I am evaluating the fix of M206. It seems broken after upstream commits.

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix6] Auxl. lvl. zoffset adjusting stopped at -2.08mm. Fixed.

Changelog of already released bugfixes:

## [MARLIN-E3S1PROFORK-BYTT-7] - 2023-04-17

In this release today i again fixed the filament runout sensor. Me myself fatfingered it on the last rebase and so my initial fix was not implemented. Sorry.

I also adjusted the manual leveling points of the Ender 3 S1 Plus. I am not 100% satisfied with it. Further changes will follow. Problematic on this machine is the locked screen firmware to x=300 and y=300. We will see how it works with this release.

### Added
- [MARLIN-E3S1PROFORK-BYTT-add6] I included all marlin upstream commits since the last release.

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change11] CHANGE PENDING! WAITING FOR CONFIRMATION FROM UPSTREAM! I am evaluating the fix of M206. It seems broken after upstream commits.
- [MARLIN-E3S1PROFORK-BYTT-change14] Ender 3 S1 Plus manual leveling points ubl correction. More room for the mesh is possible, so i will adjust this.

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix5] Users report that filament runout sensor is broken again. I can confir that i fatfingered it myself on the last rebase of the code. Fixed again. Sorry.


## [MARLIN-E3S1PROFORK-BYTT-6] - 2023-04-16

In this release i changed the dimensions of Ender 3 S1 Pro slightly to match more users defaults.
The esteps for x and y have been adjusted after testing dimensions and movement width from 80 to 79.5 for x an y.

Added
- [MARLIN-E3S1PROFORK-BYTT-add5] I included all marlin upstream commits since the last release.

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change11] CHANGE Pending. See next release!
- [MARLIN-E3S1PROFORK-BYTT-change12] Dimensional change Ender 3 S1 Pro. X-Min position from -0.8 to -2. 
- [MARLIN-E3S1PROFORK-BYTT-change13] Esteps x and y from 80 to 79.5 to have better dimensional accuracy of printed parts.

### Fixed
tba

## [MARLIN-E3S1PROFORK-BYTT-5] - 2023-04-15

This release mainly covers UBL functionality. The mesh area has been extended and the manual leveling points changed to match the new location of the autoleveling points. it has still 45 mm clearance on the back as the probe can not reach much more (probe offset exactly. so 45mm is 3.2mm near to this and ok to have some clearance.)
 
### Added
- [MARLIN-E3S1PROFORK-BYTT-add4] I included all marlin upstream commits since the last release.

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change8] The display will show which version is installed exactly (abl5x5-byTT,ubl5x5-byTT, etc..).
- [MARLIN-E3S1PROFORK-BYTT-change9] Change all UBL builds to new coordinates. Accordingly the manual leveling points will be adjusted to match the autoleveling points. Change is from 45mm mesh_inset all around to. 27mm for left (EDIT: Added 2mm for cable clearance), right and front and 45 mm for the back as the probe cant reach more. Movement area extended with +6 on X. 
- [MARLIN-E3S1PROFORK-BYTT-change10] As of now i will release the releases on the releases page https://github.com/ThomasToka/MarlinFirmware/releases

### Fixed
- nothing had to be fixed..

Changelog of already released bugfixes:

## [MARLIN-E3S1PROFORK-BYTT-4] - 2023-04-09

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ATTENTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 

With the next release i will release a self forked version of the Creality Ender 3 S1 Pro code based on Marlin bugfix-2.1.x with todays commits.

To comply with the GPL i will also release my fixed source files to publicity within 30 days after release.

I want to make sure released source files are fixed as the port of all this was a lot of codeing.

But hell. Yeah i did it. Just with the help the existing repositories by Creality and the initial old port of Synman.

I have taken the original Creality files and upgraded/updated those to match with actual marlin.

 
### Added
- [MARLIN-E3S1PROFORK-BYTT-add4] I included all marlin upstream commits.

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change4] Ender 3S1 Pro build top z limit from 250mm to 270mm.
- [MARLIN-E3S1PROFORK-BYTT-change5] Sd cardreader shows 5 pages/files per page not 4 like the stock or other firmwares
- [MARLIN-E3S1PROFORK-BYTT-change6] Complete code rebase on Marlin bugfix-2.1.x and the initial port by Synman.
- [MARLIN-E3S1PROFORK-BYTT-change7] Name change of the fork from [MARLIN-E3S1FORK-BYTT] to [MARLIN-E3S1PROFORK-BYTT] in order to make clear that this is not a professional firmware clone.

### Fixed
tba


## [MARLIN-E3S1PROFORK-BYTT-3] - 2023-04-03

This is a sneak preview of the comming updates. I will edit this file frequently..
 
### Added
- [MARLIN-E3S1PROFORK-BYTT-add3] Some non relevant Marlin commits were included.

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change3] The S1 non Pro/Plus version has been rebased on the actual Marlin bufix-2.1.x as there is no toch class needed and it is easier to maintain a recent marlin for the DWIN_CREALITY_LCD. Laser support vanished out of this version for now. Maybe i will include it sometime.

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix4] M600, pause and filament runout for the Ender 3 S1 nonProPlus with the encoder display. 



## [MARLIN-E3S1PROFORK-BYTT-2] - 2023-04-02

The following adds/changes/fixes delivered with this release.
 
### Added
- [MARLIN-E3S1PROFORK-BYTT-add2] minor important marlin commits were added

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change2] I changed the behavior of the "print" button for the folders and subfolders. Now the print button enters the sd card on first click, and when you are in a folder or subfolder you can go one folder up with the "print" button. Real navigation.

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix3] ubl7x7 finished percentage does not match and is stuck at 98%. With this release this visual bug is fixed.



## [MARLIN-E3S1PROFORK-BYTT-1] - 2023-03-31
 
This release is called "M600 fix"

I also reverted a critical linear advance commit. 
2 of about 25 testers experiences printer halts on the skirt. 
Reverting this commit fixed it for one of them.

The second has yet to respond. As i could reproduce this i will push the revert as we did not have this problem before.
 
### Added
- [MARLIN-E3S1PROFORK-BYTT-add1] Changelog added

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change1] Buffers reduced as they are not needed so high and sometimes lower buffers (faster reaction of the printer) are better.

before:

#define BLOCK_BUFFER_SIZE  64

#define BUFSIZE 64

#define TX_BUFFER_SIZE 128


now:

#define BLOCK_BUFFER_SIZE  16

#define BUFSIZE 8

#define TX_BUFFER_SIZE 128


### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix1] Reverted Linear Advance Marlin commit https://github.com/MarlinFirmware/Marlin/commit/ca77850cbb8ed57d4cdcf29a12a278d6bfa5c0d5
- [MARLIN-E3S1PROFORK-BYTT-fix2] M600 filament runout fixed. You can now use M600 in your gcode.

-------------------------------------------------------------------------------------------------------------------
Old changelog for historical purposes:


Update 30.03.2023 01:06 CET:

Today i released a new major update of my fork.

"folders and subfolders" support has been added to the firmware.

You can now open folders and subfolders and load files out of these.

There are some minor optimizations to do but overall it works.

You can open folder with 8 chars or less, more chars folders wont be opened!

Enjoy!

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




