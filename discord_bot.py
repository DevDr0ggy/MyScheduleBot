import discord
from discord.ext import commands, tasks
import datetime
import pytz
import os
import json
import aiohttp
import random
from dotenv import load_dotenv

load_dotenv()

HOMEWORK_FILE = 'homework.json'
def load_homework():
    if not os.path.exists(HOMEWORK_FILE):
        return {}

    with open(HOMEWORK_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# ==========================================
# Database for Attendance Tracker
# ==========================================
ATTENDANCE_FILE = 'attendance.json'

# Load attendance data
def load_attendance():
    if not os.path.exists(ATTENDANCE_FILE):
        return {} # ถ้ายังไม่มีไฟล์ ให้ส่ง Dictionary ว่างๆ กลับไป
    with open(ATTENDANCE_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# Save attendance data
def save_attendance(data):
    with open(ATTENDANCE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

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

@bot.tree.command(name="hw_add", description="Add a new homework or project task")
async def hw_add(interaction: discord.Interaction, subject: str, task: str, due_date: str):
    data = load_homework()

    if "tasks" not in data:
        data["tasks"] = []

    if len(data["tasks"]) == 0:
        new_id = 1
    else:
        new_id = data["tasks"][-1]["id"] + 1

    new_task = {
        "id": new_id,
        "subject": subject,
        "task": task,
        "due_date": due_date
    }

    data["tasks"].append(new_task)
    save_homework(data)

    msg = (
        f"✅ **บันทึกการบ้านเรียบร้อย!**\n"
        f"📚 **วิชา:** {subject}\n"
        f"📝 **งานที่สั่ง:** {task}\n"
        f"📅 **กำหนดส่ง:** {due_date}\n"
        f"*(รหัสงาน: {new_id})*"
    )
    await interaction.response.send_message(msg)

@bot.tree.command(name="hw_list", description="Show all pending homework")
async def hw_list(interaction: discord.Interaction):
    data = load_homework()

    if "tasks" not in data or len(data["tasks"]) == 0:
        await interaction.response.send_message("🎉 **ไม่มีการบ้านค้างเลย!** ไปเล่นเกม ดูกันพลาได้สบายใจ!")
        return

    msg = "📋 **รายการการบ้านที่ต้องทำ:**\n"
    for task in data["tasks"]:
        msg += f"🔹 **[ID: {task['id']}]** วิชา {task['subject']} | 📝 {task['task']} | 📅 ส่ง: {task['due_date']}\n"

    await interaction.response.send_message(msg)

@bot.tree.command(name="hw_done", description="Mark homework as done and remove it")
async def hw_done(interaction: discord.Interaction, task_id: int):
    data = load_homework()

    if "tasks" not in data or len(data["tasks"]) == 0:
        await interaction.response.send_message("❌ ไม่มีการบ้านในระบบให้ลบครับ!")
        return

    task_found = False
    for i in range(len(data["tasks"])):
        if data["tasks"][i]["id"] == task_id:
            removed_task = data["tasks"].pop(i)
            task_found = True
            break

    if task_found:
        save_homework(data)
        await interaction.response.send_message(
            f"✅ **เย้! ลบงานรหัส {task_id} เรียบร้อย!**\n(ลบวิชา {removed_task['subject']} ออกจากสมุดจดแล้ว เก่งมากครับ!)")
    else:
        await interaction.response.send_message(
            f"❌ **หาไม่เจอ!** ไม่มีงานรหัส {task_id} ในสมุดจดครับ ลองพิมพ์ /hw_list เช็คดูอีกทีนะ")

@bot.tree.command(name="skip_add", description="Add 1 skip quota to a specific subject")
async def skip_add(interaction: discord.Interaction, subject: str):
    data = load_attendance()

    if subject not in data:
        data[subject] = 0

    data[subject] += 1
    save_attendance(data)

    warning = ""
    if data[subject] >= 3:
        warning = "\n🚨 **อันตราย!** ขาดเกิน 3 ครั้งระวังหมดสิทธิ์สอบ (ติด F) นะครับ!"

    msg = f"⚠️ บันทึกการขาดเรียนวิชา **{subject}**\nรวมขาดไปแล้ว: **{data[subject]} ครั้ง**{warning}"
    await interaction.response.send_message(msg)

@bot.tree.command(name="skip_check", description="Check your skip count for all subjects")
async def skip_check(interaction: discord.Interaction):
    data = load_attendance()

    if not data:
        await interaction.response.send_message("✅ **เยี่ยมมาก!** ยังไม่เคยขาดเรียนเลยสักวิชาครับ รักษาความฟิตนี้ไว้!")
        return

    msg = "📊 **สรุปโควต้าการขาดเรียน:**\n"
    for subj, count in data.items():
        msg += f"🔹 วิชา {subj}: ขาดไปแล้ว **{count}** ครั้ง\n"

    await interaction.response.send_message(msg)

@bot.tree.command(name="skip_reset", description="Reset the skip count for a subject to 0")
async def skip_reset(interaction: discord.Interaction, subject: str):
    data = load_attendance()

    if subject in data:
        del data[subject]
        save_attendance(data)
        await interaction.response.send_message(
            f"🔄 **รีเซ็ต!** ลบประวัติการขาดเรียนวิชา **{subject}** เรียบร้อยแล้วครับ")
    else:
        await interaction.response.send_message(f"❌ **หาไม่เจอ!** ไม่พบประวัติการขาดเรียนวิชา **{subject}** ในระบบครับ")

@bot.tree.command(name="weather", description="Check current weather in Bang Phra, Chon Buri")
async def weather(interaction: discord.Interaction):
    lat = 13.2148
    lon = 100.9416
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    await interaction.response.defer()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()

                current = data.get("current_weather", {})
                temp = current.get("temperature", "-")
                wind_speed = current.get("windspeed", "-")
                weather_code = current.get("weathercode", 0)

                condition = "ท้องฟ้าแจ่มใส ☀️"
                if weather_code in [1, 2, 3]:
                    condition = "มีเมฆบางส่วน ⛅"
                elif weather_code in [45, 48]:
                    condition = "มีหมอก 🌫️"
                elif weather_code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
                    condition = "ฝนตก 🌧️ (อย่าลืมพกเสื้อกันฝน!)"
                elif weather_code in [71, 73, 75]:
                    condition = "หิมะตก (ในไทยเนี่ยนะ!) ❄️"
                elif weather_code in [95, 96, 99]:
                    condition = "พายุฝนฟ้าคะนอง ⛈️ (อันตราย! งดแว้นเด็ดขาด)"

                msg = (
                    "🌤️ **รายงานสภาพอากาศ ณ บางพระ ชลบุรี** 🌤️\n"
                    f"🌡️ อุณหภูมิ: **{temp} °C**\n"
                    f"🌬️ ความเร็วลม: **{wind_speed} km/h**\n"
                    f"👀 สภาพอากาศ: **{condition}**"
                )

                await interaction.followup.send(msg)
            else:
                await interaction.followup.send("❌ บอทติดต่อกรมอุตุฯ ไม่ได้ครับ ลองใหม่อีกครั้งนะ")

@bot.tree.command(name="randomday", description="สุ่มกิจกรรมทำในวันว่าง (จันทร์/ศุกร์)")
async def randomday(interaction: discord.Interaction):
    activities = [
        "🤖 **ลุยงานโมเดล**: หยิบกันพลาหรือรถทามิย่าตัวใหม่มาต่อ พ่นสีแอร์บรัช ติดดีคอลให้ฉ่ำๆ ไปเลย!",
        "📖 **เสพมังงะ/อนิเมะ**: หยิบ Dr. Stone, Chainsaw Man, Sanda หรือเรื่องอื่นมาอ่านชิลๆ ต่อให้จบเล่ม!",
        "🧟 **Dev Roblox**: เปิด Studio ลุยเขียนโค้ด Lua อัปเกรดระบบเกมซอมบี้ของเราต่อให้เดือดๆ!",
        "⛏️ **อัปเดตม็อด Minecraft**: ลุยเขียน Java ปรับปรุงม็อด Mob & Item Stacker และม็อดอื่นๆ บน CurseForge!",
        "💻 **เล่น AI & เขียนโค้ด**: ลุยโปรเจกต์ Python สร้างแอปเจ๋งๆ หรือลองเล่นเจนรูปจาก Stable Diffusion!",
        "🎮 **เกมเมอร์โหมด**: ปิดโหมด Dev ทิ้งไป วันนี้ขอจับจอยลุยเล่นเกมให้หนำใจยาวๆ!"
    ]
    chosen_activity = random.choice(activities)
    msg = (
        "🎲 **ตู้กาชาสุ่มกิจกรรมวันว่างทำงานแล้ว!** 🎲\n"
        f"🎉 วันนี้บอทขอเสนอให้ชัย... \n\n"
        f"👉 {chosen_activity}"
    )

    await interaction.response.send_message(msg)

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

if DISCORD_TOKEN is None:
    print("Error: DISCORD_TOKEN not found! Please check your .env file.")
else:
    bot.run(DISCORD_TOKEN)