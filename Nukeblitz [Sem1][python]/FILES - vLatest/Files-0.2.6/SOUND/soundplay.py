def soundplay():
        import winsound as ws
        ws.PlaySound("theme.wav",ws.SND_ALIAS|ws.SND_NODEFAULT|ws.SND_ASYNC|ws.SND_LOOP)
