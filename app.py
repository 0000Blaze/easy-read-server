import io
import base64
import logging
from PIL import Image
import subprocess
from tts import textToSpeech
from server_try import printStdoutLog,printStderrLog

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
    binimagepath = "temp.jpg" #provide name of file where to save the output binarized image
    binarization_program_name = "BinarizeForServer"

    # run the Java program
    process = subprocess.Popen(["java", binarization_program_name, imagepath, binimagepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print("Waiting for Binarization to complete")

    # wait for the Java program to finish ##not needed when using subprocess.run() as it blocks by default (though it sets system call parameters to not block)
    process.wait()


    # check the return code to see if the java process completed successfully
    if process.returncode != 0:
        print("Java program failed with error code: ", process.returncode)
        printStderrLog(process)
        printStdoutLog(process)
    else:
        print("Java program finished successfully")
        printStdoutLog(process)
        #the output from java program is path to the binarized image file

    img = Image.open(binimagepath)

    # process OCR with tesseract
    myconfig = r"--psm 6 --oem 3"
    try:
        print("Working on pytessaract OCR")
        text = pytesseract.image_to_string(img,config=myconfig)
    except:
        text ='''Hello from server, This is a test song
            The club isn't the best place to find a lover
            So the bar is where I go
            Me and my friends at the table doing shots
            Drinking fast and then we talk slow
            And you come over and start up a conversation with just me
            And trust me I'll give it a chance now
            Take my hand, stop, put Van the Man on the jukebox
            And then we start to dance, and now I'm singing like
            Girl, you know I want your love
            Your love was handmade for somebody like me
            Come on now, follow my lead
            I may be crazy, don't mind me
            Say, boy, let's not talk too much
            Grab on my waist and put that body on me'''
    
    #pritn output from OCR
    print(text)
    # process TTS
    print("Working on TTS")
    
    textToSpeech(text)

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
