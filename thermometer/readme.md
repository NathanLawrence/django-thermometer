# Fundraiser-Thermometer
A simple thermometer application for creating animated calls to action for fundraising campaigns.
Originally created for the Fall 2015 KBIA pledge drive.
## Deployment Instructions
1. Clone the full repository.
2. Modify the variables.less and fonts.less file to suit your needs.
3. Recompile and minify the less files (by compiling from index.less) to therm-dist-min.css.
4. Copy files into an existing Django project in a new folder named “thermometer.” Add the app name “thermometer” to your settings.py.
5. Copy the files in place_in_project to your main project folder. Make sure the folder “thermometer/static” and its contents are being passed through the main URL structure.
6. Access the thermometer admin in the typical Django admin interface by going to your.url/admin.