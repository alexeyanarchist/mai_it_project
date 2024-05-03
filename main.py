import requests

token = "547e9955547e9955547e9955025766beba5547e547e99553250aa59320ed33b91dc33c6"
version = 5.199
domain = str(input("Enter user id: ")).lower()
fields = "bdate,education,followers_count,counters"


response = requests.get("https://api.vk.com/method/users.get",
                        params={
                            "access_token": token,
                            "v": version,
                            "user_ids": domain,
                            "fields": fields
                        }
                        )

step_val = response.json()
data = step_val['response'][0]

print(f"Имя: {data['first_name']} {data['last_name']}")
print(f"Количество подписчиков: {data['followers_count']}")
print(f"Остальные сведения: {data['counters']}")