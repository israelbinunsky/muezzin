import speech_recognition as sr

class Stt:
    def stt(self, filepath):
        r = sr.Recognizer()
        with sr.AudioFile(filepath) as source:
            audio_data = r.record(source)

            try:
                text = r.recognize_google(audio_data)
                print("Transcribed Text: " + text)
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")