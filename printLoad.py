import time
import timeit

def count_letter(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

def Write_str():
    text = input("Text: ")

    aplhpbet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","q","p","r","s","t","u","v","y","z","w","x"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","Q","P","R","S","T","U","V","Y","Z","W","X","!",".",",","?","0","1","2","3","4","5","6","7","8","9","░"]
    output = [None] * len(text)
    text_arr = []
    count = 0
    for char in text:
        text_arr.append(char)

    for i in range(len(text_arr)):
        for j in range(len(aplhpbet)):       
            if text_arr[i] == aplhpbet[j]:
                output[i] = aplhpbet[j]
                break
            else:
                output[i] = aplhpbet[j]

            output_str = "".join(map(str,filter(lambda x: x is not None, output)))
            print(output_str)

            time.sleep(0.000001)    

    output_str = "".join(map(str,filter(lambda x: x is not None, output)))
    print(output_str)
    print(f"Unkown Character Count: {count_letter(output_str,'░')}")
    time.sleep(1)
    print()
    print()
    print()
    print()
    print()
    
while True:
    elapsed_time = timeit.timeit(Write_str, number=1)
    print(f"Elapsed time: {elapsed_time} seconds")