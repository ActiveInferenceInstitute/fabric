#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime
import re
import json
import yt_dlp
import argparse

# List of YouTube URLs
youtube_urls = [
    "https://youtube.com/watch?v=4MQUMZxBm6k"
    # Add more URLs here
]

# List of fabric patterns to apply
patterns = [
    "extract_wisdom",
    "summarize",
    "extract_main_idea",
    "extract_extraordinary_claims",
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
    "capture_thinkers_work" 
]

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def get_video_metadata(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            'title': info.get('title'),
            'upload_date': info.get('upload_date'),
            'duration': info.get('duration'),
            'view_count': info.get('view_count'),
            'like_count': info.get('like_count'),
            'channel': info.get('channel'),
            'description': info.get('description')
        }

def download_audio_and_video(url, output_path, download_audio, download_video):
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
        log_message(f"Audio downloaded to: {audio_filename}")  # Added logging for audio download

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
        
        # Extract screenshots every 2 seconds
        extract_screenshots(video_filename, output_path)
        log_message(f"Video downloaded to: {video_filename}")  # Added logging for video download

    return audio_filename, video_filename

def extract_screenshots(video_file, output_path):
    screenshot_dir = os.path.join(output_path, "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, "screenshot_%03d.png")
    log_message("Extracting screenshots every 2 seconds")
    try:
        subprocess.run([
            'ffmpeg',
            '-i', video_file,
            '-vf', 'fps=1/2',
            screenshot_path
        ], check=True)
        log_message(f"Screenshots saved to: {screenshot_dir}")
    except subprocess.CalledProcessError as e:
        log_message(f"Error extracting screenshots: {e}")  # Added error logging
        # Save error details
        with open(os.path.join(output_path, "screenshot_error.md"), "w") as f:
            f.write(f"Error: {str(e)}\n\nStderr:\n{e.stderr}")  # Added saving error details
        log_message("Screenshot extraction error details saved.")  # Added logging

def main(download_audio, download_video):
    # Process each YouTube URL
    for url in youtube_urls:
        # Extract video ID from URL
        video_id = re.search(r"v=([^&]*)", url)
        if video_id:
            video_id = video_id.group(1)
        else:
            log_message(f"Could not extract video ID from URL: {url}")
            continue
        
        log_message(f"Processing video: {video_id}")
        
        # Create a folder for this video
        output_path = f"output/{video_id}"
        os.makedirs(output_path, exist_ok=True)
        
        # Get and save video metadata
        try:
            metadata = get_video_metadata(url)
            with open(f"{output_path}/metadata.json", "w") as f:
                json.dump(metadata, f, indent=2)
            log_message(f"Metadata saved to: {output_path}/metadata.json")
        except Exception as e:
            log_message(f"Error fetching metadata for video {video_id}: {e}")
        
        # Download audio and video if flags are set
        if download_audio or download_video:
            try:
                log_message(f"Downloading {'audio' if download_audio else ''} {'and' if download_audio and download_video else ''} {'video' if download_video else ''} for {video_id}")
                audio_file, video_file = download_audio_and_video(url, output_path, download_audio, download_video)
                if audio_file:
                    log_message(f"Audio downloaded to: {audio_file}")
                if video_file:
                    log_message(f"Video downloaded to: {video_file}")
            except Exception as e:
                log_message(f"Error downloading audio/video for {video_id}: {e}")
        
        # Save transcript
        transcript_file = f"{output_path}/transcript.md"
        log_message(f"Saving transcript for video {video_id}")
        try:
            result = subprocess.run(["fabric", "-y", url, "--transcript"], 
                                    capture_output=True, text=True, check=True)
            
            # Replace &#39; with ' in the transcript
            transcript_content = result.stdout.replace("&#39;", "'")
            
            with open(transcript_file, "w") as f:
                f.write(transcript_content)
            log_message(f"Transcript saved to: {transcript_file}")
        except subprocess.CalledProcessError as e:
            log_message(f"Error saving transcript for video {video_id}: {e}")
            with open(f"{output_path}/transcript_error.md", "w") as f:
                f.write(f"Error: {str(e)}\n\nStderr:\n{e.stderr}")
        
        # Apply each pattern and save output
        for pattern in patterns:
            output_file = f"{output_path}/{pattern}_output.md"
            log_message(f"Applying pattern '{pattern}' to video {video_id}")
            
            try:
                result = subprocess.run(["fabric", "-y", url, "--pattern", pattern], 
                                        capture_output=True, text=True, check=True)
                with open(output_file, "w") as f:
                    f.write(result.stdout)
                log_message(f"Output saved to: {output_file}")
            except subprocess.CalledProcessError as e:
                log_message(f"Error applying pattern '{pattern}' to video {video_id}: {e}")
                # Save error output to a file
                error_file = f"{output_path}/{pattern}_error.md"
                with open(error_file, "w") as f:
                    f.write(f"Error: {str(e)}\n\nStderr:\n{e.stderr}")
                log_message(f"Error details saved to: {error_file}")
        
        log_message(f"Finished processing video: {video_id}")
        print("----------------------------------------")

    log_message("Processing complete. All outputs saved in the 'output' folder.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process YouTube videos with fabric patterns and optionally download audio/video.")
    parser.add_argument("--download-audio", action="store_true", help="Download audio from the YouTube videos")
    parser.add_argument("--download-video", action="store_true", help="Download video from the YouTube videos")
    args = parser.parse_args()

    main(args.download_audio, args.download_video)