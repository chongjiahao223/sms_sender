# 设置 Aliyun 的配置参数（通常这些会放在 settings配置中）
ALIYUN_ACCESS_KEY_ID = ''  # 替换为你的阿里云 Access Key ID
ALIYUN_ACCESS_KEY_SECRET = ''  # 替换为你的阿里云 Access Key Secret
ALIYUN_SMS_SIGN_NAME = ''  # 短信签名
ALIYUN_SMS_TEMPLATE_CODE = ''  # 短信模板代码

# 实例化 AliyunSmsSender 对象
# sms_sender = AliyunSmsSender(ALIYUN_ACCESS_KEY_ID, ALIYUN_ACCESS_KEY_SECRET, ALIYUN_SMS_SIGN_NAME)
# phone_number = '15531876188'
# res = sms_sender.send_sms(phone_number, ALIYUN_SMS_TEMPLATE_CODE, generate_sms_code())
# print(res)