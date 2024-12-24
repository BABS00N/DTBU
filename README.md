# <ins>D</ins>ownload <ins>t</ins>ext <ins>b</ins>u <ins>U</ins>RL from RanobeLib
The program downloads text, images and chapter titles from the RanobeLib website and writes them into an html page.
## Content
- **chromedriver-win64/** - The [chromedriver](https://github.com/jsnjack/chromedriver/releases/tag/v131.0.6778.204) is located here, which the DTBU-program uses to load html pages. Chromedriver version is 131.0.6778.204.
- **DTBU.py** - A program that downloads web pages, parses them, and extracts text from them.
## Usage
0. Download Google Chrome version 131.0.6778.205. (I used this version. It should work on every 131.* version). Perhaps this will work in future versions.
1. Run the **DTBU.py** file
2. Enter the **link** to the page that will start the download.
3. Enter the **name** of the file in which the result of the program will be written.
4. Specify the **number of pages** (integer), including the start page, to download. You can specify a number greater than this, then the program will simply download all the pages from the initial one (which you specified) to the last one available.
5. Next, I simply open the resulting page, **select all the text** from it, put it in **MS Word** and then put it in the e-reader that I use.
## Life hacks
- Since the final file is not overwritten, but supplemented, you can simply specify the same file name when loading again and, as a link to the page, indicate the one on which the code stopped.
- You can download different version of  [chromedriver](https://github.com/jsnjack/chromedriver), which will suit your chrome.

### P.s.s. Perhaps in the future I'll update this program.