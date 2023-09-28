# from roboflow import Roboflow
# rf = Roboflow(api_key="c1kgDFjWWVIH693OKbZ7")
# project = rf.workspace("yolov7-n1bli").project("facemask-vucnu")
# dataset = project.version(1).download("yolov7")
import cv2 as cv
image=cv.imread("runs\train\Facemask5\train_batch0.jpg")
cv.imshow("Image",image)
cv.waitKey(0)
cv.destroyAllWindows()