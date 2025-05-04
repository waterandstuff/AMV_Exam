import cv2
import datetime

def main():
    # Select the camera (0 is default, use 1 or other if you have multiple)
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("❌ Cannot open camera")
        return

    # Get frame dimensions
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Set up the video writer

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use 'XVID' or 'MJPG' too
    output_filename = f"output_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    out = cv2.VideoWriter(output_filename, fourcc, 20.0, (frame_width, frame_height))

    print("📹 Recording started. Press 'q' to stop.")
    picturecount = 1
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame")
            break

        key = cv2.waitKey(1) & 0xFF
       
        if key == ord('p'):
            picture_filename = f"picture_{picturecount}.jpg"
            cv2.imwrite(picture_filename, frame)
            print(f"📸 Picture saved as: {picture_filename}")
            picturecount += 1

        cv2.imshow("Live USB Camera Feed", frame)  # Show the live video           

        if key == ord('q'):
            print("🛑 Stopping...")
            break

    # Release everything
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()