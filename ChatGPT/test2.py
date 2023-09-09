#audio test

import openai


audio_file = open("/path/to/file/audio.mp3", "rb")
# audio -> text
transcript = openai.Audio.transcribe("whisper-1", audio_file)
# language translate
transcript = openai.Audio.translate("whisper-1", audio_file)