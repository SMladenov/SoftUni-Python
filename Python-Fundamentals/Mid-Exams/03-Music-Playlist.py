#Music Playlist

songs = input().split(' ')
numCmds = int(input())

for i in range (numCmds):
    cmd = input()
    cmdSplit = cmd.split(' * ')

    #Case 1
    if cmdSplit[0] == "Add Song":
        if cmdSplit[1] not in songs:
            songs.append(cmdSplit[1])
            print (f"{cmdSplit[1]} successfully added")

    #Case2
    if cmdSplit[0] == "Delete Song":
        songsToRemove = int(cmdSplit[1])
        if len(songs) >= songsToRemove:
            tempToPrint = []
            for b in range (songsToRemove):
                tempToPrint.append(songs[0])
                songs.remove(songs[0])
            if len(tempToPrint) > 0:
                print (f"{', '.join(tempToPrint)} deleted")
            tempToPrint.clear()
            

    #Case 3
    if cmdSplit[0] == "Shuffle Songs":
        index1 = int(cmdSplit[1])
        index2 = int(cmdSplit[2])
        if (0 <= index1 <= (len(songs) - 1)) and (0 <= index2 <= (len(songs) - 1)):
            firstSong = songs[index1]
            secondSong = songs[index2]
            songs[index1] = secondSong
            songs[index2] = firstSong
            print (f"{secondSong} is swapped with {firstSong}")

    #Case 4
    if cmdSplit[0] == "Insert":
        songToInsert = cmdSplit[1]
        songIndex = int(cmdSplit[2])
        if 0 <= songIndex <= (len(songs) - 1):
            if songToInsert not in songs:
                songs.insert(songIndex, songToInsert)
                print (f"{songToInsert} successfully inserted")
            else:
                print (f"Song is already in the playlist")
        else:
            print (f"Index out of range")

    #Case 5
    if cmdSplit[0] == "Sort":
        songs.sort(reverse=True)

    
    if cmdSplit[0] == "Play":
        print (f"Songs to Play:")
        for b in songs:
            print (b)
