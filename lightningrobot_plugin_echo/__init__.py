from lightningrobot.plugin import *

PluginMetadata = Metadata(
    name="复读机Echo",
    description="复读用户消息",
    usage="发送echo 需要复读的内容即可使用。",
    type="application",
    homepage="github.com/Zhihan2727/LightningRobot-Plugin-Echo",
    # 发布必填。
)

def commands(message):
    if message == "复读":
        return command1(message)
 
def command1(text: str) -> str:
    return text
