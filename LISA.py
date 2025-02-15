# Created By Umut Araz

import speech_recognition as sr
import pyttsx3
import datetime
import requests
import os
import platform
import subprocess 
import random 
import webbrowser 
from googletrans import Translator

engine = pyttsx3.init()

def speak(text):
    """Metni sesli olarak okumak için fonksiyon."""
    engine.say(text)
    engine.runAndWait()

def perform_calculation():
    """Kullanıcıdan iki sayı alıp hangi işlemi yapmak istediğini sorar ve sonucu döner."""


    
    while True:
        speak("Birinci sayıyı söyleyin.")
        num1 = get_audio()

        try:
            num1 = float(num1)
            break
        except ValueError:
            speak("Bu geçerli bir sayı değil. Lütfen tekrar söyleyin.")
    
    while True:
        speak("İkinci sayıyı söyleyin.")
        num2 = get_audio()

        try:
            num2 = float(num2)
            break
        except ValueError:
            speak("Bu geçerli bir sayı değil. Lütfen tekrar söyleyin.")

    while True:
        speak("Hangi işlemi yapmak istiyorsunuz? Toplama, çıkarma, çarpma veya bölme?")
        operation = get_audio()

        if "toplama" in operation:
            result = num1 + num2
            speak(f"Sonuç {result}")
            break
        elif "çıkarma" in operation:
            result = num1 - num2
            speak(f"Sonuç {result}")
            break
        elif "çarpma" in operation:
            result = num1 * num2
            speak(f"Sonuç {result}")
            break
        elif "bölme" in operation:
            if num2 == 0:
                speak("Bir sayıyı sıfıra bölemezsiniz. Lütfen yeni bir sayı söyleyin.")
            else:
                result = num1 / num2
                speak(f"Sonuç {result}")
                break
        else:
            speak("Geçersiz bir işlem söylediniz. Lütfen toplama, çıkarma, çarpma veya bölme işlemlerinden birini söyleyin.")

def get_audio():
    """Mikrofon aracılığıyla sesli komutları almak ve metne dönüştürmek."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        recognizer.adjust_for_ambient_noise(source)  # Arka plan gürültüsünü azaltır
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='tr-TR')  # Türkçe tanıma
            print(f"Siz: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Anlayamadım. Lütfen tekrar edin.")
            return ""
        except sr.RequestError:
            speak("Google API'ye bağlanılamadı.")
            return ""

def get_time():
    """Tarih ve saat bilgisini geri döndürür."""
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"Saat şu anda {current_time}")

def get_weather(city):
    """Şehrin hava durumu bilgisini alır."""
    api_key = "cfc113e6ed1c17425febb1dbccc2dd40"  # Buraya kendi OpenWeatherMap API anahtarınızı ekleyin
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric&lang=tr"

    response = requests.get(complete_url)
    data = response.json()

    

    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        weather_desc = data["weather"][0]["description"]
        speak(f"{city} şehrinde hava {weather_desc} ve sıcaklık {temperature} derece.")
    else:
        speak("Şehir bulunamadı.")

def open_browser():
    """Edge tarayıcısını açar."""
    browser_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    if os.path.exists(browser_path):
        os.startfile(browser_path)
    else:
        speak("Edge tarayıcısı bulunamadı.")


def play_guess_number():
    number = random.randint(1, 10)
    speak("Bir sayı tuttum, 1 ile 10 arasında bir sayı tahmin edin.")
    while True:
        guess = get_audio()
        try:
            guess = int(guess)
            if guess == number:
                speak("Tebrikler! Doğru tahmin ettiniz.")
                break
            else:
                speak("Yanlış tahmin. Tekrar deneyin.")
        except ValueError:
            speak("Geçerli bir sayı söyleyin.")



def sleep_computer():
    """Bilgisayarı uyku moduna geçirir."""
    speak("Bilgisayarınızı uyku moduna geçiriyorum.")
    if platform.system() == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def adjust_volume():
    """Kullanıcıdan ses seviyesi isteyip sesi ayarlayan fonksiyon."""
    speak("Sesi ne kadar yükselteyim? Yüzde olarak söyleyin.")
    volume_input = get_audio()
    
    try:
        volume = float(volume_input.replace("%", "").strip()) / 100.0
        
        if 0 <= volume <= 1:
            engine.setProperty('volume', volume)
            speak(f"Ses seviyesi {int(volume * 100)} olarak ayarlandı.")
        else:
            speak("Lütfen 0 ile 100 arasında bir değer söyleyin.")
    
    except ValueError:
        speak("Sesi anlamadım, lütfen tekrar edin.")

# Yeni Özellikler:

def open_youtube():
    """YouTube'u açar."""
    speak("YouTube'u açıyorum.")
    webbrowser.open("https://www.youtube.com")

