import boto3




def saveimage(image):

    bucket_name = "teella"
    key = 'Aliviamos/Img/archivo.jpg'

    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-2',
        aws_access_key_id='AKIARP6D4SYXVPI27Y6U',
        aws_secret_access_key='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'
    )
    s3.Object(bucket_name, key).put(Body=image)
    location = boto3.client(
        service_name='s3',
        region_name='us-east-2',
        aws_access_key_id='AKIARP6D4SYXVPI27Y6U',
        aws_secret_access_key='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'
    ).get_bucket_location(Bucket=bucket_name)['LocationConstraint']
    url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, key)
    return url