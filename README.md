# DFM-Timestable-Bot
A bot for DrFrostMaths.com, opens a chromedriver, logs in to DFM and navigates to timetable app before executing to ensure you get the highscore.

# Requirements
Make sure selenium is installed, this can be done from the command line and typing pip installl selenium. Then download the chromedriver from https://chromedriver.chromium.org/downloads relating to your current version of chrome which can be found from the meatball menu going to the about chrome section.

In the DFM.py file there are two empty variables, Name and Pass, before running the script make sure you enter your DFM username and password into the two fields.

The code is set to run for 2 hours, this can be changed on line 29 by setting the "timeElapsed = {}" to any time you want in seconds.
