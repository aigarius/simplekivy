[app]

# (str) Title of your application
title = Simple Drawer

# (str) Package name
package.name = simpledraw

# (str) Package domain (needed for android/ios packaging)
package.domain = com.aigarius

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,cache

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = env

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
# version.regex = __version__ = '(.*)'
#version.filename = %(source.dir)s/main.py

# (str) Application versioning (method 2)
version = 0.0.1

# (list) Application requirements
requirements = kivy, pygame, plyer

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = all

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1


#
# Android specific
#

# (list) Permissions
android.permissions = VIBRATE

# (int) Android API to use
android.api = 19

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 1
