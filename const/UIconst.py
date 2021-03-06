# -*- coding: cp1252 -*-
# UI related constants for the Artisan application.
#
# LICENSE
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.
#
# This file is part of Artisan.

from PyQt4.QtGui import QApplication
import platform

import sys
if sys.version < '3':
    import codecs
    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x
        
platf = str(platform.system())

#######################################################################################
#################### MENU STRINGS  ####################################################
#######################################################################################

#Fake entries to get translations for the Mac Application Menu
_mac_services = QApplication.translate("MAC_APPLICATION_MENU", "Services", None, QApplication.UnicodeUTF8)
_mac_hide = QApplication.translate("MAC_APPLICATION_MENU", "Hide %1", None, QApplication.UnicodeUTF8)
_mac_hideothers = QApplication.translate("MAC_APPLICATION_MENU", "Hide Others", None, QApplication.UnicodeUTF8)
_mac_showall = QApplication.translate("MAC_APPLICATION_MENU", "Show All", None, QApplication.UnicodeUTF8)
_mac_preferences = QApplication.translate("MAC_APPLICATION_MENU", "Preferences...", None, QApplication.UnicodeUTF8)
_mac_quit = QApplication.translate("MAC_APPLICATION_MENU", "Quit %1", None, QApplication.UnicodeUTF8)
_mac_about = QApplication.translate("MAC_APPLICATION_MENU", "About %1", None, QApplication.UnicodeUTF8)

#File menu items
FILE_MENU = QApplication.translate("Menu", "File", None, QApplication.UnicodeUTF8)
if platf != 'Darwin':
    FILE_MENU = "&" + FILE_MENU
FILE_MENU_NEW = QApplication.translate("Menu", "New", None, QApplication.UnicodeUTF8)
FILE_MENU_OPEN = QApplication.translate("Menu", "Open...", None, QApplication.UnicodeUTF8)
FILE_MENU_OPENRECENT = QApplication.translate("Menu", "Open Recent", None, QApplication.UnicodeUTF8)
FILE_MENU_IMPORT = QApplication.translate("Menu", "Import", None, QApplication.UnicodeUTF8)
FILE_MENU_SAVE = QApplication.translate("Menu", "Save", None, QApplication.UnicodeUTF8)
FILE_MENU_SAVEAS = QApplication.translate("Menu", "Save As...", None, QApplication.UnicodeUTF8)
FILE_MENU_EXPORT = QApplication.translate("Menu", "Export", None, QApplication.UnicodeUTF8)
FILE_MENU_SAVEGRAPH = QApplication.translate("Menu", "Save Graph", None, QApplication.UnicodeUTF8)
FILE_MENU_SAVEGRAPH_FULL_SIZE = QApplication.translate("Menu", "Full Size...", None, QApplication.UnicodeUTF8)
FILE_MENU_HTMLREPORT = QApplication.translate("Menu", "Roasting Report", None, QApplication.UnicodeUTF8)
FILE_MENU_PRINT = QApplication.translate("Menu", "Print...", None, QApplication.UnicodeUTF8)
if platf == 'Darwin':
    FILE_MENU_QUIT = "Quit"
else:
    FILE_MENU_QUIT = QApplication.translate("MAC_APPLICATION_MENU", "Quit %1", None, QApplication.UnicodeUTF8).arg("Artisan")   

#Edit menu items
EDIT_MENU = QApplication.translate("Menu", "Edit", None, QApplication.UnicodeUTF8)
if platf != 'Darwin':
    EDIT_MENU = "&" + EDIT_MENU
EDIT_MENU_CUT = QApplication.translate("Menu", "Cut", None, QApplication.UnicodeUTF8)
EDIT_MENU_COPY = QApplication.translate("Menu", "Copy", None, QApplication.UnicodeUTF8)
EDIT_MENU_PASTE = QApplication.translate("Menu", "Paste", None, QApplication.UnicodeUTF8)
    
#Roast menu items
ROAST_MENU = QApplication.translate("Menu", "Roast", None, QApplication.UnicodeUTF8)
if platf != 'Darwin':
    ROAST_MENU = "&" + ROAST_MENU
