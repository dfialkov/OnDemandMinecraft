class Config:
    # AWS Information
    ACCESS_KEY = 'AKIARNGELKMI4UHIMQ7T'
    SECRET_KEY = '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'
    INSTANCE_ID = 'i-0b61582c5b01aa051'
    ec2_region = "us-west-2"
    ec2_amis = ['ami-01773ce53581acf22']
    ec2_keypair = 'MinecraftServerKeypair'
    ec2_secgroups = ['MinecraftServer']
    ec2_instancetype = 't3.large'

    # SSH Key Path
    SSH_KEY_FILE_PATH = './MinecraftServerKeypair.pem'

    SERVER_PASSWORD = '39g4w8he9o8r5hyj'
    # Server Memory Size
    # This is default to no memory specification but can be: '-Xmx1024M -Xms1024M ' (KEEP TRAILING SPACE)
    MEMORY_ALLOCATION = ''
