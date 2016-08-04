#!/usr/bin/python

PATH=r"/var/tmp/temperature_sensor2.dat"
my_array= []
alameda_records=[]
from datetime import datetime



#date_object = datetime.strptime('2016-06-18 22:33:16', '%Y-%m-%d %H:%M:%S')

def get_alameda_dataset():
	myfile=open(PATH, 'r')
	mylines=myfile.read().splitlines()
	for ele in mylines:
	    my_array.append(ele.split(" "))
	myfile.close()
	return my_array

def get_alameda_records_with_datetime_and_temperature():
	ala_dt = get_alameda_dataset()
	for record in ala_dt:
		datetime_record = datetime.strptime((record[0] + " " + record[1]),'%Y-%m-%d %H:%M:%S')
	#	print "year {} day {} second {}".format(datetime_record.year, datetime_record.day, datetime_record.second)
		obj = datetime_record, record[2]
		alameda_records.append(obj)
#	print "year {} day {}".format(alameda_records[-1]
	return alameda_records

alameda_records=get_alameda_records_with_datetime_and_temperature()


#here = get_alameda_records_with_datetime_and_temperature()
#print "year {} time {}".format(here[-1].

#alameda_records = zip(datetime_record,record[2])


