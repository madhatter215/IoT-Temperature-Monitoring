#!/usr/bin/python
from myfunctions import *


print "Content-type: text/html"
print ""
print "<html>"
print "  <head>"
print "   <script type=\"text/javascript\" src=\"https://www.gstatic.com/charts/loader.js\"></script>"
print "   <script type=\"text/javascript\">"
print "      google.charts.load('current', {'packages':['gauge']});"
print "      google.charts.setOnLoadCallback(drawChart);"
print "      function drawChart() {"
print ""
print "        var data = google.visualization.arrayToDataTable(["
print "          ['Label', 'Value'],"
#print "          ['Alameda', %s]," %get_alameda_last_val()
print "          ['Alameda', 80],"
print "          ['Ottawa', 55],"
print "          ['Beijing', 68]"
print "        ]);"
print ""
print "        var options = {"
print "          width: 800, height: 420,"
print "          redFrom: 90, redTo: 100,"
print "          yellowFrom:75, yellowTo: 90,"
print "          minorTicks: 5"
print "        };"
print ""
print "        var chart = new google.visualization.Gauge(document.getElementById('chart_div'));"
print ""
print "        chart.draw(data, options);"
print ""
print "        setInterval(function() {"
print "          data.setValue(0, 1, %s);" %get_alameda_last_val()
print "          chart.draw(data, options);"
print "        }, 1600);"
print "        setInterval(function() {"
print "          data.setValue(1, 1, 40 + Math.round(60 * Math.random()));"
print "          chart.draw(data, options);"
print "        }, 5000);"
print "        setInterval(function() {"
print "          data.setValue(2, 1, 60 + Math.round(20 * Math.random()));"
print "          chart.draw(data, options);"
print "        }, 26000);"
print "      }"
print "    </script>"
print "  </head>"
print "  <body>"
print "    <div id=\"chart_div\" style=\"width: 400px; height: 120px;\"></div>"
print "  </body>"
print "</html>"

