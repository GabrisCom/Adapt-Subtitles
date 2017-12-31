# Adapt-Subtitles
Convert from WebVtt to SRT

Problem: I want to download series (with subtitles) from SVT Play, TV4, etc to watch them off-line whenever I want
Solution: https://mrs0m30n3.github.io/youtube-dl-gui/

Problem: After I download subtitles my media player in Windows do not recognize the file
Solution: I have figured out that it has to do with file syntax, you basically need to do this:

- Translate encoding from UTF-8 to ISO-8859-1
- Terminate lines with CRLF (\r\n) instead of LF (\n)
- Replace dot with comma as delimiter in time representation

I have made a Python script for it.

You can use the script or try some WebVtt to Srt convertor online. 
In any the case, I can now download whatever video and subtitle from SVT Play and it works all smooth.
That shall be good for my Swedish skills :-)