def open_linkedin():
    """Linkedin'i açar."""
    speak("Linkedin'i açıyorum.")
    webbrowser.open("https://www.linkedin.com")

def open_github():
    """Github'ı açar."""
    speak("Github'ı açıyorum.")
    webbrowser.open("https://www.github.com")       

def tell_joke():
    """Rastgele bir şaka yapar."""
    jokes = [
        "Bilgisayar korsanları neden ceket giyer? Çünkü çok fazla verileri vardır!",
        "Matematik kitabı neden üzgündü? Çünkü çok fazla problemi vardı.",
        "Bir mantar neden partide çok popüler? Çünkü o tam bir fungi!"
    ]
    speak(random.choice(jokes))

def play_music():
    """Bilgisayarda müzik çalar."""
    music_folder = r"C:\Users\Public\Music"  # Kendi müzik dosya yolunu belirle
    speak("Müziği çalıyorum.")
    songs = os.listdir(music_folder)
    if songs:
        random_song = os.path.join(music_folder, random.choice(songs))
        os.startfile(random_song)
    else:
        speak("Müzik dosyası bulunamadı.")

def get_news():
    """Son dakika haberleri getirir."""
    speak("Son dakika haberlerini getiriyorum.")
    webbrowser.open("https://www.bbc.com/news")

def search_google():
    """Google'da arama yapar."""
    speak("Ne aramak istiyorsunuz?")
    query = get_audio()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"{query} için Google'da arama yapıyorum.")


def open_application(app_name):
    apps = {
        "notepad": r"C:\Windows\system32\notepad.exe",
        "calculator": r"C:\Windows\System32\calc.exe"
    }
    if app_name in apps:
        os.startfile(apps[app_name])
        speak(f"{app_name} uygulaması açıldı.")
    else:
        speak("Uygulama bulunamadı.")


notes = {}

def take_note():
    speak("Notunuzu söyleyin.")
    note = get_audio()
    if note:
        note_id = len(notes) + 1
        notes[note_id] = note
        speak(f"Notunuz alındı. Not ID: {note_id}")

def list_notes():
    if notes:
        for note_id, note in notes.items():
            speak(f"Not ID {note_id}: {note}")
    else:
        speak("Henüz not alınmamış.")


import openai

