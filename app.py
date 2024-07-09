# import streamlit as st
# import cv2
# import numpy as np
# from main.gesture import process_hand

# def main():
#     st.title("Hand Gesture Recognition")

#     run = st.button("run")
#     FRAME_WINDOW = st.image([])
#     EMOJI_PLACEHOLDER = st.empty()

#     camera = cv2.VideoCapture(0)
#     while run:
#         _, frame = camera.read()
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         processed_frame, gesture = process_hand(frame)
#         FRAME_WINDOW.image(processed_frame)
#         if gesture == "thums up":
#             EMOJI_PLACEHOLDER.markdown("# 😊")
#         elif gesture == "thumbs down":
#             EMOJI_PLACEHOLDER.markdown("# 😔")
#         elif gesture == "heart":
#             EMOJI_PLACEHOLDER.markdown("# ❤️")
#         else:
#             EMOJI_PLACEHOLDER.empty()

#     else:
#         st.button("stop")

# if __name__ == "__main__":
#     main()


# import cv2
# import numpy as np
# import mediapipe as mp
# import time
# import streamlit as st

# import random
# from main.gesture import process_hand

# def get_computer_choice():
#     return random.choice(['rock', 'paper', 'scissors'])

# def  determine_winner(player_choice, computer_choice):
#     if player_choice == computer_choice:
#         return "game is a tie"
#     elif(player_choice == "rock" and computer_choice == "scissors") or \
#     (player_choice == "scissors" and computer_choice == "paper") or \
#     (player_choice == "paper" and computer_choice == "rock"):
#         return "you win!"
    
#     else:
#         return "computer wins!"
    

# def main():
#     st.title("Rock Paper Scissors Game")
#     run = st.button('Run')
#     FRAME_WINDOW = st.image([])
#     RESULT_PLACEHOLDER = st.empty()

#     camera = cv2.VideoCapture(0)
#     player_score = 0
#     computer_score = 0
#     rounds_played = 0
#     while run:
#         _, frame =  camera.read()
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         process_image, gesture = process_hand(frame)
#         FRAME_WINDOW.image(process_image)

#         if gesture in ['rock', 'paper', 'scissors']:
#             computer_choice = get_computer_choice()
#             result = determine_winner(gesture, computer_choice)

#             if result == "you win!":
#                 player_score += 1
#             elif result == "computer wins!":
#                 computer_score += 1
#             rounds_played += 1

#             RESULT_PLACEHOLDER.markdown(f"""
#             Your Choice: {gesture}
#             Computer's Choice: {computer_choice}
#             Result: {result}
#             Score:
#             You:{player_score}
# Computer:{computer_score}
# Rounds Played:{rounds_played}
#                                         """)
#             time.sleep(2)

#     else:
#         st.write('Game Stopped')

# if __name__ == "__main__":
#     main()

# import streamlit as st
# import cv2
# import numpy as np
# from main.gesture import process_hand
# import random
# import time

# def get_computer_choice():
#     return random.choice(["rock", "paper", "scissors"])

# def determine_winner(player_choice, computer_choice):
#     if player_choice == computer_choice:
#         return "It's a tie! 🤝"
#     elif (player_choice == "rock" and computer_choice == "scissors") or \
#          (player_choice == "scissors" and computer_choice == "paper") or \
#          (player_choice == "paper" and computer_choice == "rock"):
#         return "You win! 🎉"
#     else:
#         return "Computer wins! 💻"

# def get_emoji(choice):
#     if choice == "rock":
#         return "🪨"
#     elif choice == "paper":
#         return "📄"
#     elif choice == "scissors":
#         return "✂️"
#     return ""

# def main():
#     st.set_page_config(page_title="Rock Paper Scissors Game", page_icon="🎮", layout="wide")

#     # Custom CSS
#     st.markdown("""
#     <style>
#     .big-font {
#         font-size:30px !important;
#         font-weight: bold;
#     }
#     .medium-font {
#         font-size:24px !important;
#     }
#     .centered {
#         text-align: center;
#     }
#     .stButton>button {
#         width: 200px;
#         height: 60px;
#         font-size: 24px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     st.markdown("<h1 class='centered'>🪨📄✂️ Rock Paper Scissors Game 🎮</h1>", unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("<p class='big-font centered'>Camera Feed</p>", unsafe_allow_html=True)
#         FRAME_WINDOW = st.image([])
#         run = st.checkbox('Start Game', value=False)

#     with col2:
#         st.markdown("<p class='big-font centered'>Game Status</p>", unsafe_allow_html=True)
#         RESULT_PLACEHOLDER = st.empty()
#         SCORE_PLACEHOLDER = st.empty()

#     camera = cv2.VideoCapture(0)

#     player_score = 0
#     computer_score = 0
#     rounds_played = 0

