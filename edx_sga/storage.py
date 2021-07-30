from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class SgaStorage(S3Boto3Storage):
    bucket_name = settings.SGA_STORAGE_BUCKET_NAME