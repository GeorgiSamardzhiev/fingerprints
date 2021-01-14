import numpy as np
import matplotlib.pyplot as plt
import cv2
import fingerprint_enhancer
import math
from fingerprints_kernels import *

def enhance_and_binarize(img): 
    enhanced_img = fingerprint_enhancer.enhance_Fingerprint(img)
    _, binarized_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    _, binarized_enhanced_img = cv2.threshold(enhanced_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return binarized_enhanced_img

def thin(input_img, kernels = thinning_kernels_w):   
    temp = input_img.copy()
    result = input_img.copy()
    while True:
        for j in range(len(kernels)):
            result = result - cv2.morphologyEx(result, cv2.MORPH_HITMISS, kernels[j])
        if (temp == result).all():
            break
        temp = result.copy()
    
    return result


def prune(img):
    X1 = thin(img, pruning_kernels)

    #Find End Points
    X2 = np.zeros(img.shape, dtype=np.uint8)
    for i in range(len(pruning_kernels)):
        X2 = cv2.bitwise_or(X2,
                            cv2.morphologyEx(X1, cv2.MORPH_HITMISS, pruning_kernels[i]))

    #Dilate End Point
    X3 = cv2.bitwise_and(img, 
                         cv2.dilate(X2,
                                    cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))))

    #Union of X1 & X3
    X4 = cv2.bitwise_or(X1, X3)
    
    return X4

def skeleton(input_img):
    img = input_img.copy()
    result = np.zeros(img.shape, dtype=np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    i = 0
    while cv2.countNonZero(img):
        i = i + 1
        erode = cv2.erode(img, kernel)
        opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, kernel)
        subset = erode - opening
        result = cv2.bitwise_or(subset, result)
        img = erode.copy()
    return i, result

def preprocess(img):
    pruned_img = prune(img)
    closed_img = cv2.morphologyEx(pruned_img, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)))
    opened_img = cv2.morphologyEx(closed_img, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2)))
    return opened_img

def extract_ridge(input_img, kernel):
    img = input_img.copy()
    result = np.zeros(img.shape, dtype=np.uint8)
    for i in range(len(kernel)):
        result = cv2.bitwise_or(result, cv2.morphologyEx(img, cv2.MORPH_HITMISS, kernel[i]))
    return result  

def manhattanDistance(x, y):
    (x1,x2)=x
    (y1,y2)=y
    return abs(x1 - y1) + abs(x2 - y2)

def euclideanDistance(x, y):
    (x1,x2)=x
    (y1,y2)=y
    return math.sqrt((x1 - y1)**2 + (x2 - y2)** 2)

def getMinutiaeList(minutiaeImg):
    minutiae = []
    (iMax, jMax) = minutiaeImg.shape
    for i in range(iMax):
        for j in range(jMax):
            if minutiaeImg[i][j] != 0:
                minutiae.append((i,j))
    return minutiae

def postprocessingMinutiaeListSameType(minutiaeList, tresh = 8, dist = manhattanDistance):
    res = minutiaeList.copy()
    for m1 in minutiaeList:
        for m2 in minutiaeList:
            if m1 != m2 and dist(m1, m2) < tresh:
                if m1 in res:
                    res.remove(m1)
                if m2 in res:
                    res.remove(m2)
    return res

def postprocessingMinutiaeListDiffType(minutiaeList1, minutiaeList2, tresh = 8, dist = manhattanDistance):
    res = minutiaeList1.copy()
    res = res + minutiaeList2
    for m1 in minutiaeList1:
        for m2 in minutiaeList2:
            if dist(m1, m2) < tresh:
                if m1 in res:
                    res.remove(m1)
                if m2 in res:
                    res.remove(m2)
    return res

def postprocessing(terminations_img, bifurcations_img, tresh1 = 3, tresh2 = 3, tresh3 = 3, dist = manhattanDistance):
    terminations_list = getMinutiaeList(terminations_img)
    bifurcations_list = getMinutiaeList(bifurcations_img)
    terminations_list = postprocessingMinutiaeListSameType(terminations_list, tresh1, dist)
    bifurcations_list = postprocessingMinutiaeListSameType(bifurcations_list, tresh2, dist)
    result_list = postprocessingMinutiaeListDiffType(terminations_list, bifurcations_list, tresh3, dist)
    iMax, jMax = terminations_img.shape
    result_img = np.zeros((iMax, jMax), dtype=np.uint8)
    for (i,j) in result_list:
        result_img[i][j] = 1
    return result_img, result_list

if __name__ == "__main__":
    img = cv2.imread('DB1_B/107_2.tif', cv2.IMREAD_GRAYSCALE)
    enhanced_and_binarized_img = enhance_and_binarize(img)
    preprocessed_img = preprocess(enhanced_and_binarized_img)
    thinned_img = thin(preprocessed_img)
    # i, thinned_img = skeleton(preprocessed_img)
    terminations = extract_ridge(thinned_img, ridge_terminations_kernel)
    bifurcations = extract_ridge(thinned_img, ridge_bifurcations_kernel)
    fin_img, fin_list = postprocessing(terminations, bifurcations)
    show_minutiae = enhanced_and_binarized_img.copy()
    show_minutiae = cv2.cvtColor(show_minutiae, cv2.COLOR_GRAY2BGR)
    for (i,j) in fin_list:
        cv2.circle(show_minutiae,(j,i), 4, (255,0,0), cv2.LINE_4)
    
    cv2.imshow('raw image', img) 
    cv2.imshow('enhanced_and_binarized_img', enhanced_and_binarized_img) 
    cv2.imshow('preprocessed_img', preprocessed_img) 
    cv2.imshow('thinned_img', thinned_img) 
    cv2.imshow('result', fin_img) 
    cv2.imshow('terminations', terminations)
    cv2.imshow('bifurcations', bifurcations)
    cv2.imshow('result_circled', show_minutiae) 
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
