import cv2
from detect_vehicles import detect_vehicles
from violation_logic import check_violation

cap = cv2.VideoCapture("data/videos/traffic.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cars = detect_vehicles(frame)
    violations = check_violation(cars)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    for (x, y, w, h) in violations:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
        cv2.putText(frame, "Violation", (x,y-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

    cv2.imshow("Traffic Violation Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
