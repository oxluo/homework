import cv2
import numpy
import os
import sys


def read_images(path, sz=None):
    c = 0
    x, y = [], []
    for dirpath, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirpath, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    if filename == ".directory":
                        continue
                    file_path = os.path.join(subject_path, filename)
                    img = cv2.imread(file_path,  cv2.IMREAD_GRAYSCALE)

                    if sz is not None:
                        img = cv2.resize(img, (200, 200))

                    x.append(numpy.asarray(img, dtype=numpy.uint8))
                    y.append(c)
                except:
                    print("error")
                    raise
            c = c+1
    return [x, y]


def face_rec():

    names = ['DYB', 'MYC', 'WZH']
    '''
    if len(sys.argv) < 2:
        sys.exit()
    [x, y] = read_images(sys.argv[1])
    '''
    [x, y] = read_images('F:/python/images/faces', True)
    y = numpy.asarray(y, dtype=numpy.int32)
    '''
    if len(sys.argv) == 3:
        out_dir = sys.argv[2]
    '''

    '''
    
    cv2.face.EigenFaceRecognizer_create()
            .FisherFaceRecognizer_create()
    置信度4000-5000以下可靠
    
    cv2.face.LBPHFaceRecognizer_create()
    置信度50以下好，80以上不可靠
    '''
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(numpy.asarray(x), numpy.asarray(y))
    camera = cv2.VideoCapture(1)
    face_cascade = cv2.CascadeClassifier(
        'F:/python/haarcascades/haarcascade_frontalface_default.xml')
    while True:
        ret, frame = camera.read()
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            roi = gray[y:y + h, x:x + w]
            try:
                roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)
                params = model.predict(roi)
                print("Label: %s, Confidence: %.2f" % (params[0], params[1]))
                if params[1] <= 80:
                    cv2.putText(frame, names[params[0]], (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
            except:
                continue
        cv2.imshow('face', frame)
        if cv2.waitKey(1) & 0xff == 27:
            break

    cv2.destroyAllWindows()


face_rec()
