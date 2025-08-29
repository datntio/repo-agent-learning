import os
import requests

# Lấy API key từ biến môi trường (hoặc gán trực tiếp)
api_key = ""
url = "https://api.openai.com/v1/dashboard/billing/credit_grants"

headers = {
    "Authorization": f"Bearer {api_key}",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    total = data.get("total_granted", 0)
    used = data.get("total_used", 0)
    remaining = data.get("total_available", 0)
    
    print(f"💳 Tổng credits được cấp: ${total}")
    print(f"💸 Đã dùng: ${used}")
    print(f"✅ Còn lại: ${remaining}")
else:
    print("Lỗi khi gọi API:", response.text)
