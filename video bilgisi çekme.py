
from pytube import YouTube
def bilgi():
    url = input("Lütfen indirmek istediğiniz YouTube videosunun URL'sini girin: ")
    try:
        yt = YouTube(url)
        print(f"Video Başlığı: {yt.title}")
        print(f"Video Uzunluğu: {yt.length} saniye")
        print(f"Video Açıklaması: {yt.description}")
        print(f"Video Yazar: {yt.author}")
        print(f"Video Yayınlanma Tarihi: {yt.publish_date}")
    except Exception as e:
        print(f"Hata oluştu: {e}")