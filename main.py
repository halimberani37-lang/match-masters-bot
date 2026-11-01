import os
import random
import requests

# مفتاح Dev.to API الخاص بك
DEV_TO_API_KEY = "ZZL6qZqChVHcwdYTJqsPta7j"

# رابط عرض CPAlead الخاص بك المطابق للمطلوب
CPA_OFFER_LINK = "https://www.cpalead.com/en/offers/cpa/match-masters-trophies-rewards-5547190"

# عناوين مخصصة ومستهدفة لجذب عشاق لعبة Match Masters
GAMING_TOPICS = [
    {
        "title": "Match Masters Free Trophies and Booster Rewards (2026 Updated Guide)", 
        "tag": "gaming"
    },
    {
        "title": "How to Get Free Daily Boosters and Rewards in Match Masters", 
        "tag": "tutorial"
    },
    {
        "title": "Claim Your Exclusive Match Masters Trophies Pack Now", 
        "tag": "mobile"
    }
]

def create_cpa_article():
    topic = random.choice(GAMING_TOPICS)
    
    body = f"""# {topic['title']}

Are you a passionate Match Masters player looking to level up your game, boost your trophies, and unlock exclusive rewards without spending real money? 

Getting ahead in competitive mobile matches requires the right boosters and daily rewards. We have verified a direct portal for players to claim their special promotional trophy packages.

### How to Claim Your Rewards:
1. Click the official secure link below to open the reward portal.
2. Complete a quick verification step (takes less than 60 seconds).
3. Instantly claim your Match Masters trophies and boosters directly to your account!

👉 **[Click Here to Claim Match Masters Trophies & Rewards Now]({CPA_OFFER_LINK})**

---
*Disclaimer: This promotional guide is intended for active mobile gamers. Rewards are subject to completion of standard sponsor offers.*
"""
    
    url = "https://dev.to/api/articles"
    headers = {"api-key": DEV_TO_API_KEY, "Content-Type": "application/json"}
    payload = {
        "article": {
            "title": topic["title"],
            "published": True,
            "body_markdown": body,
            "tags": [topic["tag"], "games", "mobile", "rewards"]
        }
    }
    
    res = requests.post(url, json=payload, headers=headers)
    if res.status_code == 201:
        print("[+] Article published successfully! Automated traffic funnel is live.")
    else:
        print(f"[-] Error: {res.status_code} - {res.text}")

if __name__ == "__main__":
    create_cpa_article()
  
