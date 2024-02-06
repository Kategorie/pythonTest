import os
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
from music21 import stream, meter, tempo, note, metadata, converter

score = stream.Score()


class AudioConverterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Audio Converter")

        # 1열: 오디오 파일 입력
        self.label_input_audio = tk.Label(master, text="Input Audio:")
        self.label_input_audio.grid(row=0, column=0, sticky="e")

        self.input_audio_path = tk.Entry(master, width=40)
        self.input_audio_path.grid(row=0, column=1)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_audio)
        self.browse_button.grid(row=0, column=2)

        # 2열: 오디오 파형 디스플레이
        self.label_waveform = tk.Label(master, text="Waveform Display:")
        self.label_waveform.grid(row=1, column=0, sticky="e")

        # TODO: 오디오 파형 디스플레이 추가 (예: Canvas 사용)

        # 3열: 변환 및 저장 버튼
        self.convert_button = tk.Button(
            master, text="Convert", command=self.convert_audio
        )
        self.convert_button.grid(row=2, column=1, pady=10)

        self.save_button = tk.Button(master, text="Save", command=self.save_files)
        self.save_button.grid(row=2, column=2, pady=10)

    def browse_audio(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Audio files", "*.mp3;*.wav")]
        )
        self.input_audio_path.delete(0, tk.END)
        self.input_audio_path.insert(0, file_path)

    def convert_audio(self):
        input_audio_path = self.input_audio_path.get()

        if input_audio_path:
            output_sheet_music_path = "output_sheet_music.xml"
            output_midi_path = "output_midi.mid"
            self.analyze_and_create_sheet_music(
                input_audio_path, output_sheet_music_path, output_midi_path
            )

            # 악보와 MIDI 파일을 새 창에 표시
            self.display_sheet_music(output_sheet_music_path)
            self.display_midi(output_midi_path)

    def classify_pitch(self, pitch):
        # 피아노 음계에 매핑
        piano_mapping = {
            "C": "C",
            "C#": "C#",
            "D": "D",
            "D#": "D#",
            "E": "E",
            "F": "F",
            "F#": "F#",
            "G": "G",
            "G#": "G#",
            "A": "A",
            "A#": "A#",
            "B": "B",
        }

        # pitch를 가장 가까운 음계로 매핑
        closest_pitch = min(
            piano_mapping.keys(), key=lambda x: abs(pitch - piano_mapping[x])
        )
        return closest_pitch

    def analyze_and_create_sheet_music(
        self, mp3_file_path, output_sheet_music_path, output_midi_path
    ):
        # mp3 파일 로드
        audio = AudioSegment.from_file(mp3_file_path)

        # 악보 및 MIDI를 위한 Music21 Stream 생성
        score = stream.Score()

        # 음원에서 pitch를 추출하여 분석
        for i, segment in enumerate(audio[::10]):  # 10ms 간격으로 처리
            pitch = segment.max
            classified_pitch = self.classify_pitch(pitch)
            duration = segment.duration_seconds

            # Music21 Note 객체 생성
            n = note.Note(classified_pitch)
            n.duration = duration

            # Part에 Note 추가
            score.append(n)

        # Part를 Score에 추가
        # ...

        # 악보 출력
        score.write("musicxml", output_sheet_music_path)

        # MIDI 파일 출력
        self.midi_stream = stream.Score()
        midi_stream.append(score.parts[0].makeMeasures())
        midi_stream.write("midi", output_midi_path)

    def display_sheet_music(self, sheet_music_path):
        new_window = tk.Toplevel(self.master)
        new_window.title("Sheet Music Display")

        # Music21 Converter를 사용하여 악보를 이미지로 변환 및 표시
        sheet_music_image = converter.parse(sheet_music_path).show("musicxml.png")
        image_label = tk.Label(new_window, image=sheet_music_image)
        image_label.pack()

    def display_midi(self, midi_path):
        new_window = tk.Toplevel(self.master)
        new_window.title("MIDI Display")

        # TODO: MIDI 파일을 표시하는 방법 추가

    def save_files(self):
        # 악보와 MIDI 파일을 사용자가 지정한 위치에 저장
        sheet_music_path = "output_sheet_music.xml"
        midi_path = "output_midi.mid"

        sheet_music_save_path = filedialog.asksaveasfilename(
            defaultextension=".xml", filetypes=[("MusicXML files", "*.xml")]
        )
        midi_save_path = filedialog.asksaveasfilename(
            defaultextension=".mid", filetypes=[("MIDI files", "*.mid")]
        )

        if sheet_music_save_path:
            os.rename(sheet_music_path, sheet_music_save_path)

        if midi_save_path:
            os.rename(midi_path, midi_save_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = AudioConverterGUI(root)
    root.mainloop()
