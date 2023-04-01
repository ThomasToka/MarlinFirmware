# Change Log Marlin bugfix-2.1.x fork for Ender 3 S1 Pro/Plus/noneProPlus
This is a fork of a fork.

The initial port of the Creality lcd_rts.cpp was made by Synman.

After this i forked Synmans repository and created my own fork.

All notable changes to this project will be documented in this file.

I hope you like my work.

## [MARLIN-E3S1FORK-BYTT-2-UNRELEASED] - 2023-04-?? (Preview of the next bugfix release)

This is a sneak preview of the comming updates. I will edit this file frequently..
 
### Added
- [MARLIN-E3S1FORK-BYTT-add2] I will include recent marlin commits if they make sense.

### Changed
- [MARLIN-E3S1FORK-BYTT-change2] I changed the behavior of the "print" button for the folders and subfolders. Now the print button enters the sd card on first click, and when you are in a folder or subfolder you can go one folder up with the "print" button. Real navigation.

### Fixed
- [MARLIN-E3S1FORK-BYTT-fix3] Is there something to fix?



## [MARLIN-E3S1FORK-BYTT-1] - 2023-03-31
 
This release is called "M600 fix"

I also reverted a critical linear advance commit. 
2 of about 25 testers experiences printer halts on the skirt. 
Reverting this commit fixed it for one of them.

The second has yet to respond. As i could reproduce this i will push the revert as we did not have this problem before.
 
### Added
- [MARLIN-E3S1FORK-BYTT-add1] Changelog added

### Changed
- [MARLIN-E3S1FORK-BYTT-change1] Buffers reduced as they are not needed so high and sometimes lower buffers (faster reaction of the printer) are better.

before:

#define BLOCK_BUFFER_SIZE  64

#define BUFSIZE 64

#define TX_BUFFER_SIZE 128


now:

#define BLOCK_BUFFER_SIZE  16

#define BUFSIZE 8

#define TX_BUFFER_SIZE 128


### Fixed
- [MARLIN-E3S1FORK-BYTT-fix1] Reverted Linear Advance Marlin commit https://github.com/MarlinFirmware/Marlin/commit/ca77850cbb8ed57d4cdcf29a12a278d6bfa5c0d5
- [MARLIN-E3S1FORK-BYTT-fix2] M600 filament runout fixed. You can now use M600 in your gcode.
