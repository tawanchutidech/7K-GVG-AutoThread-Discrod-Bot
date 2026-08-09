# 7K GVG Auto-Thread Discord Bot

บอท Discord ที่สร้าง thread อัตโนมัติเมื่อมีข้อความใหม่โพสต์ในช่องที่กำหนดไว้สำหรับกิจกรรม GVG ของเกม 7 Knights

## Setup

1. ติดตั้ง dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. คัดลอก `.env.example` เป็น `.env` แล้วกรอกค่า:

   - `DISCORD_TOKEN`: token ของบอท (จาก [Discord Developer Portal](https://discord.com/developers/applications))
   - `GVG_CHANNEL_IDS`: id ของช่องที่ต้องการให้บอทสร้าง thread อัตโนมัติ คั่นด้วย comma ถ้ามีหลายช่อง
   - `THREAD_AUTO_ARCHIVE_MINUTES`: เวลาก่อน thread จะถูก archive อัตโนมัติ (นาที) ค่าเริ่มต้น 1440 (1 วัน)

3. เปิดสิทธิ์ **Message Content Intent** ให้บอทในหน้า Developer Portal (Bot > Privileged Gateway Intents)

4. เชิญบอทเข้าเซิร์ฟเวอร์ด้วยสิทธิ์อย่างน้อย: `View Channel`, `Send Messages`, `Create Public Threads`, `Manage Threads`

5. รันบอท:

   ```bash
   python bot.py
   ```

## การทำงาน

เมื่อมีข้อความใหม่ (ที่ไม่ใช่จากบอท) ถูกโพสต์ในช่องที่ระบุใน `GVG_CHANNEL_IDS` บอทจะสร้าง thread ต่อจากข้อความนั้นให้อัตโนมัติ โดยตั้งชื่อ thread จากบรรทัดแรกของข้อความ
