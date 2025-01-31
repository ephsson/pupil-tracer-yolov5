Bu kodu çalıştırmak için izlenmesi gereken adımlar şunlardır:

Gerekli Kütüphanelerin Yüklenmesi:
requirements.txt dosyasını kullanarak aşağıdaki komutla gerekli kütüphaneleri yükleyin

pip install -r requirements.txt

Datasetin Hazırlanması:
Dataset, belirtilen bağlantıdan (https://universe.roboflow.com/objectdetection-ajslg/my_project-2/dataset/5) indirilmeli ve YOLOv5 formatında olmalıdır.

Model Yolu:
Kodda şu satırda belirtilen path kısmına, best.pt dosyasının tam yolu yazılmalıdır:

model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\cagan\\OneDrive\\Belgeler\\derinogrenme\\yolov5\\runs\\train\\exp2\\weights\\best.pt')

Kodun Çalıştırılması:
Kod çalıştırıldığında kamera açılır ve gerçek zamanlı tespit yapılır. Kod çalışırken çıkış yapmak için q tuşuna basabilirsiniz.