IMG_CONTAINER_URL = "../resources/assets/"
json_filepath = "../resources/"
json_filename = "data.json"

audio_filepath = "../../voice_authentication/extractAudio/wavs/voxceleb1/test/wav/"  # wav format file -> username/username/file.wav
train_filepath = "../../voice_authentication/extractAudio/wavs/voxceleb1/dev/feat/train_logfbank_nfilt40/"  # .p format file -> username/username/file.p
train_wav_filepath = "../../voice_authentication/extractAudio/wavs/voxceleb1/dev/wav/" # wav format file -> username/username/file.wav
TRAIN_FEAT_DIR_ANOTHER_PATH = '../../voice_authentication/feat_logfbank_nfilt40/train/'
TEST_FEAT_DIR_ANOTHER_PATH = '../../voice_authentication/feat_logfbank_nfilt40/test/'
enroll_filepath = "../../voice_authentication/feat_logfbank_nfilt40/test/"  # enroll .p
identify_filepath = "../../voice_authentication/feat_logfbank_nfilt40/test/"  # enroll .p
command_dir = '../../voice_controller/user_command/'
train_py_path = "../../voice_authentication/train.py"
prediction_py_path = "../../voice_controller/prediction.py"
APPS_PY = "../resources/Apps.py"

SIGNUP_DURATION = 10  # in seconds
LOGIN_DURATION = 10  # in seconds
TRAIN_DURATION = 5
COMMAND_DURATION = 5  # in seconds
SAMPLE_RATE = 22050
TOTAL_TRAIN_FILE = 10

# login_record_button_size = 310
# signup_record_button_size = 180
# entry_height = 43
# entry_radius = 10

main_color = "#2B2C33"
nav_color = "#2F3A48"
main_text_color = "white"
alternative_text_color = "#FEA2A2"
button_text_color = main_color
button_bck_color = "white"
footer_text_color = "white"
count_down_size = 11