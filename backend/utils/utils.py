import os

RP_ID='5b76-2800-810-469-744-45f3-9aa7-b834-15d7.ngrok-free.app' #URL de página
RP_NAME='UNGSNet'
UKEY_DEFAULT_BYTE_LEN = 20


def generate_challenge():
    return os.urandom(32)