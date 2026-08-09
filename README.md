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

## Deploy บน Railway

โปรเจกต์นี้มี `Procfile` และ `railway.json` เตรียมไว้ให้แล้ว (รันเป็น worker process ไม่ใช่ web service)

1. เข้า [railway.app](https://railway.app) แล้วสร้างโปรเจกต์ใหม่แบบ **Deploy from GitHub repo**
2. เลือก repo `tawanchutidech/7K-GVG-AutoThread-Discrod-Bot`
3. ไปที่แท็บ **Variables** ของ service แล้วเพิ่ม environment variables ต่อไปนี้ (ค่าจริงของคุณ ไม่ต้องแชร์ให้ใคร):
   - `DISCORD_TOKEN`
   - `GVG_CHANNEL_IDS`
   - `THREAD_AUTO_ARCHIVE_MINUTES` (ถ้าต้องการตั้งค่าอื่นนอกจากค่า default)
4. Railway จะ build ด้วย Nixpacks และรันคำสั่งใน `railway.json` (`python bot.py`) อัตโนมัติ
5. ดู log ในแท็บ **Deployments** เพื่อยืนยันว่าบอทออนไลน์ (ควรเห็นข้อความ `Logged in as ...`)
