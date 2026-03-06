import discord
from discord.ext import commands, tasks
import datetime
import pytz
import os
import json
from dotenv import load_dotenv

load_dotenv()

HOMEWORK_FILE = 'homework.json'
def load_homework():
    if not os.path.exists(HOMEWORK_FILE):
        return {}

    with open(HOMEWORK_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_homework(data):
    with open(HOMEWORK_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

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

# Command to add new homework
@bot.tree.command(name="hw_add", description="Add a new homework or project task")
async def hw_add(interaction: discord.Interaction, subject: str, task: str, due_date: str):
    # 1. Load existing data from the database
    data = load_homework()

    # 2. Check if 'tasks' list exists in data; if not, create an empty list
    if "tasks" not in data:
        data["tasks"] = []

    # 3. Generate a unique ID for the new task (Auto-increment ID)
    if len(data["tasks"]) == 0:
        new_id = 1
    else:
        # Get the ID of the last task and add 1
        new_id = data["tasks"][-1]["id"] + 1

    # 4. Create a dictionary for the new task
    new_task = {
        "id": new_id,
        "subject": subject,
        "task": task,
        "due_date": due_date
    }

    # 5. Append the new task to our list and save it to the JSON file
    data["tasks"].append(new_task)
    save_homework(data)

    # 6. Send a success message back to Discord
    msg = (
        f"✅ **บันทึกการบ้านเรียบร้อย!**\n"
        f"📚 **วิชา:** {subject}\n"
        f"📝 **งานที่สั่ง:** {task}\n"
        f"📅 **กำหนดส่ง:** {due_date}\n"
        f"*(รหัสงาน: {new_id})*"
    )
    await interaction.response.send_message(msg)

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

if DISCORD_TOKEN is None:
    print("Error: DISCORD_TOKEN not found! Please check your .env file.")
else:
    bot.run(DISCORD_TOKEN)