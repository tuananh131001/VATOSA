import os

import librosa
import tensorflow as tf
import numpy as np

SAVED_MODEL_PATH = "model.h5"
SAVED_MODEL_PATH_ANOTHER_PATH = "../../voice_controller/model.h5"
SAMPLES_TO_CONSIDER = 44100


class _Keyword_Spotting_Service:
    """Singleton class for keyword spotting inference with trained models.
    :param model: Trained model
    """

    model = None
    _mapping = [
        "dataset\\open excel",
        "dataset\\open teams",
        "dataset\\open word",
        "dataset\\open zalo",

    ]
    _instance = None

    def predict(self, file_path):
        """
        :param file_path (str): Path to audio file to predict
        :return predicted_keyword (str): Keyword predicted by the model
        """
        try:
            # extract MFCC
            MFCCs = self.preprocess(file_path)

            # we need a 4-dim array to feed to the model for prediction: (# samples, # time steps, # coefficients, 1)
            MFCCs = MFCCs[np.newaxis, ..., np.newaxis]

            # get the predicted label
            predictions = self.model.predict(MFCCs)
            predicted_index = np.argmax(predictions)
            predicted_keyword = self._mapping[predicted_index]
            return predicted_keyword
        except IndexError as inder_err:
            print("PREDICTION ERROR: ", inder_err)
            return ""

    def preprocess(self, file_path, num_mfcc=13, n_fft=2048, hop_length=512):
        """Extract MFCCs from audio file.
        :param file_path (str): Path of audio file
        :param num_mfcc (int): # of coefficients to extract
        :param n_fft (int): Interval we consider to apply STFT. Measured in # of samples
        :param hop_length (int): Sliding window for STFT. Measured in # of samples
        :return MFCCs (ndarray): 2-dim array with MFCC data of shape (# time steps, # coefficients)
        """

        # load audio file
        signal, sample_rate = librosa.load(file_path)

        if len(signal) >= SAMPLES_TO_CONSIDER:
            # ensure consistency of the length of the signal
            signal = signal[:SAMPLES_TO_CONSIDER]

            # extract MFCCs
            MFCCs = librosa.feature.mfcc(signal, sample_rate, n_mfcc=num_mfcc, n_fft=n_fft,
                                         hop_length=hop_length)
        return MFCCs.T


def Keyword_Spotting_Service(SAVED_MODEL_PATH=SAVED_MODEL_PATH):
    """Factory function for Keyword_Spotting_Service class.
    :return _Keyword_Spotting_Service._instance (_Keyword_Spotting_Service):
    """

    if not os.path.exists(SAVED_MODEL_PATH) and os.path.exists(SAVED_MODEL_PATH_ANOTHER_PATH):
        SAVED_MODEL_PATH = SAVED_MODEL_PATH_ANOTHER_PATH

    # ensure an instance is created only the first time the factory function is called
    if _Keyword_Spotting_Service._instance is None:
        _Keyword_Spotting_Service._instance = _Keyword_Spotting_Service()
        _Keyword_Spotting_Service.model = tf.keras.models.load_model(SAVED_MODEL_PATH)
    return _Keyword_Spotting_Service._instance


def speech_to_text(command_wav_file):
    # create 2 instances of the keyword spotting service
    kss_temp = Keyword_Spotting_Service()
    kss1_temp = Keyword_Spotting_Service()

    # check that different instances of the keyword spotting service point back to the same object (singleton)
    assert kss_temp is kss1_temp

    # make a prediction
    if os.path.exists(command_wav_file):
        keyword_result = kss_temp.predict(command_wav_file)
    else:
        print("PREDICT: FILEPATH NOT EXIST")
        keyword_result = ""

    return keyword_result


if __name__ == "__main__":
    # create 2 instances of the keyword spotting service
    kss = Keyword_Spotting_Service()
    kss1 = Keyword_Spotting_Service()

    # check that different instances of the keyword spotting service point back to the same object (singleton)
    assert kss is kss1

    # make a prediction
    # keyword = kss.predict("test/close excel nhung 9.wav")
    # keyword2 = kss.predict("test/close pp nhung 10.wav")
    keyword3 = kss.predict("test/close excel nhung 2s 15.wav")
    keyword4 = kss.predict("test/close word nhung 2s 10.wav")
    # keyword5 = kss.predict("test/open Excel nhung 2s 2.wav")
    keyword6 = kss.predict("test/open word nhung 2s 15.wav")
    # keyword8 = kss.predict("test/openWordTA9.wav")

    # print('Expected output: "close excel"')
    # print("Actual output: " + keyword)
    # print("---------------------------------------")
    # print('Expected output: "close pp"')
    # print("Actual output 2: " + keyword2)
    print('Expected output3: "close excel"')
    print("Actual output 3: " + keyword3)
    print('Expected output4: "close word"')
    print("Actual output 4: " + keyword4)

    # print('Expected output: "open excel"')
    # print("Actual output:5 " + keyword5)
    # print("---------------------------------------")
    print('Expected output6: "open word"')
    print("Actual output 6: " + keyword6)
    # print('Expected output: "open vs"')
    # print("Actual output 7: " + keyword7)
    # print('Expected output: "open word"')
    # print("Actual output 8: " + keyword8)
