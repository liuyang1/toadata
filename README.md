# toadata :frog: :eyeglasses:

Index various media meta-data

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fec14c25e255475b8023f5f8e3818d2d)](https://www.codacy.com/app/lujing-zui/toadata?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=liuyang1/toadata&amp;utm_campaign=Badge_Grade)

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
- [x] install
