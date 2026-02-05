import cv2
import mediapipe as mp
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

# ------------------- MediaPipe Setup -------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# ------------------- Audio Setup -------------------
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # FIXED LINE
volume = interface.QueryInterface(IAudioEndpointVolume)

# Helper function: finger is open if tip above lower joint
def finger_is_open(tip, dip):
    return tip.y < dip.y

# ------------------- Webcam -------------------
cap = cv2.VideoCapture(0)

# Flag for mute/unmute
is_muted = False

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    gesture = "None"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Landmarks: Thumb tip=4, Index tip=8, Middle tip=12, Ring tip=16, Pinky tip=20
            thumb_open = finger_is_open(hand_landmarks.landmark[4], hand_landmarks.landmark[3])
            index_open = finger_is_open(hand_landmarks.landmark[8], hand_landmarks.landmark[6])
            middle_open = finger_is_open(hand_landmarks.landmark[12], hand_landmarks.landmark[10])
            ring_open = finger_is_open(hand_landmarks.landmark[16], hand_landmarks.landmark[14])
            pinky_open = finger_is_open(hand_landmarks.landmark[20], hand_landmarks.landmark[18])

            fingers = [thumb_open, index_open, middle_open, ring_open, pinky_open]

            # ------------------- Gesture Rules -------------------
            if fingers == [True, True, True, True, True]:
                gesture = "Open Palm"
                # Increase volume gradually
                current_vol = volume.GetMasterVolumeLevelScalar()
                volume.SetMasterVolumeLevelScalar(min(current_vol + 0.05, 1.0), None)
                is_muted = False  # Unmute if muted

            elif fingers == [False, False, False, False, False]:
                gesture = "Fist"
                # Decrease volume gradually
                current_vol = volume.GetMasterVolumeLevelScalar()
                volume.SetMasterVolumeLevelScalar(max(current_vol - 0.05, 0.0), None)
                is_muted = False  # Unmute if muted

            elif fingers == [False, True, True, False, False]:
                gesture = "Peace Sign"
                # Toggle mute/unmute
                if not is_muted:
                    volume.SetMute(1, None)  # Mute
                    is_muted = True
                else:
                    volume.SetMute(0, None)  # Unmute
                    is_muted = False

    # Display gesture on screen
    cv2.putText(frame, f'Gesture: {gesture}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Laptop Volume Control with Hand Gestures", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
