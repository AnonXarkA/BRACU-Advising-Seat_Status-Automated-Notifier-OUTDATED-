# BRACU-Advising-Seat-Status-Automated-Notifier [OUTDATED]

🛑 OUTDATED - DOES NOT WORK ANYMORE! 🛑
BRAC University has transitioned from USIS to a new system called Connect (Student Life Cycle Management System - SLMS). This script was designed for the old USIS system and will no longer function for checking course availability. Please refer to official BRAC University channels for information on the new Connect system.

🎯 If a new script is developed for the new Connect system, this repository will be updated.

🚀 BRACU Advising Course Seat Status Notifier 🎓🔔
(Formerly for USIS - Now Outdated)

 ⚡ <a href="https://github.com/AnonXarkA/BRACU-Advising-Seat_Status-Automated-Notifier-OUTDATED-/blob/main/main.py">Script</a> <br>

Never miss an open seat again! This bot was your personal automated assistant for monitoring course availability on the BRAC University USIS portal. It tirelessly checked for open spots in your desired courses and sections, instantly notifying you via Slack the moment a seat became available.

✨ How It Worked (Legacy USIS System) ✨
This script automated the tedious task of manually checking for course openings on the old USIS system. Here's the magic behind it:

🌐 Constant Vigilance: It relentlessly visited the official BRAC University USIS page that listed course seat availability.

🎯 Targeted Search: You told it exactly which courses (e.g., CSE321, CSE422) and even specific sections (like Section 02 of CSE321 or Sections 07 & 09 of CSE422) you were hunting for.

📊 Seat Counter: For your chosen courses and sections, it scanned the webpage and accurately counted the number of currently available seats.

📢 Instant Slack Alerts: The moment it detected at least one seat available in any of your monitored courses/sections, it sprang into action! A notification zipped its way to your designated Slack channel (and pinged a specific user if configured), telling you something like:

💬 "Hey <@YourUserID>! CSE321 Section 02 is available now! Check the website for more details."

📝 Log Keeper: Every time a seat was found and a notification was sent, the script diligently recorded the details (course code, section, faculty, number of seats, and the time of discovery) in a local file named notification.txt.

⚡ Lightning Fast Checks: This wasn't a once-an-hour check. The script was designed to re-check the website at an extremely rapid pace (currently set to every 0.01 seconds!), maximizing your chances of snagging that coveted spot.

This script offered peace of mind for the old system, but please look for solutions compatible with the new BRAC University Connect SLMS. 🧘‍♂️💻
