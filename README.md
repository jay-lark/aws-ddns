# aws-ddns
Personal DDNS system using AWS Route 53.  

## Requirements
- Python 3
- Boto 3

## Usage

### ip.php
Place this PHP file somewhere on the internet that the system with a dynamic IP can reach.

This PHP file simply grabs the IP of any visitor and displays it on the page.  

### ip.py
Fill in the following variables at the top of the file:
- zone_id - This is referred to as the Hosted Zone ID if you are looking at the AWS Management Console.
- zone_record - The DNS record you want to monitor and change. This variable must end in a period.  (www.example.com., mail.example.com.)
- public_url - The direct link to the ip.php file.

Once you've entered your details just save the file somewhere and run it manually or have it run in a regular basis by your favorite task scheduler.






