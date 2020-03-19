"# gather_4G_stats" 

Using **Netmiko**, connect through a Linux jump host in order to connect to a Cisco router in order to gather the 4G stats over a period of time.

Router in question is an 819.  
Command in question is "show cellular 0 radio".  
Saves the stats to a csv file. This makes it easy to open in Excel and create the chart for the non-Pythonic in the workforce. 