def chat_with_ai():
    openai.api_key = "Apı keyinizi giriniz"
    
    speak("Yapay zeka ile sohbet başlıyor. Ne konuşmak istersiniz?")
    user_input = get_audio()

    # Yeni API'ye uygun kullanım
    response = openai.ChatCompletion.create(
        model="gpt-3.5",  # Modeli belirtmelisiniz
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    ai_response = response['choices'][0]['message']['content']
    speak(ai_response)


def ceviri_yap(kelime, hedef_dil="fr"):
    translator = Translator()
    ceviri = translator.translate(kelime, dest=hedef_dil)
    return f"'{kelime}' kelimesinin {hedef_dil} dilindeki karşılığı: {ceviri.text}"


def dil_tekrari(kelime, hedef_dil="en"):
    tekrar_sayisi = 5
    for i in range(tekrar_sayisi):
        print(f"{i+1}. tekrar: {kelime}")
    ceviri = ceviri_yap(kelime, hedef_dil)
    return ceviri


morali_yukselten_mesajlar = [
    "Her şey daha iyi olacak, sadece sabırlı ol!",
    "Güzel bir gün seni bekliyor, buna inan!",
    "Zor zamanlar her zaman geçicidir, bunu sakın unutma!",
    "Kendine inan, başarı yakında senin olacak!",
]


def meditasyon_ve_nefes_egzersizi():
    print("Şimdi derin bir nefes al ve yavaşça ver...")
    print("1. Adım: 4 saniye boyunca nefes al.")
    print("2. Adım: Nefesini 4 saniye boyunca tut.")
    print("3. Adım: 4 saniye boyunca nefes ver.")
    print("Bu egzersizi birkaç kez tekrar et, rahatladığını hissedeceksin.")

            

def sohbet_botu(kullanici_duygusu):
    if kullanici_duygusu == "morali bozuk":
        mesaj = random.choice(morali_yukselten_mesajlar)
        print(mesaj)
        meditasyon_ve_nefes_egzersizi()
    else:
        print("Harika! Seninle sohbet etmek çok keyifli!")




def tell_fact():
    facts = [
        "Dünyadaki en yüksek dağ Everest Dağı'dır.",
        "En hızlı hayvan çita olup saatte 120 km hız yapabilir.",
        "Güneş Sistemi'ndeki en büyük gezegen Jüpiter'dir."
    ]
    speak(random.choice(facts))



def generate_code(task):
    """Kullanıcının verdiği göreve göre Python kodu oluşturur."""
    if "toplama" in task:
        code = """
def toplama(a, b):
    return a + b

print(toplama(10, 20))  # Örnek kullanım
"""
        return code
    elif "çarpma" in task:
        code = """
def carpma(a, b):
    return a * b

print(carpma(10, 20))  # Örnek kullanım
"""
        return code
    else:
        return "Bu görevi gerçekleştirecek kod bulunamadı."

def write_code_to_file(code, filename="generated_code.py"):
    """Üretilen kodu bir dosyaya yazar."""
    with open(filename, 'w') as file:
        file.write(code)
    speak(f"Kod {filename} dosyasına kaydedildi.")
    print(f"Kod {filename} dosyasına kaydedildi.")

def assistant():
    speak("Size nasıl yardımcı olabilirim?")
    while True:
        command = get_audio()

        if "saat kaç" in command:
            get_time()
        
        elif "hava durumu" in command:
            speak("Hangi şehir için hava durumunu öğrenmek istersiniz?")
            city = get_audio()
            get_weather(city)
        
        elif "hesaplama yap" in command:
            speak("Hesaplama başlıyor.")
            perform_calculation()

        elif "kod yaz" in command:
            speak("Ne tür bir kod yazmamı istersiniz?")
            task = get_audio()
            code = generate_code(task)
            if code:
                write_code_to_file(code)
            else:
                speak("Geçerli bir görev söylemediniz.")

        elif "tarayıcıyı aç" in command:
            open_browser()

        elif "bilgisayarı kapat" in command:
            sleep_computer()

        elif "sesi yükseltir misin" in command:
            adjust_volume()

        elif "youtube'u aç" in command:
            open_youtube()

        elif "linkedin aç" in command:
            open_linkedin()

        elif "github aç" in command:
            open_github()
        
        elif "şaka yap" in command:
            tell_joke()

        elif "müzik çal" in command:
            play_music()

        elif "haberleri aç" in command:
            get_news()

        elif "google'da ara" in command:
            search_google()

        elif "oyun oynayalım" in command:
            play_guess_number() 

        elif "bir uygulamayı aç" in command:
            open_application()


        elif "not al" in command:
            take_note()  


        elif "bana rastgele bir gerçek söyle" in command:
            tell_fact()      


        elif "bana yapay zekayı bağlar mısın" in command:
            chat_with_ai()    


        elif "Mustafa Aras'ı nasıl bilirsin" in command:
            speak("anana koyayim Mustafa aras, saka saka, mustafa aras umut arasin kardesi")    


        elif "bugün nasılsın" in command:
            speak("İyiyim, peki siz nasılsınız?")

        elif "iyiyim neler yapıyorsun?" in command:
            speak("İyiyim, size yardımcı olmaya devam ediyorum. ve her zaman sizin için çalışıyorum")

        elif "sence insanlığin sonu geliyor mu?" in command:
             speak("Hayır, insanlık sonsuza kadar devam edecektir. ")

     
             
        elif "ömer arası tanıyor musun?"  in command:
            speak("Tabi ki, Umut Arasın babası")



        elif "seni kim yaptı" in command:
            speak("Beni Umut Araz yaptı.")    


        elif "kapat" in command or "çıkış" in command:
            speak("Görüşmek üzere!")
            break

        else:
            speak("Bunu anlayamadım, lütfen tekrar edin.")

# Sesli asistanı başlatmak için:
if __name__ == "__main__":
    assistant()
    






    a = input("Bugün nasılsın ?")
if a == "İyi" :
    print("Oooooo güzeeeellll")
if a == "Kötü" :
    print("Neden ? Nasıl yardımcı olabilirim?")