ROAST_MENU_PROPERTIES = QApplication.translate("Menu", "Properties...", None, QApplication.UnicodeUTF8)
ROAST_MENU_BACKGROUND = QApplication.translate("Menu", "Background...", None, QApplication.UnicodeUTF8)
ROAST_MENU_CUPPROFILE = QApplication.translate("Menu", "Cup Profile...", None, QApplication.UnicodeUTF8)
ROAST_MENU_TEMPERATURE = QApplication.translate("Menu", "Temperature", None, QApplication.UnicodeUTF8)
ROAST_MENU_CONVERT_TO_FAHRENHEIT = QApplication.translate("Menu", "Convert to Fahrenheit", None, QApplication.UnicodeUTF8)
ROAST_MENU_CONVERT_TO_CELSIUS = QApplication.translate("Menu", "Convert to Celsius", None, QApplication.UnicodeUTF8)
ROAST_MENU_FAHRENHEIT_MODE = QApplication.translate("Menu", "Fahrenheit Mode", None, QApplication.UnicodeUTF8)
ROAST_MENU_CELSIUS_MODE = QApplication.translate("Menu", "Celsius Mode", None, QApplication.UnicodeUTF8)
ROAST_MENU_SWITCH = QApplication.translate("Menu", "Switch Profiles", None, QApplication.UnicodeUTF8)

#Conf menu items
CONF_MENU = QApplication.translate("Menu", "Config", None, QApplication.UnicodeUTF8)
if platf != 'Darwin':
    CONF_MENU = "&" + CONF_MENU
CONF_MENU_DEVICE = QApplication.translate("Menu", "Device...", None, QApplication.UnicodeUTF8)
CONF_MENU_SERIALPORT = QApplication.translate("Menu", "Serial Port...", None, QApplication.UnicodeUTF8)
CONF_MENU_SAMPLING = QApplication.translate("Menu", "Sampling Interval...", None, QApplication.UnicodeUTF8)
CONF_MENU_OVERSAMPLING = QApplication.translate("Menu", "Oversampling", None, QApplication.UnicodeUTF8)
CONF_MENU_COLORS = QApplication.translate("Menu", "Colors...", None, QApplication.UnicodeUTF8)
CONF_MENU_PHASES = QApplication.translate("Menu", "Phases...", None, QApplication.UnicodeUTF8)
CONF_MENU_EVENTS = QApplication.translate("Menu", "Events...", None, QApplication.UnicodeUTF8)
CONF_MENU_STATISTICS = QApplication.translate("Menu", "Statistics...", None, QApplication.UnicodeUTF8)
CONF_MENU_AXES = QApplication.translate("Menu", "Axes...", None, QApplication.UnicodeUTF8)
CONF_MENU_AUTOSAVE = QApplication.translate("Menu", "Autosave...", None, QApplication.UnicodeUTF8)
CONF_MENU_ALARMS = QApplication.translate("Menu", "Alarms...", None, QApplication.UnicodeUTF8)
CONF_MENU_LANGUAGE = QApplication.translate("Menu", "Language", None, QApplication.UnicodeUTF8)
CONF_MENU_ENGLISH = u("English") # Do not translate
CONF_MENU_GERMAN = u("Deutsch")  # Do not translate
CONF_MENU_SPANISH = u("Espa\u00f1ol") # Do not translate
CONF_MENU_FRENCH = u("Fran\u00e7ais") # Do not translate
CONF_MENU_SWEDISH = u("Svenska") # Do not translate

