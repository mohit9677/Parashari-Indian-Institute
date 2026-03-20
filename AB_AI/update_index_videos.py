import shutil
import os
import re

# Source and Destination paths
source_imgs = [
    r"D:\ParashariTeam\free video 1.png",
    r"D:\ParashariTeam\free video 2.png",
    r"D:\ParashariTeam\free video 3.png",
    r"D:\ParashariTeam\free video 4.png"
]
dest_imgs = [
    r"d:\ParashariTeam\AB_AI\assets\images\free-video-1.png",
    r"d:\ParashariTeam\AB_AI\assets\images\free-video-2.png",
    r"d:\ParashariTeam\AB_AI\assets\images\free-video-3.png",
    r"d:\ParashariTeam\AB_AI\assets\images\free-video-4.png"
]

# Copy images
for src, dst in zip(source_imgs, dest_imgs):
    try:
        shutil.copy2(src, dst)
        print(f"Copied: {src} -> {dst}")
    except Exception as e:
        print(f"Error copying {src}: {e}")

# Update index.html
html_path = r"d:\ParashariTeam\AB_AI\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new playlist HTML
new_playlist = """
        <!-- Playlist Sidebar -->
        <div class="playlist-sidebar">
          <div class="playlist-item active" onclick="switchMainVideo('https://drive.google.com/file/d/1EeSlZNorC3rfVjnx2CU-vsXmO7Y3pYi6/preview', 'assets/images/free-video-1.png', this)">
            <img src="assets/images/free-video-1.png" class="playlist-thumb">
            <div class="playlist-info">
              <h5>Introduction to Astrology</h5>
              <span>Part 1: The Basics (15 min)</span>
            </div>
          </div>
          <div class="playlist-item" onclick="switchMainVideo('https://drive.google.com/file/d/1pGuy1R19WNCPFncZB2CPOF6oBHjk-B9m/preview', 'assets/images/free-video-2.png', this)">
            <img src="assets/images/free-video-2.png" class="playlist-thumb">
            <div class="playlist-info">
              <h5>The Secret of Zodiacs</h5>
              <span>Part 2: Hidden Meanings (22 min)</span>
            </div>
          </div>
          <div class="playlist-item" onclick="switchMainVideo('https://drive.google.com/file/d/1ueubDhCuricSLb2Lyhtw30bMWQJ2sXW6/preview', 'assets/images/free-video-3.png', this)">
            <img src="assets/images/free-video-3.png" class="playlist-thumb">
            <div class="playlist-info">
              <h5>Vastu for Prosperity</h5>
              <span>Masterclass Preview (18 min)</span>
            </div>
          </div>
          <div class="playlist-item" onclick="switchMainVideo('https://drive.google.com/file/d/1ueubDhCuricSLb2Lyhtw30bMWQJ2sXW6/preview', 'assets/images/free-video-4.png', this)">
            <img src="assets/images/free-video-4.png" class="playlist-thumb">
            <div class="playlist-info">
              <h5>Astrology Remedies</h5>
              <span>Part 4: Effective Solutions (20 min)</span>
            </div>
          </div>
        </div><!-- End Playlist Sidebar -->"""

# Replace the playlist sidebar section accurately
content = re.sub(r'<!-- Playlist Sidebar -->.*?<!-- End Playlist Sidebar -->', new_playlist, content, flags=re.DOTALL)

# Update the featured video container default poster
content = content.replace('src="assets/images/video-poster-1.jpg"', 'src="assets/images/free-video-1.png"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully.")
