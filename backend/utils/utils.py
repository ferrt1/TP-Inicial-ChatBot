import os

RP_ID='8742-2800-810-469-744-25ff-831f-c8e9-8c49.ngrok-free.app' #URL de página
RP_NAME='UNGSNet'
UKEY_DEFAULT_BYTE_LEN = 20


def generate_challenge():
    return os.urandom(32)