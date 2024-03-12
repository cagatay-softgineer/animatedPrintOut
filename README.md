# animatedPrintOut


 # Character Counter 
  This is a simple Python program that counts occurrences of each character in a given text input. It also identifies and counts unknown characters. 
  ## Usage 
  1. Clone this repository: 
     ```bash -
     git clone <repository-url> -
     ``` 
  2. Navigate to the directory: 
     ```bash -
     cd <repository-folder> -
     ``` 
  3. Run the script: 
     ```bash -
     python character_counter.py -
     ``` 
  4. Enter the text when prompted. 
  ## Example 
  Suppose you have the following text: 
  ``` -
  Hello, World! -
  ``` 
  The program will output: 
  ``` -
  Text: Hello, World! -
  H -
  He -
  Hel -
  Hell -
  Hello -
  Hello, -
  Hello,  -
  Hello, W -
  Hello, Wo -
  Hello, Wor -
  Hello, Worl -
  Hello, World -
  Hello, World! -
  Unkown Character Count: 0 -
  ``` 
  ## Notes 
  - The program accepts alphabets (both lowercase and uppercase), digits, spaces, and some special characters like '.', '!', '?', etc. -
  - It identifies unknown characters with '░' and counts them separately.
