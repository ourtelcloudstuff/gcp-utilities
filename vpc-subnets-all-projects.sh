#!/bin/bash
# Script to retrieve Networks and secondary subnet ranges
echo 'project,subnet-name,gateway-ip,ip-cidr-range,secondary-ip-range-name,secondary-ip-range-cidr' > subnets-all-projects.csv
prjs=( $(gcloud projects list --format="value(project_id)" | grep -v '^sys-') )
for i in "${prjs[@]}"
    do
        echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        echo "Collecting subnet details for project: $i"       
        echo $(gcloud compute networks subnets list --project $i --format=json |python3 subnets-reformat.py $i>> subnets-all-projects.csv)		
        echo "Details are available in subnets-all-projects.csv"	
    done


