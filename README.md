# Auto Splitter Time Remover for Journey
This program compares split images to a capture region of any window (OBS, xsplit, etc.) and automatically hits your split hotkey when there is a match. It can be used in tandem with any speedrun timer that accepts hotkeys (LiveSplit, wsplit, etc.). The purpose of this program is to remove the need to manually press your split hotkey as well as removing loading time from your final time.

This program only works for Journey.

# DISCLAIMER

This program is a fork of the project [AutoSplitter](https://github.com/Toufool/Auto-Split) created by Toufool and Faschz.

I take no credits for this work, as 95% of the code comes from this project.

# TUTORIAL

## DOWNLOAD AND OPEN

### Compatability
- Windows 7 and 10.

### Opening the program
- Download the [latest version](https://github.com/robincherix/AutoSplitterJourney/releases)
- Extract the file and open AutoSplit.exe.

## Split Image Folder
- Supported image file types: .png, .jpg, .jpeg, .bmp, and [more](https://docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html#imread).
- Images can be any size.
- Images are matched in alphanumerical order.
- Recommended filenaming convention: `001_SplitName.png, 002_SplitName.png, 003_SplitName.png`... 
- Custom split image settings are handled in the filename. See how [here](https://github.com/Toufool/Auto-Split#custom-split-image-settings).
- Images can be created using Print Screen, [Snipping Tool](https://support.microsoft.com/en-us/help/4027213/windows-10-open-snipping-tool-and-take-a-screenshot), or AutoSplit's Take Screenshot button.

## Capture Region
- This is the region that your split images are compared to. Usually, this is going to be the full game screen.
- Click "Select Region"
- Click and drag to form a rectangle over the region you want to capture.
- Adjust the x, y, width, and height of the capture region manually to make adjustments as needed.
- If you want to align your capture region by using a reference image, click "Align Region"
- You can freely move the window that the program is capturing, but resizing the window will cause the capture region to change.
- Once you are happy with your capture region, you may unselect Live Capture Region to decrease CPU usage if you wish.
- You can save a screenshot of the capture region to your split image folder using the Take Screenshot button.

## Max FPS
  - Calculates the maximum comparison rate of the capture region to split images. This value will likely be much higher than needed, so it is highly recommended to limit your FPS depending on the frame rate of the game you are capturing.

### Timer Global Hotkeys
- Click "Set Hotkey" on each hotkey to set the hotkeys to AutoSplit. Start / Split hotkey must be the same as the one used in your preferred timer program in order for the splitting to work properly.
- Make sure that Global Hotkeys are enabled in your speedrun timer.
- All of these actions can also be handled by their corresponding buttons.

### Settings
Each time AutoSplit is closed, it saves a the setting file `settings.pkl` to the directory AutoSplit.exe is located in. This settings file is loaded upon opening the program. These settings include split image directory, capture region, capture region dimensions, fps limit and hotkeys. Settings can be reloaded using the Reload Settings button.

## Known Limitations
- Starting your timer/AutoSplit is still manual.
- Last split is still manual
- The window of the capture region cannot be minimized.

## Known Issues
- When setting your region, you may only see a black image. This is caused by hardware acceleration. You may be able to disable this through the application itself like in [Google Chrome](https://www.technize.net/google-chrome-disable-hardware-acceleration/). If not, this can also be disabled through [Windows](https://www.thewindowsclub.com/hardware-acceleration-windows-7). NOTE: If you notice any computer performance issues after disabling hardware acceleration, re-enable it.
- Known to currently have issues selecting a region in Streamlabs OBS (only shows black image).
- Using numpad number keys when numlock is on does not split correctly. Either avoid using numpad or turn numlock off to avoid this issue.
- LiveSplit and wsplit will not split correctly if you are holding shift, ctrl, or alt when a match occurs.
- Numlock on keys are linked to numlock-off keys. For example, if you set your reset hotkey to 2, you can hit arrow down and it will reset and vice versa.

## Credits 
### Original project
- https://github.com/harupy/ for the snipping tool code that I used to integrate into the autosplitter.
- [amaringos](https://twitter.com/amaringos) for the icon.
- [ZanasoBayncuh](https://twitter.com/ZanasoBayncuh) for motivating me to start this project back up and for all of the time spent testing and suggesting improvements.
- Created by [Toufool](https://twitter.com/Toufool) and [Faschz](https://twitter.com/faschz).

### Loading time removal feature
 - Robin Cherix (zuki)