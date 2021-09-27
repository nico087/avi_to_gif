import ffmpeg
import os


def avi_to_gif():

    for video_file in os.listdir("avi"):
        if video_file.endswith((".avi", ".AVI")):
            video_file_name = video_file.split(".")[0]
            gif_file = video_file_name + ".gif"

            stream = ffmpeg.input(f"avi/{video_file}")
            stream = ffmpeg.filter(stream, "fps", fps=10)
            stream = ffmpeg.output(stream, f"gif/{gif_file}")
            ffmpeg.run(stream)

        else:
            print("Extension error in file!")

def main():
    avi_to_gif()


if __name__ == "__main__":
    main()