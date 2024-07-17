from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class SgaStorage(S3Boto3Storage):
    bucket_name = vars(settings).get('SGA_STORAGE_BUCKET_NAME', settings.FILE_UPLOAD_STORAGE_BUCKET_NAME)
