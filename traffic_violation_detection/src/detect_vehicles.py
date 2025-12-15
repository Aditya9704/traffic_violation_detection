import cv2

fgbg = cv2.createBackgroundSubtractorMOG2()

def detect_vehicles(frame):
    fgmask = fgbg.apply(frame)
    contours, _ = cv2.findContours(
        fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    vehicles = []
    for cnt in contours:
        if cv2.contourArea(cnt) > 1500:
            x, y, w, h = cv2.boundingRect(cnt)
            vehicles.append((x, y, w, h))
    return vehicles
