# toadata

Index various media meta-data

## Why need this tools?

We have plenty of video format, and so many tools to check them. I am tired to use `mediainfo`, `ffmpeg` and etc to check them.

I just want to check information of video. So write this tool.

## Target

- [ ] collect result from many tools
    - [x] mediainfo
    - [ ] ffmpeg
        - [ ] show streams
        - [ ] show frames
        - [x] capture sample picture for video
- [ ] output format
    - [x] markdown (for review)
        - [x] support comment section, (comment section won't affect when update)
    - [ ] json (key-value format for search)
- [ ] daemon to check new added video file
