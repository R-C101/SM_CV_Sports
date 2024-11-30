import numpy
from trackers import Tracker
from team_assigner import TeamAssigner
from utils import read_video, save_video

def main():
    video_frames = read_video('input_videos/sample1.mp4')
    # save_video(video_frames, 'output_videos/outputvideo.avi')
    tracker = Tracker('best.pt')
    tracks = tracker.get_object_tracks(video_frames,read_from_stub=False,stub_path='stubs/track_stubs.pkl')
    
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], 
                                    tracks['players'][0])
    
    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],   
                                                 track['bbox'],
                                                 player_id)
            tracks['players'][frame_num][player_id]['team'] = team 
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]
            
    output_video_frames = tracker.draw_annotations(video_frames,tracks)
    
    save_video(output_video_frames, 'output_videos/sample.avi')
    
    
    
if __name__ == '__main__':
    main()