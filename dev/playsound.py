# simpleAudio.py
# very basic audio file player without external modules
# for Windows and Mac in Python.  Only plays wav files
# on Windows, seems to work with wav, mp3 and other formats on Macs.

# Provides two functions:
# startSound(filename, async=True, loop=True)
# stopSound()

import sys, platform, subprocess, time, threading

def checkForOS(*terms):
    platformString = (sys.platform + platform.platform()).lower()
    for term in terms:
        if (term in platformString): return True
    return False
osIsWindows = checkForOS("win32", "win64", "windows")
osIsLinux = checkForOS("linux")

if (osIsWindows == True):
    import winsound
    def startSound(filename, async=True, loop=True):
        flags = winsound.SND_FILENAME
        if (async == True): flags |= winsound.SND_ASYNC
        if (loop == True):  flags |= winsound.SND_LOOP
        winsound.PlaySound(filename, flags)
    def stopSound():
        winsound.PlaySound(None, 0)
else:
    # For now, just do Mac OS (sorry, Linux...)
    soundProcesses = [ ]
    soundThreads = [ ]
    soundThreadCounter = 0
    def startSound(filename, async=True, loop=True):
        if (async == True): startAsyncSound(filename, loop)
        else: startSyncSound(filename, loop)
    def startSyncSound(filename, loop, thread=None):
        while True:
            app = "aplay" if osIsLinux else "afplay"
            p = subprocess.Popen([app, filename])
            soundProcesses.append(p)
            p.wait()
            if (p in soundProcesses): soundProcesses.remove(p)
            if (loop == False): break
            if ((thread != None) and (thread not in soundThreads)): break
    def startAsyncSound(filename, loop):
        global soundThreadCounter
        tc = soundThreadCounter
        soundThreadCounter += 1
        soundThreads.append(tc)
        thread = threading.Thread(target=startSyncSound,
                                  args=(filename,loop,tc))
        thread.daemon = True
        thread.start()
    def stopSound():
        global soundThreads
        soundThreads = [ ]
        while (soundProcesses != [ ]):
            try: soundProcesses.pop().terminate()
            except: pass

#####################################
# Simple test
#####################################
"""
def testSoundPlaying():
    print "starting sound!...",
    startSound("tetris.wav", async=True, loop=True)
    print "done!"

    print "sleeping for 4 seconds...",
    time.sleep(4)
    print "done!"

    print "stopping sound...",
    stopSound()
    print "done!"

testSoundPlaying()
"""