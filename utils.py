import boto3
import json

def read_s3_json_file(bucket_name, key):
    s3_obj = boto3.client('s3')
    s3_clientobj = s3_obj.get_object(Bucket=bucket_name, Key=key)
    s3_clientdata = s3_clientobj['Body'].read().decode('utf-8')
    return json.loads(s3_clientdata)


def write_s3_json_file(data, bucket_name, key):
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_name, key)
    obj.put(Body=json.dumps(data).encode('UTF-8'))
