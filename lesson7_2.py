import tools


def main():             #創建main function記憶體區塊,main    
    while(True):
        tools.PlayGame()
        PlayAgain = input("您還要繼續嗎(y,n)?")
        if PlayAgain == 'n':
            break
    
    print("遊戲結束")
    
if __name__=="__main__":
    main() #執行main function呼叫