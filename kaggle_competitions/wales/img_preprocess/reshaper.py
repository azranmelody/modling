##several reshape options
import cv2

def reshape_to_avg(data):
    for_reshape_AVG_imgs = data.copy()
    sum1 = 0
    sum2 = 0
    for pic in data:
        sum1 = sum1 + pic.shape[0]
        sum2 = sum2 + pic.shape[1]

    average_hight = int(sum1/len(for_reshape_AVG_imgs))
    average_width = int(sum2/len(for_reshape_AVG_imgs))

    for i in range(len(for_reshape_AVG_imgs)):
        for_reshape_AVG_imgs[i] = cv2.resize(for_reshape_AVG_imgs[i], (average_hight, average_width))
        
    return for_reshape_AVG_imgs


def reshape_to_constant(data, weight,height):
    for i in range(len(data)):
        data[i] = cv2.resize(data[i], (height, weight))
        
    return data