# Changelog of [MARLIN-E3S1PROFORK-BYTT] based on Marlin bugfix-2.1.x
# for Ender 3 S1 Pro/Plus/noneProPlus

This is a fork of Marlin bugfix-2.1.x and the Creality Ender 3 S1 Pro source code.

As of the release of [MARLIN-E3S1PROFORK-BYTT-4] this port is made by me.

All notable changes to this project will be documented in this file.

I hope you like my work.

I have created a discord server for faster communication https://discord.gg/Fh4jsUJWe6 .

If you like my work please support me with a donation:

Paypal: https://www.paypal.me/ThomasToka

Patreon: https://www.patreon.com/ThomasToka

Github Sponsors: https://github.com/sponsors/ThomasToka

## [MARLIN-E3S1PROFORK-BYTT-v022] - 2023-12-12

This release i call "The dynamic probes update".

Santa Claus was early this year. I wish you great winter holidays and merrry christmas.

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add93] added dynamic probes. you can now choose 1-5 probes for autoleveling, cr-touch measuring and assisted tramming
- [MARLIN-E3S1PROFORK-BYTT-add94] added assisted tramming on the cr-touch site

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change68] removed select print file scrolling on mainsite
- [MARLIN-E3S1PROFORK-BYTT-change69] rearranged main site with new select file field
- [MARLIN-E3S1PROFORK-BYTT-change70] - selected print file shown on main site has now three visibility functions 
  1) under 25 chars centered and bigger 
  2) from 26 to 55 chars left arranged and in two rows.
  3) over 55 chars like 2 but cropped to 55 chars
- [MARLIN-E3S1PROFORK-BYTT-change71] cardreader now supports filenames up to 55 chars shown in 2 lines
- [MARLIN-E3S1PROFORK-BYTT-change72] adjusted M117 messages to be shown like a select file with the 3 mentioned options
- [MARLIN-E3S1PROFORK-BYTT-change73] restructured lcd_rts code with new classes. it saved around 4k flash space
- [MARLIN-E3S1PROFORK-BYTT-change74] rearranged address space for cardreader update
- [MARLIN-E3S1PROFORK-BYTT-change75] with this release the firmware is not more backward compatible to the stock firmware. 
  this means you cant mix screen of stock and my firmware anymore. 
  naturally a downgrade to both stock mainboard and stock screen firmware is still possible.

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix37] fixed folders and files accounting so always the correct site number is shown
- [MARLIN-E3S1PROFORK-BYTT-fix38]fixed inability to enter the adjust site during printing when G29 was in the start Gcode due to a wrong routing in g29cpp and ubl_g29.cpp

## [MARLIN-E3S1PROFORK-BYTT-v021] - 2023-12-05

This release i call "The mesh colors update part 2".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add86] added main site preheat shortcuts (inactive during print)
- [MARLIN-E3S1PROFORK-BYTT-add87] added main site cool and off toggle for temps/fans (inactive during print)
- [MARLIN-E3S1PROFORK-BYTT-add88] added optional M73 functionality toggle to show slicer time
- [MARLIN-E3S1PROFORK-BYTT-add89] added M600 on demand functionality (active during print)
- [MARLIN-E3S1PROFORK-BYTT-add90] added mesh status on main site
- [MARLIN-E3S1PROFORK-BYTT-add91] added in and out extrusion on the pause sites
- [MARLIN-E3S1PROFORK-BYTT-add92] introduced new classes to save flash space

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change66] meshes are now colored
- [MARLIN-E3S1PROFORK-BYTT-change67] reworked about site for qrcode display

### Fixed
- nothing had to be fixed

## [MARLIN-E3S1PROFORK-BYTT-v020] - 2023-11-26

This release i call "The instructions update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add82] added hints on cr-touch measuring site
- [MARLIN-E3S1PROFORK-BYTT-add83] added hints on manual tramming site
- [MARLIN-E3S1PROFORK-BYTT-add84] added a guard to not overflow the display on loading a too big gcode preview image
- [MARLIN-E3S1PROFORK-BYTT-add85] secured mesh size change on leveling


