from pytube import YouTube

def bilgi():
    url = input("Lütfen YouTube video URL'sini girin: ")
    try:
        video = YouTube(url)
        print(f"Video Başlığı: {video.title}")
        print(f"Video Açıklaması: {video.description}")
        print(f"Video Uzunluğu: {video.length} saniye")
        print(f"Video Yayın Tarihi: {video.publish_date}")
        print(f"Video Görüntüleme Sayısı: {video.views}")
    except Exception as e:
        print(f"Hata oluştu: {e}")

def ses_indir():
    url = input("Lütfen YouTube video URL'sini girin: ")
    try:
        video = YouTube(url)
        ses = video.streams.filter(only_audio=True).first()
        ses.download()
        print(f"Ses dosyası başarıyla indirildi: {ses.default_filename}")
    except Exception as e:
        print(f"Hata oluştu: {e}")