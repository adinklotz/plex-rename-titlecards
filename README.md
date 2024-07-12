The Plex media server [allows](https://support.plex.tv/articles/200220717-local-media-assets-tv-shows/#toc-2) placing images alongside episodes to be used as thumbnails or title cards.
The problem is that in order to be recognized, the title cards must have the identical filename to the episode, making them a pain to manage.

This is a quick and dirty little script that helps with that. Drop title cards into the corresponding season folders, named like "S01E01.png, S01E02.png", etc, run `rename-plex-titlecards.py <path-to-plex-library>`,
and it will rename those title cards to match their episodes and be picked up by Plex. That's it, couldn't be simpler but it does the job!
