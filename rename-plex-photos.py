#!/usr/bin/env python3

import re
import sys
from pathlib import Path
from itertools import chain

def rename_in_season(path):
    episode_stems = set()
    image_paths = []
    pattern = re.compile('[sS]0*(\d+)[eE]0*(\d+)')

    for child in path.iterdir():
        if child.suffix in {".mkv", ".mp4", ".webm"}:
            episode_stems.add(child.stem)

        elif child.suffix in {".jpg", ".jpeg", ".png"}:
            image_paths.append(child)
    
    for image in image_paths:
        if image.stem not in episode_stems:
            match = re.search(pattern, image.stem)
            if match is None: continue
            image_season = match.group(1)
            image_episode = match.group(2)

            for episode_stem in episode_stems:
                match = re.search(pattern, episode_stem)
                episode_season = match.group(1)
                episode_episode = match.group(2)
                if (episode_season == image_season and episode_episode == image_episode):
                    new_name = image.with_stem(episode_stem)
                    print(f"Renaming {image.name} to {new_name.name}")
                    image.replace(new_name)
                

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing argument: path to Plex tv library")
        print("e.g. /hdd/media/tv")
        exit(1)
    path = Path(sys.argv[1])
    if not path.exists():
        print("Invalid path")
        exit(1)
    for season in chain(path.rglob("Season */"), path.rglob("Specials/")):
        rename_in_season(season)