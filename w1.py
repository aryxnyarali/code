from Mongo_Connection.connection import Connection
def get_live_chat_user_details(bot_id,ext):
    connection = Connection()
    print(ext)
    if "PJSIP"in ext:
        ext = ext.split("/")[1]
    print(ext)

    db = connection.get_mongodb_connection(bot_id)
    user_ext_details = list(db["voice_livechat_ext"].find({"ext":str(ext)}))[0]
    expo_db= connection.get_expo_master()
    user_details = list(expo_db["users_master"].find({"Email_Address":user_ext_details["user"]}))[0]
    return {"customer_no":i['CallerIDNum'],
                    "agent":{"agent_name":"","agent_email_id":"","agent_image":"","agent_ext":""},
                    'start_time':get_datetime_from_unique_id(i['Uniqueid']),
                    "unique_id":i['Uniqueid'],
                    'status':"queued"}
