#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime, timedelta
import re
import json
import yt_dlp
import argparse
import csv

# List of fabric patterns to apply
patterns = [
    "extract_wisdom",
    "summarize",
    "extract_main_idea",
    "improve_academic_writing",
    "extract_wisdom_agents",
    "extract_predictions",
    "extract_questions",
    "solve_with_cot",
    "tweet",
    "write_essay",
    "write_micro_essay",
    "write_hackerone_report",
    "create_quiz",
    "create_markmap_visualization",
    "create_mermaid_visualization",
    "analyze_presentation",
    "clean_text",
    "create_ai_jobs_analysis",
    "create_art_prompt",
    "create_keynote",
    "create_logo",
    "create_visualization",
    "explain_project",
    "explain_terms",
    "find_hidden_message",
    "get_wow_per_minute",
    "summarize_legislation",
    "to_flashcards",
    "transcribe_minutes"
    "capture_thinkers_work"
]

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def parse_time_string(time_str):
    if "days" in time_str:
        days = int(time_str.split()[0])
        return timedelta(days=days)
    elif "hours" in time_str:
        hours = int(time_str.split()[0])
        return timedelta(hours=hours)
    else:
        return timedelta()

def convert_youtube_url(url):
    if '/live/' in url:
        video_id = url.split('/live/')[1].split('?')[0]
        return f'https://www.youtube.com/watch?v={video_id}'
    return url

