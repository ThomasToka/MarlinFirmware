Marlin 2.1.x [MARLIN-E3S1PROFORK-BYTT]

This firmware is open source and based Marlin Firmware and the Creality Ender 3 S1 PRO source code.

Additional changes and additions were made by Thomas Toka.

Features Ender 3 S1 Pro:

- bed size (235mmx235mm)
- printing height 270
- correct homeing offsets
- correct nozzle to probe offsets
- z-offset set to 0.0 in order calibrate for your printer
- babystepping while printing fixed and set to 0.01mm steps
- babystepping on leveling page fixed and set to 0.01mm steps
- linear advance set to 0.05
- input shaping activated and set to x 40hz and y 40hz.
- increased buffers for faster octoprint and sd communication
- increased feedrates in reasonable borders for faster printing
- increased min_segmenttime for better quality
- unified bedleveling with a 5x5, 7x7, 10x10 mesh
- bilinear bedleveling with a 5x5, 7x7, 10x10 mesh
- probing margin bumped to 45mm to get a square mesh
- no preheat before leveling, set what you want for that before leveling.
- pidtemp and piditemp set to values of my runs with stock bed, but calibrate for your printer please
- fixed manual bed leveling point 1 from x=117 to y=117 to x=117.5 to y=117.5
- fixed filament runount sensor resume not functional
- fixed sd print pause resume not functional
- fixed prusa sclicer M600 functionality
- fixed octoprint print progress
- laser functionality enabled
- included relevant marlin upstream fixes
- firmware supports folders and subfolders - max 8 chars for a folder name, if longer it will not be entered
- firmware supports 5 folders/files per site, print key is "cdup" if your are in a subfolder
- firmware complete rebased on Marlin 2.1.x-bugfix
- M117 set lcd message supported
- M851 and M290 changes force update of zoffset on screen
- z-offset to host notification
- restore bedleveling after G28
- M48 probe repeatability test
- extruder minimum temperature lowered to 170C
- heatbreak fan extruder minimum temperature set to 80C
- bltouch high speed mode enabled on 5x5 and 7x7 builds
- G26 mesh validation
- G12 clean the nozzle
- include adc values when reporting temperature
- emergency parser
- auto report position
- host action commands
- host prompt support enabled
- M486 cancel objects


Features Ender 3 S1 Plus:

- bed size (315mmx310mm)
- printing height 300
- correct homeing offsets
- correct nozzle to probe offsets
- z-offset set to 0.0 in order calibrate for your printer
- babystepping while printing fixed and set to 0.01mm steps
- babystepping on leveling page fixed and set to 0.01mm steps
- linear advance set to 0.05
- input shaping activated and set to x 40hz and y 40hz.
- increased buffers for faster octoprint and sd communication
- increased feedrates in reasonable borders for faster printing
- increased min_segmenttime for better quality
- unified bedleveling with a 5x5, 7x7, 10x10 mesh
- bilinear bedleveling with a 5x5, 7x7, 10x10 mesh
- probing margin bumped to 55mm to get a square mesh
- no preheat before leveling, set what you want for that before leveling.
- pidtemp and piditemp set to values of my runs with stock bed, but calibrate for your printer please
- fixed manual bed leveling point 1 from x=157 to y=157.5
- fixed filament runount sensor resume not functional
- fixed sd print pause resume not functional
- fixed prusa sclicer M600 functionality
- fixed octoprint print progress
- laser functionality enabled
- included relevant marlin upstream fixes
- firmware supports folders and subfolders - max 8 chars for a folder name, if longer it will not be entered
- firmware supports 5 folders/files per site, print key is "cdup" if your are in a subfolder
- firmware complete rebased on Marlin 2.1.x-bugfix
- M117 set lcd message supported
- M851 and M290 changes force update of zoffset on screen
- z-offset to host notification
- restore bedleveling after G28
- M48 probe repeatability test
- extruder minimum temperature lowered to 170C
- heatbreak fan extruder minimum temperature set to 80C
- bltouch high speed mode enabled on 5x5 and 7x7 builds
- G26 mesh validation
- G12 clean the nozzle
- include adc values when reporting temperature
- emergency parser
- auto report position
- host action commands
- host prompt support enabled
- M486 cancel objects