#     while run:
#         _, frame = camera.read()
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
#         processed_frame, gesture = process_hand(frame)
        
#         FRAME_WINDOW.image(processed_frame)
        
#         if gesture in ["rock", "paper", "scissors"]:
#             computer_choice = get_computer_choice()
#             result = determine_winner(gesture, computer_choice)
            
#             if "You win!" in result:
#                 player_score += 1
#             elif "Computer wins!" in result:
#                 computer_score += 1
            
#             rounds_played += 1
            
#             RESULT_PLACEHOLDER.markdown(f"""
#             <p class='medium-font centered'>
#             Your choice: {get_emoji(gesture)} {gesture.capitalize()}<br>
#             Computer's choice: {get_emoji(computer_choice)} {computer_choice.capitalize()}<br>
#             Result: {result}
#             </p>
#             """, unsafe_allow_html=True)
            
#             SCORE_PLACEHOLDER.markdown(f"""
#             <p class='medium-font centered'>
#             Score:<br>
#             You: {player_score} 😊 | Computer: {computer_score} 💻<br>
#             Rounds played: {rounds_played}
#             </p>
#             """, unsafe_allow_html=True)
            
#             time.sleep(10)  # Wait for 10 seconds before the next round
#     else:
#         st.write('Game stopped')

#     if st.button('Reset Game'):
#         player_score = 0
#         computer_score = 0
#         rounds_played = 0
#         RESULT_PLACEHOLDER.empty()
#         SCORE_PLACEHOLDER.empty()

# if __name__ == '__main__':
#     main()

import streamlit as st
import cv2
import numpy as np
from main.gesture import process_hand
import random
import time
from threading import Thread
from queue import Queue

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie! 🤝"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win! 🎉"
    else:
        return "Computer wins! 💻"

def get_emoji(choice):
    if choice == "rock":
        return "🪨"
    elif choice == "paper":
        return "📄"
    elif choice == "scissors":
        return "✂️"
    return ""

def video_capture_loop(cap, queue):
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        queue.put(frame)

def main():
    st.set_page_config(page_title="Rock Paper Scissors Game", page_icon="🎮", layout="wide")

    # Custom CSS (same as before)
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .medium-font {
        font-size:24px !important;
    }
    .centered {
        text-align: center;
    }
    .stButton>button {
        width: 200px;
        height: 60px;
        font-size: 24px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='centered'>🪨📄✂️ Rock Paper Scissors Game 🎮</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<p class='big-font centered'>Camera Feed</p>", unsafe_allow_html=True)
        FRAME_WINDOW = st.image([])
        run = st.checkbox('Start Game', value=False)

    with col2:
        st.markdown("<p class='big-font centered'>Game Status</p>", unsafe_allow_html=True)
        RESULT_PLACEHOLDER = st.empty()
        SCORE_PLACEHOLDER = st.empty()

    cap = cv2.VideoCapture(0)
    frame_queue = Queue(maxsize=1)
    video_thread = Thread(target=video_capture_loop, args=(cap, frame_queue), daemon=True)
    video_thread.start()

    player_score = 0
    computer_score = 0
    rounds_played = 0
    last_gesture_time = time.time()
    gesture_cooldown = 10 # seconds

    while run:
        if not frame_queue.empty():
            frame = frame_queue.get()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            processed_frame, gesture = process_hand(frame)
            
            FRAME_WINDOW.image(processed_frame)
            
            current_time = time.time()
            if gesture in ["rock", "paper", "scissors"] and current_time - last_gesture_time > gesture_cooldown:
                computer_choice = get_computer_choice()
                result = determine_winner(gesture, computer_choice)
                
                if "You win!" in result:
                    player_score += 1
                elif "Computer wins!" in result:
                    computer_score += 1
                
                rounds_played += 1
                last_gesture_time = current_time
                
                RESULT_PLACEHOLDER.markdown(f"""
                <p class='medium-font centered'>
                Your choice: {get_emoji(gesture)} {gesture.capitalize()}<br>
                Computer's choice: {get_emoji(computer_choice)} {computer_choice.capitalize()}<br>
                Result: {result}
                </p>
                """, unsafe_allow_html=True)
            
            SCORE_PLACEHOLDER.markdown(f"""
            <p class='medium-font centered'>
            Score:<br>
            You: {player_score} 😊 | Computer: {computer_score} 💻<br>
            Rounds played: {rounds_played}
            </p>
            """, unsafe_allow_html=True)
    else:
        st.write('Game stopped')
        cap.release()

    if st.button('Reset Game'):
        player_score = 0
        computer_score = 0
        rounds_played = 0
        RESULT_PLACEHOLDER.empty()
        SCORE_PLACEHOLDER.empty()

if __name__ == '__main__':
    main()