from nonebot import on_request, on_notice
from nonebot.adapters.onebot.v11 import MessageSegment, Event, Bot, GroupRequestEvent, GroupIncreaseNoticeEvent

dict1 = {}

def _check1(event: Event):
    return isinstance(event, GroupIncreaseNoticeEvent)

incr = on_notice(rule=_check1)
@incr.handle()
async def _(event: GroupIncreaseNoticeEvent, bot: Bot, ):
    if event.group_id == 762898461 or event.group_id == 643245484:
        await bot.send_group_msg(group_id=event.group_id, message=
        MessageSegment.at(event.user_id)+MessageSegment.text(f'\n\n欢迎加入\n')+MessageSegment.at(2854196310))
        await incr.finish()
    else:
        await incr.finish()



