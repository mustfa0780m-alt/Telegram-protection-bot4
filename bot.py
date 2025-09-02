from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, PeerIdInvalid

BOT_TOKEN = "8426678140:AAG3721Hak7V0u_ACZOl2pQHzMgY7Udxk4k"  # ضع هنا توكن البوت
CHANNEL_USERNAME = "@sutazz"  # ضع هنا معرف القناة

# إنشاء تطبيق Pyrogram باستخدام البوت فقط
app = Client("subscription_bot", bot_token=BOT_TOKEN)

@app.on_message(filters.group)
async def check_subscription(client, message):
    user_id = message.from_user.id

    try:
        # التحقق إذا العضو مشترك في القناة
        member = await app.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ["left", "kicked"]:
            raise UserNotParticipant
    except UserNotParticipant:
        # العضو غير مشترك: حذف الرسالة
        await message.delete()
        try:
            # إرسال رسالة خاصة للعضو
            await client.send_message(
                user_id,
                "🚫 يجب الاشتراك في قناة السوبر لعرض منتجاتك."
            )
        except PeerIdInvalid:
            # إذا أغلق العضو الرسائل الخاصة للبوت، يظهر التنبيه في المجموعة
            await message.reply_text(
                f"🚫 @{message.from_user.username or message.from_user.first_name}, يجب الاشتراك في قناة السوبر لعرض منتجاتك."
            )

# تشغيل البوت
app.run()