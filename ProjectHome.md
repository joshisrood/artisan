## Summary ##

Artisan is a software that helps coffee roasters record, analyze, and control roast profiles. When used in conjunction with a thermocouple data logger or a proportional–integral–derivative controller (PID controller), this software can automate the creation of roasting metrics to help make decisions that influence the final coffee flavor.

![http://artisan.googlecode.com/svn/wiki/screenshots/teaser.jpg](http://artisan.googlecode.com/svn/wiki/screenshots/teaser.jpg)
<p align='right'><a href='http://www.roastmagazine.com'><img src='http://artisan.googlecode.com/svn/wiki/screenshots/ROAST.jpg' /></a></p>

## Features ##

  * open-source & cloud-free (distributed under [GPLv3](http://gplv3.fsf.org))
  * free for personal and commercial use
  * multi-platform (Mac, Windows, and Linux)
  * multi-language (German, French, Spanish, Portuguese, Swedish, Italian, Arabic, Japanese, Dutch, Norwegian, Greek, Turkish, Chinese, Hungarian,...)
  * multi-device (manual and automatic logging of roast temperatures via supported devices; see blog post [Device Selection](http://artisan-roasterscope.blogspot.de/2013/06/device-selection.html))
    * Fuji PXR/PXG 4 & 5 PID
    * Delta DTA PID (works for DTB too)
    * [Modbus](http://artisan-roasterscope.blogspot.de/2013/05/more-modbus.html) Serial ASCII/RTU/Binary, TCP and UDP (known to work with PIDs of Fuji, ENDA, Watlow, meters like myPCLab, as well as several variable frequency drives)
    * Omega HH309, HH506RA, HH802U, HH806AU, HHM28
    * [General Tools DT309DL](http://www.tequipment.net/GeneralDT309DL.html)
    * CENTER 300, 301, 302, 303, 304, 305, 306, 309
    * VOLTCRAFT K201, K202, K204, 300K, 302KJ
    * EXTECH 421509
    * [Arduino TC4](http://www.mlgp-llc.com/arduino/public/arduino-pcb.html) with PID
    * TE VA18B
    * HHM28 multimeter
    * Amprobe TMD-56 (non-wireless)
    * Phidget USB and [remote](http://www.phidgets.com/docs/Phidget_WebService) (1010, 1011, 1018, 1019, 1045, 1046 (WS & VD), 1048, 1073)
    * Mastech MS6514
    * Yocto Thermocouple and PT100
    * external program
  * multi-format (import and export of various file formats:  HTML, PDF, SVG, CSV, JSON, Omega HH506RA, K202, K204, [RoastLogger](http://homepage.ntlworld.com/green_bean/coffee/roastlogger/roastlogger.htm))
  * unlimited number of temperature and virtual curves incl. rate-of-rise curves for ET and BT
  * [spike filter](http://artisan-roasterscope.blogspot.de/2013/05/fighting-spikes.html) and curve smoothing
  * Fahrenheit and Celsius support
  * logging of roast events like FCs, FCe,.. via tablet-friendly buttons
  * [custom event programmable buttons and sliders](http://artisan-roasterscope.blogspot.de/2013/02/events-buttons-and-palettes.html) supporting the [Hottop Roaster Interface](http://artisan-roasterscope.blogspot.de/2013/02/controlling-hottop.html)
  * [time and temperature-based alarms](http://artisan-roasterscope.blogspot.de/2013/03/alarms.html) with user defined actions
  * head-up-display and projections predicting ET/BT development
  * phases LCDs predicting and counting developments per phase
  * automatic CHARGE/DROP event detection
  * template/background profile with playback aid for reproduction of roasts
  * configurable profile evaluations and statistics
  * weight input from digital scales ([Kern](http://www.kern-sohn.com) and [Acaia](http://acaia.co))
  * color input from color meters (supports for now [Tonino](http://my-tonino.com))
  * cupping editor and graphs
  * profile designer and wheel graph editor
  * LargeLCDs and WebLCDs
  * volume calculator

## Documentation ##

  * [Installation](Installation.md)
  * [Documentation](http://coffeetroupe.com/artisandocs/)
  * [Blog](http://artisan-roasterscope.blogspot.de)
  * [aArtisan/TC4 Driver Installation (PDF)](https://drive.google.com/file/d/0B4HTX5wS3NB2SlRQa1ozNnZ4Uk0/edit?usp=sharing) by John Hannon
  * [Controlling a Hottop Roaster with Artisan: The Basics v6 (PDF)](https://drive.google.com/file/d/0B4HTX5wS3NB2ZGxsTU4tbmtVUmM/edit?usp=sharing) by Barrie Fairley

## Support ##

  * [User Mailing List](https://lists.mokelbu.de/listinfo/artisan-user)
  * [Profile Database](https://docs.google.com/folder/d/0B-Bcer800P7hVjdqanphTzNKWHM/edit)

## Donations ##

We don't accept donations. But if you think Artisan is useful and you want to give something back: consider making a donation to a non-profit organization.

## Screenshots ##

> [![](http://artisan.googlecode.com/svn/wiki/screenshots/ubuntu-curves-small.png)](https://code.google.com/p/artisan/wiki/ScreenShots) [![](http://artisan.googlecode.com/svn/wiki/screenshots/win-wheel-small.png)](https://code.google.com/p/artisan/wiki/ScreenShots)
> [![](http://artisan.googlecode.com/svn/wiki/screenshots/mac-curves-small.png)](https://code.google.com/p/artisan/wiki/ScreenShots)  [![](http://artisan.googlecode.com/svn/wiki/screenshots/mac-roast-properties-small.png)](https://code.google.com/p/artisan/wiki/ScreenShots) [![](http://artisan.googlecode.com/svn/wiki/screenshots/win-cupping-small.png)](https://code.google.com/p/artisan/wiki/ScreenShots) [![](http://artisan.googlecode.com/svn/wiki/screenshots/mac-designer-small.png)](https://code.google.com/p/artisan/wiki/ScreenShots)
> [![](http://artisan.googlecode.com/svn/wiki/screenshots/centos-sliders-small.png)](https://code.google.com/p/artisan/wiki/ScreenShots)
> [![](http://artisan.googlecode.com/svn/wiki/screenshots/artisan-0.7-small.png)](https://code.google.com/p/artisan/wiki/ScreenShots)


## Release History ##

| **Version** | **Date** | **Comment** |
|:------------|:---------|:------------|
| 0.9.2 | 16.01.2015 | Bug fixes |
| 0.9.1 | 03.01.2015 | [Acaia](http://acaia.co) scale support, QR code, bug fixes |
| 0.9.0 | 17.11.2014 | MODBUS ASCII/TCP/UDP, Yocto TC and PT100, Phidget 1045 IR, Phidget 1046 Wheatstone Bridge wiring, Phidgets async mode, Polish translations, LargeLCDs, WebLCDs, 2nd set of roast phases, volume calculator, moisture loss and organic loss, container tare, RoR delta span, phasesLCDs showing Rao's development ratio |
| 0.8.0 | 25.05.2014 | Phidget IO, Phidget remote, Arduino TC4 PID, Mastech MS6514 |
| 0.7.5 | 06.04.2014 | Bug fixes |
| 0.7.4 | 13.01.2014 | Bug fixes |
| 0.7.3 | 12.01.2014 | Bug fixes |
| 0.7.2 | 19.12.2013 | Bug fixes |
| 0.7.1 | 02.12.2013 | Bug fixes |
| 0.7.0 | 30.11.2013 | Phidget 1046/1048, phases LCDs, xkcd style, extended alarms, [Tonino](http://my-tonino.com) support |
| 0.6.0 | 14.06.2013 | Monitoring-only mode, sliders, extended alarms, Modbus RTU, Amprobe TMD-56, spike filter, additional localizations |
| 0.5.6 | 08.11.2012 | Bug fixes |
| 0.5.2 | 23.07.2011 | Delta DTA PID support, automatic CHARGE/DROP |
| 0.5.0 | 10.06.2011 | HHM28, wheel graph, math plotter, multiple and virtual devices, symbolic expressions,  custom buttons |
| 0.4.0 | 10.04.2011 | localization, events replay, alarms, profile designer |
| 0.3.4 | 28.02.2011 | Arduino TC4, TE VA18B, delta filter |
| 0.3.3 | 13.02.2011 | Fuji PXR5/PXG5, manual device, keyboard shortcuts, Linux |
| 0.3.0 | 11.01.2011 | New profile file format |
| 0.2.0 | 31.12.2010 | CENTER 300, 301, 302, 303, 304, 305, 306, VOLTCRAFT K202, K204 300K, 302KJ, EXTECH 421509 |
| 0.1.0 | 20.12.2010 | Initial release |

[Detailed Release History](ReleaseHistory.md)

## Old Downloads ##
[Downloads](http://code.google.com/p/artisan/downloads/list?can=1&q=&colspec=Filename+Summary+Uploaded+ReleaseDate+Size+DownloadCount)

## Related Software ##

  * [RoastLogger](http://homepage.ntlworld.com/green_bean/coffee/roastlogger/roastlogger.htm)
  * [RoasterThing](http://www.roasterthing.com/)
  * [Typica](http://www.randomfield.com/programs/typica/)
  * [Roast Monitor](http://coffeesnobs.com.au/RoastMonitor/)

if you need commercial support

  * [Cropster](https://www.cropster.org/products/coffee-roaster/features/roasting/)
  * [roastlog](http://roastlog.com)
  * [Profiling Dynamics™ Coffee Roasting Control by Roaster Dynamics](http://www.roasterdynamics.com/Profiling_Dynamics.html)
  * [Probat Pilot](http://www.probat.com/en/gourmet-world/pilot.html)