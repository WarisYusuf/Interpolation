import cv2
import matplotlib.pyplot as plt

def scale_image(image, scale_factor=8.0, method=cv2.INTER_LINEAR):
    # Neue Dimensionen berechnen
    new_width = int(image.shape[1] * scale_factor)
    new_height = int(image.shape[0] * scale_factor)
    
    # Bild skalieren
    scaled_image = cv2.resize(image, (new_width, new_height), interpolation=method)
    
    return scaled_image

# Bild laden
image_path = "landschaft.jpg"  # Stelle sicher, dass dieser Pfad korrekt ist
original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
if original_image is None:
    raise FileNotFoundError("Das Bild wurde nicht gefunden.")

# Einen kleinen, detailreichen Ausschnitt auswählen
crop_image = original_image[100:150, 100:150]  # Passen Sie diese Werte entsprechend an

# Skalieren des Bildausschnittes mit verschiedenen Methoden
image_nearest = scale_image(crop_image, method=cv2.INTER_NEAREST)
image_linear = scale_image(crop_image, method=cv2.INTER_LINEAR)
image_cubic = scale_image(crop_image, method=cv2.INTER_CUBIC)

# Bilder anzeigen
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image_nearest, cv2.COLOR_BGR2RGB))
plt.title('Nearest Neighbor')
plt.axis('off')

plt.subplot(132)
plt.imshow(cv2.cvtColor(image_linear, cv2.COLOR_BGR2RGB))
plt.title('Bilinear')
plt.axis('off')

plt.subplot(133)
plt.imshow(cv2.cvtColor(image_cubic, cv2.COLOR_BGR2RGB))
plt.title('Bicubic')
plt.axis('off')

plt.tight_layout()
plt.show()
