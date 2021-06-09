# Clump Feature Extraction Tool
These are a set of small scripts to clump feature extraction which are used in the reasearch manuscript titlted "Machine learning approach for discrimination of genotypes based on bright-field cellular images."

## Requirements
- These scripts are run on Windows 10 but I believe that making them run on other OS is an easy task.
- Python version 3.8.8 is used to execute the scripts but they do not use any version specific features inside.
- Java (JRE) version 1.8.0_291 is used. Please make your PATH environmental variable contain java command path.
- ImageJ version 1.53h is used.
- [LPIXEL plug-in](https://lpixel.net/products/lpixel-imagej-plugins/) particularly LPX Feature Lpx296 is used.
- Nuclear cropped bright-field images which are available as supplimental files.

## How to run
- Make a directory as a place to store and run the scripts. Let us represent it `$WORK'.
- Let your working directory $WORK.
- Copy the scripts to $WORK.
- Copy the nuclear images under $WORK and extract them.
- They should be stored $WORK/D2_Additional_file_3_SupDataS1/nuclear-\*/\*.tif
- Run run.BAT
- You will find D2_Additional_file_5_SupDataS3.txt under $WORK.

## LICENSE: [The Unlicense](https://opensource.org/licenses/unlicense)
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

