#!/usr/bin/env python
# Python script to reformat subnets json data
import json,sys

data = []

def hello(jdata, project):
    for i in range(len(jdata)):
        subnet_row = jdata[i]
        if 'secondaryIpRanges' not in subnet_row:
            print("{},{},{},{},None,None".format(project,subnet_row['name'], \
                subnet_row['gatewayAddress'],subnet_row['ipCidrRange']))
        else:
            for j in range(len(subnet_row['secondaryIpRanges'])):
                print("{},{},{},{},{},{}".format(project,subnet_row['name'], \
                    subnet_row['gatewayAddress'],subnet_row['ipCidrRange'], \
                        subnet_row['secondaryIpRanges'][j]['rangeName'], \
                            subnet_row['secondaryIpRanges'][j]['ipCidrRange']))

if sys.argv[1]:
    project = sys.argv[1]
else:
    project = "Current-Active-Project"
data = sys.stdin.read()
jdata = json.loads(data)
hello(jdata, project)