### Changed
- [MARLIN-E3S1PROFORK-BYTT-change61] changed behavior of the home button on cr-touch measuring site
- [MARLIN-E3S1PROFORK-BYTT-change62] changed behavior of the home button on the manual tramming site
- [MARLIN-E3S1PROFORK-BYTT-change63] changed linear advance to 3 digits.
- [MARLIN-E3S1PROFORK-BYTT-change64] changed default linear advance K value to 0.035
- [MARLIN-E3S1PROFORK-BYTT-change65] increased gcode preview image size to 24KB by moving it from 0xB000 to 0xA000

### Fixed
- nothing had to be fixed

## [MARLIN-E3S1PROFORK-BYTT-v019] - 2023-11-24

This release i call "The rectangle update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add78] I included all marlin upstream commits since the last release
- [MARLIN-E3S1PROFORK-BYTT-add79] active mesh points have now a rectangle
- [MARLIN-E3S1PROFORK-BYTT-add80] secured mesh edit on leveling
- [MARLIN-E3S1PROFORK-BYTT-add81] secured mesh size change on leveling


### Changed
- [MARLIN-E3S1PROFORK-BYTT-change59] screen updates to reflect the rectangles
- [MARLIN-E3S1PROFORK-BYTT-change60] stripped code down and removed unneeded code

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix34] screen fixed to have a consistent output on page change
- [MARLIN-E3S1PROFORK-BYTT-fix35] 7x7 mesh site on dacai displays now shows all rows consistent
- [MARLIN-E3S1PROFORK-BYTT-fix36] mainboard firmware fixed to not show a wrong mesh size site on autoleveling start

## [MARLIN-E3S1PROFORK-BYTT-v018] - 2023-11-18

This release i call "The mesh colors update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add75] I included all marlin upstream commits since the last release
- [MARLIN-E3S1PROFORK-BYTT-add76] mesh viewer now shows a coloured mesh after generation
- [MARLIN-E3S1PROFORK-BYTT-add77] folders and files colors (folders blue, files white)

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change56] reduced variables on startup
- [MARLIN-E3S1PROFORK-BYTT-change57] rearranged the plus tramming point 1 to be in the middle of 310x310 size
- [MARLIN-E3S1PROFORK-BYTT-change58] lots of unused variables deleted

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix32] fixed default preview pic reset on sd card pull
- [MARLIN-E3S1PROFORK-BYTT-fix33] fixed folders and files icons reset on sd card pull

## [MARLIN-E3S1PROFORK-BYTT-v017] - 2023-11-15

This release i call "The file and folder icons update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add72] I included all marlin upstream commits since the last release
- [MARLIN-E3S1PROFORK-BYTT-add73] folders and files icons
- [MARLIN-E3S1PROFORK-BYTT-add74] folders and files colors (folders blue, files white)

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change54] stripping of the gcode preview class to save flash without interferance of our functionality
- [MARLIN-E3S1PROFORK-BYTT-change55] BLTOUCH_HS_MODE default on removed as it is enabled on mesh change on request and saves flash

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix31] probe pull up after reboot fix

## [MARLIN-E3S1PROFORK-BYTT-v016] - 2023-11-03

This release i call "The dynamic ubl update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add69] ubl builds are now able to switch between mesh sizes (5x5,7x7,10x10) without reboot and loosing settings
- [MARLIN-E3S1PROFORK-BYTT-add70] ubl builds are now able to change the margin for x and y like abl builds
- [MARLIN-E3S1PROFORK-BYTT-add71] ubl builds now take also the probe offsets into account and maybe work with the 0 y offset (please report if it still fails!)

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change51] reworked mesh sites to reflect mesh switch for ubl builds
- [MARLIN-E3S1PROFORK-BYTT-change52] adjusted the following parameters: LA 0.05 to 0.03, Jerk X/Y 12 to 20, Jerk E to 0.4 to 0.6, Jerk Z 5 to 10, Default Max Acceleration E 1000 to 5000
- [MARLIN-E3S1PROFORK-BYTT-change53] changed nameing of "Hotend offsets" to the better matching term "Probe offsets"

### Fixed
- nothing had to be fixed

## [MARLIN-E3S1PROFORK-BYTT-v015] - 2023-10-27

This release i call "The dynamic abl mesh size update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add66] I included all marlin upstream commits since the last release
- [MARLIN-E3S1PROFORK-BYTT-add67] abl builds are now able to switch between mesh sizes (5x5,7x7,10x10) without reboot and loosing settings
- [MARLIN-E3S1PROFORK-BYTT-add68] added min, max and dev to the mesh sites and calculate the mesh deviation after the autoleveling run

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change49] reworked mesh sites to reflect mesh switch
- [MARLIN-E3S1PROFORK-BYTT-change50] disabled GCODE_REPEAT_MARKERS to safe flash

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix30] fixed power loss recovery in all builds

