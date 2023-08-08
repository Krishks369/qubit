import csv
flag_map={"SF":1,"S0":2,"S1":3,"S2":4,"S3":5,"REJ":6,"RSTOS0":7,"RSTO":8,"RSTR":9,"SH":10,"RSTRH":11,"SHR":12,"OTH":13}
protocol_map={"tcp":1,"udp":2,"icmp":3}
service_map={"other":1,"private":2,"ecr_i":3,"urp_i":4,"urh_i":5,"red_i":6,"eco_i":7,"tim_i":8,
             "oth_i":9,"domain_u":10,"tftp_u":11,"ntp_u":12,"IRC":13,"X11":14,"Z39_50":15,"aol":16,
             "auth":17,"bgp":18,"courier":19,"csnet_ns":20,"ctf":21,"daytime":22,"discard":23,"domain":24,
             "echo":25,"efs":26,"exec":27,"finger":28,"ftp":29,"ftp_data":30,"gopher":31,"harvest":32,
             "hostnames":33,"http":34,"http_2784":35,"http_443":36,"http_8001":37,"icmp":38,"imap4":39,"iso_tsap":40,
             "klogin":41,"kshell":42,"ldap":43,"link":44,"login":45,"mtp":46,"name":47,"netbios_dgm":48,
             "netbios_ns":49,"netbios_ssn":50,"netstat":51,"nnsp":52,"nntp":53,"pm_dump":54,"pop_2":55,"pop_3":56,
             "printer":57,"remote_job":58,"rje":59,"shell":60,"smtp":61,"sql_net":62,"ssh":63,"sunrpc":64,"supdup":65,
             "systat":66,"telnet":67,"time":68,"uucp":69,"uucp_path":70,"vmnet":71,"whois":72
}

import csv
modified_lines = []
 
# opening the CSV file
with open('input.csv', mode ='r')as file:
  # reading the CSV file
  csvFile = csv.reader(file)
  # displaying the contents of the CSV file
  for lines in csvFile:
        lines[1]=protocol_map.get(lines[1])
        lines[2]=service_map.get(lines[2])
        lines[3]=flag_map.get(lines[3])
        modified_lines.append(lines)

# Opening the output CSV file for writing
with open('output.csv', mode='w', newline='') as outfile:
    csv_writer = csv.writer(outfile)
    csv_writer.writerows(modified_lines)

print("CSV file 'output.csv' created with modified lines.")
