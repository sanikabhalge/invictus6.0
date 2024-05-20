import cv2
import numpy as np

def black_only(img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, (0, 0, 0), (0, 0, 0))
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    return mask

def road_frame(image):
    mask = black_only(image)
    kernel_size = 5
    blur = cv2.GaussianBlur(mask, (kernel_size, kernel_size), 0)
    low_t = 50
    high_t = 150
    edges = cv2.Canny(blur, low_t, high_t)
    region = getROI(edges)
    hough = hough_transform(region)
    result = draw_lane_lines(image, lane_lines(image, hough))
    return result

def hough_transform(image):
    rho = 1
    theta = np.pi / 180
    threshold = 20
    minLineLength = 20
    maxLineGap = 500
    return cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=minLineLength, maxLineGap=maxLineGap)

def average_slope_intercept(lines):
    left_lines = []
    left_weights = []
    right_lines = []
    right_weights = []

    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 == x2:
                continue
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - (slope * x1)
            length = np.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
            if slope < 0:
                left_lines.append((slope, intercept))
                left_weights.append(length)
            else:
                right_lines.append((slope, intercept))
                right_weights.append(length)

    left_lane = np.dot(left_weights, left_lines) / np.sum(left_weights) if len(left_weights) > 0 else None
    right_lane = np.dot(right_weights, right_lines) / np.sum(right_weights) if len(right_weights) > 0 else None
    return left_lane, right_lane


def pixel_points(y1, y2, line):
    if line is None:
        return None
    slope, intercept = line
    if slope == 0:
        return None
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return ((x1, int(y1)), (x2, int(y2)))

def lane_lines(image, lines):
    left_lane, right_lane = average_slope_intercept(lines)
    y1 = image.shape[0]
    y2 = y1 * 0.6
    left_line = pixel_points(y1, y2, left_lane)
    right_line = pixel_points(y1, y2, right_lane)
    return left_line, right_line

def draw_lane_lines(image, lines, color_left=(0, 255, 255), color_right=(255, 0, 0), thickness=12):
    line_image = np.zeros_like(image)
    if lines[0] is not None:
        cv2.line(line_image, *lines[0], color_left, thickness)
    if lines[1] is not None:
        cv2.line(line_image, *lines[1], color_right, thickness)
    return cv2.addWeighted(image, 1.0, line_image, 1.0, 0.0)

def getROI(image):
    height, width = image.shape[:2]
    triangle = np.array([[(100, height), (width, height), (width // 2, height // 2)]], dtype=np.int32)
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, triangle, 255)
    return cv2.bitwise_and(image, mask)

def kuchkar(image):
    mask=black_only(image)
    lines=hough_transform(mask)
    for line in lines:
        x1,y1,x2,y2=line[0]
        cv2.line(image,(x1,y1),(x2,y2),(0,225,225),3)
    return image



def select_roi(image):
# Read image


# Select ROI
    r = cv2.selectROI("select the area", image)
    return r

