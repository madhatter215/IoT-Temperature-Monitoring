PATH=r"/var/tmp/temperature_sensor2.dat"
my_array= []


def get_alameda_last_val():
	myfile=open(PATH, 'r')
	mylines=myfile.read().splitlines()
	for ele in mylines:
	    my_array.append(ele.split(" "))
	myfile.close()
	return my_array[-1][2]