## [MARLIN-E3S1PROFORK-BYTT-v014] - 2023-10-13

This release i call "The mesh edit update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add65] mesh points are now editable (abl and ubl)

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change48] reworked mesh sites to reflect mesh editing functions

### Fixed
- nothing had to be fixed

## [MARLIN-E3S1PROFORK-BYTT-v013] - 2023-10-09

This release i call "The pause at height update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add64] I included all marlin upstream commits since the last release

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change46] powerloss recovery POWER_LOSS_MIN_Z_CHANGE 0.05 changed to POWER_LOSS_MIN_Z_CHANGE 0.1
- [MARLIN-E3S1PROFORK-BYTT-change47] reworked several sites to show the power loss and runout sensor toggle

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix29] M0 aka "pause at height" is now functional and has its own wiki entry


## [MARLIN-E3S1PROFORK-BYTT-v012] - 2023-09-25

This release i call "The dynamic abl y margin update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add63] the y margin is now unbound of the x margin and can be set separately. it has a min of 10 if you for example use a 0 x offset.

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change42] the x and y margins take the probe offsets into account and will adjust the set value to the maximum hardware boundries for each axis.
- [MARLIN-E3S1PROFORK-BYTT-change43] the cardreader is now able to enter folders up to 65 chars. folders between 20 and 65 chars will be cropped to 20 chars but are still enterable.
- [MARLIN-E3S1PROFORK-BYTT-change44] the mesh sites have been reworked to reflect the dynamic x and y margins
- [MARLIN-E3S1PROFORK-BYTT-change45] the cr-touch measurement site has been reworked to reflect the dynamic x and y margins

### Fixed
- nothing had to be fixed

## [MARLIN-E3S1PROFORK-BYTT-v011] - 2023-09-19

This release i call "The progress bar update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add62] changed scrolling behavior: it now stops if another button than the home button is pressed. pressing "print" invalidates scrolling also.

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change40] replaced printing progress bar with a self developed version to have better visuality of the percentage.
- [MARLIN-E3S1PROFORK-BYTT-change41] cardreader now supports/reads filenames up to 65 chars (incl.filextension)

### Fixed
- nothing had to be fixed

## [MARLIN-E3S1PROFORK-BYTT-v010] - 2023-09-14

This release i call "The printfile scrolling update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add60] selected printfile now scrolls if the filename is longer than 16 chars (incl. fileextension) once. pushing on "home" lets the filename scroll again. pushing once on "print" to enter the filelist invalidates scrolling for the already chosen file and also fileprint is then not possible. scrolling starts again if you load another file. starting print is also possible if you load another file after you entered "print" once with a loaded file.
- [MARLIN-E3S1PROFORK-BYTT-add61] while scrolling the response of the display for other clicks may be blocked

### Changed
- nothing had to be changed

### Fixed
- nothing had to be fixed

## [MARLIN-E3S1PROFORK-BYTT-v009] - 2023-09-12

This release i call "The cr-touch measuring dynamic margin update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add57] I included all marlin upstream commits since the last release
- [MARLIN-E3S1PROFORK-BYTT-add58] added new variable manual_crtouch_5position to unbind the crtouch positions from the manual_level_5position as they go further cause with those the nozzle moves to the set position. the cr-touch is not capable to reach this positions.
- [MARLIN-E3S1PROFORK-BYTT-add59] gcode preview for supersclicer (working) and orca slicer (mostly not working. it seems the generated thumbnails are simply too big) in 250x250px

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change36] dynamic probing margin for abl builds now is also respected for the cr-touch measuring site, so the points have the margin set from the edge
- [MARLIN-E3S1PROFORK-BYTT-change37] changed ubl margins for Ender 3 S1 Pro to front 25 back 45 to cover more
- [MARLIN-E3S1PROFORK-BYTT-change38] changed ubl margins for Ender 3 S1 Plus to most possible front 27 and back 45 to cover more 
- [MARLIN-E3S1PROFORK-BYTT-change39] increased x_max_position for the Ender 3 S1 Pro from 241 to 242 to allow 25mm probing margin as 242-32(hotened offset x)=210. and that we need if we want to set 25 as probing margin as 235-25=210.

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix28] fixed cr-touch autorun multiple starts. a variable prevents now a second run while running. after it finishes the variable is reset so a new run can be started.


