import os

LINE = "I'm on vacation, so your email auto-escalated to my human. He has been paged and is now ticket #4821, flagged flaky after ignoring his last three replies."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
