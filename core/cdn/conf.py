import os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')
AWS_ENDPOINT_URL = "https://fra1.digitaloceanspaces.com"
AWS_ENDPOINT = "fra1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
DEFAULT_FILE_STORAGE = "core.cdn.backends.MediaRootS3Boto3Storages"
STATICFILES_STORAGE = "core.cdn.backends.StaticRootS3Boto3Storages"
