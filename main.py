import fake_useragent

from inizel import script as sc

app = sc.App(user_agent=fake_useragent.UserAgent().chrome)

get_data = (app.Start('121d4b1fcc1406dea3c475e1f74c6265', html=True))

print(get_data)
