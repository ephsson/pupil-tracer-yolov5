import cv2
import torch

# Eğitilmiş modeli yükleyin
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\cagan\\OneDrive\\Belgeler\\derinogrenme\\yolov5\\runs\\train\\exp2\\weights\\best.pt')

# Kamerayı başlatın
cap = cv2.VideoCapture(0)  # 0 genellikle varsayılan kamerayı ifade eder

while True:
    # Kamera görüntüsünü al
    ret, frame = cap.read()

    # Görüntü alındıysa işle
    if ret:
        # Görüntüyü modelle tespit et
        results = model(frame)

        # Sonuçları göster
        results.render()  # Görüntüye tespit çizimleri ekler
        cv2.imshow("Tespit Sonuçları", frame)  # Tespit edilen görüntü

        # 'q' tuşuna basıldığında çıkış yap
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Kamerayı ve pencereyi kapatın
cap.release()
cv2.destroyAllWindows()