def get_video_metadata(url):
    url = convert_youtube_url(url)
    ydl_opts = {
        'skip_download': True,
        'no_warnings': True,
        'quiet': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            metadata = {
                'title': info.get('title'),
                'upload_date': info.get('upload_date'),
                'duration': info.get('duration'),
                'view_count': info.get('view_count'),
                'like_count': info.get('like_count'),
                'channel': info.get('channel'),
                'description': info.get('description'),
                'is_live': info.get('is_live'),
                'live_status': info.get('live_status'),
            }
            return metadata
        except yt_dlp.utils.DownloadError as e:
            if "This live event will begin in" in str(e):
                time_str = str(e).split("begin in ")[1].split(".")[0]
                start_time = datetime.now() + parse_time_string(time_str)
                return {"status": "future", "start_time": start_time.isoformat()}
            elif "Private video" in str(e):
                return {"status": "private"}
            else:
                return {"status": "error", "message": str(e)}

def download_audio_and_video(url, output_path, download_audio, download_video):
    url = convert_youtube_url(url)
    audio_filename = None
    video_filename = None

    if download_audio:
        # Download audio
        ydl_opts_audio = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            audio_filename = ydl.prepare_filename(info_dict).rsplit('.', 1)[0] + '.mp3'
        
        # Ensure audio is in MP3 format
        if not os.path.exists(audio_filename):
            log_message(f"Converting audio to MP3: {audio_filename}")
            subprocess.run(['ffmpeg', '-i', audio_filename.rsplit('.', 1)[0] + '.webm', 
                            '-acodec', 'libmp3lame', '-b:a', '192k', audio_filename])

    if download_video:
        # Download video (medium quality)
        ydl_opts_video = {
            'format': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best[height<=720]',
            'outtmpl': os.path.join(output_path, '%(title)s_medium_quality.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_filename = ydl.prepare_filename(info_dict)
        
        # Ensure video is in MP4 format
        if not video_filename.endswith('.mp4'):
            new_video_filename = video_filename.rsplit('.', 1)[0] + '.mp4'
            log_message(f"Converting video to MP4: {new_video_filename}")
            subprocess.run(['ffmpeg', '-i', video_filename, '-c:v', 'libx264', '-crf', '23', 
                            '-c:a', 'aac', '-b:a', '128k', new_video_filename])
            os.remove(video_filename)
            video_filename = new_video_filename
    
    return audio_filename, video_filename

def save_transcript(video_url, output_file):
    video_url = convert_youtube_url(video_url)
    try:
        result = subprocess.run(['fabric', '-y', video_url, '--transcript'], 
                                capture_output=True, text=True, check=True)
        transcript_content = result.stdout.replace("&#39;", "'")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(transcript_content)
        log_message(f"Transcript saved to: {output_file}")
    except subprocess.CalledProcessError as e:
        log_message(f"Error saving transcript: {e}")
        log_message(f"Error details: {e.stderr}")
        error_file = output_file.replace('.md', '_error.md')
        with open(error_file, 'w', encoding='utf-8') as f:
            f.write(f"Error saving transcript: {e}\n\nError details:\n{e.stderr}")
        log_message(f"Error details saved to: {error_file}")

def main(download_audio, download_video):
    # Read YouTube URLs and metadata from CSV
    with open('All_Institute_Videos.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        entries = list(reader)

    # Process each entry from CSV
    for entry in entries:
        url = convert_youtube_url(entry['YouTube'].strip())
        series = entry['Series'].strip()
        unique_event_name = entry['Unique event name'].strip()
        
        log_message(f"Processing video: {unique_event_name}")
        
        # Create a folder for this video under its Series
        output_path = os.path.join("output", series, unique_event_name)
        os.makedirs(output_path, exist_ok=True)
        
        # Get and save video metadata
        metadata = get_video_metadata(url)
        
        if metadata.get('status') == 'future':
            log_message(f"Video '{unique_event_name}' is a future live event scheduled for {metadata['start_time']}. Skipping processing.")
            continue
        elif metadata.get('status') == 'private':
            log_message(f"Video '{unique_event_name}' is private and cannot be accessed. Skipping processing.")
            continue
        elif metadata.get('status') == 'error':
            log_message(f"Error fetching metadata for video '{unique_event_name}': {metadata['message']}. Skipping processing.")
            continue
        
        with open(os.path.join(output_path, "metadata.json"), "w") as f:
            json.dump(metadata, f, indent=2)
        log_message(f"Metadata saved to: {output_path}/metadata.json")
        
        # Download audio and video if flags are set
        if download_audio or download_video:
            try:
                log_message(f"Downloading {'audio' if download_audio else ''} {'and' if download_audio and download_video else ''} {'video' if download_video else ''} for {unique_event_name}")
                audio_file, video_file = download_audio_and_video(url, output_path, download_audio, download_video)
                if audio_file:
                    log_message(f"Audio downloaded to: {audio_file}")
                if video_file:
                    log_message(f"Video downloaded to: {video_file}")
            except Exception as e:
                log_message(f"Error downloading audio/video for {unique_event_name}: {e}")
        
        # Save transcript
        transcript_file = os.path.join(output_path, "transcript.md")
        log_message(f"Saving transcript for video {unique_event_name}")
        save_transcript(url, transcript_file)
        
        # Apply each pattern and save output
        for pattern in patterns:
            output_file = os.path.join(output_path, f"{pattern}_output.md")
            log_message(f"Applying pattern '{pattern}' to video {unique_event_name}")
            
            try:
                result = subprocess.run(["fabric", "-y", url, "--pattern", pattern], 
                                        capture_output=True, text=True, check=True)
                with open(output_file, "w") as f:
                    f.write(result.stdout)
                log_message(f"Output saved to: {output_file}")
            except subprocess.CalledProcessError as e:
                log_message(f"Error applying pattern '{pattern}' to video {unique_event_name}: {e}")
                # Save error output to a file
                error_file = os.path.join(output_path, f"{pattern}_error.md")
                with open(error_file, "w") as f:
                    f.write(f"Error: {str(e)}\n\nStderr:\n{e.stderr}")
                log_message(f"Error details saved to: {error_file}")
        
        log_message(f"Finished processing video: {unique_event_name}")
        print("----------------------------------------")
    
    log_message("Processing complete. All outputs saved in the 'output' folder.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process YouTube videos with fabric patterns and optionally download audio/video.")
    parser.add_argument("--download-audio", action="store_true", help="Download audio from the YouTube videos")
    parser.add_argument("--download-video", action="store_true", help="Download video from the YouTube videos")
    args = parser.parse_args()

    main(args.download_audio, args.download_video)