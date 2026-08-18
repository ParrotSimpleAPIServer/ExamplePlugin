#  ____   ____      _     ____      _____                                 _
# |  _ \ / ___|    / \   / ___|    | ____|__  __  __ _  _ __ ___   _ __  | |  ___
# | |_) |\___ \   / _ \  \___ \    |  _|  \ \/ / / _` || '_ ` _ \ | '_ \ | | / _ \
# |  __/  ___) | / ___ \  ___) |   | |___  >  < | (_| || | | | | || |_) || ||  __/
# |_|    |____/ /_/   \_\|____/    |_____|/_/\_\ \__,_||_| |_| |_|| .__/ |_| \___|
#                                                                 |_|

class register:
    version = 1.0
    commands = {
        "test":"ExampleP.test",
        "hi":"ExampleP.hi",
        "head":"ExampleP.headget"
    }

def test(api):
    return str(api)

def hi(api):
    return {'code':'200','data':'Hi','msg':"Everything is (200)ok"}
    
def head(api):
    return api['client']['request']['head'].get('User-Agent')
