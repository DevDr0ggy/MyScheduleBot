import discord
from discord.ext import commands, tasks
from keep_alive import keep_alive
import datetime
import pytz
import os

class ScheduleBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.default())

    async def setup_hook(self):
        await self.tree.sync()
        self.check_schedule.start()

    @tasks.loop(minutes=1)
    async def check_schedule(self):
        tz = pytz.timezone('Asia/Bangkok')
        now = datetime.datetime.now(tz)

        current_day = now.strftime('%A')
        current_time = now.strftime('%H:%M')

        channel_id = 1478673451681185816
        channel = self.get_channel(channel_id)

        if channel is None:
            return

        if current_day == 'Tuesday' and current_time == '07:50':
            msg = "🔔 **แจ้งเตือน!** 08:00 น. มีเรียน 'ท.การคิดเชิงระบบกับการวิเคราะห์ปัญหา' ตึกเรียนรวม SEC 01 ศร. 202 ครับ"
            await channel.send(msg)

        elif current_day == 'Tuesday' and current_time == '12:50':
            msg = "🔔 **แจ้งเตือน!** 13:00 น. มีเรียน 'เทคโนโลยีสารสนเทศเพื่อการค้นคว้า' ตึกอธิการบดี ชั้น 3 SEC 01 ครับ"
            await channel.send(msg)

        elif current_day == 'Wednesday' and current_time == '07:50':
            msg = "🔔 **แจ้งเตือน!** 08:00 น. มีเรียน 'ท.การโปรแกรมคอมพิวเตอร์' กับอ.สกุลชาย ห้อง SC208 เตรียมเปิดคอมรอได้เลย!"
            await channel.send(msg)

        elif current_day == 'Wednesday' and current_time == '12:50':
            msg = "🔔 **แจ้งเตือน!** 13:00 น. มีเรียน 'การพัฒนาคุณภาพชีวิตและสังคม' ตึกเรียนรวม SEC 02 ศร. 211 ครับ"
            await channel.send(msg)

        elif current_day == 'Thursday' and current_time == '12:50':
            msg = "🔔 **แจ้งเตือน!** 13:00 น. มีเรียน 'ท.คณิตศาสตร์ดิสครีตและทฤษฎีการคำนวณ' ตึกคณะ SEC 01 อ.ชานนท์ SC201 ครับ"
            await channel.send(msg)

        elif current_day == 'Thursday' and current_time == '14:50':
            msg = "🔔 **แจ้งเตือน!** 15:00 น. มีเรียน 'ท./ป. ระบบปฏิบัติการ' ตึกคณะ SEC 01 อ.ชานนท์ SC201 ครับ"
            await channel.send(msg)

    @check_schedule.before_loop
    async def before_check_schedule(self):
        await self.wait_until_ready()

bot = ScheduleBot()

@bot.event
async def on_ready():
    print(f'Bot is online! Logged in as {bot.user}')

@bot.tree.command(name="monday", description="Show schedule for Monday (Free day)")
async def monday(interaction: discord.Interaction):
    msg = "🎮 **วันจันทร์:** ว่างเต็มวัน! พักผ่อนอ่านมังงะ ดูอนิเมะ หรือเล่นเกมได้ยาวๆ เลยครับ"
    await interaction.response.send_message(msg)

@bot.tree.command(name="tuesday", description="Show schedule for Tuesday")
async def tuesday(interaction: discord.Interaction):
    msg = (
        "**ตารางเรียนวันอังคาร:**\n"
        "⏰ 08:00 - 10:00 น.\n"
        "📖 00-41-008 ท.การคิดเชิงระบบกับการวิเคราะห์ปัญหา\n"
        "🏢 ตึกเรียนรวม SEC 01 ศร. 202\n"
        "-------------------------------\n"
        "⏰ 10:00 - 12:00 น.\n"
        "📖 00-41-008 ป.การคิดเชิงระบบกับการวิเคราะห์ปัญหา\n"
        "🏢 ตึกเรียนรวม SEC 01 ศร. 202\n"
        "-------------------------------\n"
        "⏰ 13:00 - 17:00 น.\n"
        "📖 00-12-003 เทคโนโลยีสารสนเทศเพื่อการค้นคว้า\n"
        "🏢 ตึกอธิการบดี ชั้น 3 SEC 01"
    )
    await interaction.response.send_message(msg)

@bot.tree.command(name="wednesday", description="Show schedule for Wednesday")
async def wednesday(interaction: discord.Interaction):
    msg = (
        "**ตารางเรียนวันพุธ:**\n"
        "⏰ 08:00 - 10:00 น.\n"
        "📖 06-13-101 ท.การโปรแกรมคอมพิวเตอร์\n"
        "🏢 อ.สกุลชาย SC208\n"
        "-------------------------------\n"
        "⏰ 10:00 - 12:00 น.\n"
        "📖 06-13-101 ป.การโปรแกรมคอมพิวเตอร์\n"
        "🏢 อ.สกุลชาย SC208\n"
        "-------------------------------\n"
        "⏰ 13:00 - 17:00 น.\n"
        "📖 00-41-001 การพัฒนาคุณภาพชีวิตและสังคม\n"
        "🏢 ตึกเรียนรวม SEC 02 ศร. 211"
    )
    await interaction.response.send_message(msg)

@bot.tree.command(name="thursday", description="Show schedule for Thursday")
async def thursday(interaction: discord.Interaction):
    msg = (
        "**ตารางเรียนวันพฤหัสบดี:**\n"
        "⏰ 13:00 - 15:00 น.\n"
        "📖 06-01-313 ท.คณิตศาสตร์ดิสครีตและทฤษฎีการคำนวณ\n"
        "🏢 ตึกคณะ SEC 01 อ.ชานนท์ SC201\n"
        "-------------------------------\n"
        "⏰ 15:00 - 17:00 น.\n"
        "📖 06-14-102 ท./ป. ระบบปฏิบัติการ\n"
        "🏢 ตึกคณะ SEC 01 อ.ชานนท์ SC201"
    )
    await interaction.response.send_message(msg)

@bot.tree.command(name="friday", description="Show schedule for Friday (Free day)")
async def friday(interaction: discord.Interaction):
    msg = "🎮 **วันศุกร์:** ว่างเต็มวัน! ลุยโปรเจกต์เขียนโค้ดต่อ หรือพักผ่อนตามสบายเลยครับ"
    await interaction.response.send_message(msg)

@bot.tree.command(name="myweek", description="Show summary schedule for the entire week")
async def myweek(interaction: discord.Interaction):
    summary_msg = (
        "**สรุปตารางเรียนเทอม 2:**\n"
        "วันจันทร์: ว่างเต็มวัน! 🎮\n"
        "วันอังคาร: การคิดเชิงระบบฯ (เช้า) และ IT (บ่าย)\n"
        "วันพุธ: โปรแกรมคอมพิวเตอร์ (เช้า) และ พัฒนาคุณภาพชีวิตฯ (บ่าย)\n"
        "วันพฤหัสบดี: ดิสครีต (บ่าย) และ ระบบปฏิบัติการ (บ่าย)\n"
        "วันศุกร์: ว่างเต็มวัน! 🎮"
    )
    await interaction.response.send_message(summary_msg)

keep_alive()
# ดึง Token จาก Environment Variable ที่ตั้งไว้ในเว็บ Cloud
DISCORD_TOKEN = os.getenv('MTQ3ODY3MjgzMjkyNDg4MDk1Nw.GMjBWq.cw2AfyXdZXIsbXZ-cMIw2PpPfj_Edp3hr5ZKSU')
bot.run(DISCORD_TOKEN)