## [MARLIN-E3S1PROFORK-BYTT-v008] - 2023-09-03

This release i call "The gcode preview update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add53] I included all marlin upstream commits since the last release
- [MARLIN-E3S1PROFORK-BYTT-add54] gcode preview for prusa slicer, creality slicer, cura in 250x250px
- [MARLIN-E3S1PROFORK-BYTT-add55] gcode preview wiki site with own scripts and instructions: https://github.com/ThomasToka/MarlinFirmware/wiki/Gcode-preview
- [MARLIN-E3S1PROFORK-BYTT-add56] new environment for F1 RC chipset with 256KB, F1 now has F1-RC (256KB) and F1-RE (512KB) builds

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change32] front, pause, resume sites changed to show gcode preview
- [MARLIN-E3S1PROFORK-BYTT-change33] rearranged front, pause, resume sites functionaly (powerloss toggle, runout toggle)
- [MARLIN-E3S1PROFORK-BYTT-change34] disabled G26 mesh validation test to save flash 
- [MARLIN-E3S1PROFORK-BYTT-change35] reverted Ubl dynamic change prepare as it does not work like abl

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix27] changed the icons on the acceleration site


## [MARLIN-E3S1PROFORK-BYTT-v007] - 2023-08-20

This release i call "The display features update".

EDIT: 08/15/2023: I hotfixed the hotend offset function as it did not do what it should. it simply went in the wrong direction. Sorry!

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add51] added the ability to manipulate the abl probing margin (25-100, default is 45)
- [MARLIN-E3S1PROFORK-BYTT-add52] prepared system for more dynamic manipulation

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change31] changed MAX_FEEDRATE_EDIT_VALUES and MAX_ACCEL_EDIT_VALUES from 3000 to 9999 for x and y for input shaping calibration

### Fixed
nothing had to be fixed
  
## [MARLIN-E3S1PROFORK-BYTT-v006] - 2023-08-13

This release i call "The display features update".

EDIT: 08/15/2023: I hotfixed the hotend offset function as it did not do what it should. it simply went in the wrong direction. Sorry!

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add44] I included all marlin upstream commits since the last release
- [MARLIN-E3S1PROFORK-BYTT-add45] added the ability to manipulate the sound (toggle should work for all)
- [MARLIN-E3S1PROFORK-BYTT-add46] prepared the ability to manipulate the sound with pads (implemented correctly, but seems not to work!)
- [MARLIN-E3S1PROFORK-BYTT-add47] added the ability to manipulate the display brightness
- [MARLIN-E3S1PROFORK-BYTT-add48] added the ability to manipulate the display standby brightness
- [MARLIN-E3S1PROFORK-BYTT-add49] added the ability to manipulate the display standby timeout
- [MARLIN-E3S1PROFORK-BYTT-add50] added a sound off/on toggle on the main, resume, pause and finish site

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change30] prepared the system for a lcd_rts_settings data struct which is saved in eeprom (display features use this already!)
  
### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix25] fixed eeprom saving of parameters in bigger builds
- [MARLIN-E3S1PROFORK-BYTT-fix26] ***hotfixed past release*** i had to hotfix the hotend offset function cause it die not work as expected. new binaries uploaded on 08/15/2023

## [MARLIN-E3S1PROFORK-BYTT-v005] - 2023-08-05

This release i call "The return of 10x10 ubl and cardreader update".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add40] I included all marlin upstream commits since the last release
- [MARLIN-E3S1PROFORK-BYTT-add41] readded 10x10 ubl builds as they work as intended.
- [MARLIN-E3S1PROFORK-BYTT-add42] added cardreader site accounting (also for the laser part).
- [MARLIN-E3S1PROFORK-BYTT-add43] added temperature adjustment on the main site.

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change29] changed cardreader max files per folder from 20 to 40.
  
### Fixed
nothing had to be fixed

## [MARLIN-E3S1PROFORK-BYTT-v004] - 2023-07-28