CONF_MENU_ITALIAN = u("Italiano") # Do not translate
CONF_MENU_CHINESE_CN = u("\u7b80\u4f53\u4e2d\u6587\u7248") # Do not translate
CONF_MENU_CHINESE_TW = u("\u4e2d\u570b\u50b3\u7d71") # Do not translate
CONF_MENU_GREEK = u("\u03b5\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac") # Do not translate
CONF_MENU_NORWEGIAN = u("Norsk") # Do not translate
CONF_MENU_DUTCH = u("Nederlands") # Do not translate
CONF_MENU_KOREAN = u("\ud55c\uad6d\uc758") # Do not translate
CONF_MENU_PORTUGUESE = u("Portugu\xeas") # Do not translate
CONF_MENU_RUSSIAN = u("\u0440\u0443\u0441\u0441\u043a\u0438\u0439") # Do not translate
CONF_MENU_ARABIC = u("\u0627\u0644\u0639\u0631\u0628\u064a\u0629") # Do not translate
CONF_MENU_FINISH = u("Suomalainen") # Do not translate
CONF_MENU_TURKISH = u("T\xfcrk") # Do not translate
CONF_MENU_JAPANESE = u("\u65e5\u672c\u8a9e") # Do not translate
CONF_MENU_HUNGARIAN = u("Hungarian") # Do not translate
CONF_MENU_HEBREW = u("\u05e2\u05d1\u05e8\u05d9\u05ea") # Do not translate
CONF_MENU_POLISH = u("Polski") # Do not translate

#Toolkit menu
TOOLKIT_MENU = QApplication.translate("Menu", "Tools", None, QApplication.UnicodeUTF8)
if platf != 'Darwin':
    TOOLKIT_MENU = "&" + TOOLKIT_MENU
TOOLKIT_MENU_DESIGNER = QApplication.translate("Menu", "Designer", None, QApplication.UnicodeUTF8)    
TOOLKIT_MENU_CALCULATOR = QApplication.translate("Menu", "Calculator", None, QApplication.UnicodeUTF8)
TOOLKIT_MENU_WHEELGRAPH = QApplication.translate("Menu", "Wheel Graph", None, QApplication.UnicodeUTF8)
TOOLKIT_MENU_LCDS = QApplication.translate("Menu", "LCDs", None, QApplication.UnicodeUTF8)
TOOLKIT_MENU_EXTRAS = QApplication.translate("Menu", "Extras...", None, QApplication.UnicodeUTF8)

    
#Help menu items
HELP_MENU = QApplication.translate("Menu", "Help", None, QApplication.UnicodeUTF8)
if platf != 'Darwin':
    HELP_MENU = "&" + HELP_MENU
#note that the "About" menu item is recognized only if it is named "About" on the Mac, but automatically translated by the Qt standard tranlators
if platf == 'Darwin':
    HELP_MENU_ABOUT = "About"
else:
    HELP_MENU_ABOUT = QApplication.translate("MAC_APPLICATION_MENU", "About %1", None, QApplication.UnicodeUTF8).arg("Artisan") 
HELP_MENU_ABOUTQT = QApplication.translate("Menu", "About Qt", None, QApplication.UnicodeUTF8)
HELP_MENU_DOCUMENTATION = QApplication.translate("Menu", "Documentation", None, QApplication.UnicodeUTF8)
#HELP_MENU_BLOG = QApplication.translate("Menu", "Blog", None, QApplication.UnicodeUTF8)
HELP_MENU_KEYBOARDSHORTCUTS = QApplication.translate("Menu", "Keyboard Shortcuts", None, QApplication.UnicodeUTF8)
HELP_MENU_ERRORS = QApplication.translate("Menu", "Errors", None, QApplication.UnicodeUTF8)
HELP_MENU_MESSAGES = QApplication.translate("Menu", "Messages", None, QApplication.UnicodeUTF8)
HELP_MENU_SERIAL = QApplication.translate("Menu", "Serial", None, QApplication.UnicodeUTF8)
if platf == 'Darwin':
    HELP_MENU_SETTINGS = "Settings"
else:
    HELP_MENU_SETTINGS = QApplication.translate("Menu", "Settings", None, QApplication.UnicodeUTF8)
HELP_MENU_PLATFORM = QApplication.translate("Menu", "Platform", None, QApplication.UnicodeUTF8)
HELP_MENU_RESET = QApplication.translate("Menu", "Factory Reset", None, QApplication.UnicodeUTF8)
  
#######################################################################################
#################### DIALOG STRINGS  ##################################################
#######################################################################################
