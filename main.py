from utils.video_utils import read_video, save_video
from tracker.tracker import Tracker
def main():
    video_frame = read_video('input_data/input.mp4')

    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frame, read_from_stub = True, stub_path='stub/track_stub.pkl')

    output_video_frames = tracker.draw_annotation(video_frame, tracks)

    save_video(output_video_frames, 'output_data/output.avi')

if __name__ == '__main__':
    main()