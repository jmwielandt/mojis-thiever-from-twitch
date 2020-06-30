$folderDest = "mojis"
foreach ($file in ls .) {
    if ($file.name.endswith(".links.txt")) {
        foreach ($link in get-content $file) {
            $nameOut = $folderDest + "/" + $link.split("/")[-2] + ".png"
            Start-BitsTransfer -Source $link -Destination $nameOut
        }
    }
}