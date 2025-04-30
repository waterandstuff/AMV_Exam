import cv2
import datetime

def main():
    # Select the camera (0 is default, use 1 or other if you have multiple)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Cannot open camera")
        return

    # Get frame dimensions
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Set up the video writer
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"recording_{timestamp}.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use 'XVID' or 'MJPG' too
    out = cv2.VideoWriter(output_filename, fourcc, 20.0, (frame_width, frame_height))

    print("📹 Recording started. Press 'q' to stop.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame")
            break

        # Optional: draw timestamp on frame
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, now, (10, frame_height - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imshow("Live USB Camera Feed", frame)  # Show the live video

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("🛑 Stopping...")
            break

    # Release everything
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()