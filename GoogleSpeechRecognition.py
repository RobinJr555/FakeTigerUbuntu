#<head>--------------------------------------------------------------------------</head>-#
#@description:RobinJr's personnal Google speech recognition API interface for GreatWork
#@author:RobinJr.
#@firstedit:2018/4/18
#@lastedit :2018/4/19

#<body>--------------------------------------------------------------------------</body>-#
# for performing speech recognition,whith support for several engines and API
# in this example , we use Google Speech Recognition API
# import module as alias :define a alias for module
import speech_recognition as sr
import os

class GoogleRecognitionclass():
    def __init__(self):
        self.r = sr.Recognizer()                       # create a new Recognizer instance

    def getaudio(self):
        # with .. as .. a elegant syntax in python for dealing some automatic petty tasks
        # open the microphone and start recording
        # source is the Microphone instance created above
        with sr.Microphone() as source:                 
            print("Say something!")
            try:
                return self.r.listen(source,timeout = 10)               # records a single phrase from source
            except sr.WaitTimeoutError:
                print("Wait time out, no audio input!")
                return False

    def recognizeingoogle(self,argaudio):
        # no input
        if argaudio == False:
            return ""
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            self.audiotext = self.r.recognize_google(argaudio)
            return self.audiotext
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

#<main>--------------------------------------------------------------------------</main>-#
if __name__ == "__main__":
    t = os.system('clear')
    gr = GoogleRecognitionclass()
    print("you said:"+gr.recognizeingoogle(gr.getaudio()))

