import feedparser
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# ==============================
# YOUR EMAIL SETTINGS
# ==============================

SENDER_EMAIL = "poojyayaservices05@gmail.com"
RECEIVER_EMAIL = "poojyayaservices05@gmail.com"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# ==============================
# ADD ALL 43 RSS LINKS BELOW
# ==============================

rss_feeds = [
    "https://www.google.co.in/alerts/feeds/10748322816189185840/1320877466155729826",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/1320877466155731200",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/5124911605297393947",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/5124911605297396858",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/5124911605297396875",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/5124911605297394001",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/12485425858453399122",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/12485425858453399008",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/12485425858453399982",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/12485425858453401426",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/8265646033163724062",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/11508536874343699620",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/11508536874343698889",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/3852864190958493558",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/3852864190958491926",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/3852864190958489716",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/3852864190958491711",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/9252584025276769865",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/3852864190958492632",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/8737806420766564858",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/8737806420766565599",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/8737806420766565180",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/6683281150689694559",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/8737806420766565313",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/8737806420766564743",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/5841962531194199371",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/5841962531194199371",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/6683281150689697233",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/17178036024535804533",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/17178036024535803793",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/17178036024535803377",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/17178036024535802984",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/17178036024535804268",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/6331781132756083251",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/6331781132756085664",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/1364694785644620932",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/6331781132756084113",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/10903339286186028952",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/10903339286186025653",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/10903339286186026100",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/16925737594949036953",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/7305869655932463942",
    "https://www.google.co.in/alerts/feeds/10748322816189185840/2350521390048332835",
]


# ==============================
# KEYWORDS
# ==============================

security_keywords = [
    "security", "guard", "watchman", "psara",
    "cctv", "surveillance", "atm", "bank security"
]

manpower_keywords = [
    "manpower", "housekeeping", "outsourcing",
    "mts", "labour", "staffing", "data entry"
]

karnataka_keywords = [
    "karnataka", "bengaluru", "mysuru",
    "mangaluru", "ballari", "hubballi",
    "belagavi", "tumakuru", "shivamogga"
]

# ==============================
# FETCH TENDERS
# ==============================

# ==============================
# FETCH TENDERS (DEBUG MODE)
# ==============================

valid_tenders = []
all_entries = []

for feed_url in rss_feeds:
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        title = entry.title
        link = entry.link

        all_entries.append((title, link))

# DEBUG: Print total entries found
print("Total entries fetched from RSS:", len(all_entries))

# Temporarily send ALL entries without filtering
valid_tenders = all_entries


# ==============================
# CREATE EMAIL BODY
# ==============================

body = "<h2>Daily Karnataka Tender Report</h2>"

if not valid_tenders:
    body += "<p>No new relevant tenders found in last 24 hours.</p>"
else:
    body += "<ul>"
    for title, link in valid_tenders:
        body += f"<li><a href='{link}'>{title}</a></li>"
    body += "</ul>"

# ==============================
# SEND EMAIL
# ==============================

msg = MIMEMultipart()
msg['From'] = SENDER_EMAIL
msg['To'] = RECEIVER_EMAIL
msg['Subject'] = "Daily Karnataka Security & Manpower Tender Report"

msg.attach(MIMEText(body, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(SENDER_EMAIL, EMAIL_PASSWORD)
server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
server.quit()

print("Email sent successfully!")
