import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')


def bringCity():
    url = "https://api.collectapi.com/weather/getWeather?data.lang=tr&data.city=" + str(city_combobox.get())
    authorization = "apikey 2mWB9ilHdfkknqcf8qaQMW:7k8s9SjXgz5yLR79SaDnB4"
    weather_response = requests.get(url, headers={"Authorization": authorization})
    resp = weather_response.json()
    label_today_day_name.config(text=resp["result"][0]["day"])
    label_day_name2.config(text=resp["result"][1]["day"])
    label_day_name3.config(text=resp["result"][2]["day"])
    label_day_name4.config(text=resp["result"][3]["day"])
    label_day_name5.config(text=resp["result"][4]["day"])
    label_day_name6.config(text=resp["result"][5]["day"])
    label_day_name7.config(text=resp["result"][6]["day"])

    label_date1.config(text=resp["result"][0]["date"])
    label_date2.config(text=resp["result"][1]["date"])
    label_date3.config(text=resp["result"][2]["date"])
    label_date4.config(text=resp["result"][3]["date"])
    label_date5.config(text=resp["result"][4]["date"])
    label_date6.config(text=resp["result"][5]["date"])
    label_date7.config(text=resp["result"][6]["date"])

    label_min12.config(text=str(round(float(resp["result"][0]["min"]))) + "°")
    label_min22.config(text=str(round(float(resp["result"][1]["min"]))) + "°")
    label_min32.config(text=str(round(float(resp["result"][2]["min"]))) + "°")
    label_min42.config(text=str(round(float(resp["result"][3]["min"]))) + "°")
    label_min52.config(text=str(round(float(resp["result"][4]["min"]))) + "°")
    label_min62.config(text=str(round(float(resp["result"][5]["min"]))) + "°")
    label_min72.config(text=str(round(float(resp["result"][6]["min"]))) + "°")

    label_max122.config(text=str(round(float(resp["result"][0]["max"]))) + "°")
    label_max222.config(text=str(round(float(resp["result"][1]["max"]))) + "°")
    label_max322.config(text=str(round(float(resp["result"][2]["max"]))) + "°")
    label_max422.config(text=str(round(float(resp["result"][3]["max"]))) + "°")
    label_max522.config(text=str(round(float(resp["result"][4]["max"]))) + "°")
    label_max622.config(text=str(round(float(resp["result"][5]["max"]))) + "°")
    label_max722.config(text=str(round(float(resp["result"][6]["max"]))) + "°")

    label_day_current_temperature1.config(text=str(round(float(resp["result"][0]["degree"]))) + "°")
    label_day_current_temperature2.config(text=str(round(float(resp["result"][1]["degree"]))) + "°")
    label_day_current_temperature3.config(text=str(round(float(resp["result"][2]["degree"]))) + "°")
    label_day_current_temperature4.config(text=str(round(float(resp["result"][3]["degree"]))) + "°")
    label_day_current_temperature5.config(text=str(round(float(resp["result"][4]["degree"]))) + "°")
    label_day_current_temperature6.config(text=str(round(float(resp["result"][5]["degree"]))) + "°")
    label_day_current_temperature7.config(text=str(round(float(resp["result"][6]["degree"]))) + "°")

    label_night.config(text=str(round(float(resp["result"][0]["night"]))) + "°")
    label_night2.config(text=str(round(float(resp["result"][2]["night"]))) + "°")
    label_night3.config(text=str(round(float(resp["result"][1]["night"]))) + "°")
    label_night4.config(text=str(round(float(resp["result"][3]["night"]))) + "°")
    label_night5.config(text=str(round(float(resp["result"][5]["night"]))) + "°")
    label_night6.config(text=str(round(float(resp["result"][4]["night"]))) + "°")
    label_night7.config(text=str(round(float(resp["result"][6]["night"]))) + "°")

    label_Nem122.config(text="%" + str(round(float(resp["result"][0]["humidity"]))))
    label_Nem222.config(text="%" + str(round(float(resp["result"][1]["humidity"]))))
    label_Nem322.config(text="%" + str(round(float(resp["result"][2]["humidity"]))))
    label_Nem422.config(text="%" + str(round(float(resp["result"][3]["humidity"]))))
    label_Nem522.config(text="%" + str(round(float(resp["result"][4]["humidity"]))))
    label_Nem622.config(text="%" + str(round(float(resp["result"][5]["humidity"]))))
    label_Nem722.config(text="%" + str(round(float(resp["result"][6]["humidity"]))))

    label_sitation.config(text=resp["result"][0]["description"].title(), font=("Montserrat", 10, "normal"))
    label_sitation2.config(text=resp["result"][2]["description"].title(), font=("Montserrat", 10, "normal"))
    label_sitation3.config(text=resp["result"][1]["description"].title(), font=("Montserrat", 10, "normal"))
    label_sitation4.config(text=resp["result"][3]["description"].title(), font=("Montserrat", 10, "normal"))
    label_sitation5.config(text=resp["result"][5]["description"].title(), font=("Montserrat", 10, "normal"))
    label_sitation6.config(text=resp["result"][4]["description"].title(), font=("Montserrat", 10, "normal"))
    label_sitation7.config(text=resp["result"][6]["description"].title(), font=("Montserrat", 10, "normal"))

    image_url = resp["result"][0]["icon"]
    response = requests.get(image_url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    canvas_width = 100
    canvas_height = 100
    image = image.resize((canvas_width, canvas_height), Image.LANCZOS)
    image_tk = ImageTk.PhotoImage(image)
    canvas_image = Canvas(window, width=canvas_width, height=canvas_height)
    canvas_image.place(x=168, y=195)
    canvas_image.create_image(0, 0, anchor="nw", image=image_tk)
    canvas_image.image = image_tk

    image_url2 = resp["result"][1]["icon"]
    response2 = requests.get(image_url2)
    image_data2 = response2.content
    image2 = Image.open(BytesIO(image_data2))
    canvas_width2 = 50
    canvas_height2 = 50
    image2 = image2.resize((canvas_width2, canvas_height2), Image.LANCZOS)
    image_tk2 = ImageTk.PhotoImage(image2)
    canvas_image2 = Canvas(window, width=canvas_width2, height=canvas_height2)
    canvas_image2.place(x=490, y=25)
    canvas_image2.create_image(0, 0, anchor="nw", image=image_tk2)
    canvas_image2.image = image_tk2

    image_url3 = resp["result"][2]["icon"]
    response3 = requests.get(image_url3)
    image_data3 = response3.content
    image3 = Image.open(BytesIO(image_data3))
    canvas_width3 = 50
    canvas_height3 = 50
    image3 = image3.resize((canvas_width3, canvas_height3), Image.LANCZOS)
    image_tk3 = ImageTk.PhotoImage(image3)
    canvas_image3 = Canvas(window, width=canvas_width3, height=canvas_height3)
    canvas_image3.place(x=490, y=180)
    canvas_image3.create_image(0, 0, anchor="nw", image=image_tk3)
    canvas_image3.image = image_tk3

    image_url4 = resp["result"][3]["icon"]
    response4 = requests.get(image_url4)
    image_data4 = response4.content
    image4 = Image.open(BytesIO(image_data4))
    canvas_width4 = 50
    canvas_height4 = 50
    image4 = image4.resize((canvas_width4, canvas_height4), Image.LANCZOS)
    image_tk4 = ImageTk.PhotoImage(image4)
    canvas_image4 = Canvas(window, width=canvas_width4, height=canvas_height4)
    canvas_image4.place(x=490, y=335)
    canvas_image4.create_image(0, 0, anchor="nw", image=image_tk4)
    canvas_image4.image = image_tk4

    image_url7 = resp["result"][6]["icon"]
    response7 = requests.get(image_url7)
    image_data7 = response7.content
    image7 = Image.open(BytesIO(image_data7))
    canvas_width7 = 50
    canvas_height7 = 50
    image7 = image7.resize((canvas_width7, canvas_height7), Image.LANCZOS)
    image_tk7 = ImageTk.PhotoImage(image7)
    canvas_image7 = Canvas(window, width=canvas_width7, height=canvas_height7)
    canvas_image7.place(x=780, y=335)
    canvas_image7.create_image(0, 0, anchor="nw", image=image_tk7)
    canvas_image7.image = image_tk7

    image_url6 = resp["result"][4]["icon"]
    response6 = requests.get(image_url6)
    image_data6 = response6.content
    image6 = Image.open(BytesIO(image_data6))
    canvas_width6 = 50
    canvas_height6 = 50
    image6 = image6.resize((canvas_width6, canvas_height6), Image.LANCZOS)
    image_tk6 = ImageTk.PhotoImage(image6)
    canvas_image6 = Canvas(window, width=canvas_width6, height=canvas_height6)
    canvas_image6.place(x=780, y=25)
    canvas_image6.create_image(0, 0, anchor="nw", image=image_tk6)
    canvas_image6.image = image_tk6

    image_url5 = resp["result"][5]["icon"]
    response5 = requests.get(image_url5)
    image_data5 = response5.content
    image5 = Image.open(BytesIO(image_data5))
    canvas_width5 = 50
    canvas_height5 = 50
    image5 = image5.resize((canvas_width5, canvas_height5), Image.LANCZOS)
    image_tk5 = ImageTk.PhotoImage(image5)
    canvas_image5 = Canvas(window, width=canvas_width5, height=canvas_height5)
    canvas_image5.place(x=780, y=180)
    canvas_image5.create_image(0, 0, anchor="nw", image=image_tk5)
    canvas_image5.image = image_tk5


class CustomCanvas(Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg=bek, bd=1, relief="solid")


class CustomLabels(Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Montserrat", 15, "normal"), bg="#E6B0AA")


class CustomLabels2(Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Montserrat", 13, "normal"), bg="#E6B0AA")


window = Tk()
bek = '#D98880'
window_width = 865
window_height = 490
center_window(window, window_width, window_height)
window.title("WeatherApp")
window.config(bg=bek)
window.update()
window.resizable(False, False)

canvas = CustomCanvas(window, width=265, height=140)
canvas.place(x=20, y=20)
canvas.config(bg="#E6B0AA")

canvas2 = CustomCanvas(window, width=265, height=295)
canvas2.place(x=20, y=175)
canvas2.config(bg="#E6B0AA")

canvas3 = CustomCanvas(window, width=265, height=140)
canvas3.place(x=300, y=20)
canvas3.config(bg="#E6B0AA")

canvas4 = CustomCanvas(window, width=265, height=140)
canvas4.place(x=300, y=175)
canvas4.config(bg="#E6B0AA")

canvas5 = CustomCanvas(window, width=265, height=140)
canvas5.place(x=300, y=330)
canvas5.config(bg="#E6B0AA")

canvas6 = CustomCanvas(window, width=265, height=140)
canvas6.place(x=300, y=20)
canvas6.config(bg="#E6B0AA")

canvas7 = CustomCanvas(window, width=265, height=140)
canvas7.place(x=580, y=20)
canvas7.config(bg="#E6B0AA")

canvas8 = CustomCanvas(window, width=265, height=140)
canvas8.place(x=580, y=175)
canvas8.config(bg="#E6B0AA")

canvas9 = CustomCanvas(window, width=265, height=140)
canvas9.place(x=580, y=330)
canvas9.config(bg="#E6B0AA")

sehirler = [
    "adana",
    "adiyaman",
    "afyonkarahisar",
    "agri",
    "amasya",
    "ankara",
    "antalya",
    "artvin",
    "aydin",
    "balikesir",
    "bilecik",
    "bingol",
    "bitlis",
    "bolu",
    "burdur",
    "bursa",
    "canakkale",
    "cankiri",
    "corum",
    "denizli",
    "diyarbakir",
    "edirne",
    "elazig",
    "erzincan",
    "erzurum",
    "eskisehir",
    "gaziantep",
    "giresun",
    "gumushane",
    "hakkari",
    "hatay",
    "isparta",
    "mersin",
    "istanbul",
    "izmir",
    "kars",
    "kastamonu",
    "kayseri",
    "kirklareli",
    "kirsehir",
    "kocaeli",
    "konya",
    "kutahya",
    "malatya",
    "manisa",
    "kahramanmaras",
    "mardin",
    "mugla",
    "mus",
    "nevsehir",
    "nigde",
    "ordu",
    "rize",
    "sakarya",
    "samsun",
    "siirt",
    "sinop",
    "sivas",
    "tekirdag",
    "tokat",
    "trabzon",
    "tunceli",
    "sanliurfa",
    "usak",
    "van",
    "yozgat",
    "zonguldak",
    "aksaray",
    "bayburt",
    "karaman",
    "kirikkale",
    "batman",
    "sirnak",
    "bartin",
    "ardahan",
    "igdir",
    "yalova",
    "karabuk",
    "kilis",
    "osmaniye",
    "duzce"
]
city_combobox = ttk.Combobox(window, values=sehirler, font=("Montserrat", 12, "normal"))
city_combobox.place(x=75, y=70)
city_combobox.config(width=12)

city_search_button = Button(text="Ara", font=("Montserrat", 14, "normal"), command=bringCity)
city_search_button.place(x=179, y=105)

choose_city_label = CustomLabels(text="     Şehir seçin")
choose_city_label.place(x=70, y=35)

label_today = CustomLabels(text="Bugün")
label_today.place(x=35, y=180)
label_today.config(font=("Montserrat", 25, "normal"))

label_today = CustomLabels(text="Bugün")
label_today.place(x=35, y=180)
label_today.config(font=("Montserrat", 25, "normal"))

label_today_day_name = CustomLabels(text="dayname")
label_today_day_name.place(x=37, y=222)

label_day_name2 = CustomLabels(text="dayname")
label_day_name2.place(x=305, y=30)

label_day_name3 = CustomLabels(text="dayname")
label_day_name3.place(x=305, y=185)

label_day_name4 = CustomLabels(text="dayname")
label_day_name4.place(x=305, y=340)

label_day_name5 = CustomLabels(text="dayname")
label_day_name5.place(x=585, y=30)

label_day_name6 = CustomLabels(text="dayname")
label_day_name6.place(x=585, y=185)

label_day_name7 = CustomLabels(text="dayname")
label_day_name7.place(x=585, y=340)

########

label_date2 = CustomLabels(text="date")
label_date2.place(x=310, y=60)
label_date2.config(font=("Montserrat", 12, "normal"))

label_date3 = CustomLabels(text="date")
label_date3.place(x=310, y=215)
label_date3.config(font=("Montserrat", 12, "normal"))

label_date4 = CustomLabels(text="date")
label_date4.place(x=310, y=370)
label_date4.config(font=("Montserrat", 12, "normal"))

label_date5 = CustomLabels(text="date")
label_date5.place(x=590, y=60)
label_date5.config(font=("Montserrat", 12, "normal"))

label_date6 = CustomLabels(text="date")
label_date6.place(x=590, y=215)
label_date6.config(font=("Montserrat", 12, "normal"))

label_date7 = CustomLabels(text="date")
label_date7.place(x=590, y=370)
label_date7.config(font=("Montserrat", 12, "normal"))

#######

label_max12 = CustomLabels2(text="En Yüksek:")
label_max12.place(x=30, y=380)

label_max22 = CustomLabels2(text="En Yüksek:")
label_max22.place(x=310, y=120)

label_max32 = CustomLabels2(text="En Yüksek:")
label_max32.place(x=310, y=275)

label_max42 = CustomLabels2(text="En Yüksek:")
label_max42.place(x=310, y=430)

label_max52 = CustomLabels2(text="En Yüksek:")
label_max52.place(x=590, y=120)

label_max62 = CustomLabels2(text="En Yüksek:")
label_max62.place(x=590, y=275)

label_max72 = CustomLabels2(text="En Yüksek:")
label_max72.place(x=590, y=430)

########

label_Nem12 = CustomLabels2(text="Nem:")
label_Nem12.place(x=30, y=410)

label_Nem22 = CustomLabels2(text="Nem:")
label_Nem22.place(x=460, y=120)

label_Nem32 = CustomLabels2(text="Nem:")
label_Nem32.place(x=460, y=275)

label_Nem42 = CustomLabels2(text="Nem:")
label_Nem42.place(x=460, y=430)

label_Nem52 = CustomLabels2(text="Nem:")
label_Nem52.place(x=743, y=120)

label_Nem62 = CustomLabels2(text="Nem:")
label_Nem62.place(x=743, y=275)

label_Nem72 = CustomLabels2(text="Nem:")
label_Nem72.place(x=743, y=430)

######

label_min22 = CustomLabels2(text="min")
label_min22.place(x=400, y=90)

label_min32 = CustomLabels2(text="min")
label_min32.place(x=400, y=245)

label_min42 = CustomLabels2(text="min")
label_min42.place(x=400, y=400)

label_min52 = CustomLabels2(text="min")
label_min52.place(x=680, y=90)

label_min62 = CustomLabels2(text="min")
label_min62.place(x=680, y=245)

label_min72 = CustomLabels2(text="min")
label_min72.place(x=680, y=400)

########

label_Nem122 = CustomLabels2(text="hum")
label_Nem122.place(x=85, y=410)

label_Nem222 = CustomLabels2(text="hum")
label_Nem222.place(x=515, y=120)

label_Nem322 = CustomLabels2(text="hum")
label_Nem322.place(x=515, y=275)

label_Nem422 = CustomLabels2(text="hum")
label_Nem422.place(x=515, y=430)

label_Nem522 = CustomLabels2(text="hum")
label_Nem522.place(x=795, y=120)

label_Nem622 = CustomLabels2(text="hum")
label_Nem622.place(x=795, y=275)

label_Nem722 = CustomLabels2(text="hum")
label_Nem722.place(x=795, y=430)

########

label_day_current_temperature1 = CustomLabels(text="0")
label_day_current_temperature1.place(x=40, y=260)
label_day_current_temperature1.config(font=("Montserrat", 60, "normal"))

label_day_current_temperature2 = CustomLabels(text="0")
label_day_current_temperature2.place(x=410, y=25)
label_day_current_temperature2.config(font=("Montserrat", 40, "normal"))

label_day_current_temperature3 = CustomLabels(text="0")
label_day_current_temperature3.place(x=410, y=180)
label_day_current_temperature3.config(font=("Montserrat", 40, "normal"))

label_day_current_temperature4 = CustomLabels(text="0")
label_day_current_temperature4.place(x=410, y=335)
label_day_current_temperature4.config(font=("Montserrat", 40, "normal"))

label_day_current_temperature5 = CustomLabels(text="0")
label_day_current_temperature5.place(x=690, y=25)
label_day_current_temperature5.config(font=("Montserrat", 40, "normal"))

label_day_current_temperature6 = CustomLabels(text="0")
label_day_current_temperature6.place(x=690, y=180)
label_day_current_temperature6.config(font=("Montserrat", 40, "normal"))

label_day_current_temperature7 = CustomLabels(text="0")
label_day_current_temperature7.place(x=690, y=335)
label_day_current_temperature7.config(font=("Montserrat", 40, "normal"))

#########

label_today_day_name12 = CustomLabels2(text="Gece:")
label_today_day_name12.place(x=30, y=440)

label_today_day_name22 = CustomLabels2(text="Gece:")
label_today_day_name22.place(x=460, y=245)

label_today_day_name32 = CustomLabels2(text="Gece:")
label_today_day_name32.place(x=460, y=90)

label_today_day_name42 = CustomLabels2(text="Gece:")
label_today_day_name42.place(x=460, y=400)

label_today_day_name52 = CustomLabels2(text="Gece:")
label_today_day_name52.place(x=740, y=245)

label_today_day_name62 = CustomLabels2(text="Gece:")
label_today_day_name62.place(x=740, y=90)

label_today_day_name72 = CustomLabels2(text="Gece:")
label_today_day_name72.place(x=740, y=400)

############

label_night = CustomLabels2(text="night")
label_night.place(x=85, y=440)

label_night2 = CustomLabels2(text="night")
label_night2.place(x=515, y=245)

label_night3 = CustomLabels2(text="night")
label_night3.place(x=515, y=90)

label_night4 = CustomLabels2(text="night")
label_night4.place(x=515, y=400)

label_night5 = CustomLabels2(text="night")
label_night5.place(x=795, y=245)

label_night6 = CustomLabels2(text="night")
label_night6.place(x=795, y=90)

label_night7 = CustomLabels2(text="night")
label_night7.place(x=795, y=400)

################

label_min1 = CustomLabels2(text="En Düşük:")
label_min1.place(x=30, y=350)

label_min3 = CustomLabels2(text="En Düşük:")
label_min3.place(x=310, y=245)

label_min5 = CustomLabels2(text="En Düşük:")
label_min5.place(x=590, y=90)

label_min6 = CustomLabels2(text="En Düşük:")
label_min6.place(x=590, y=245)

label_min2 = CustomLabels2(text="En Düşük:")
label_min2.place(x=310, y=90)

label_min4 = CustomLabels2(text="En Düşük:")
label_min4.place(x=310, y=400)

label_min7 = CustomLabels2(text="En Düşük:")
label_min7.place(x=590, y=400)

#######

label_max122 = CustomLabels2(text="max")
label_max122.place(x=130, y=380)

label_max222 = CustomLabels2(text="max")
label_max222.place(x=410, y=120)

label_max322 = CustomLabels2(text="max")
label_max322.place(x=410, y=275)

label_max422 = CustomLabels2(text="max")
label_max422.place(x=410, y=430)

label_max522 = CustomLabels2(text="max")
label_max522.place(x=690, y=120)

label_max622 = CustomLabels2(text="max")
label_max622.place(x=690, y=275)

label_max722 = CustomLabels2(text="max")
label_max722.place(x=690, y=430)

#########

label_max12 = CustomLabels2(text="En Yüksek:")
label_max12.place(x=30, y=380)

label_max22 = CustomLabels2(text="En Yüksek:")
label_max22.place(x=310, y=120)

label_max32 = CustomLabels2(text="En Yüksek:")
label_max32.place(x=310, y=275)

label_max42 = CustomLabels2(text="En Yüksek:")
label_max42.place(x=310, y=430)

label_max52 = CustomLabels2(text="En Yüksek:")
label_max52.place(x=590, y=120)

label_max62 = CustomLabels2(text="En Yüksek:")
label_max62.place(x=590, y=275)

label_max72 = CustomLabels2(text="En Yüksek:")
label_max72.place(x=590, y=430)

###########

label_sitation = CustomLabels2(text="sitation")
label_sitation.place(x=165, y=300)

label_sitation2 = CustomLabels2(text="sitation")
label_sitation2.place(x=470, y=230)

label_sitation3 = CustomLabels2(text="sitation")
label_sitation3.place(x=470, y=75)

label_sitation4 = CustomLabels2(text="sitation")
label_sitation4.place(x=470, y=385)

label_sitation5 = CustomLabels2(text="sitation")
label_sitation5.place(x=750, y=230)

label_sitation6 = CustomLabels2(text="sitation")
label_sitation6.place(x=750, y=75)

label_sitation7 = CustomLabels2(text="sitation")
label_sitation7.place(x=755, y=385)

label_date1 = CustomLabels(text="date")
label_date1.config(font=("Montserrat", 12, "normal"))
label_date1.place(x=37, y=252)

label_min12 = CustomLabels2(text="min")
label_min12.place(x=125, y=350)

window.mainloop()
