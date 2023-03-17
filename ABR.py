import cv2
import time

# Input RTSP URL
rtsp_url = 'rtsp://root:0011J00001Mnty2QAB@10.76.1.140:556/axis-media/media.amp?videocodec=h264&resolution=1280x720&fps=5'

# Open the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

# Initialize variables
bitrates = []
frame_count = 0
last_timestamp = time.time()

# Loop through the first 200 frames
while frame_count < 200:
    ret, frame = cap.read()
    if not ret:
        break

    # Get the current timestamp in seconds
    timestamp = time.time()

    # Get the frame size in bits
    frame_size = len(frame.tobytes()) * 8

    # Calculate the bitrate in kbps
    bitrate = (frame_size) / (timestamp - last_timestamp) / 1000000

    # Append the bitrate to the list
    bitrates.append(bitrate)

    # Increment the frame count
    frame_count += 1

    # Set the last timestamp to the current timestamp
    last_timestamp = timestamp

    # Print the bitrate for this frame
    print("Frame {}: {:.2f} kbps".format(frame_count, bitrate))

# Release the RTSP stream
cap.release()

# Calculate the average bitrate
average_bitrate = sum(bitrates) / len(bitrates)

# Print the average bitrate
print("Average Bitrate: {:.2f} kbps".format(average_bitrate))