This release i call "The laser feature and power loss recovery release".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add35] I included all marlin upstream commits since the last release
- [MARLIN-E3S1PROFORK-BYTT-add36] added better barriers for the home offset pads to not break out to max position
- [MARLIN-E3S1PROFORK-BYTT-add37] added a power loss recovery status and toggle on main and resume sites. it updates on each entering of the site.
- [MARLIN-E3S1PROFORK-BYTT-add38] added a extruder flowrate status and toggle on main and resume sites. it updates on each entering of the site.
- [MARLIN-E3S1PROFORK-BYTT-add39] added a reset of the mesh on autoleveling start
- [MARLIN-E3S1PROFORK-BYTT-add40] added a check for a running autoleveling so it is not possible to "queue" a second run or reset the running mesh while autoleveling is running

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change28] removed 10x10 builds for now as they dont save to eeprom. investigating this.
  
### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix20] fixed laser feature PWM Range. Now it supports standard gcode that also works in stock firmware.
- [MARLIN-E3S1PROFORK-BYTT-fix21] fixed general laser feature gcode parsing for the range for example.
- [MARLIN-E3S1PROFORK-BYTT-fix22] fixed tramming point 1 on the autorun which was not functional
- [MARLIN-E3S1PROFORK-BYTT-fix23] fixed basic power loss recovery functionality. Attention: USE at your own risk. I see a marlin bug here where the extruder sometimes extrudes much on the resume position. It is under investigation. But i release this now as it the part that i coudl fix is fixed. Now its on marlin devs to fix the rest.
- [MARLIN-E3S1PROFORK-BYTT-fix24] fixed some minor visual missalignments (ex. mesh 7x7 on dacai)


## [MARLIN-E3S1PROFORK-BYTT-v003] - 2023-07-19

This release i call "The 5x5 7x7 10x10 release".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add29] I included all marlin upstream commits since the last release
- [MARLIN-E3S1PROFORK-BYTT-add30] added the ability to adjust hotend flow and included this in M503 report
- [MARLIN-E3S1PROFORK-BYTT-add31] added the ability to change hotend flow, input shaping, linear advance during print
- [MARLIN-E3S1PROFORK-BYTT-add32] added 7x7 10x10 abl builds including meshviewer integration
- [MARLIN-E3S1PROFORK-BYTT-add33] added 7x7 10x10 ubl builds including meshviewer integration
- [MARLIN-E3S1PROFORK-BYTT-add34] added the ability to use gcode repeat markers with M808

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change27] extended the new home offset functionality and reworked the home offset page
  
### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix18] fixed tramming point 1 on the autorun which was not functional
- [MARLIN-E3S1PROFORK-BYTT-fix19] fixed runout sensor mocking for filament on print start or resume from pause if runout sensor was off but no filament in the sensor


## [MARLIN-E3S1PROFORK-BYTT-v002] - 2023-07-15

This release i call "The return of UBL and M206 release".

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add24] I included all marlin upstream commits since the last release and PR #25996.
- [MARLIN-E3S1PROFORK-BYTT-add25] added the ability to set x_min_pos and y_min_pos for better printable area calibration over touch or with M206. Marlin PR #25996
- [MARLIN-E3S1PROFORK-BYTT-add26] reintroduced ubl5x5 build and integrated with meshviewer (laser disabled in ubl build!)
- [MARLIN-E3S1PROFORK-BYTT-add27] added offsetrouting page for home offset and hotend offset
- [MARLIN-E3S1PROFORK-BYTT-add28] added runout sensor on/off on front page, pause and resume pages

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change25] secured auxl. lvl and cr-touch pages points in case of "M84" motors off. G28 will be forced before a point can be used after M84.
- [MARLIN-E3S1PROFORK-BYTT-change26] changed sound on/off setting serial output to human readable (dacai displays still cant on/off the sound)
  
### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix14] fixed some screen firmware buttons
- [MARLIN-E3S1PROFORK-BYTT-fix15] fixed leading 0 of the remaining time minutes not shown while printing in the screen firmware
- [MARLIN-E3S1PROFORK-BYTT-fix16] fixed saving of input shaping frequency so it survives a reboot.
- [MARLIN-E3S1PROFORK-BYTT-fix17] fixed start button status after autoleveling back to not pushed


## [MARLIN-E3S1PROFORK-BYTT-v001] - 2023-06-09

This is the final release of MARLIN-E3S1PROFORK-BYTT.

