#!/usr/bin/python
from myfunctions_test import *
from datetime import datetime
#new Date(Year, Month, Day, Hours, Minutes, Seconds, Milliseconds)

print "Content-type: text/html"
print ""
print "<html>"
print "  <head>"
print "   <script type=\"text/javascript\" src=\"https://www.gstatic.com/charts/loader.js\"></script>"
print "   <script type=\"text/javascript\">"
print "google.charts.load(\'current\', {packages: [\'corechart\', \'line\']});"
print "google.charts.setOnLoadCallback(drawBackgroundColor);"
print ""
print "function drawBackgroundColor() {"
print "      var data = new google.visualization.DataTable();"
print "      data.addColumn(\'date\', \'X\');"
print "      data.addColumn(\'number\', \'Alameda D3078\');"
print ""
print "        data.addRows(["

for n in range(0, len(alameda_records)):
	print "\
          [new Date(%d, %d, %d, %d, %d, %d), %d]," % (int(alameda_records[n][0].year), int(alameda_records[n][0].month-1), int(alameda_records[n][0].day), int(alameda_records[n][0].hour), int(alameda_records[n][0].minute), int(alameda_records[n][0].second), int(alameda_records[n][1]))

##Prints a string, some webbrowsers (IE7) require digit 
#for n in range(0, len(alameda_records)):
#	print "\
#          [new Date({}, {}, {}, {}, {}, {}), {}],".format(
#		alameda_records[n][0].year, 
#		alameda_records[n][0].month, 
#		alameda_records[n][0].day, 
#		alameda_records[n][0].hour, 
#		alameda_records[n][0].minute, 
#		alameda_records[n][0].second, 
#		alameda_records[n][1])


#print "          [new Date(2015, 0, 1), 5],  [new Date(2015, 0, 2), 7],  [new Date(2015, 0, 3), 3],"
#print "          [new Date(2015, 0, 4), 1],  [new Date(2015, 0, 5), 3],  [new Date(2015, 0, 6), 4],"
#print "          [new Date(2015, 0, 7), 3],  [new Date(2015, 0, 8), 4],  [new Date(2015, 0, 9), 2],"
#print "          [new Date(2015, 0, 10), 5], [new Date(2015, 0, 11), 8], [new Date(2015, 0, 12), 6],"
#print "          [new Date(2015, 0, 13), 3], [new Date(2015, 0, 14), 3], [new Date(2015, 0, 15), 5],"
#print "          [new Date(2015, 0, 16), 7], [new Date(2015, 0, 17), 6], [new Date(2015, 0, 18), 6],"
#print "          [new Date(2015, 0, 19), 3], [new Date(2015, 0, 20), 1], [new Date(2015, 0, 21), 2],"
#print "          [new Date(2015, 0, 22), 4], [new Date(2015, 0, 23), 6], [new Date(2015, 0, 24), 5],"
#print "          [new Date(2015, 0, 25), 9], [new Date(2015, 0, 26), 4], [new Date(2015, 0, 27), 9],"
#print "          [new Date(2015, 0, 28), 8], [new Date(2015, 0, 29), 6], [new Date(2015, 0, 30), 4],"
#print "          [new Date(2015, 0, 31), 6], [new Date(2015, 1, 1), 7],  [new Date(2015, 1, 2), 9]"


print "        ]);"
print ""
print ""
print "      var options = {"
print "        width: 1200, height: 420,"
print "        hAxis: {"
print "          title: \'Time\'"
print "        },"
print "        vAxis: {"
print "          title: \'Temp in F\',"
print "          maxValue: 85,"
print "          minValue: 70"
print "        },"
print "        backgroundColor: \'#f1f8e9\'"
print "      };"
print ""
print "      var chart = new google.visualization.LineChart(document.getElementById(\'chart_div\'));"
print "      chart.draw(data, options);"
print "    }"
print "    </script>"
print "  </head>"
print "  <body>"
print "    <div id=\"chart_div\" style=\"width: 400px; height: 120px;\"></div>"
print "  </body>"
print "</html>"

