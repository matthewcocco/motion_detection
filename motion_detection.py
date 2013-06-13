# opencv hello world
# creates window, pulls from first camera it finds.
# displays feed from camera

# lots of slightly-tweaked copypasta; refer to the readme.
# may be re-implemented in the future in a more sophisticated fashion.

import cv

cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
capture = cv.CaptureFromCAM(camera_index)

gx = gy = 1
grayscale = blur = canny = motion = False

display_image = cv.QueryFrame(capture)
running_average_image = cv.CreateImage(cv.GetSize(display_image), cv.IPL_DEPTH_32F, 3)
running_average_in_color = cv.CloneImage(display_image)
difference = cv.CloneImage(display_image)


def repeat():
    global capture  # declare as globals since we are assigning to them now
    global camera_index
    global gx, gy, grayscale, canny, blur, motion
    frame = cv.QueryFrame(capture)
    # import pdb; pdb.set_trace()

    # if grayscale:
    #     gray = cv.CreateImage(cv.GetSize(frame), frame.depth, 1)
    #     cv.CvtColor(frame, gray, cv.CV_RGB2GRAY)
    #     frame = gray

    # if blur:
    #     g = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_8U, frame.channels)
    #     cv.Smooth(frame, g, cv.CV_GAUSSIAN, gx, gy)
    #     frame = g

    # if grayscale and canny:
    #     c = cv.CreateImage(cv.GetSize(frame), frame.depth, frame.channels)
    #     cv.Canny(frame, c, 10, 100, 3)
    #     frame = c

    if motion:
        cv.Smooth(frame, frame, cv.CV_GAUSSIAN, 19, 0)                                # blur to reduce false positives
        cv.RunningAvg(frame, running_average_image, 0.320, None)                      # get the running average
        cv.ConvertScale(running_average_image, running_average_in_color, 1.0, 0.0)    # convert running average to color
        cv.AbsDiff(frame, running_average_in_color, difference)                       # store the absolute difference in [difference]

        frame = difference                                                            # write [difference] to [frame]

        frame_grayscale = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_8U, 1)

        cv.CvtColor(difference, frame_grayscale, cv.CV_RGB2GRAY)
        cv.Threshold(frame_grayscale, frame_grayscale, 70, 255, cv.CV_THRESH_BINARY)
        cv.Dilate(frame_grayscale, frame_grayscale, None, 9)
        cv.Erode(frame_grayscale, frame_grayscale, None, 5)

        # begin snippet

        storage = cv.CreateMemStorage(0)
        contour = cv.FindContours(frame_grayscale, storage, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
        points = []

        while contour:
            bound_rect = cv.BoundingRect(list(contour))
            contour = contour.h_next()

            pt1 = (bound_rect[0], bound_rect[1])
            pt2 = (bound_rect[0] + bound_rect[2], bound_rect[1] + bound_rect[3])
            points.append(pt1)
            points.append(pt2)
            cv.Rectangle(frame, pt1, pt2, cv.CV_RGB(255, 0, 0), 1)

        if len(points):
            center_point = reduce(lambda a, b: ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2), points)
            cv.Circle(frame, center_point, 40, cv.CV_RGB(255, 255, 255), 1)
            cv.Circle(frame, center_point, 30, cv.CV_RGB(255, 100, 0), 1)
            cv.Circle(frame, center_point, 20, cv.CV_RGB(255, 255, 255), 1)
            cv.Circle(frame, center_point, 10, cv.CV_RGB(255, 100, 0), 1)

        # end snippet

        

    cv.ShowImage("w1", frame)  # display frame

    c = cv.WaitKey(10)

    if c==ord('='):   #in "n" key is pressed while the popup window is in focus
        gx += 2
        gy += 2
    elif c == ord('-'):
        gx = max(1, gx-2)
        gy = max(1, gy-2)
    elif c == ord('x'):
        gx += 2
    elif c == ord('X'):
        gx = max(1, gx-2)
    elif c == ord('q'):      # quit
        exit(0)
    elif c == ord('m'):      # toggle motion detection (raptor-vision)
        motion = not motion
    # elif c == ord('b'):
    #     blur = not blur
    # elif c == ord('g'):
    #     grayscale = not grayscale
    # elif c == ord('c'):
    #     canny = not canny


while True:
    repeat()