With this version we beginn at v001 as version number.

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add20] I included all marlin upstream commits since the last release.
- [MARLIN-E3S1PROFORK-BYTT-add21] sound off/on toggle added. it seems not to work on most dacai displays. i have both dwin and dacai and here it works on both. to be fixed for all..
- [MARLIN-E3S1PROFORK-BYTT-add22] source code release and pull request to marlin upstream
- [MARLIN-E3S1PROFORK-BYTT-add23] added the abilty to stop and pause a host print (ex. from octoprint). but there will be not popus. resume is to be done on touch or on the "resume" button in octoprint.

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change24] aux.lvl and cr-touch page reworked

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix13] fixed manual leveling/cr-touch points on Ender 3 S1 Plus again as there was a typo.


## [MARLIN-E3S1PROFORK-BYTT-rc4] - 2023-06-02

This is the last release candidate release before the final release.

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add16] I included all marlin upstream commits since the last release.
- [MARLIN-E3S1PROFORK-BYTT-add17] added "Autorun" on the CR-Touch measuring page to initially measure the five points automatically
- [MARLIN-E3S1PROFORK-BYTT-add18] added icons on the Manual Tramming and Cr-Touch measuring page
- [MARLIN-E3S1PROFORK-BYTT-add19] added the ability to stop a octoprint print with the touch displays stop button

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change21] extended the deciamals to 3 on the CR-Touch measuring page to be consistent with the meshviewer
- [MARLIN-E3S1PROFORK-BYTT-change22] changed output of autopid to serial to a human readable understandable output
- [MARLIN-E3S1PROFORK-BYTT-change23] removed debug headers

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix11] fixed visual discrepancy on the touch and terminal output while running autopid
- [MARLIN-E3S1PROFORK-BYTT-fix12] visual corrections on pidrouting page


## [MARLIN-E3S1PROFORK-BYTT-rc3] - 2023-05-27

In this release the following additions/changes/fixes have been made:

### Added
- [MARLIN-E3S1PROFORK-BYTT-add12] I included all marlin upstream commits since the last release.
- [MARLIN-E3S1PROFORK-BYTT-add13] extended preset materials to 4. PLA,ABS,PETG,CUST (for Custom)
- [MARLIN-E3S1PROFORK-BYTT-add14] input shaping manipulation via touch added on the acceleration site
- [MARLIN-E3S1PROFORK-BYTT-add15] added two home buttons on the manual leveleing pages to home after stepper deactivation
- 
### Changed
- [MARLIN-E3S1PROFORK-BYTT-change19] #define HOME_AFTER_DEACTIVATE was activated to force the need of a manual G28 after motor deactivation in every situation
- [MARLIN-E3S1PROFORK-BYTT-change20] x jerk to 12, y jerk to 12

### Fixed
- nothing had to be fixed.

## [MARLIN-E3S1PROFORK-BYTT-rc2] - 2023-05-22

In this release a visual mesh bug was fixed. Mesh was saved and used correctly but the visual output after reboot was not correct as the points were swapped in each line. Technically the correct mesh was used on printing also after reboot where it showed wrong on the mesh visualisation site. rc2 fixes this.

I also added a CR-Toch messurement for points 1,6,7,8,9. points 3,4,5 are not reachable by the probe. Point 2 has no counterparts so also left away. You can enter the messuring mode on the Auxl.Lvl page.

### Added
- [MARLIN-E3S1PROFORK-BYTT-add10] I included all marlin upstream commits since the last release.
- [MARLIN-E3S1PROFORK-BYTT-add11] I added a CR-Touch messurement for points 1,6,7,8,9

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change18] Small changes under the hood to make new features possible.

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix10] meshview loading after reboot visually fixed.


## [MARLIN-E3S1PROFORK-BYTT-rc1] - 2023-05-19

This release is the next major release. So i won´t write the details. 


### Added
- [MARLIN-E3S1PROFORK-BYTT-add9] I included all marlin upstream commits since the last release.

### Changed
- [MARLIN-E3S1PROFORK-BYTT-change17] too much to list. :-) See installation.txt in the release.

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix9] too much to list.


## [MARLIN-E3S1PROFORK-BYTT-10] - 2023-05-11

This release is another service release. During my development i have found a bug in the saving of the mesh to the eeprom. So it is lost after reboot of the printer.

This service release correts this.


### Added
- nothing

### Changed
- nothing

### Fixed
- [MARLIN-E3S1PROFORK-BYTT-fix8] Mesh save after G29 was faulty and not saved.

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




