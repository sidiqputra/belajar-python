import os
import boto3
from datetime import datetime, timedelta
import slackweb

filedir = "./"
todayfile = datetime.now().strftime('%Y%m%d')
oldfile = (datetime.now() - timedelta(days=2)).strftime('%Y%m%d')
extfile = ".000000.gz"


bucketName = "mybucket"
filetoupload = filedir+todayfile+extfile
filetodelete = oldfile+extfile
remoteName = todayfile+extfile

#slack environment
slackchannel = '#testchannel'
successnotif = "file success to upload"
failednotif = "file failed to upload"
slackuser = "test-bot"
slackemoji = ":cactus:"
slack = slackweb.Slack(url="https://hooks.slack.com/services/0000000000/00000000/XXXXXXXXXXXXXXXXX")


#upload file to s3
try :
   s3 = boto3.client('s3')
   s3.upload_file(filetoupload,bucketName,remoteName)
   slack.notify(text=successnotif, channel=slackchannel, username=slackuser, icon_emoji=slackemoji)
   print(filetoupload + " Uploaded")
except:
   slack.notify(text=failednotif, channel=slackchannel, username=slackuser, icon_emoji=slackemoji)
   print("Failed to upload")

#delete old file on s3
try :
   s3.delete_object(
     Bucket=bucketName,
     Key=filetodelete,
   )
   print("delete old file success")
except :
   print("delete old file failed")

#remove backup file on local
os.remove(filetoupload)