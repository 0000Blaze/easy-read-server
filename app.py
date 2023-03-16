import io
import base64
import logging
from PIL import Image
import cv2
from tts import textToSpeech  #gtts program
from server_try import runJavaProgram
# from ravitts import textToSpeech2 #pyttsx3 program

import pytesseract

from flask import Flask, request, abort, jsonify,send_file

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)


@app.route('/SendImage', methods=['POST'])

def returner():
    if not request.json or 'image' not in request.json: 
        abort(400)
    # get the base64 encoded string
    im_b64 = request.json['image']
    # convert it into bytes  
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))
    # convert bytes data to PIL Image object
    img = Image.open(io.BytesIO(img_bytes))
    img = img.save("picture.jpg")
    
    #binarization DC
    imagepath = "picture.jpg" #provide complete path of the saved image that is to be provided to the java ocr program
    binimagepath = "tempb.jpg" #provide name of file where to save the output binarized image
    noisereducedimagepath = "tempn.jpg" #provide name of file where to save the noise reduced output binarized image
    readingordertextfile = "readingorder.txt" #provide name of file where to save the reading order text file
    postnoisereducedimagepath = "tempp.jpg" #provide name of file where to save the noise reduced output binarized image

    binarization_program_name = "BinarizeForServer"
    noisereducer_program_name = "NoiseReducerForServer"
    readingorder_program_name = "TopDownSegmenterForServer"
    postnoisereducer_program_name = "PostNoiseReducerForServer"

    # run the Java program
    #print("Waiting for Binarization to complete")
    runJavaProgram(binarization_program_name, [imagepath, binimagepath])
    # print("Waiting for Noise Reduction to complete")
    runJavaProgram(noisereducer_program_name, [binimagepath, noisereducedimagepath])
    #print("Waiting for Reading Order Determination to complete")
    runJavaProgram(readingorder_program_name, [noisereducedimagepath, readingordertextfile])
    runJavaProgram(postnoisereducer_program_name, [noisereducedimagepath, readingordertextfile,postnoisereducedimagepath])


    # process OCR with tesseract
    myconfig = r"--psm 6"
    try:
        '''print("Working on pytessaract OCR")
        img = cv2.imread(postnoisereducedimagepath)
        f = open(readingordertextfile)
        lines = f.readlines()
        # remove metadatas
        lines.pop(0)
        lines.pop(0)
        
        text = ''
        for line in lines:
          bounds = line.strip().split(',')
          x1 = int(bounds[0])
          x2 = int(bounds[1]) + 1   
          y1 = int(bounds[2])
          y2 = int(bounds[3]) + 1
          img_cropped = img[y1:y2, x1:x2]
          #ar = (x2-x1)/(y2-y1)
          height = x2 - x1
          width = y2 -y1
          borderWidth = min((int)(min(height, width) * 0.25), 20)
          img_border_added = cv2.copyMakeBorder(img_cropped, borderWidth,borderWidth,borderWidth,borderWidth, cv2.BORDER_CONSTANT,value=[255,255,255])
          convString = pytesseract.image_to_string(img_border_added,lang='eng',config = myconfig)
          text += " " + convString.strip()'''
        # f.close()
        text = pytesseract.image_to_string(img,lang='eng', config = myconfig)
        text.strip()
    except:
        text ='''Hello from server'''
    
    # print output from OCR
    print(text)
    # write output from OCR
    with open('text.txt', 'w') as f:
        f.writelines(text)
    
    # process TTS
    print("Working on TTS")
    
    textToSpeech(text)  #gtts
    # textToSpeech2(text)   #pyttsx3

    #response
    data ={
        "content":"Successful,"
    }

    print("Successful")
    return jsonify(data)
    

@app.route("/mpeg")
def streamwav():
    return send_file("./response.mp3",mimetype="audio/mpeg",as_attachment=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
