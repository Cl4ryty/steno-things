# theory_dictionaries
Dictionaries based on the [Platinum Steno Theory](https://www.youtube.com/@PlatinumSteno) that add upon the [dictionary provided by Platinum Steno](https://platinumsteno.com/downloads/platinum-steno-ncrs-theory-dictionary/). 

# Contents
- the folder `lesson_dicts` contains dictionaries for the first dozen Platinum lessons, with each dictionary containing only the new words introduced in the lesson and the read back video for that lesson (missing words from some read back videos) - this is useful because some of the words used in those early lessons are not in the dictionary provided by Platinum or are later written differently, and also because these individual dictionaries do not contain misstrokes
- `platinum_times.json` contains entries for writing time figures as taught in Platinum lesson 21 (does not contain entries for a.m., p.m., o'clock as they are already in the theory dictionary)
- `fingerspelling.json` contains entries that I use for spelling words following the pattern introduced in lesson 18, using the letters combined with the asterisk for lower-case letters and combined with RBGS for upper-case letters - for stitching I utilize the [Plover Stitching plug-in](https://github.com/morinted/plover_stitching) and the outline `ST*EUFP`
- `platinum_thumber_ordinals.json` defines entries for writing ordinals as in lesson 20 but using `-U` instead of `-E` to make it possible to use with boards using (outer) thumber keys instead on a number bar
- `platinum_Q&A.json` defines rudimentary entries for taking down Q&A - I now use a more complex system using a modified [speaker-id plug-in](https://github.com/sammdot/plover-speaker-id) and another dictionary
- `numbers.py` allows for writing numbers over 100 and dollar amounts as described in lesson 26 - however, it does not (yet) contain entries for writing years as thought in Platinum
- `numbers.json` contains entries for writing fractions (lesson 39), or more specifically the first number of the fraction followed by a hyphen, that are missing in the theory dictionary
- `platinum_user.json` contains entries of words that came up in lessons but either were not defined in the provided theory dictionary or defined differently than taught in the theory lessons
- `spelling_ordinals_times_numbers.json` combines `fingerspelling.json`, `platinum_thumber_ordinals.json`, `platinum_times.json`, and `numbers.json`
