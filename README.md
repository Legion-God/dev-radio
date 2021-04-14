![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Code Grade](https://www.code-inspector.com/project/21254/status/svg)
![Code Quality Score](https://www.code-inspector.com/project/21254/score/svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# dev-radio
dev-radio is simple command line tool to listen to radio and developer podcasts.

Listen to radio.

![Snap! Radio GIF is dead](https://media.giphy.com/media/i7aG1z2oEjc92N3BVw/giphy.gif)

Listen to podcasts.

![Snap! Podcast GIF is dead](https://media.giphy.com/media/F3qVzAGaNi1qw2Tzhg/giphy.gif)

## Contents
1. [How to install](#installation)
2. [How to use](#usage)
   1. [dev-radio help](#help-menu)
   2. [Radio](#radio)
       1. [Radio help](#radio-help)
       2. [List all the radio stations.](#listing-all-the-radio-stations)
       3. [Playing a radio station.](#playing-a-radio-station-named-_jpop_)
       4. [Adding a new radio station.](#adding-new-radio-station)
       5. [Deleting a radio station.](#deleting-a-radio-station)
       6. [Renaming a radio station.](#renaming-a-radio-station)
       7. [Resetting all radio station to default ones.](#resetting-all-the-stations-to-default-ones)
       8. [Check which stations are working.](#check-which-stations-are-working)
   3. [Podcast](#podcast)
       1. [Podcast help.](#podcast-help)
       2. [List all the podcasts.](#list-all-the-podcasts)
       3. [Show all the episodes of a podcast.](#show-all-the-episodes-of-a-podcast)
       4. [Play an episode of a podcast.](#play-an-episode-of-a-podcast)
3. [Setting up for development.](#setting-up-development-environment)


## Installation
Just run `pip install dev-radio`

use `pip3` if you are on Linux.  

## Usage

### Help menu 
Shows the help menu about dradio and it's subcommands.

```bash
$ dradio --help
```
---
## Radio
Play radio streams.

### radio help

```bash
$ dradio radio --help

# Using alias.
$ dradio rad --help
```

### Listing all the radio stations.

```bash
$ dradio radio --list

# Using alias.
$ dradio radio -L
# or 
$ dradio rad -L
```

### Playing a radio station named _jpop_.

```bash
$ dradio radio --play jpop

# Using alias
$ dradio radio -P jpop
# or 
$ dradio rad -P jpop
```

### Adding new radio station.

```bash
# adds a new station with name hip-hop0
$ dradio radio --add-station hip-hop0 https://stream.laut.fm/1000hiphop

# Using alias 
$ dradio radio -A hip-hop0 https://stream.laut.fm/1000hiphop
# or 
$ dradio rad -A hip-hop0 https://stream.laut.fm/1000hiphop
```

### Deleting a radio station.

```bash
$ dradio radio --del-station hip-hop0

# Using alias
$ dradio radio -D hip-hop0
# or
$ dradio rad -D hip-hop0
```

### Renaming a radio station.

```bash
$ dradio radio --rename-station hip-hop0 hip-hop

# Using alias
$ dradio radio -R hip-hop0 hip-hop 
# or
$ dradio rad -R hip-hop0 hip-hop
```

### Resetting all the stations to default ones.
This deletes any newly added stations, renamed stations and restores the default radio stations.

```bash
$ dradio radio --reset 

# No alias for reset option.
$ dradio rad --reset
```

### Check which stations are working.

```bash
$ dradio radio --check 

# Using alias
$ dradio radio -C
# or
$ dradio rad -C
```
---
## Podcast
Play podcasts.

### podcast help

```bash
$ dradio podcast --help

# Using alias
$ dradio pod --help
```

### List all the podcasts.
This prints list of all currently available podcasts.

```bash
$ dradio podcast --list

# Using alias
$ dradio pod --list
# or 
$ dradio pod -L
```

### Show all the episodes of a podcast.

```bash
$ dradio podcast --all-eps

# Using alias
$ dradio podcast -A
# or 
$ dradio pod -A
```

### Play an episode of a podcast.

```bash
# 0 is the episode ID NOT episode number.
# Passing episode ID as 0 plays the latest episode of the podcast.
$ dradio podcast --play stackoverflow 0

# Using alias
$ dradio podcast -P stackoverflow 0
# or
$ dradio pod -P stackoverflow 0
```
---

## Setting up development environment.
1. `git clone https://github.com/Legion-God/dev-radio.git`  
2. `cd dev-radio` then create your virtual environment `virtualenv venv`  
3. Activate your venv by entering `source venv/bin/activate`, if you are on Windows use
`.\venv\Scripts\activate`
4. `pip install -r requirements.txt` 
5. To install package locally, run `pip install -e .`    
6. And you are done !
