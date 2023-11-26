import cv2
import numpy as np

def text_to_binary(text):
    binary_message = ''.join(format(ord(char), '08b') for char in text)
    return binary_message

def hide_text_in_image(img, text):
    binary_message = text_to_binary(text)
    binary_message += '1111111111111110'

    data_index = 0

    for row in img:
        for pixel in row:
            for i in range(3):
                if data_index < len(binary_message):
                    pixel[i] = int(format(pixel[i], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1

    return img

def reveal_text_from_image(img):
    binary_message = ''
    for row in img:
        for pixel in row:
            for i in range(3):
                binary_message += format(pixel[i], '08b')[-1]

    delimiter_index = binary_message.find('1111111111111110')
    binary_message = binary_message[:delimiter_index]

    text = ''.join([chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8)])

    return text
image_path = "flower.jpg"
img = cv2.imread(image_path)

secret_message = input("Enter secret message: ")
img_with_hidden_text = hide_text_in_image(np.copy(img), secret_message)
cv2.imwrite("image_with_hidden_text.jpg", img_with_hidden_text)
cv2.imshow("Image with Hidden Text", img_with_hidden_text)
cv2.waitKey(0)
cv2.destroyAllWindows()
img_with_hidden_text = cv2.imread("image_with_hidden_text.jpg")
revealed_text = reveal_text_from_image(np.copy(img_with_hidden_text))
print("Revealed text:", revealed_text)
