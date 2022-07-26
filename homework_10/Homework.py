import cv2
import sys
import time


if __name__ == '__main__' :
    fps = 60
    # Set up tracker.
    # Instead of MIL, you can also use

    tracker_types = ['KCF','TLD', 'CSRT']
    tracker_type = tracker_types[2]

    if tracker_type == 'KCF':
        tracker = cv2.TrackerKCF_create()
    if tracker_type == "TLD":
        tracker = cv2.legacy.TrackerTLD_create()
    if tracker_type == "CSRT":
        tracker = cv2.TrackerCSRT_create()

    # Read video
    video = cv2.VideoCapture("/home/denys_pylypenko/Downloads/output1.mp4")

    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()

    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    
    # Define an initial bounding box
    bbox = (140, 137, 54, 47)

    # Uncomment the line below to select a different bounding box
    #bbox = cv2.selectROI(frame, False)
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(f"output{int(time.time())}.avi", fourcc, fps, (960,  540))

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox) 
    
    # With target and counter we can skip frames and decrease fps video
    target = 5
    counter = 0

    while True:
        # Read a new frame
        if counter == target: 
            # display and stuff 
            ok, frame = video.read() 
            counter = 0
        else: 
            # Skip
            out.write(frame)
            ok, frame_ = video.read()
            counter += 1
            continue
        
        if not ok:
            break

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
        
        # Display FPS on frame
        cv2.putText(frame, "Video FPS : " + str(int(fps/(target+1))), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
        
        # Display result
        cv2.imshow("Tracking", frame)
        
        # write the flipped frame
        out.write(frame)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
    # Close video window and save result video
    video.release()
    out.release()
    cv2.destroyAllWindows()