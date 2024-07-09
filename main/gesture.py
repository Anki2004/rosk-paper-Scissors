# import cv2
# import mediapipe as mp
# import numpy as np

# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(static_image_mode = False, max_num_hands = 2, min_detection_confidence = 0.5)
# mp_hands_drawing = mp.solutions.drawing_utils

# def is_thumbs_up(hand_landmarks):
#     thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#     thumb_mc = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]
#     return thumb_tip.y < thumb_mc.y

# def is_thumb_down(hand_landmarks):
#     thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#     thumb_mc = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]
#     return thumb_tip.y > thumb_mc.y

# def is_heart(hand_landmarks):
#     index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER]
#     thumb_tip = hand_landmarks.landmarks[mp_hands.HandLandmarks.THUMBS_TIP]
#     middle_fig = hand_landmarks.landmarks[mp_hands.HandLandmarks.MIDDLE_FINGER_TIP]

#     if(abs(index_tip.x - thumb_tip.x)) < 0.1 and (abs(index_tip.y - thumb_tip.y))  < 0.1 and middle_fig.y < index_tip.y:
#         return True
#     return False



# def process_hand(image):
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = hands.process(image_rgb)

#     gesture = None
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_hands_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#             if is_thumbs_up(hand_landmarks):
#                 gesture = "thums up"
#             elif is_thumb_down(hand_landmarks):
#                 gesture = "thumbs down"
#             elif is_heart(hand_landmarks):
#                 gesture = "heart"

#     return image, gesture



# import cv2
# import mediapipe as mp
# import numpy as np

# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(static_image_mode = False, max_num_hands = 2, min_detection_confidence = 0.5)
# mp_hands_drawing = mp.solutions.drawing_utils

# def get_gesture(hand_landmarks):
#     thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#     index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

#     middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
#     ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
#     pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

#     ## FOR ROCK (closed fist)
#     if(thumb_tip.y >  index_tip.y and middle_tip.y > index_tip.y and
#        ring_tip.y >index_tip.y and pinky_tip.y > index_tip.y):
#         return "rock"
    
#     ## for scissors
#     elif (index_tip.y < ring_tip.y and middle_tip.y < ring_tip.y and
#           ring_tip.y > index_tip.y and pinky_tip.y > index_tip.y ):
#         return "scissors"
#     elif(thumb_tip.y < index_tip.y and middle_tip.y < ring_tip.y and
#          ring_tip.y < pinky_tip.y):
#         return "paper"
    
#     return None

# def process_hand(image):
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = hands.process(image_rgb)

#     gesture = None
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_hands_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#             gesture = get_gesture(hand_landmarks)

#     return image, gesture



import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('rps_model.h5')
class_names = ['rock', 'paper', 'scissors']

def process_hand(image):
    resized  = cv2.resize(image, (150, 150))
    normalized = resized / 255.0
    input_image = np.expand_dims(normalized, axis = 0)

    prediction = model.predict(input_image)

    prediction_class = class_names[np.argmax(prediction)]
    cv2.putText(image, prediction_class, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return image, prediction_class

