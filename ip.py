
#!/usr/bin/env python3
import urllib.request
import boto3

zone_id = "xxxxxxx"
zone_record = "xxxxxxx."


external_ip = urllib.request.urlopen('xxxxxxxxxx').read().decode('utf8')

print(external_ip)

client = boto3.client('route53')

r = client.list_resource_record_sets(HostedZoneId=zone_id)
for i in r['ResourceRecordSets']:
    records = i['ResourceRecords'][0]
    if (i['Name']) == zone_record:
        current_r53 = (records['Value'])


print(current_r53)

if external_ip != current_r53:
    response = client.change_resource_record_sets(
    HostedZoneId='Z2TMLDL02Q0S1F',
    ChangeBatch={
        "Comment": "Automatic DNS update",
        "Changes": [
            {
                "Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": zone_record,
                    "Type": "A",
                    "TTL": 300,
                    "ResourceRecords": [
                        {
                            "Value": external_ip
                        },
                    ],
                }
            },
        ]
    }
)
