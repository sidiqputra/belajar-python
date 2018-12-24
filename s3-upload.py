import boto3

bucketName = "your bucketname"
Key = "file to upload"
remotename = "filename after uploaded"

try :
 s3 = boto3.client('s3')
 s3.upload_file(Key,bucketName,remotename)
 print(Key + " Uploaded")
except:
 print("Failed to upload")
