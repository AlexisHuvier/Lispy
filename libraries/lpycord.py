from libraries_src.lpycord_src.lispy_functions import *

module = {
    "lpycord:bot:create": lpycord_bot_create, "lpycord:bot:run": lpycord_bot_run, "lpycord:bot:addcommand": lpycord_bot_addcommand, "lpycord:bot:removecommand": lpycord_bot_removecommand,
    "lpycord:bot:prefix": lpycord_bot_prefix, "lpycord:bot:setprefix": lpycord_bot_setprefix, "lpycord:bot:commands": lpycord_bot_commands, "lpycord:bot:latency": lpycord_bot_latency, 
    "lpycord:bot:user": lpycord_bot_user, "lpycord:bot:guilds": lpycord_bot_guilds, "lpycord:bot:isready": lpycord_bot_isready, "lpycord:bot:close": lpycord_bot_close, 
    "lpycord:bot:getchannel": lpycord_bot_getchannel, "lpycord:bot:getguild": lpycord_bot_getguild, "lpycord:bot:getuser": lpycord_bot_getuser, "lpycord:bot:getemoji": lpycord_bot_getemoji, 
    "lpycord:bot:users": lpycord_bot_users, "lpycord:bot:setready": lpycord_bot_setready, "lpycord:bot:setmessage": lpycord_bot_setmessage, "lpycord:bot:setready": lpycord_bot_setready, 
    "lpycord:bot:setmessage": lpycord_bot_setmessage, "lpycord:bot:setmessagedelete": lpycord_bot_setmessagedelete, "lpycord:bot:setmessageedit": lpycord_bot_setmessageedit, 
    "lpycord:bot:setreactionadd": lpycord_bot_setreactionadd, "lpycord:bot:setreactionremove": lpycord_bot_setreactionremove, "lpycord:bot:setmemberjoin": lpycord_bot_setmemberjoin, 
    "lpycord:bot:setmemberremove": lpycord_bot_setmemberremove,

    "lpycord:user:name": lpycord_user_name, "lpycord:user:id": lpycord_user_id, "lpycord:user:discriminator": lpycord_user_discriminator, "lpycord:user:avatar": lpycord_user_avatar, 
    "lpycord:user:bot": lpycord_user_bot, "lpycord:user:system": lpycord_user_system, "lpycord:user:creating": lpycord_user_creating, "lpycord:user:mention": lpycord_user_mention, 
    "lpycord:user:mentionin": lpycord_user_mentionin, "lpycord:user:send": lpycord_user_send, "lpycord:user:sendembed": lpycord_user_sendembed, 
    "lpycord:user:sendfile": lpycord_user_sendfile,

    "lpycord:command:create": lpycord_command_create, "lpycord:command:name": lpycord_command_name, "lpycord:command:setname": lpycord_command_setname,
    "lpycord:command:setcallback": lpycord_command_setcallback,

    "lpycord:message:author": lpycord_message_author, "lpycord:message:id": lpycord_message_id, "lpycord:message:content": lpycord_message_content, 
    "lpycord:message:cleancontent": lpycord_message_cleancontent, "lpycord:message:guild": lpycord_message_guild, "lpycord:message:channel": lpycord_message_channel, 
    "lpycord:message:type": lpycord_message_type, "lpycord:message:pin": lpycord_message_pin, "lpycord:message:unpin": lpycord_message_unpin, 
    "lpycord:message:delete": lpycord_message_delete, "lpycord:message:deletedelay": lpycord_message_deletedelay, "lpycord:message:reply": lpycord_message_reply,

    "lpycord:textchan:id": lpycord_textchan_id, "lpycord:textchan:category": lpycord_textchan_category, "lpycord:textchan:name": lpycord_textchan_name, 
    "lpycord:textchan:topic": lpycord_textchan_topic, "lpycord:textchan:history": lpycord_textchan_history, "lpycord:textchan:members": lpycord_textchan_members, 
    "lpycord:textchan:isnsfw": lpycord_textchan_isnsfw, "lpycord:textchan:isnews": lpycord_textchan_isnews, "lpycord:textchan:clone": lpycord_textchan_clone, 
    "lpycord:textchan:purge": lpycord_textchan_purge, "lpycord:textchan:creation": lpycord_textchan_creation, "lpycord:textchan:delete": lpycord_textchan_delete, 
    "lpycord:textchan:mention": lpycord_textchan_mention, "lpycord:textchan:pins": lpycord_textchan_pins, "lpycord:textchan:send": lpycord_textchan_send, 
    "lpycord:textchan:sendembed": lpycord_textchan_sendembed, "lpycord:textchan:sendfile": lpycord_textchan_sendfile,

    "lpycord:embed:create": lpycord_embed_create, "lpycord:embed:length": lpycord_embed_length, "lpycord:embed:title": lpycord_embed_title, 
    "lpycord:embed:settitle": lpycord_embed_settitle, "lpycord:embed:description": lpycord_embed_description, "lpycord:embed:setdescription": lpycord_embed_setdescription, 
    "lpycord:embed:url": lpycord_embed_url, "lpycord:embed:seturl": lpycord_embed_seturl, "lpycord:embed:setimage": lpycord_embed_setimage, 
    "lpycord:embed:setfooter": lpycord_embed_setfooter, "lpycord:embed:setthumbnail": lpycord_embed_setthumbnail, "lpycord:embed:setauthor": lpycord_embed_setauthor, 
    "lpycord:embed:removeauthor": lpycord_embed_removeauthor, "lpycord:embed:addfield": lpycord_embed_addfield, "lpycord:embed:addinlinefield": lpycord_embed_addinlinefield, 
    "lpycord:embed:clearfields": lpycord_embed_clearfields
}