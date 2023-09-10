def getCC(s):
    from youtube_transcript_api import YouTubeTranscriptApi
    try:
        if '=' in s:
            s=s[s.index('=')+1:]
        srt = YouTubeTranscriptApi.get_transcript(s)
        l=['']
        for i in srt:
            l[0]+=i["text"]+' '
        return l
    except:
        return ['No caption']


