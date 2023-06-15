#*** 紫微斗數排命盤 ***
# -*- coding: utf-8 -*-
from tkinter import Tk
from tkinter.ttk import* #Frame, Style
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import *
import datetime
import clander_cc
import tkinter.font as tkFont
import copy
import sxtwl
import pyscreenshot as ImageGrab
from tkinter import messagebox
def show_result(result_data):   #顯示宮位主星說明
    print(result_data)
    return 0

def fate_palace(palace_name):   #說明十二宮的特質及用法
    root_palace = Tk()
    screenwidth = root_palace.winfo_screenwidth()
    screenheight = root_palace.winfo_screenheight()
    w_win = 800
    h_win = 300
    x_offset = (screenwidth - w_win) / 2
    y_offset = ((screenheight - h_win) / 2)
    root_palace.title("十二宮說明")
    root_palace.geometry("%dx%d+%d-%d" %(w_win,h_win,x_offset,y_offset))

    style = Style()
    style.theme_use("alt")
    fontStyle = tkFont.Font(family="標楷體", size=20)#Keiu 16
    #*********************** 基本資料 ****************************
    text= tk.Text(root_palace,height=12)
    text.configure(font=fontStyle)
    text.pack(fill=BOTH,padx=5)#,expand=True,pady=10
    if palace_name == '命宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"什麼樣的人(類似太陽星座)\n")
        text.insert(END,"個性、能力、智慧、價值觀、態度、特質、長相。\n")
        text.insert(END,"自身個性與能力特質，影響十二宮。\n")
    elif palace_name == '兄弟宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"同性別兄弟姊妹。\n")
        text.insert(END,"代表媽媽(父宮的夫妻宮)。\n")
        text.insert(END,"岳父、公公(夫妻的父母宮)。\n")
        text.insert(END,"與兄弟姊妹的對待態度，母親。\n")
    elif palace_name == '夫妻宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"對感情的態度看法(本命盤)。\n")
        text.insert(END,"喜歡什麼類型的人(本命盤)。\n")
        text.insert(END,"期待的感情狀況。\n")
        text.insert(END,"感情價值觀，對象的選擇與喜好。\n")
    elif palace_name == '子女宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"對小孩的養育態度。\n")
        text.insert(END,"小孩是哪一型的人。\n")
        text.insert(END,"有無子息命、性生活(財庫)、婆婆、岳母、食慾。\n")
        text.insert(END,"對子女的態度，對性的態度。\n")
    elif palace_name == '財帛宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"用錢的態度。\n")
        text.insert(END,"理財態度及方式。\n")
        text.insert(END,"對錢的看法。\n")
        text.insert(END,"對錢財的態度。\n")
    elif palace_name == '疾惡宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"身體狀態。\n")
        text.insert(END,"外型、長相、體力、體能。\n")
        text.insert(END,"體型、外型、遺傳。\n")
    elif palace_name == '遷移宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"在外別人對我的看法。\n")
        text.insert(END,"在外的表現。\n")
        text.insert(END,"內心世界。\n")
        text.insert(END,"個人在外的展現，希望外人對自己的看法，內心世界的想法。\n")
    elif palace_name == '僕役宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"平輩關係(不論年紀)。\n")
        text.insert(END,"(EX業主或客人關係))。\n")
        text.insert(END,"交友態度，各類平輩關係。\n")
    elif palace_name == '官祿宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"工作態度、狀況。\n")
        text.insert(END,"喜歡的工作類型。\n")
        text.insert(END,"跟上司關係(看小限或太歲盤)。\n")
        text.insert(END,"學業與工作態度、喜好，人生價值的追求。\n")
    elif palace_name == '田宅宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"出生的地方(本命盤)。\n")
        text.insert(END,"居住環境、家世背景、與家人關係、合夥人(事業的兄弟宮)(財庫)。\n")
        text.insert(END,"家世背景、財庫、家人。\n")
    elif palace_name == '福德宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"過世的前10-15年。\n")
        text.insert(END,"來財的方式、品味、靈魂精神、\n")
        text.insert(END,"有無福氣、前世修行、祖上有無積德。\n")
        text.insert(END,"福氣，祖上，精神狀態，靈魂。\n")
    elif palace_name == '父母宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"代表爸爸(本命盤)。\n")
        text.insert(END,"扶養你的人。\n")
        text.insert(END,"父親，家世背景，教育環境，長相遺傳。\n")
    elif palace_name == '身宮':
        text.insert(END,palace_name +"\n")
        text.insert(END,"身宮的意義，說的是他所重疊的宮位就是這個人一生追求的價值所在，\n")
        text.insert(END,"而追求的方式則依照身宮內的星曜來解釋。\n")
    elif palace_name == '本命命盤':
        text.insert(END,palace_name +"\n")
        text.insert(END,"是以我們的出生年月日時排出命盤，一出生就定下來，不會再改變。\n")
        text.insert(END,"解開我們一生下來就具備的特質能力、個性，價值觀、長相、家世背景等等。\n")
        text.insert(END,"不能表示現象，只有父母、家世背景這一類一出生就具備的，才能以本命盤解釋。\n")
        text.insert(END,"例如本命夫妻宮只能代表感情態度，不能代表自己的另外一半。\n")
    elif palace_name == '大限命盤':
        text.insert(END,palace_name +"\n")
        text.insert(END,"紫微斗數給了一張地圖告訴我們現在在哪裡?前方有甚麼?這就是所謂的'大限命盤'。\n")
        text.insert(END,"這是依照我們每十年的年歲所設定出來的命盤，以十年為一個大的限制範圍，\n")
        text.insert(END,"所以稱為十年大限命盤，簡稱大限命盤。這裡的十歲用的是實歲，\n")
        text.insert(END,"我們可以用這十年所在的宮位，當成是我們大限命盤的命宮，\n")
        text.insert(END,"而十二宮的相對位置是相同的，依序排出其他十一宮，而形成一張大限的命盤。\n")
        text.insert(END,"這個命盤表示這十年，我們因為自己的個性特質而做的判斷，\n")
        text.insert(END,"也就是我們依照自己的個性特質所產生出來的人生道路，也因此，\n")
        text.insert(END,"大限命盤除了有價值觀等等形而上的心理層面，也有現象的發生，\n")
        text.insert(END,"因為個性會決定命運。例如，我們隨著年紀的增長，面對感情的態度會不同，\n")
        text.insert(END,"所以每個大限的夫妻宮會變化。\n")        
    elif palace_name == '小限命盤':
        text.insert(END,palace_name +"\n")
        text.insert(END,"小限命盤用的就是我們自己的虛歲歲數，當下歲數所在的宮位即是小限命宮。\n")
        text.insert(END,"而小限命宮所重疊本命命盤的宮位，也就是今年最會影響自己的那個宮位。\n")
        text.insert(END,"小限也是依照我們的歲數所定出來一年的時間範疇，\n")
        text.insert(END,"因此也可以說是我們在這一個年歲內的人生態度，也可說在這段時間自己當下的作為，引起的現象發生。\n")
        text.insert(END,"也就是我們可以在這一個年歲內自己做的決定容易在哪裡犯錯。\n")
        text.insert(END,"例如，我們在某一年因為自己對於感情的想法而決定了要結婚。\n")
    elif palace_name == '太歲命盤':
        text.insert(END,palace_name +"\n")
        text.insert(END,"太歲命盤(流年命盤)是依據每年生肖對應的地支那個宮位，即是太歲的命宮。\n")
        text.insert(END,"所以每年每人的太歲(流年)命宮都會一樣，只是對應到自己本命命盤的宮位不同而已。\n")
        text.insert(END,"所以這個時間是大家的時間，也就是--整體環境對我們的影響--。\n")
        text.insert(END,"所以可以看出每年外界環境給我們帶來的風險會在什麼地方。\n")
        text.insert(END,"例如在某一年因為環境外界的影響，讓我們下定決心要分手。\n")
    enter_bt=tk.Button(root_palace, font=fontStyle, text='確定', width = 4, height=1,command=root_palace.destroy)#root_palace.quit
    enter_bt.place(x=350,y=250)
    root_palace.mainloop()
    return

def star_explain(star_name):    #簡易星曜說明
    root_explain = Tk()
    screenwidth = root_explain.winfo_screenwidth()
    screenheight = root_explain.winfo_screenheight()
    w_win = 800
    h_win = 300
    x_offset = (screenwidth - w_win) / 2
    y_offset = ((screenheight - h_win) / 2)
    root_explain.title("星曜說明")
    root_explain.geometry("%dx%d+%d-%d" %(w_win,h_win,x_offset,y_offset))

    style = Style()
    style.theme_use("alt")
    fontStyle = tkFont.Font(family="標楷體", size=20)#Keiu 16
    #*********************** 基本資料 ****************************
    text= tk.Text(root_explain,height=12)
    text.configure(font=fontStyle)
    text.pack(fill=BOTH,padx=5)#,expand=True,pady=10
    if star_name == '紫微星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '天機星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '太陽星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '武曲星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '天同星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '廉貞星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '天府星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '太陰星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '貪狼星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '巨門星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '天相星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '天梁星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '七殺星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '破軍星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '陀羅':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是源自於佛教，永遠無法擺脫的業力糾纏，\n")
        text.insert(END,"就如同陀螺般一直旋轉，是內心不願意放棄的糾結，\n")
        text.insert(END,"也可以是堅持下去原地不動的力量，也有鑽研的意思\n")

        text.insert(END,"命宮\n")
        text.insert(END,"個性糾結拖延，自己的個性為一生最需要努力修正的問題。\n")
        text.insert(END,"兄弟\n")
        text.insert(END,"一生與嬤嬤或者兄弟關係糾纏不休。\n")
        text.insert(END,"需要耐心與努力好好經營與他們的關係。\n")
        text.insert(END,"夫妻\n")
        text.insert(END,"感情問題會是一生最需要努力的問題。\n")
        text.insert(END,"也表示容易在選擇對象上選錯人。\n")
        text.insert(END,"子女\n")
        text.insert(END,"表示子女會是一生的問題所在。\n")
        text.insert(END,"相處上糾結但又在意，會持續的造成煩惱產生。\n")
        text.insert(END,"財帛\n")
        text.insert(END,"財務問題會是一生始終需要去面對與正視的問題。\n")
        text.insert(END,"疾惡\n")
        text.insert(END,"表示身體會有不容易治好且會糾纏很久的疾病。\n")
        text.insert(END,"例如皮膚病。\n")
        text.insert(END,"遷移\n")
        text.insert(END,"自我的內心和在外與人交往是一生糾結的所在，\n")
        text.insert(END,"容易自我懷疑，需要努力建立自信。\n")
        text.insert(END,"僕役\n")
        text.insert(END,"與朋友的交往是一生在意的問題。\n")
        text.insert(END,"也表示朋友容易造成麻煩。\n")
        text.insert(END,"官祿\n")
        text.insert(END,"工作是一生糾結的問題所在。\n")
        text.insert(END,"適合有毅力高專注的工作。\n")
        text.insert(END,"田宅\n")
        text.insert(END,"家人為一生在意糾結的事情。\n")
        text.insert(END,"存錢會有困難。\n")
        text.insert(END,"容易住到有壁癌的房子。\n")
        text.insert(END,"福德\n")
        text.insert(END,"精神靈魂很糾結，最需要學習自我排解。\n")
        text.insert(END,"避免鑽牛角尖，來財方式也是煩惱來源。\n")
        text.insert(END,"父母\n")
        text.insert(END,"一生與父親關係糾纏，既在意又為其所拖累。\n")
        text.insert(END,"是最需要好好經營的關係。\n")
    elif star_name == '擎羊':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是源自於古代塞外胡人蠻族的羊角刀，\n")
        text.insert(END,"象徵著巨大的衝動與破壞力，表示斬斷的力量，\n")
        text.insert(END,"但是也表示了很強大的堅持力量，不動搖、往前衝的固執個性。\n")
    elif star_name == '火星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '鈴星':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")

    elif star_name == '四化星說明':
        text.insert(END,"所謂四化，是紫微斗數中的主星，會依照時空環境不同而產生出四種不同的變化。\n")
        text.insert(END,"在古老的年代，當紫微斗數還是占星學的時候，\n")
        text.insert(END,"利用了時空造成星曜變化的概念設計了這個機制。\n")
        text.insert(END,"也就是透過星座的變動反推出事件的發生。\n")
        text.insert(END,"到了和易經整合的時代，利用這個占星學上的機制，替代原本易經占掛的變動機制，\n")
        text.insert(END,"進而讓我們更能夠掌握事情的變動，因為相對於易經原本的機制，\n")
        text.insert(END,"占星學的概念更加理性有條理且能夠被掌握，因此紫微斗數就用了這個機制，\n")
        text.insert(END,"讓星曜依照宮位環境的不同而造成星曜產生變動，雖然同樣是那一顆星，\n")
        text.insert(END,"但是會因時空變化而出現不同的風貌，這讓紫微斗數有了更豐富的解析能力。\n")
        text.insert(END,"這個星曜因時空不同而產生變化的概念，就是--祿、權、科、忌--四種變化，簡稱四化。\n")

    elif star_name == '化祿':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '化權':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '化科':
        text.insert(END,star_name +"\n")
        text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
        text.insert(END,"視窗部分採用Tkinter模組。\n")
    elif star_name == '化忌':
        text.insert(END,star_name +"\n")
        text.insert(END,"忌就是自己的內心，而忌所在的宮位，就可能是我們自己內心空缺的地方。\n")
        text.insert(END,"因為空缺，自然就希望去彌補或追求他。但是，人往往因為空虛而做錯事情，\n")
        text.insert(END,"因此有忌在的宮位，表示會有許多問題和紛爭，其實就是自己的內心，\n")
        text.insert(END,"在那個部分有空缺，而難以理性地做出好的判斷與決定。，\n")
        text.insert(END,"\n")
        text.insert(END,"命宮\n")
        text.insert(END,"覺得自己本身有空缺，所以這樣的人會努力去填補這空缺。\n")
        text.insert(END,"這樣做對自己比較好。\n")
        text.insert(END,"\n")
        text.insert(END,"兄弟\n")
        text.insert(END,"會對媽媽與兄弟付出，但相處上不是很良好。\n")
        text.insert(END,"\n")
        text.insert(END,"夫妻\n")
        text.insert(END,"對於感情很渴望，重視感情，但容易選錯人。\n")
        text.insert(END,"\n")
        text.insert(END,"子女\n")
        text.insert(END,"會對子女好，不斷地對子女付出。\n")
        text.insert(END,"但是與子女的相處關係不是很順暢。\n")
        text.insert(END,"\n")
        text.insert(END,"財帛\n")
        text.insert(END,"覺得自己缺錢，更會產生賺錢的動力。\n")
        text.insert(END,"\n")
        text.insert(END,"疾惡\n")
        text.insert(END,"表示身體有空缺。\n")
        text.insert(END,"看化忌的星曜，可表示身體容易有某些方面的疾病。\n")
        text.insert(END,"\n")
        text.insert(END,"遷移\n")
        text.insert(END,"覺得內心與外在有空缺，重視自己內心會想往外跑但不一定順利。\n")
        text.insert(END,"\n")
        text.insert(END,"僕役\n")
        text.insert(END,"對於朋友的關係覺得有空缺，所以會重視與朋友的關係，但有時會相處的不好。\n")
        text.insert(END,"\n")
        text.insert(END,"官祿\n")
        text.insert(END,"在工作上有空缺，重視工作成就與表現，會視工作上的拼命三郎。\n")
        text.insert(END,"\n")
        text.insert(END,"田宅\n")
        text.insert(END,"渴望有個家，重視且會對家人好，但是不會處理與家人的關係。\n")
        text.insert(END,"\n")
        text.insert(END,"福德\n")
        text.insert(END,"精神上有空缺不滿足，比較容易透過花錢，去追尋精神上的滿足。\n")
        text.insert(END,"\n")
        text.insert(END,"父母\n")
        text.insert(END,"會對爸爸好，但是不會處理關係，也表示說容易帶有先天上的疾病問題。\n")

    enter_bt=tk.Button(root_explain, font=fontStyle, text='確定', width = 4, height=1,command=root_explain.destroy)#root_explain.quit
    enter_bt.place(x=350,y=250)
    root_explain.mainloop()
    return

def star_character():   #說明星曜的特質
    fpbg ='#F0F0F0'#'lightgreen''#F0F0F0'
    root_character = Tk()
    screenwidth = root_character.winfo_screenwidth()
    screenheight = root_character.winfo_screenheight()
    w_win = 1080
    h_win = 480
    x_offset = (screenwidth - w_win) / 2
    y_offset = ((screenheight - h_win) / 2)
    root_character.title("星曜特質")
    root_character.geometry("%dx%d+%d-%d" %(w_win,h_win,x_offset,y_offset))
    root_character.resizable(False, False)
    style = Style()
    style.theme_use("alt")
    fontStyle = tkFont.Font(family="標楷體", size=16)
    character_value=[['星曜名稱', '陰陽五行', '化氣','喜會' ,'忌會'],
                     ['紫微', '陰土', '尊','昌曲、左右、魁鉞' ,'煞忌'],
                     ['天機', '陰木', '善','昌曲、左右、魁鉞' ,'空亡、煞'],
                     ['太陽', '陽火', '貴','祿存、三台、八座' ,'空、落陷'],
                     ['武曲', '陰金', '財','權祿、昌曲、貪狼' ,'破、殺、火'],
                     ['天同', '陽水', '福','左右、昌曲' ,'空亡、煞'],
                     ['廉貞', '陰火', '囚','左右、魁鉞、祿存' ,'破、煞、昌曲'],
                     ['天府', '陽土', '權','祿存、昌曲、左右、不怕煞' ,'空亡、六親宮位'],
                     ['太陰', '陰水', '富','旺位、左右' ,'落陷、昌曲、煞忌'],
                     ['貪狼', '陰水/陽木', '桃花','火鈴、左右、魁鉞' ,'落陷、忌、羊陀、昌曲'],
                     ['巨門', '陰水', '暗','祿權、太陽對照' ,'煞忌、落陷'],
                     ['天相', '陽水', '印','紫微、天府、昌曲、左右、魁鉞、祿存' ,'火鈴、天刑、忌、桃花'],
                     ['天梁', '陽土', '蔭','化科、左右、昌曲' ,'化權'],
                     ['七殺', '陰火/陽金', '殺權','祿存、左右、昌曲、魁鉞' ,'煞忌、廉破'],
                     ['破軍', '陰水/陰金', '耗','左右、魁鉞' ,'廉貞、煞忌、昌曲']]
    for i in range(0,15):
        if (i % 2 == 0):
            fpbg =  '#F0F0F0' #'lightgreen''#F0F0F0'
        else:
            fpbg =  'lightgreen' #F0F0F0'
        if i == 0:
            fpbg =  'pink' #'lightgreen''#F0F0F0'
        tk.Label(root_character,text = character_value[i][0],font = fontStyle,width=8,bg=fpbg).place(x=20,y=i*30)
        tk.Label(root_character,text = character_value[i][1],font = fontStyle,width=10,bg=fpbg).place(x=120,y=i*30)
        tk.Label(root_character,text = character_value[i][2],font = fontStyle,width=8,bg=fpbg).place(x=240,y=i*30)
        tk.Label(root_character,text = character_value[i][3],font = fontStyle,width=32,bg=fpbg).place(x=350,y=i*30)
        tk.Label(root_character,text = character_value[i][4],font = fontStyle,width=30,bg=fpbg).place(x=720,y=i*30)
    root_character.mainloop()
    return

def aboutme():  #顯示關於本程式
    root_about = Tk()
    screenwidth = root_about.winfo_screenwidth()
    screenheight = root_about.winfo_screenheight()
    w_win = 800
    h_win = 300
    x_offset = (screenwidth - w_win) / 2
    y_offset = ((screenheight - h_win) / 2)
    root_about.title("關於本程式")
    root_about.geometry("%dx%d+%d-%d" %(w_win,h_win,x_offset,y_offset))

    style = Style()
    style.theme_use("alt")
    fontStyle = tkFont.Font(family="標楷體", size=20)#Keiu 16
    #*********************** 基本資料 ****************************
    text= tk.Text(root_about,height=12)
    text.configure(font=fontStyle)
    text.pack(fill=BOTH,padx=5)#,expand=True,pady=10
    text.insert(END,"這是用Python3.10所寫成的排盤程式。\n")
    text.insert(END,"\n")
    text.insert(END,"視窗部分採用Tkinter模組。\n")
    text.insert(END,"\n")
    text.insert(END,"命盤解析採用大耕老師的說明。\n")
    text.insert(END,"\n")
    text.insert(END,"庚年的四化星也是採用大耕老師的用法。\n")

    enter_bt=tk.Button(root_about, font=fontStyle, text='確定', width = 4, height=1,command=root_about.destroy)#root_about.quit
    enter_bt.place(x=350,y=250)
    root_about.mainloop()

    return

def line34(drawtray,location_kk):
    canvas = drawtray
    canvas.place(x=0,y=0)
    canvas.delete("all")
    if location_kk == "0":
        canvas.create_line(450,153,750,489) #對宮
        canvas.create_line(300,234,750,489)
        canvas.create_line(300,234,900,163)
        canvas.create_line(900,160,750,489)

    elif location_kk == "1":
        canvas.create_line(450,489,750,153) #對宮
        canvas.create_line(450,489,300,160)
        canvas.create_line(300,163,900,234)
        canvas.create_line(900,234,450,489)

    elif location_kk == "2":
        canvas.create_line(280,498,915,153) #對宮
        canvas.create_line(296,498,450,163)
        canvas.create_line(450,163,900,408)
        canvas.create_line(900,408,280,490)
    elif location_kk == "3":
        canvas.create_line(300,408,900,234) #對宮
        canvas.create_line(300,408,750,163)
        canvas.create_line(900,489,750,163)
        canvas.create_line(300,408,900,489)

    elif location_kk == "4":
        canvas.create_line(280,228,900,408) #對宮
        canvas.create_line(300,234,750,489)
        canvas.create_line(300,234,900,163)
        canvas.create_line(900,160,750,489)        
    elif location_kk == "5":
        canvas.create_line(280,153,900,489) #對宮
        canvas.create_line(450,489,300,160)
        canvas.create_line(300,163,900,234)
        canvas.create_line(900,234,450,489)

    elif location_kk == "6":
        canvas.create_line(450,163,750,489) #對宮
        canvas.create_line(296,498,450,163)
        canvas.create_line(450,163,900,408)
        canvas.create_line(900,408,280,490)        
    elif location_kk == "7":
        canvas.create_line(750,163,450,489) #對宮
        canvas.create_line(300,408,750,163)
        canvas.create_line(900,489,750,163)
        canvas.create_line(300,408,900,489)

    elif location_kk == "8":
        canvas.create_line(280,498,915,153) #對宮
        canvas.create_line(300,234,750,489)
        canvas.create_line(300,234,900,163)
        canvas.create_line(900,160,750,489)        
    elif location_kk == "9":
        canvas.create_line(900,234,280,408) #對宮
        canvas.create_line(450,489,300,160)
        canvas.create_line(300,163,900,234)
        canvas.create_line(900,234,450,489)

    elif location_kk == "10":
        canvas.create_line(900,408,280,234) #對宮
        canvas.create_line(296,498,450,163)
        canvas.create_line(450,163,900,408)
        canvas.create_line(900,408,280,490)        
    elif location_kk == "11":
        canvas.create_line(280,153,900,489) #對宮
        canvas.create_line(300,408,750,163)
        canvas.create_line(900,489,750,163)
        canvas.create_line(300,408,900,489)

    return

def fateplat_new(fate_data):    #命盤排列
    #ftype_place = fate_data[4]
    fpbg ='#F0F0F0'#'lightgreen''#F0F0F0'
    #ftype_star_14 = fate_data[6]
    root = Tk()
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    #print(screenwidth)
    #print(screenheight)
    w_win = 1200
    h_win = 652
    w_frame = 300
    h_frame = 163
    x_offset = (screenwidth - w_win) / 2
    y_offset = ((screenheight - h_win) / 2)
    root.title("紫微斗數")
    root.geometry("%dx%d+%d-%d" %(w_win,h_win,x_offset,y_offset))
    root.resizable(False, False)
    style = Style()
    style.theme_use("alt")
    fontStyle = tkFont.Font(family="標楷體", size=14)
    fontStyle_1 = tkFont.Font(family="標楷體", size=20)

    
    #********** 建立下拉式功能表 **********
    menubar = Menu(root)    #建立最上層功能表
    #建立功能表類別物件，和將此功能表類別命名File
    filemenu = Menu(menubar,tearoff=False, font=('Keiu', 14 ))
    menubar.add_cascade(label="檔案",menu=filemenu)
    #File功能表內建立功能表清單
    filemenu.add_command(label="開啟舊檔")#,command=openfile
    filemenu.add_command(label="儲存圖片",command=lambda:save_img(fate_data[16]))#lambda:save_img(fate_data[16])
    filemenu.add_separator()
    filemenu.add_command(label="離開程式",command=root.destroy)

    #建立功能表類別物件，和將此功能表類別命名宮位說明
    plate_place = Menu(menubar, font=('Keiu', 14 ))
    menubar.add_cascade(label="宮位說明",menu=plate_place)
    #About功能表內建立功能表清單    
    plate_place.add_command(label="命宮",command=lambda:fate_palace("命宮"))#,command=lambda:fate_palace(5)
    plate_place.add_command(label="兄弟宮",command=lambda:fate_palace("兄弟宮"))#
    plate_place.add_command(label="夫妻宮",command=lambda:fate_palace("夫妻宮"))#
    plate_place.add_command(label="子女宮",command=lambda:fate_palace("子女宮"))#
    plate_place.add_command(label="財帛宮",command=lambda:fate_palace("財帛宮"))#
    plate_place.add_command(label="疾惡宮",command=lambda:fate_palace("疾惡宮"))#
    plate_place.add_command(label="遷移宮",command=lambda:fate_palace("遷移宮"))#
    plate_place.add_command(label="僕役宮",command=lambda:fate_palace("僕役宮"))#
    plate_place.add_command(label="官祿宮",command=lambda:fate_palace("官祿宮"))#
    plate_place.add_command(label="田宅宮",command=lambda:fate_palace("田宅宮"))#
    plate_place.add_command(label="福德宮",command=lambda:fate_palace("福德宮"))#
    plate_place.add_command(label="父母宮",command=lambda:fate_palace("父母宮"))#
    plate_place.add_command(label="身宮",command=lambda:fate_palace("身宮"))#
    plate_place.add_separator()
    plate_place.add_command(label="本命命盤",command=lambda:fate_palace("本命命盤"))#
    plate_place.add_command(label="大限命盤",command=lambda:fate_palace("大限命盤"))#
    plate_place.add_command(label="小限命盤",command=lambda:fate_palace("小限命盤"))#
    plate_place.add_command(label="太歲命盤",command=lambda:fate_palace("太歲命盤"))#

    #建立功能表類別物件，和將此功能表類別命名星曜說明
    star_14 = Menu(menubar, font=('Keiu', 14 ))
    menubar.add_cascade(label="星曜說明",menu=star_14)
    star_14.add_command(label="星曜特質",command=lambda:star_character())#,command=lambda:notebook
    star_14.add_separator()
    star_14.add_command(label="紫微星",command=lambda:star_explain('紫微星'))#,command=lambda:notebook
    star_14.add_command(label="天機星",command=lambda:star_explain('天機星'))#
    star_14.add_command(label="太陽星",command=lambda:star_explain('太陽星'))#
    star_14.add_command(label="武曲星",command=lambda:star_explain('武曲星'))#
    star_14.add_command(label="天同星",command=lambda:star_explain('天同星'))#
    star_14.add_command(label="廉貞星",command=lambda:star_explain('廉貞星'))#
    star_14.add_command(label="天府星",command=lambda:star_explain('天府星'))#
    star_14.add_command(label="太陰星",command=lambda:star_explain('太陰星'))#
    star_14.add_command(label="貪狼星",command=lambda:star_explain('貪狼星'))#
    star_14.add_command(label="巨門星",command=lambda:star_explain('巨門星'))#
    star_14.add_command(label="天相星",command=lambda:star_explain('天相星'))#
    star_14.add_command(label="天梁星",command=lambda:star_explain('天梁星'))#
    star_14.add_command(label="七殺星",command=lambda:star_explain('七殺星'))#
    star_14.add_command(label="破軍星",command=lambda:star_explain('破軍星'))#
    star_14.add_separator()
    star_14.add_command(label="陀羅",command=lambda:star_explain('陀羅'))#
    star_14.add_command(label="擎羊",command=lambda:star_explain('擎羊'))#
    star_14.add_command(label="火星",command=lambda:star_explain('火星'))#
    star_14.add_command(label="鈴星",command=lambda:star_explain('鈴星'))#

    #建立功能表類別物件，和將此功能表類別命名星曜說明
    star_4fly = Menu(menubar, font=('Keiu', 14 ))
    menubar.add_cascade(label="四化星說明",menu=star_4fly)
    star_4fly.add_command(label="四化星說明",command=lambda:star_explain('四化星說明'))#
    plate_place.add_separator()    
    star_4fly.add_command(label="化祿",command=lambda:star_explain('化祿'))#
    star_4fly.add_command(label="化權",command=lambda:star_explain('化權'))#
    star_4fly.add_command(label="化科",command=lambda:star_explain('化科'))#
    star_4fly.add_command(label="化忌",command=lambda:star_explain('化忌'))#

    #建立功能表類別物件，和將此功能表類別命名About
    helpmenu = Menu(menubar, font=('Keiu', 14 ))
    menubar.add_cascade(label="Help",menu=helpmenu)
    #About功能表內建立功能表清單    
    helpmenu.add_command(label="健康",command=health)#

    helpmenu.add_command(label="關於",command=aboutme)#
    root.config(menu=menubar)
    #********** 建立下拉式功能表 End **********

    #*********************** 基本資料 ****************************
    tk.Label(root, font=fontStyle, text=fate_data[0][0]+'年', width=8, height=1).place(x=800,y=220)
    tk.Label(root, font=fontStyle, text=fate_data[0][1], width=8, height=1).place(x=800,y=240)
    tk.Label(root, font=fontStyle, text=fate_data[0][2]+'日', width=8, height=1).place(x=800,y=260)
    tk.Label(root, font=fontStyle, text=fate_data[0][3]+'時', width=8, height=1).place(x=800,y=280)

    #*********************** 大限流年資料 ****************************
    #s_y = fate_data[7][0]   #大限流年起始數
    b_g = fate_data[7][1]   #男女性別
    p_m = fate_data[7][2]   #本生年天干陰陽
    if b_g == 1:
        temp_b_g = '男'
    else:
        temp_b_g = '女'
    if p_m == 0:
        temp_p_m = '陽'
    else:
        temp_p_m = '陰'        
    #tk.Label(root, text=str(s_y)+' ~ '+str((s_y+10-1)),font=fontStyle, width=8, height=1,bg='yellow').place(x=400,y=340)
    tk.Label(root, text=temp_p_m+temp_b_g,font=fontStyle, width=8, height=1,bg='yellow').place(x=400,y=350)
    tk.Label(root, text=fate_data[16],font=fontStyle_1, width=20, height=1).place(x=445,y=310)
    tk.Label(root, text=fate_data[7][4],font=fontStyle_1, width=20, height=1).place(x=445,y=250)
    tk.Label(root, text='身宮 : '+fate_data[18],font=fontStyle_1, width=10, height=1).place(x=520,y=340)
    tk.Button(root, font=fontStyle_1, text='流年四煞', width=8, height=1, command=lambda:fateplat_4star_data(fate_data)).place(x=750,y=400)#fate_data

    star_a_6 = fate_data[2]    #紫微星系
    star_a_8 = fate_data[3]    #天府星系
    time_start_1 = fate_data[12]    #文昌
    time_start_2 = fate_data[13]    #文曲    
    month_start_1 = fate_data[9]   #左輔
    month_start_2 = fate_data[10]   #右弼

    var_tenken = tk.StringVar()
    timecb = ttk.Combobox(root,textvariable=var_tenken, width=4, height=2, font=fontStyle_1)
    timecb['values'] = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
    timecb.place(x = 310, y = 415)
    timecb.current(0)
    tk.Button(root, font=fontStyle_1, text='四化飛星', width=8, height=1, command=lambda:fly_4star(var_tenken.get(),star_a_6,star_a_8,time_start_1,time_start_2,month_start_1,month_start_2,'noth_4fly')).place(x=400,y=400)#fate_data
    
    #big_limit =[大限起始歲數,男女,出生年陰陽,命宮所在位置,五行局] #fate_data[7]
    
    #*********************** 十二宮繪製布局 ****************************
    fm1 =LabelFrame(root,width=w_frame,height=h_frame,relief="groove")
    fm1.grid(row=3,column=2)#子
    #print(type(fm1))
    tk.Label(fm1, text=fate_data[2][0][0],font=fontStyle, width=4, height=1, bg=fpbg).place(x=0,y=0)  #紫微星系  
    tk.Label(fm1, text=fate_data[2][0][1],font=fontStyle, width=4, height=1, bg=fpbg).place(x=50,y=0) #紫微星系四化
    tk.Label(fm1, text=fate_data[3][0][0],font=fontStyle, width=4, height=1, bg=fpbg).place(x=0,y=25) #天府星系
    tk.Label(fm1, text=fate_data[3][0][1],font=fontStyle, width=4, height=1, bg=fpbg).place(x=50,y=25)    #天府星系四化
    tk.Label(fm1, text=fate_data[12][0][0],font=fontStyle, width=4, height=1, bg=fpbg).place(x=0,y=50)    #文昌星
    tk.Label(fm1, text=fate_data[12][0][1],font=fontStyle, width=4, height=1, bg=fpbg).place(x=50,y=50)   #文昌星四化
    tk.Label(fm1, text=fate_data[13][0][0],font=fontStyle, width=4, height=1, bg=fpbg).place(x=0,y=75)    #文曲星
    tk.Label(fm1, text=fate_data[13][0][1],font=fontStyle, width=4, height=1, bg=fpbg).place(x=50,y=75)   #文曲星四化
    tk.Label(fm1, text=fate_data[9][0][0],font=fontStyle, width=4, height=1, bg=fpbg).place(x=0,y=100)    #左輔星
    tk.Label(fm1, text=fate_data[9][0][1],font=fontStyle, width=4, height=1, bg=fpbg).place(x=50,y=100)   #左輔星四化
    tk.Label(fm1, text=fate_data[10][0][0],font=fontStyle, width=4, height=1, bg=fpbg).place(x=0,y=125)   #右弼星
    tk.Label(fm1, text=fate_data[10][0][1],font=fontStyle, width=4, height=1, bg=fpbg).place(x=50,y=125)   #右弼星四化

    tk.Label(fm1, text=fate_data[19][0],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=30)    #地劫
    tk.Label(fm1, text=fate_data[20][0],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #地空
    tk.Label(fm1, text=fate_data[21][0],font=fontStyle, width=4, height=1,bg=fpbg).place(x=250,y=30)    #紅鸞、天喜

    tk.Label(fm1, text=fate_data[23][0],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #天刑、天馬
    tk.Label(fm1, text=fate_data[24][0],font=fontStyle, width=4, height=1,bg=fpbg).place(x=150,y=60)    #三台
    tk.Label(fm1, text=fate_data[25][0],font=fontStyle, width=4, height=1,bg=fpbg).place(x=200,y=60)    #八座

    tk.Label(fm1, text=fate_data[11][0],font=fontStyle, width=4, height=1, bg=fpbg).place(x=200,y=0)  #火星、鈴星
    tk.Label(fm1, text=fate_data[15][0],font=fontStyle, width=4, height=1, bg=fpbg).place(x=200,y=30) #天魁、天鉞
    tk.Label(fm1, text=fate_data[14][0],font=fontStyle, width=4, height=1, bg=fpbg).place(x=250,y=0) #陀羅、祿存、擎羊

    fm1_sm_li = tk.Label(fm1, text=fate_data[8][0],font=fontStyle, width=4, height=1, bg=fpbg).place(x=200,y=90)    #小限流年
    fm1_bm_li = tk.Label(fm1, text=fate_data[7][5][0], width=8, height=1,bg='lightgreen').place(x=120,y=90)    #大限流年
    fm1_local_t = tk.Label(fm1, text=fate_data[17][0], width=4, height=1,bg='yellow').place(x=250,y=105)    #命盤宮位天干--寅首
    fm1_local = tk.Label(fm1, text='子', width=4, height=1,bg='yellow').place(x=250,y=130)  #命盤宮位地支--固定
    #傳送至解釋宮位程式的資料 1:宮位 2:紫微星系 3:天府星系 9:左輔 10:右弼 
    #                       11:火星，鈴星 14:祿存、陀羅、擎羊 15:天魁、天鉞
    #                       12:文昌 13:文曲
    #                       19:地劫 20:天空 21:紅鸞、天喜
    fm1_result=[fate_data[1][0],fate_data[2][0],fate_data[3][0],
                fate_data[9][0],fate_data[10][0],
                fate_data[11][0],fate_data[14][0],fate_data[15][0],
                fate_data[12][0],fate_data[13][0],
                fate_data[19][0],fate_data[20][0],fate_data[21][0]]    #宮位程式的資料
    fm1_name = tk.Button(fm1, font=fontStyle, text=fate_data[1][0], width=6, height=1, command=lambda:show_result(fm1_result)).place(x=120,y=120)   #命盤宮位名稱

    fm2 =LabelFrame(root,width=w_frame,height=h_frame,relief="groove")
    fm2.grid(row=3,column=1)#丑
    tk.Label(fm2, text=fate_data[2][1][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm2, text=fate_data[2][1][1],font=fontStyle, width=4, height=1).place(x=50,y=0)
    tk.Label(fm2, text=fate_data[3][1][0],font=fontStyle, width=4, height=1).place(x=0,y=25)
    tk.Label(fm2, text=fate_data[3][1][1],font=fontStyle, width=4, height=1,).place(x=50,y=25)
    tk.Label(fm2, text=fate_data[12][1][0],font=fontStyle, width=4, height=1).place(x=0,y=50)
    tk.Label(fm2, text=fate_data[12][1][1],font=fontStyle, width=4, height=1).place(x=50,y=50)
    tk.Label(fm2, text=fate_data[13][1][0],font=fontStyle, width=4, height=1).place(x=0,y=75)
    tk.Label(fm2, text=fate_data[13][1][1],font=fontStyle, width=4, height=1).place(x=50,y=75)
    tk.Label(fm2, text=fate_data[9][1][0],font=fontStyle, width=4, height=1).place(x=0,y=100)
    tk.Label(fm2, text=fate_data[9][1][1],font=fontStyle, width=4, height=1).place(x=50,y=100)
    tk.Label(fm2, text=fate_data[10][1][0],font=fontStyle, width=4, height=1).place(x=0,y=125)
    tk.Label(fm2, text=fate_data[10][1][1],font=fontStyle, width=4, height=1).place(x=50,y=125)

    tk.Label(fm2, text=fate_data[19][1],font=fontStyle, width=4, height=1).place(x=100,y=30)    #地劫
    tk.Label(fm2, text=fate_data[20][1],font=fontStyle, width=4, height=1).place(x=100,y=60)    #地空
    tk.Label(fm2, text=fate_data[21][1],font=fontStyle, width=4, height=1).place(x=250,y=30)    #紅鸞、天喜

    tk.Label(fm2, text=fate_data[23][1],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #天刑、天馬
    tk.Label(fm2, text=fate_data[24][1],font=fontStyle, width=4, height=1,bg=fpbg).place(x=150,y=60)    #三台
    tk.Label(fm2, text=fate_data[25][1],font=fontStyle, width=4, height=1,bg=fpbg).place(x=200,y=60)    #八座

    tk.Label(fm2, text=fate_data[11][1],font=fontStyle, width=4, height=1).place(x=200,y=0)
    tk.Label(fm2, text=fate_data[15][1],font=fontStyle, width=4, height=1).place(x=200,y=30)
    tk.Label(fm2, text=fate_data[14][1],font=fontStyle, width=4, height=1).place(x=250,y=0)

    fm2_sm_li = tk.Label(fm2, text=fate_data[8][1],font=fontStyle, width=4, height=1).place(x=200,y=90)
    fm2_bm_li = tk.Label(fm2, text=fate_data[7][5][1], width=8, height=1,bg='lightgreen').place(x=120,y=90)    #大限流年
    fm2_local_t = tk.Label(fm2, text=fate_data[17][1], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm2_local = tk.Label(fm2, text='丑', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm2_result=[fate_data[1][1],fate_data[2][1],fate_data[3][1]]
    fm2_name = tk.Button(fm2, font=fontStyle, text=fate_data[1][1], width=6, height=1, command=lambda:show_result(fm2_result)).place(x=120,y=120)

    fm3 =LabelFrame(root,width=w_frame,height=h_frame,relief="groove")
    fm3.grid(row=3,column=0)#寅
    tk.Label(fm3, text=fate_data[2][2][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm3, text=fate_data[2][2][1],font=fontStyle, width=4, height=1).place(x=50,y=0)
    tk.Label(fm3, text=fate_data[3][2][0],font=fontStyle, width=4, height=1).place(x=0,y=25)
    tk.Label(fm3, text=fate_data[3][2][1],font=fontStyle, width=4, height=1).place(x=50,y=25)
    tk.Label(fm3, text=fate_data[12][2][0],font=fontStyle, width=4, height=1).place(x=0,y=50)
    tk.Label(fm3, text=fate_data[12][2][1],font=fontStyle, width=4, height=1).place(x=50,y=50)
    tk.Label(fm3, text=fate_data[13][2][0],font=fontStyle, width=4, height=1).place(x=0,y=75)
    tk.Label(fm3, text=fate_data[13][2][1],font=fontStyle, width=4, height=1).place(x=50,y=75)
    tk.Label(fm3, text=fate_data[9][2][0],font=fontStyle, width=4, height=1).place(x=0,y=100)
    tk.Label(fm3, text=fate_data[9][2][1],font=fontStyle, width=4, height=1).place(x=50,y=100)
    tk.Label(fm3, text=fate_data[10][2][0],font=fontStyle, width=4, height=1).place(x=0,y=125)
    tk.Label(fm3, text=fate_data[10][2][1],font=fontStyle, width=4, height=1).place(x=50,y=125)

    tk.Label(fm3, text=fate_data[19][2],font=fontStyle, width=4, height=1).place(x=100,y=30)    #地劫
    tk.Label(fm3, text=fate_data[20][2],font=fontStyle, width=4, height=1).place(x=100,y=60)    #地空
    tk.Label(fm3, text=fate_data[21][2],font=fontStyle, width=4, height=1).place(x=250,y=30)    #紅鸞、天喜

    tk.Label(fm3, text=fate_data[23][2],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #天刑、天馬
    tk.Label(fm3, text=fate_data[24][2],font=fontStyle, width=4, height=1,bg=fpbg).place(x=150,y=60)    #三台
    tk.Label(fm3, text=fate_data[25][2],font=fontStyle, width=4, height=1,bg=fpbg).place(x=200,y=60)    #八座

    tk.Label(fm3, text=fate_data[11][2],font=fontStyle, width=4, height=1).place(x=200,y=0)
    tk.Label(fm3, text=fate_data[15][2],font=fontStyle, width=4, height=1).place(x=200,y=30)
    tk.Label(fm3, text=fate_data[14][2],font=fontStyle, width=4, height=1).place(x=250,y=0)

    fm3_sm_li = tk.Label(fm3, text=fate_data[8][2],font=fontStyle, width=4, height=1).place(x=200,y=90)
    fm3_bm_li = tk.Label(fm3, text=fate_data[7][5][2], width=8, height=1,bg='lightgreen').place(x=120,y=90)    #大限流年
    fm3_local_t = tk.Label(fm3, text=fate_data[17][2], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm3_local = tk.Label(fm3, text='寅', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm3_result=[fate_data[1][2],fate_data[2][2],fate_data[3][2]]
    fm3_name = tk.Button(fm3, font=fontStyle, text=fate_data[1][2], width=6, height=1, command=lambda:show_result(fm3_result)).place(x=120,y=120)

    fm4 =LabelFrame(root,width=w_frame,height=h_frame,relief="groove")
    fm4.grid(row=2,column=0)#卯
    tk.Label(fm4, text=fate_data[2][3][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm4, text=fate_data[2][3][1],font=fontStyle, width=4, height=1).place(x=50,y=0)
    tk.Label(fm4, text=fate_data[3][3][0],font=fontStyle, width=4, height=1).place(x=0,y=25)
    tk.Label(fm4, text=fate_data[3][3][1],font=fontStyle, width=4, height=1).place(x=50,y=25)
    tk.Label(fm4, text=fate_data[12][3][0],font=fontStyle, width=4, height=1).place(x=0,y=50)
    tk.Label(fm4, text=fate_data[12][3][1],font=fontStyle, width=4, height=1).place(x=50,y=50)
    tk.Label(fm4, text=fate_data[13][3][0],font=fontStyle, width=4, height=1).place(x=0,y=75)
    tk.Label(fm4, text=fate_data[13][3][1],font=fontStyle, width=4, height=1).place(x=50,y=75)
    tk.Label(fm4, text=fate_data[9][3][0],font=fontStyle, width=4, height=1).place(x=0,y=100)
    tk.Label(fm4, text=fate_data[9][3][1],font=fontStyle, width=4, height=1).place(x=50,y=100)
    tk.Label(fm4, text=fate_data[10][3][0],font=fontStyle, width=4, height=1).place(x=0,y=125)
    tk.Label(fm4, text=fate_data[10][3][1],font=fontStyle, width=4, height=1).place(x=50,y=125)

    tk.Label(fm4, text=fate_data[19][3],font=fontStyle, width=4, height=1).place(x=100,y=30)    #地劫
    tk.Label(fm4, text=fate_data[20][3],font=fontStyle, width=4, height=1).place(x=100,y=60)    #地空
    tk.Label(fm4, text=fate_data[21][3],font=fontStyle, width=4, height=1).place(x=250,y=30)    #紅鸞、天喜

    tk.Label(fm4, text=fate_data[23][3],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #天刑、天馬
    tk.Label(fm4, text=fate_data[24][3],font=fontStyle, width=4, height=1,bg=fpbg).place(x=150,y=60)    #三台
    tk.Label(fm4, text=fate_data[25][3],font=fontStyle, width=4, height=1,bg=fpbg).place(x=200,y=60)    #八座

    tk.Label(fm4, text=fate_data[11][3],font=fontStyle, width=4, height=1).place(x=200,y=0)
    tk.Label(fm4, text=fate_data[15][3],font=fontStyle, width=4, height=1).place(x=200,y=30)
    tk.Label(fm4, text=fate_data[14][3],font=fontStyle, width=4, height=1).place(x=250,y=0)

    fm4_sm_li = tk.Label(fm4, text=fate_data[8][3],font=fontStyle, width=4, height=1).place(x=200,y=90)
    fm4_bm_li = tk.Label(fm4, text=fate_data[7][5][3], width=8, height=1,bg='lightgreen').place(x=120,y=90)    #大限流年
    fm4_local_t = tk.Label(fm4, text=fate_data[17][3], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm4_local = tk.Label(fm4, text='卯', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm4_result=[fate_data[1][3],fate_data[2][3],fate_data[3][3]]
    fm4_name = tk.Button(fm4, font=fontStyle, text=fate_data[1][3], width=6, height=1, command=lambda:show_result(fm4_result)).place(x=120,y=120)

    fm5 =LabelFrame(root,width=w_frame,height=h_frame,relief="groove")
    fm5.grid(row=1,column=0)#辰
    tk.Label(fm5, text=fate_data[2][4][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm5, text=fate_data[2][4][1],font=fontStyle, width=4, height=1).place(x=50,y=0)
    tk.Label(fm5, text=fate_data[3][4][0],font=fontStyle, width=4, height=1).place(x=0,y=25)
    tk.Label(fm5, text=fate_data[3][4][1],font=fontStyle, width=4, height=1).place(x=50,y=25)
    tk.Label(fm5, text=fate_data[12][4][0],font=fontStyle, width=4, height=1).place(x=0,y=50)
    tk.Label(fm5, text=fate_data[12][4][1],font=fontStyle, width=4, height=1).place(x=50,y=50)
    tk.Label(fm5, text=fate_data[13][4][0],font=fontStyle, width=4, height=1).place(x=0,y=75)
    tk.Label(fm5, text=fate_data[13][4][1],font=fontStyle, width=4, height=1).place(x=50,y=75)
    tk.Label(fm5, text=fate_data[9][4][0],font=fontStyle, width=4, height=1).place(x=0,y=100)
    tk.Label(fm5, text=fate_data[9][4][1],font=fontStyle, width=4, height=1).place(x=50,y=100)
    tk.Label(fm5, text=fate_data[10][4][0],font=fontStyle, width=4, height=1).place(x=0,y=125)
    tk.Label(fm5, text=fate_data[10][4][1],font=fontStyle, width=4, height=1).place(x=50,y=125)

    tk.Label(fm5, text=fate_data[19][4],font=fontStyle, width=4, height=1).place(x=100,y=30)    #地劫
    tk.Label(fm5, text=fate_data[20][4],font=fontStyle, width=4, height=1).place(x=100,y=60)    #地空
    tk.Label(fm5, text=fate_data[21][4],font=fontStyle, width=4, height=1).place(x=250,y=30)    #紅鸞、天喜

    tk.Label(fm5, text=fate_data[23][4],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #天刑、天馬
    tk.Label(fm5, text=fate_data[24][4],font=fontStyle, width=4, height=1,bg=fpbg).place(x=150,y=60)    #三台
    tk.Label(fm5, text=fate_data[25][4],font=fontStyle, width=4, height=1,bg=fpbg).place(x=200,y=60)    #八座

    tk.Label(fm5, text=fate_data[11][4],font=fontStyle, width=4, height=1).place(x=200,y=0)
    tk.Label(fm5, text=fate_data[15][4],font=fontStyle, width=4, height=1).place(x=200,y=30)
    tk.Label(fm5, text=fate_data[14][4],font=fontStyle, width=4, height=1).place(x=250,y=0)

    fm5_sm_li = tk.Label(fm5, text=fate_data[8][4],font=fontStyle, width=4, height=1).place(x=200,y=90)
    fm5_bm_li = tk.Label(fm5, text=fate_data[7][5][4], width=8, height=1,bg='lightgreen').place(x=120,y=90)    #大限流年
    fm5_local_t = tk.Label(fm5, text=fate_data[17][4], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm5_local = tk.Label(fm5, text='辰', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm5_result=[fate_data[1][4],fate_data[2][4],fate_data[3][4]]
    fm5_name = tk.Button(fm5, font=fontStyle, text=fate_data[1][4], width=6, height=1, command=lambda:show_result(fm5_result)).place(x=120,y=120)

    fm6 =LabelFrame(root,width=w_frame,height=h_frame,relief="groove")
    fm6.grid(row=0,column=0)#巳
    tk.Label(fm6, text=fate_data[2][5][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm6, text=fate_data[2][5][1],font=fontStyle, width=4, height=1).place(x=50,y=0)
    tk.Label(fm6, text=fate_data[3][5][0],font=fontStyle, width=4, height=1).place(x=0,y=25)
    tk.Label(fm6, text=fate_data[3][5][1],font=fontStyle, width=4, height=1).place(x=50,y=25)
    tk.Label(fm6, text=fate_data[12][5][0],font=fontStyle, width=4, height=1).place(x=0,y=50)
    tk.Label(fm6, text=fate_data[12][5][1],font=fontStyle, width=4, height=1).place(x=50,y=50)
    tk.Label(fm6, text=fate_data[13][5][0],font=fontStyle, width=4, height=1).place(x=0,y=75)
    tk.Label(fm6, text=fate_data[13][5][1],font=fontStyle, width=4, height=1).place(x=50,y=75)
    tk.Label(fm6, text=fate_data[9][5][0],font=fontStyle, width=4, height=1).place(x=0,y=100)
    tk.Label(fm6, text=fate_data[9][5][1],font=fontStyle, width=4, height=1).place(x=50,y=100)
    tk.Label(fm6, text=fate_data[10][5][0],font=fontStyle, width=4, height=1).place(x=0,y=125)
    tk.Label(fm6, text=fate_data[10][5][1],font=fontStyle, width=4, height=1).place(x=50,y=125)

    tk.Label(fm6, text=fate_data[19][5],font=fontStyle, width=4, height=1).place(x=100,y=30)    #地劫
    tk.Label(fm6, text=fate_data[20][5],font=fontStyle, width=4, height=1).place(x=100,y=60)    #地空
    tk.Label(fm6, text=fate_data[21][5],font=fontStyle, width=4, height=1).place(x=250,y=30)    #紅鸞、天喜

    tk.Label(fm6, text=fate_data[23][5],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #天刑、天馬
    tk.Label(fm6, text=fate_data[24][5],font=fontStyle, width=4, height=1,bg=fpbg).place(x=150,y=60)    #三台
    tk.Label(fm6, text=fate_data[25][5],font=fontStyle, width=4, height=1,bg=fpbg).place(x=200,y=60)    #八座

    tk.Label(fm6, text=fate_data[11][5],font=fontStyle, width=4, height=1).place(x=200,y=0)
    tk.Label(fm6, text=fate_data[15][5],font=fontStyle, width=4, height=1).place(x=200,y=30)
    tk.Label(fm6, text=fate_data[14][5],font=fontStyle, width=4, height=1).place(x=250,y=0)

    fm6_sm_li = tk.Label(fm6, text=fate_data[8][5],font=fontStyle, width=4, height=1).place(x=200,y=90)
    fm6_bm_li = tk.Label(fm6, text=fate_data[7][5][5], width=8, height=1,bg='lightgreen').place(x=120,y=90)    #大限流年
    fm6_local_t = tk.Label(fm6, text=fate_data[17][5], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm6_local = tk.Label(fm6, text='巳', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm6_result=[fate_data[1][5],fate_data[2][5],fate_data[3][5]]
    fm6_name = tk.Button(fm6, font=fontStyle, text=fate_data[1][5], width=6, height=1, command=lambda:show_result(fm6_result)).place(x=120,y=120)

    fm7 =LabelFrame(root,width=w_frame,height=h_frame,relief="groove")
    fm7.grid(row=0,column=1)#午
    tk.Label(fm7, text=fate_data[2][6][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm7, text=fate_data[2][6][1],font=fontStyle, width=4, height=1).place(x=50,y=0)
    tk.Label(fm7, text=fate_data[3][6][0],font=fontStyle, width=4, height=1).place(x=0,y=25)
    tk.Label(fm7, text=fate_data[3][6][1],font=fontStyle, width=4, height=1).place(x=50,y=25)
    tk.Label(fm7, text=fate_data[12][6][0],font=fontStyle, width=4, height=1).place(x=0,y=50)
    tk.Label(fm7, text=fate_data[12][6][1],font=fontStyle, width=4, height=1).place(x=50,y=50)
    tk.Label(fm7, text=fate_data[13][6][0],font=fontStyle, width=4, height=1).place(x=0,y=75)
    tk.Label(fm7, text=fate_data[13][6][1],font=fontStyle, width=4, height=1).place(x=50,y=75)
    tk.Label(fm7, text=fate_data[9][6][0],font=fontStyle, width=4, height=1).place(x=0,y=100)
    tk.Label(fm7, text=fate_data[9][6][1],font=fontStyle, width=4, height=1).place(x=50,y=100)
    tk.Label(fm7, text=fate_data[10][6][0],font=fontStyle, width=4, height=1).place(x=0,y=125)
    tk.Label(fm7, text=fate_data[10][6][1],font=fontStyle, width=4, height=1).place(x=50,y=125)

    tk.Label(fm7, text=fate_data[19][6],font=fontStyle, width=4, height=1).place(x=100,y=30)    #地劫
    tk.Label(fm7, text=fate_data[20][6],font=fontStyle, width=4, height=1).place(x=100,y=60)    #地空
    tk.Label(fm7, text=fate_data[21][6],font=fontStyle, width=4, height=1).place(x=250,y=30)    #紅鸞、天喜

    tk.Label(fm7, text=fate_data[23][6],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #天刑、天馬
    tk.Label(fm7, text=fate_data[24][6],font=fontStyle, width=4, height=1,bg=fpbg).place(x=150,y=60)    #三台
    tk.Label(fm7, text=fate_data[25][6],font=fontStyle, width=4, height=1,bg=fpbg).place(x=200,y=60)    #八座

    tk.Label(fm7, text=fate_data[11][6],font=fontStyle, width=4, height=1).place(x=200,y=0)
    tk.Label(fm7, text=fate_data[15][6],font=fontStyle, width=4, height=1).place(x=200,y=30)
    tk.Label(fm7, text=fate_data[14][6],font=fontStyle, width=4, height=1).place(x=250,y=0)

    fm7_sm_li = tk.Label(fm7, text=fate_data[8][6],font=fontStyle, width=4, height=1).place(x=200,y=90)
    fm7_bm_li = tk.Label(fm7, text=fate_data[7][5][6], width=8, height=1,bg='lightgreen').place(x=120,y=90)    #大限流年
    fm7_local_t = tk.Label(fm7, text=fate_data[17][6], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm7_local = tk.Label(fm7, text='午', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm7_result=[fate_data[1][6],fate_data[2][6],fate_data[3][6]]
    fm7_name = tk.Button(fm7, font=fontStyle, text=fate_data[1][6], width=6, height=1, command=lambda:show_result(fm7_result)).place(x=120,y=120)

    fm8 =LabelFrame(root,width=w_frame,height=h_frame,relief="groove")
    fm8.grid(row=0,column=2)#未
    tk.Label(fm8, text=fate_data[2][7][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm8, text=fate_data[2][7][1],font=fontStyle, width=4, height=1).place(x=50,y=0)
    tk.Label(fm8, text=fate_data[3][7][0],font=fontStyle, width=4, height=1).place(x=0,y=25)
    tk.Label(fm8, text=fate_data[3][7][1],font=fontStyle, width=4, height=1).place(x=50,y=25)
    tk.Label(fm8, text=fate_data[12][7][0],font=fontStyle, width=4, height=1).place(x=0,y=50)
    tk.Label(fm8, text=fate_data[12][7][1],font=fontStyle, width=4, height=1).place(x=50,y=50)
    tk.Label(fm8, text=fate_data[13][7][0],font=fontStyle, width=4, height=1).place(x=0,y=75)
    tk.Label(fm8, text=fate_data[13][7][1],font=fontStyle, width=4, height=1).place(x=50,y=75)
    tk.Label(fm8, text=fate_data[9][7][0],font=fontStyle, width=4, height=1).place(x=0,y=100)
    tk.Label(fm8, text=fate_data[9][7][1],font=fontStyle, width=4, height=1).place(x=50,y=100)
    tk.Label(fm8, text=fate_data[10][7][0],font=fontStyle, width=4, height=1).place(x=0,y=125)
    tk.Label(fm8, text=fate_data[10][7][1],font=fontStyle, width=4, height=1).place(x=50,y=125)

    tk.Label(fm8, text=fate_data[19][7],font=fontStyle, width=4, height=1).place(x=100,y=30)    #地劫
    tk.Label(fm8, text=fate_data[20][7],font=fontStyle, width=4, height=1).place(x=100,y=60)    #地空
    tk.Label(fm8, text=fate_data[21][7],font=fontStyle, width=4, height=1).place(x=250,y=30)    #紅鸞、天喜

    tk.Label(fm8, text=fate_data[23][7],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #天刑、天馬
    tk.Label(fm8, text=fate_data[24][7],font=fontStyle, width=4, height=1,bg=fpbg).place(x=150,y=60)    #三台
    tk.Label(fm8, text=fate_data[25][7],font=fontStyle, width=4, height=1,bg=fpbg).place(x=200,y=60)    #八座

    tk.Label(fm8, text=fate_data[11][7],font=fontStyle, width=4, height=1).place(x=200,y=0)
    tk.Label(fm8, text=fate_data[15][7],font=fontStyle, width=4, height=1).place(x=200,y=30)
    tk.Label(fm8, text=fate_data[14][7],font=fontStyle, width=4, height=1).place(x=250,y=0)

    fm8_sm_li = tk.Label(fm8, text=fate_data[8][7],font=fontStyle, width=4, height=1).place(x=200,y=90)
    fm8_bm_li = tk.Label(fm8, text=fate_data[7][5][7], width=8, height=1,bg='lightgreen').place(x=120,y=90)    #大限流年
    fm8_local_t = tk.Label(fm8, text=fate_data[17][7], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm8_local = tk.Label(fm8, text='未', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm8_result=[fate_data[1][7],fate_data[2][7],fate_data[3][7]]
    fm8_name = tk.Button(fm8, font=fontStyle, text=fate_data[1][7], width=6, height=1, command=lambda:show_result(fm8_result)).place(x=120,y=120)

    fm9 =LabelFrame(root,width=w_frame,height=h_frame,relief="groove")
    fm9.grid(row=0,column=3)#申
    tk.Label(fm9, text=fate_data[2][8][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm9, text=fate_data[2][8][1],font=fontStyle, width=4, height=1).place(x=50,y=0)
    tk.Label(fm9, text=fate_data[3][8][0],font=fontStyle, width=4, height=1).place(x=0,y=25)
    tk.Label(fm9, text=fate_data[3][8][1],font=fontStyle, width=4, height=1).place(x=50,y=25)
    tk.Label(fm9, text=fate_data[12][8][0],font=fontStyle, width=4, height=1).place(x=0,y=50)
    tk.Label(fm9, text=fate_data[12][8][1],font=fontStyle, width=4, height=1).place(x=50,y=50)
    tk.Label(fm9, text=fate_data[13][8][0],font=fontStyle, width=4, height=1).place(x=0,y=75)
    tk.Label(fm9, text=fate_data[13][8][1],font=fontStyle, width=4, height=1).place(x=50,y=75)
    tk.Label(fm9, text=fate_data[9][8][0],font=fontStyle, width=4, height=1).place(x=0,y=100)
    tk.Label(fm9, text=fate_data[9][8][1],font=fontStyle, width=4, height=1).place(x=50,y=100)
    tk.Label(fm9, text=fate_data[10][8][0],font=fontStyle, width=4, height=1).place(x=0,y=125)
    tk.Label(fm9, text=fate_data[10][8][1],font=fontStyle, width=4, height=1).place(x=50,y=125)

    tk.Label(fm9, text=fate_data[19][8],font=fontStyle, width=4, height=1).place(x=100,y=30)    #地劫
    tk.Label(fm9, text=fate_data[20][8],font=fontStyle, width=4, height=1).place(x=100,y=60)    #地空
    tk.Label(fm9, text=fate_data[21][8],font=fontStyle, width=4, height=1).place(x=250,y=30)    #紅鸞、天喜

    tk.Label(fm9, text=fate_data[23][8],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #天刑、天馬
    tk.Label(fm9, text=fate_data[24][8],font=fontStyle, width=4, height=1,bg=fpbg).place(x=150,y=60)    #三台
    tk.Label(fm9, text=fate_data[25][8],font=fontStyle, width=4, height=1,bg=fpbg).place(x=200,y=60)    #八座

    tk.Label(fm9, text=fate_data[11][8],font=fontStyle, width=4, height=1).place(x=200,y=0)
    tk.Label(fm9, text=fate_data[15][8],font=fontStyle, width=4, height=1).place(x=200,y=30)
    tk.Label(fm9, text=fate_data[14][8],font=fontStyle, width=4, height=1).place(x=250,y=0)

    fm9_sm_li = tk.Label(fm9, text=fate_data[8][8],font=fontStyle, width=4, height=1).place(x=200,y=90)
    fm9_bm_li = tk.Label(fm9, text=fate_data[7][5][8], width=8, height=1,bg='lightgreen').place(x=120,y=90)    #大限流年
    fm9_local_t = tk.Label(fm9, text=fate_data[17][8], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm9_local = tk.Label(fm9, text='申', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm9_result=[fate_data[1][8],fate_data[2][8],fate_data[3][8]]
    fm9_name = tk.Button(fm9, font=fontStyle, text=fate_data[1][8], width=6, height=1, command=lambda:show_result(fm9_result)).place(x=120,y=120)

    fm10 =LabelFrame(root,width=w_frame,height=h_frame,relief="groove")
    fm10.grid(row=1,column=3)#酉
    tk.Label(fm10, text=fate_data[2][9][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm10, text=fate_data[2][9][1],font=fontStyle, width=4, height=1).place(x=50,y=0)
    tk.Label(fm10, text=fate_data[3][9][0],font=fontStyle, width=4, height=1).place(x=0,y=25)
    tk.Label(fm10, text=fate_data[3][9][1],font=fontStyle, width=4, height=1).place(x=50,y=25)
    tk.Label(fm10, text=fate_data[12][9][0],font=fontStyle, width=4, height=1).place(x=0,y=50)
    tk.Label(fm10, text=fate_data[12][9][1],font=fontStyle, width=4, height=1).place(x=50,y=50)
    tk.Label(fm10, text=fate_data[13][9][0],font=fontStyle, width=4, height=1).place(x=0,y=75)
    tk.Label(fm10, text=fate_data[13][9][1],font=fontStyle, width=4, height=1).place(x=50,y=75)
    tk.Label(fm10, text=fate_data[9][9][0],font=fontStyle, width=4, height=1).place(x=0,y=100)
    tk.Label(fm10, text=fate_data[9][9][1],font=fontStyle, width=4, height=1).place(x=50,y=100)
    tk.Label(fm10, text=fate_data[10][9][0],font=fontStyle, width=4, height=1).place(x=0,y=125)
    tk.Label(fm10, text=fate_data[10][9][1],font=fontStyle, width=4, height=1).place(x=50,y=125)

    tk.Label(fm10, text=fate_data[19][9],font=fontStyle, width=4, height=1).place(x=100,y=30)    #地劫
    tk.Label(fm10, text=fate_data[20][9],font=fontStyle, width=4, height=1).place(x=100,y=60)    #地空
    tk.Label(fm10, text=fate_data[21][9],font=fontStyle, width=4, height=1).place(x=250,y=30)    #紅鸞、天喜

    tk.Label(fm10, text=fate_data[23][9],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #天刑、天馬
    tk.Label(fm10, text=fate_data[24][9],font=fontStyle, width=4, height=1,bg=fpbg).place(x=150,y=60)    #三台
    tk.Label(fm10, text=fate_data[25][9],font=fontStyle, width=4, height=1,bg=fpbg).place(x=200,y=60)    #八座

    tk.Label(fm10, text=fate_data[11][9],font=fontStyle, width=4, height=1).place(x=200,y=0)
    tk.Label(fm10, text=fate_data[15][9],font=fontStyle, width=4, height=1).place(x=200,y=30)
    tk.Label(fm10, text=fate_data[14][9],font=fontStyle, width=4, height=1).place(x=250,y=0)

    fm10_sm_li = tk.Label(fm10, text=fate_data[8][9],font=fontStyle, width=4, height=1).place(x=200,y=90)
    fm10_bm_li = tk.Label(fm10, text=fate_data[7][5][9], width=8, height=1,bg='lightgreen').place(x=120,y=90)    #大限流年
    fm10_local_t = tk.Label(fm10, text=fate_data[17][9], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm10_local = tk.Label(fm10, text='酉', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm10_result=[fate_data[1][9],fate_data[2][9],fate_data[3][9]]
    fm10_name = tk.Button(fm10, font=fontStyle, text=fate_data[1][9], width=6, height=1, command=lambda:show_result(fm10_result)).place(x=120,y=120)

    fm11 =LabelFrame(root,width=w_frame,height=h_frame,relief="groove")
    fm11.grid(row=2,column=3)#戌
    tk.Label(fm11, text=fate_data[2][10][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm11, text=fate_data[2][10][1],font=fontStyle, width=4, height=1).place(x=50,y=0)
    tk.Label(fm11, text=fate_data[3][10][0],font=fontStyle, width=4, height=1).place(x=0,y=25)
    tk.Label(fm11, text=fate_data[3][10][1],font=fontStyle, width=4, height=1).place(x=50,y=25)
    tk.Label(fm11, text=fate_data[12][10][0],font=fontStyle, width=4, height=1).place(x=0,y=50)
    tk.Label(fm11, text=fate_data[12][10][1],font=fontStyle, width=4, height=1).place(x=50,y=50)
    tk.Label(fm11, text=fate_data[13][10][0],font=fontStyle, width=4, height=1).place(x=0,y=75)
    tk.Label(fm11, text=fate_data[13][10][1],font=fontStyle, width=4, height=1).place(x=50,y=75)
    tk.Label(fm11, text=fate_data[9][10][0],font=fontStyle, width=4, height=1).place(x=0,y=100)
    tk.Label(fm11, text=fate_data[9][10][1],font=fontStyle, width=4, height=1).place(x=50,y=100)
    tk.Label(fm11, text=fate_data[10][10][0],font=fontStyle, width=4, height=1).place(x=0,y=125)
    tk.Label(fm11, text=fate_data[10][10][1],font=fontStyle, width=4, height=1).place(x=50,y=125)

    tk.Label(fm11, text=fate_data[19][10],font=fontStyle, width=4, height=1).place(x=100,y=30)    #地劫
    tk.Label(fm11, text=fate_data[20][10],font=fontStyle, width=4, height=1).place(x=100,y=60)    #地空
    tk.Label(fm11, text=fate_data[21][10],font=fontStyle, width=4, height=1).place(x=250,y=30)    #紅鸞、天喜

    tk.Label(fm11, text=fate_data[23][10],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #天刑、天馬
    tk.Label(fm11, text=fate_data[24][10],font=fontStyle, width=4, height=1,bg=fpbg).place(x=150,y=60)    #三台
    tk.Label(fm11, text=fate_data[25][10],font=fontStyle, width=4, height=1,bg=fpbg).place(x=200,y=60)    #八座

    tk.Label(fm11, text=fate_data[11][10],font=fontStyle, width=4, height=1).place(x=200,y=0)
    tk.Label(fm11, text=fate_data[15][10],font=fontStyle, width=4, height=1).place(x=200,y=30)
    tk.Label(fm11, text=fate_data[14][10],font=fontStyle, width=4, height=1).place(x=250,y=0)

    fm11_sm_li = tk.Label(fm11, text=fate_data[8][10],font=fontStyle, width=4, height=1).place(x=200,y=90)
    fm11_bm_li = tk.Label(fm11, text=fate_data[7][5][10], width=8, height=1,bg='lightgreen').place(x=120,y=90)    #大限流年
    fm11_local_t = tk.Label(fm11, text=fate_data[17][10], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm11_local = tk.Label(fm11, text='戌', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm11_result=[fate_data[1][10],fate_data[2][10],fate_data[3][10]]
    fm11_name = tk.Button(fm11, font=fontStyle, text=fate_data[1][10], width=6, height=1, command=lambda:show_result(fm11_result)).place(x=120,y=120)

    fm12 =LabelFrame(root,width=w_frame,height=h_frame,relief="groove")
    fm12.grid(row=3,column=3)#亥
    tk.Label(fm12, text=fate_data[2][11][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm12, text=fate_data[2][11][1],font=fontStyle, width=4, height=1).place(x=50,y=0)
    tk.Label(fm12, text=fate_data[3][11][0],font=fontStyle, width=4, height=1).place(x=0,y=25)
    tk.Label(fm12, text=fate_data[3][11][1],font=fontStyle, width=4, height=1).place(x=50,y=25)
    tk.Label(fm12, text=fate_data[12][11][0],font=fontStyle, width=4, height=1).place(x=0,y=50)
    tk.Label(fm12, text=fate_data[12][11][1],font=fontStyle, width=4, height=1).place(x=50,y=50)
    tk.Label(fm12, text=fate_data[13][11][0],font=fontStyle, width=4, height=1).place(x=0,y=75)
    tk.Label(fm12, text=fate_data[13][11][1],font=fontStyle, width=4, height=1).place(x=50,y=75)
    tk.Label(fm12, text=fate_data[9][11][0],font=fontStyle, width=4, height=1).place(x=0,y=100)
    tk.Label(fm12, text=fate_data[9][11][1],font=fontStyle, width=4, height=1).place(x=50,y=100)
    tk.Label(fm12, text=fate_data[10][11][0],font=fontStyle, width=4, height=1).place(x=0,y=125)
    tk.Label(fm12, text=fate_data[10][11][1],font=fontStyle, width=4, height=1).place(x=50,y=125)

    tk.Label(fm12, text=fate_data[19][11],font=fontStyle, width=4, height=1).place(x=100,y=30)    #地劫
    tk.Label(fm12, text=fate_data[20][11],font=fontStyle, width=4, height=1).place(x=100,y=60)    #地空
    tk.Label(fm12, text=fate_data[21][11],font=fontStyle, width=4, height=1).place(x=250,y=30)    #紅鸞、天喜

    tk.Label(fm12, text=fate_data[11][11],font=fontStyle, width=4, height=1).place(x=200,y=0)
    tk.Label(fm12, text=fate_data[15][11],font=fontStyle, width=4, height=1).place(x=200,y=30)
    tk.Label(fm12, text=fate_data[14][11],font=fontStyle, width=4, height=1).place(x=250,y=0)

    tk.Label(fm12, text=fate_data[23][11],font=fontStyle, width=4, height=1,bg=fpbg).place(x=100,y=60)    #天刑、天馬
    tk.Label(fm12, text=fate_data[24][11],font=fontStyle, width=4, height=1,bg=fpbg).place(x=150,y=60)    #三台
    tk.Label(fm12, text=fate_data[25][11],font=fontStyle, width=4, height=1,bg=fpbg).place(x=200,y=60)    #八座

    fm12_sm_li = tk.Label(fm12, text=fate_data[8][11],font=fontStyle, width=4, height=1).place(x=200,y=90)
    fm12_bm_li = tk.Label(fm12, text=fate_data[7][5][11], width=8, height=1,bg='lightgreen').place(x=120,y=90)    #大限流年
    fm12_local_t = tk.Label(fm12, text=fate_data[17][11], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm12_local = tk.Label(fm12, text='亥', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm12_result=[fate_data[1][11],fate_data[2][11],fate_data[3][11]]
    fm12_name = tk.Button(fm12, font=fontStyle, text=fate_data[1][11], width=6, height=1, command=lambda:show_result(fm12_result)).place(x=120,y=120)
    #'''
    root.mainloop()
    
    return(1)

def keyin_data(sbase_data): #輸入基本資料生辰八字

    root_input = Tk()
    screenwidth = root_input.winfo_screenwidth()
    screenheight = root_input.winfo_screenheight()
    w_win = 600
    h_win = 400
    #w_frame = 300
    #h_frame = 163
    x_offset = (screenwidth - w_win) / 2
    y_offset = ((screenheight - h_win) / 2)
    root_input.title("生辰年月日時輸入")
    root_input.geometry("%dx%d+%d-%d" %(w_win,h_win,x_offset,y_offset))
    root_input.resizable(False, False)
    style = Style()
    style.theme_use("alt")
    fontStyle = tkFont.Font(family="標楷體", size=20)#Keiu 16
    #*********************** 基本資料 ****************************
    location_x = 10
    location_y = 0

    var_rb = tk.IntVar()
    var_rb.set(sbase_data[2])

    name_L = Label(root_input, font=fontStyle, text="姓  名")#姓名
    name_L.place(x = location_x, y = location_y)
    name_E = Entry(root_input, width=10, font=fontStyle)
    name_E.place(x = location_x+120, y = location_y)
    name_E.insert(0,sbase_data[1])#內定名字

    rbman = Radiobutton(root_input, font=fontStyle, text="男生",variable=var_rb,value=1,command='')
    rbman.place(x = location_x+300, y = location_y)
    rbwoman = Radiobutton(root_input, font=fontStyle, text="女生",variable=var_rb,value=2,command='')
    rbwoman.place(x = location_x+400, y = location_y)

    #***************陽曆生日**************************************************
    var_bd = tk.IntVar()
    var_bd.set(sbase_data[3])

    bd_yl = Radiobutton(root_input, font=fontStyle, text="陽曆生日",variable=var_bd, value=1,command='')#陽曆生日
    bd_yl.place(x = location_x, y = location_y+50)

    var_year = tk.IntVar()
    yearcb = ttk.Combobox(root_input,textvariable=var_year, width=4, height=2,font=fontStyle)
    yearcb['values'] = (list(range(1911, 2024, 1)))
    yearcb.place(x = location_x+50, y = location_y+100)
    yearcb.current(sbase_data[4])
    year_L = Label(root_input, font=fontStyle, text='年', width=4, height=1,bg='lightblue')
    year_L.place(x=location_x+125,y=location_y+100)

    var_month = tk.StringVar()
    monthcb = ttk.Combobox(root_input,textvariable=var_month, width=4, height=2, font=fontStyle)
    monthcb['values'] = ['1','2','3','4','5','6','7','8','9','10','11','12']
    monthcb.place(x = location_x+215, y = location_y+100)
    monthcb.current(sbase_data[5])
    month_L = Label(root_input, font=fontStyle, text='月', width=4, height=1,bg='lightblue')
    month_L.place(x=location_x+290,y=location_y+100)
 
    var_date = tk.IntVar()
    datecb = ttk.Combobox(root_input,textvariable=var_date, width=4, height=2, font=fontStyle)
    datecb['values'] = (list(range(1, 31, 1)))
    datecb.place(x = location_x+380, y = location_y+100)
    datecb.current(sbase_data[6])
    date_L = Label(root_input, font=fontStyle, text='日', width=4, height=1,bg='lightblue')
    date_L.place(x=location_x+455,y=location_y+100)
    #***************農曆生日**************************************************

    bd_ol = Radiobutton(root_input, font=fontStyle, text="農曆生日",variable=var_bd, value=2,command='')#農曆生日
    bd_ol.place(x = location_x, y = location_y+150)

    var_old_year = tk.IntVar()
    yearcb_old = ttk.Combobox(root_input,textvariable=var_old_year, width=4, height=2,font=fontStyle)
    yearcb_old['values'] = (list(range(1911, 2024, 1)))
    yearcb_old.place(x = location_x+50, y = location_y+200)
    yearcb_old.current(sbase_data[7])
    year_old_L = Label(root_input, font=fontStyle, text='年', width=4, height=1,bg='lightblue')
    year_old_L.place(x=location_x+125,y=location_y+200)

    var_old_month = tk.StringVar()
    monthcb_old = ttk.Combobox(root_input,textvariable=var_old_month, width=4, height=2, font=fontStyle)
    monthcb_old['values'] = ['1','2','3','4','5','6','7','8','9','10','11','12']
    monthcb_old.place(x = location_x+215, y = location_y+200)
    monthcb_old.current(sbase_data[8])
    month_old_L = Label(root_input, font=fontStyle, text='月', width=4, height=1,bg='lightblue')
    month_old_L.place(x=location_x+290,y=location_y+200)
 
    var_old_date = tk.IntVar()
    datecb_old = ttk.Combobox(root_input,textvariable=var_old_date, width=4, height=2, font=fontStyle)
    datecb_old['values'] = (list(range(1, 31, 1)))
    datecb_old.place(x = location_x+380, y = location_y+200)
    datecb_old.current(sbase_data[9])
    date_old_L = Label(root_input, font=fontStyle, text='日', width=4, height=1,bg='lightblue')
    date_old_L.place(x=location_x+455,y=location_y+200)

    #**************時辰***************************************************
    bd_time_L = Label(root_input, font=fontStyle, text="出生時辰")#出生時辰
    bd_time_L.place(x = location_x, y = location_y+250)

    var_clock = tk.IntVar()
    clockcb = ttk.Combobox(root_input,textvariable=var_clock, width=4, height=2, font=fontStyle)
    clockcb['values'] = (list(range(0, 24, 1)))
    clockcb.place(x = location_x+50, y = location_y+300)
    clockcb.current(sbase_data[10])
    clock_L = Label(root_input, font=fontStyle, text='點', width=4, height=1,bg='lightblue')
    clock_L.place(x=location_x+125,y=location_y+300)

    var_mintu = tk.IntVar()
    mintucb = ttk.Combobox(root_input,textvariable=var_mintu, width=4, height=2, font=fontStyle)
    mintucb['values'] = (list(range(0, 60, 1)))
    mintucb.place(x = location_x+215, y = location_y+300)
    mintucb.current(sbase_data[11])
    mintu_L = Label(root_input, font=fontStyle, text='分', width=4, height=1,bg='lightblue')
    mintu_L.place(x=location_x+290,y=location_y+300)

    var_time = tk.StringVar()
    timecb = ttk.Combobox(root_input,textvariable=var_time, width=4, height=2, font=fontStyle)
    timecb['values'] = ['','子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
    timecb.place(x = location_x+380, y = location_y+300)
    timecb.current(sbase_data[12])
    time_L = Label(root_input, font=fontStyle, text='時', width=4, height=1,bg='lightblue')
    time_L.place(x=location_x+455,y=location_y+300)
    #**************時辰 end***************************************************
    enter_bt=tk.Button(root_input, font=fontStyle, text='確定', width = 4, height=1,command=root_input.quit)#,command=root_input.destroy
    enter_bt.place(x=location_x+150,y=location_y+350)
    number_E = Entry(root_input, width=10, font=fontStyle)
    number_E.place(x = location_x+400, y = location_y+350)
    number_E.insert(0,sbase_data[0])#內定編號

    #enter_bt=tk.Button(root_input, font=fontStyle, text='儲存', width = 4, height=1,command=lambda:data_save(save_data))#,command=root_input.destroy
    #enter_bt.place(x=location_x+250,y=location_y+350)
    #enter_bt=tk.Button(root_input, font=fontStyle, text='載入', width = 4, height=1,command=lambda:data_load())#,command=root_input.destroy
    #enter_bt.place(x=location_x+350,y=location_y+350)
    #print(temp)

    root_input.mainloop()

    if var_bd.get() == 1:
        base_3 = var_year.get()     #陽曆出生年
        base_4 = var_month.get()    #陽曆出生月
        base_5 = var_date.get()     #陽曆出生日
    else:    
        base_9 = int(var_old_year.get())    #農曆出生年
        base_10 = int(var_old_month.get())  #農曆出生月
        base_11 = int(var_old_date.get())   #農曆出生日

        day = sxtwl.fromLunar(base_9, base_10, base_11) #農曆轉陽曆
        # 公曆的年月日
        base_3=day.getSolarYear()   #陽曆出生年
        base_4=day.getSolarMonth()  #陽曆出生月
        base_5=day.getSolarDay()    #陽曆出生日
        #s = "公曆:%d年%d月%d日" % (day.getSolarYear(), day.getSolarMonth(), day.getSolarDay())
        #print(s)
    base_0 = number_E.get() #編號
    base_1 = name_E.get()   #姓名
    base_2 = var_rb.get()   #男女
    base_6 = var_clock.get()    #幾點
    base_7 = var_mintu.get()    #幾分
    base_8 = var_time.get()     #時辰

    i_base_data = [base_0,base_1,base_2,base_3,base_4,base_5,base_6,base_7,base_8]
    #data_save(save_data)

    #********** save data **********
    data_0 = number_E.get() #編號
    data_1 = name_E.get() #姓名
    data_2 = var_rb.get() #男女
    data_3 = var_bd.get() #陽曆陰曆
    data_4 = var_year.get() #陽曆年
    data_5 = var_month.get() #陽曆月
    data_6 = var_date.get() #陽曆日
    data_7 = var_clock.get() #小時
    data_8 = var_mintu.get() #分鐘
    data_9 = var_time.get() #時辰
    data_10 = var_old_year.get() #陰曆年
    data_11 = var_old_month.get() #陰曆月
    data_12 = var_old_date.get() #陰曆日

    save_data=[data_0,data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_9,data_10,data_11,data_12]
    data_save(save_data)
    root_input.destroy()

    return i_base_data

#*-----大小限及太歲的火鈴羊陀及祿權科忌運算及排盤----*

def set_4star_limit(year_tenkan,year_dichi,step1_a,f_time): #求大小限及太歲的火鈴羊陀資料
    #*-----安大、小限及流年 火、鈴-----*

    year_dichi  #大小限流年地支
    f_time  #出生時辰
    fl_start =[]  #火星,鈴星

    step11_1 = {'寅':'丑','午':'丑','戌':'丑',
                '申':'寅','子':'寅','辰':'寅',
                '巳':'卯','酉':'卯','丑':'卯',
                '亥':'酉','卯':'酉','未':'酉'}#火星起始
    step11_2 = {'寅':'卯','午':'卯','戌':'卯',
                '申':'戌','子':'戌','辰':'戌',
                '巳':'戌','酉':'戌','丑':'戌',
                '亥':'戌','卯':'戌','未':'戌'}#鈴星起始
    
    temp_F_1 = step11_1[year_dichi]#求出火星起始地支
    temp_F_2 = step1_a[temp_F_1]#求出起始地支的數
    temp_F_3 = step1_a[f_time]#求出出生時的數
    temp_F_4 = (temp_F_2+temp_F_3)%12 #火星的數
    #print(temp_F_4) #火星宮位
    #dichi=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']    #十二地支
    #print(dichi[temp_F_4]) #火星宮位

    temp_L_1 = step11_2[year_dichi]#求出鈴星起始地支
    temp_L_2 = step1_a[temp_L_1]#求出起始地支的數
    temp_L_3 = step1_a[f_time]#求出出生時的數
    temp_L_4 = (temp_L_2+temp_L_3)%12 #鈴星的數
    #print(dichi[temp_L_4]) #鈴星宮位

    for i in range(0,12):
        if i ==temp_F_4:
            fl_start.append('火星')
        else:
            fl_start.append('')
    del fl_start[temp_L_4]
    fl_start.insert(temp_L_4,'鈴星')
    
    #print(time_start)

    #*-----安年大、小限及太歲 羊、陀-----*
    year_tenkan  #大小限流年天干
    yan_tuo = []

    step1_a #十二宮位置
    step12_2 = {'甲':'卯','乙':'辰','丙':'午','丁':'未','戊':'午','己':'未','庚':'酉','辛':'戌','壬':'子','癸':'丑'}#擎羊
    step12_3 = {'甲':'丑','乙':'寅','丙':'辰','丁':'巳','戊':'辰','己':'巳','庚':'未','辛':'申','壬':'戌','癸':'亥'}#陀羅

    temp_cheinyan = step1_a[step12_2[year_tenkan]]  #擎羊
    temp_tuolo = step1_a[step12_3[year_tenkan]]     #陀羅

    for i in range(0,12):
        if i ==temp_cheinyan:
            yan_tuo.append('擎羊')
        elif i ==temp_tuolo:
            yan_tuo.append('陀羅')
        else:
            yan_tuo.append('')

    return(fl_start,yan_tuo)

def fateplat_4star(Ly4star_data):   #大小限太歲四煞星排盤程式
    lfpbg =  '#F0F0F0'#'lightgreen'
    ftype_place =  Ly4star_data[1]   #大小限流年四煞星排盤資料
    root_4star = Tk()
    screenwidth = root_4star.winfo_screenwidth()
    screenheight = root_4star.winfo_screenheight()
    w_win = 1200
    h_win = 652
    w_frame = 300
    h_frame = 163
    x_offset = (screenwidth - w_win) / 2
    y_offset = ((screenheight - h_win) / 2)
    root_4star.title("大、小限、太歲火鈴羊陀四煞星")
    root_4star.geometry("%dx%d+%d-%d" %(w_win,h_win,x_offset,y_offset))
    root_4star.resizable(False, False)
    #style = Style()
    #style.theme_use("alt")
    #l_fontStyle = tkFont.Font(family="標楷體", size=8)

    drawtray = Canvas(root_4star,width=1200,height=652)   #設定三方四正畫布
    

    #****************** 各流年四化飛星 ***********************
    #'''
    tk.Label(root_4star, text=('大限四化:',Ly4star_data[12][0]), width=25, height=1,bg=lfpbg).place(x=320,y=200)#大限流年四化飛星
    tk.Label(root_4star, text=('小限四化:',Ly4star_data[12][1]), width=25, height=1,bg=lfpbg).place(x=320,y=240)#小限流年四化飛星
    tk.Label(root_4star, text=('太歲四化:',Ly4star_data[12][2]), width=25, height=1,bg=lfpbg).place(x=320,y=280)#太歲流年四化飛星

    tk.Label(root_4star, text='大四', width=6, height=1,bg=lfpbg).place(x=540,y=200)#大限流年四化飛星
    tk.Label(root_4star, text='小四', width=6, height=1,bg=lfpbg).place(x=600,y=200)#大限流年四化飛星
    tk.Label(root_4star, text='太四', width=6, height=1,bg=lfpbg).place(x=660,y=200)#大限流年四化飛星
    tk.Label(root_4star, text='大火鈴', width=6, height=1,bg=lfpbg).place(x=730,y=200)#大限流年火星、鈴星
    tk.Label(root_4star, text='小火鈴', width=6, height=1,bg=lfpbg).place(x=790,y=200)#大限流年火星、鈴星
    tk.Label(root_4star, text='太火鈴', width=6, height=1,bg=lfpbg).place(x=850,y=200)#大限流年火星、鈴星
    tk.Label(root_4star, text='大羊陀', width=6, height=1,bg=lfpbg).place(x=730,y=230)#大限流年擎羊、陀羅
    tk.Label(root_4star, text='小羊陀', width=6, height=1,bg=lfpbg).place(x=790,y=230)#大限流年擎羊、陀羅
    tk.Label(root_4star, text='太羊陀', width=6, height=1,bg=lfpbg).place(x=850,y=230)#大限流年擎羊、陀羅
    tk.Label(root_4star, text='如果沒有小限命宮，則是大小限命宮同宮位', width=40, height=1,bg=lfpbg).place(x=550,y=330)#大限流年擎羊、陀羅
    #'''
    #****************** 流年煞忌十二宮繪製布局 ***********************
    fm1 =LabelFrame(root_4star,width=w_frame,height=h_frame,relief="groove")
    fm1.grid(row=3,column=2)#子
    tk.Label(fm1, text=Ly4star_data[9][0][0][0], width=3, height=1,bg=lfpbg).place(x=0,y=0)#紫微星系
    tk.Label(fm1, text=Ly4star_data[9][1][0][0], width=3, height=1,bg=lfpbg).place(x=0,y=25)#天府星系
    tk.Label(fm1, text=Ly4star_data[9][2][0][0], width=3, height=1,bg=lfpbg).place(x=0,y=50)#文昌
    tk.Label(fm1, text=Ly4star_data[9][3][0][0], width=3, height=1,bg=lfpbg).place(x=0,y=75)#文曲
    tk.Label(fm1, text=Ly4star_data[9][4][0][0], width=3, height=1,bg=lfpbg).place(x=0,y=100)#左輔
    tk.Label(fm1, text=Ly4star_data[9][5][0][0], width=3, height=1,bg=lfpbg).place(x=0,y=125)#右弼

    tk.Label(fm1, text=Ly4star_data[9][0][0][1], width=3, height=1,bg=lfpbg).place(x=35,y=0)#
    tk.Label(fm1, text=Ly4star_data[9][1][0][1], width=3, height=1,bg=lfpbg).place(x=35,y=25)#
    tk.Label(fm1, text=Ly4star_data[9][2][0][1], width=3, height=1,bg=lfpbg).place(x=35,y=50)#
    tk.Label(fm1, text=Ly4star_data[9][3][0][1], width=3, height=1,bg=lfpbg).place(x=35,y=75)#
    tk.Label(fm1, text=Ly4star_data[9][4][0][1], width=3, height=1,bg=lfpbg).place(x=35,y=100)#
    tk.Label(fm1, text=Ly4star_data[9][5][0][1], width=3, height=1,bg=lfpbg).place(x=35,y=125)#

    tk.Label(fm1, text=Ly4star_data[10][0][0][1], width=3, height=1,bg=lfpbg).place(x=70,y=0)#
    tk.Label(fm1, text=Ly4star_data[10][1][0][1], width=3, height=1,bg=lfpbg).place(x=70,y=25)#
    tk.Label(fm1, text=Ly4star_data[10][2][0][1], width=3, height=1,bg=lfpbg).place(x=70,y=50)#
    tk.Label(fm1, text=Ly4star_data[10][3][0][1], width=3, height=1,bg=lfpbg).place(x=70,y=75)#
    tk.Label(fm1, text=Ly4star_data[10][4][0][1], width=3, height=1,bg=lfpbg).place(x=70,y=100)#
    tk.Label(fm1, text=Ly4star_data[10][5][0][1], width=3, height=1,bg=lfpbg).place(x=70,y=125)#

    tk.Label(fm1, text=Ly4star_data[11][0][0][1], width=3, height=1,bg=lfpbg).place(x=105,y=0)#
    tk.Label(fm1, text=Ly4star_data[11][1][0][1], width=3, height=1,bg=lfpbg).place(x=105,y=25)#
    tk.Label(fm1, text=Ly4star_data[11][2][0][1], width=3, height=1,bg=lfpbg).place(x=105,y=50)#
    tk.Label(fm1, text=Ly4star_data[11][3][0][1], width=3, height=1,bg=lfpbg).place(x=105,y=75)#
    tk.Label(fm1, text=Ly4star_data[11][4][0][1], width=3, height=1,bg=lfpbg).place(x=105,y=100)#
    tk.Label(fm1, text=Ly4star_data[11][5][0][1], width=3, height=1,bg=lfpbg).place(x=105,y=125)#

    tk.Label(fm1, text=Ly4star_data[5][0][0], width=3, height=1,bg=lfpbg).place(x=180,y=0)#大限火鈴
    tk.Label(fm1, text=Ly4star_data[5][1][0], width=3, height=1,bg=lfpbg).place(x=180,y=30)#大限羊陀
    tk.Label(fm1, text=Ly4star_data[6][0][0], width=3, height=1,bg=lfpbg).place(x=220,y=0)#小限火鈴
    tk.Label(fm1, text=Ly4star_data[6][1][0], width=3, height=1,bg=lfpbg).place(x=220,y=30)#小限羊陀
    tk.Label(fm1, text=Ly4star_data[7][0][0], width=3, height=1,bg=lfpbg).place(x=260,y=0)#太歲火鈴
    tk.Label(fm1, text=Ly4star_data[7][1][0], width=3, height=1,bg=lfpbg).place(x=260,y=30)#太歲羊陀

    fm1_sm_li = tk.Label(fm1, text=Ly4star_data[3][0], width=4, height=1).place(x=250,y=80)  #小限流年
    fm1_local_t = tk.Label(fm1, text=Ly4star_data[0][0], width=4, height=1,bg='yellow').place(x=250,y=105)  #宫位天干
    fm1_local = tk.Label(fm1, text='子', width=4, height=1,bg='yellow').place(x=250,y=130)  #宫位地支
    fm1_name = tk.Button(fm1, text=Ly4star_data[8][0], width=6, height=1, command = lambda:line34(drawtray,'0')).place(x=180,y=120)    #流年命宮

    fm2 =LabelFrame(root_4star,width=w_frame,height=h_frame,relief="groove")
    fm2.grid(row=3,column=1)#丑
    tk.Label(fm2, text=Ly4star_data[9][0][1][0], width=3, height=1,bg=lfpbg).place(x=0,y=0)#紫微星系
    tk.Label(fm2, text=Ly4star_data[9][1][1][0], width=3, height=1,bg=lfpbg).place(x=0,y=25)#天府星系
    tk.Label(fm2, text=Ly4star_data[9][2][1][0], width=3, height=1,bg=lfpbg).place(x=0,y=50)#文昌
    tk.Label(fm2, text=Ly4star_data[9][3][1][0], width=3, height=1,bg=lfpbg).place(x=0,y=75)#文曲
    tk.Label(fm2, text=Ly4star_data[9][4][1][0], width=3, height=1,bg=lfpbg).place(x=0,y=100)#左輔
    tk.Label(fm2, text=Ly4star_data[9][5][1][0], width=3, height=1,bg=lfpbg).place(x=0,y=125)#右弼

    tk.Label(fm2, text=Ly4star_data[9][0][1][1], width=3, height=1,bg=lfpbg).place(x=35,y=0)#
    tk.Label(fm2, text=Ly4star_data[9][1][1][1], width=3, height=1,bg=lfpbg).place(x=35,y=25)#
    tk.Label(fm2, text=Ly4star_data[9][2][1][1], width=3, height=1,bg=lfpbg).place(x=35,y=50)#
    tk.Label(fm2, text=Ly4star_data[9][3][1][1], width=3, height=1,bg=lfpbg).place(x=35,y=75)#
    tk.Label(fm2, text=Ly4star_data[9][4][1][1], width=3, height=1,bg=lfpbg).place(x=35,y=100)#
    tk.Label(fm2, text=Ly4star_data[9][5][1][1], width=3, height=1,bg=lfpbg).place(x=35,y=125)#

    tk.Label(fm2, text=Ly4star_data[10][0][1][1], width=3, height=1,bg=lfpbg).place(x=70,y=0)#
    tk.Label(fm2, text=Ly4star_data[10][1][1][1], width=3, height=1,bg=lfpbg).place(x=70,y=25)#
    tk.Label(fm2, text=Ly4star_data[10][2][1][1], width=3, height=1,bg=lfpbg).place(x=70,y=50)#
    tk.Label(fm2, text=Ly4star_data[10][3][1][1], width=3, height=1,bg=lfpbg).place(x=70,y=75)#
    tk.Label(fm2, text=Ly4star_data[10][4][1][1], width=3, height=1,bg=lfpbg).place(x=70,y=100)#
    tk.Label(fm2, text=Ly4star_data[10][5][1][1], width=3, height=1,bg=lfpbg).place(x=70,y=125)#

    tk.Label(fm2, text=Ly4star_data[11][0][1][1], width=3, height=1,bg=lfpbg).place(x=105,y=0)#
    tk.Label(fm2, text=Ly4star_data[11][1][1][1], width=3, height=1,bg=lfpbg).place(x=105,y=25)#
    tk.Label(fm2, text=Ly4star_data[11][2][1][1], width=3, height=1,bg=lfpbg).place(x=105,y=50)#
    tk.Label(fm2, text=Ly4star_data[11][3][1][1], width=3, height=1,bg=lfpbg).place(x=105,y=75)#
    tk.Label(fm2, text=Ly4star_data[11][4][1][1], width=3, height=1,bg=lfpbg).place(x=105,y=100)#
    tk.Label(fm2, text=Ly4star_data[11][5][1][1], width=3, height=1,bg=lfpbg).place(x=105,y=125)#

    tk.Label(fm2, text=Ly4star_data[5][0][1], width=3, height=1,bg=lfpbg).place(x=180,y=0)#大限火鈴
    tk.Label(fm2, text=Ly4star_data[5][1][1], width=3, height=1,bg=lfpbg).place(x=180,y=30)#大限羊陀
    tk.Label(fm2, text=Ly4star_data[6][0][1], width=3, height=1,bg=lfpbg).place(x=220,y=0)#小限火鈴
    tk.Label(fm2, text=Ly4star_data[6][1][1], width=3, height=1,bg=lfpbg).place(x=220,y=30)#小限羊陀
    tk.Label(fm2, text=Ly4star_data[7][0][1], width=3, height=1,bg=lfpbg).place(x=260,y=0)#太歲火鈴
    tk.Label(fm2, text=Ly4star_data[7][1][1], width=3, height=1,bg=lfpbg).place(x=260,y=30)#太歲羊陀

    fm2_sm_li = tk.Label(fm2, text=Ly4star_data[3][1], width=4, height=1).place(x=250,y=80)
    fm2_local_t = tk.Label(fm2, text=Ly4star_data[0][1], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm2_local = tk.Label(fm2, text='丑', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm2_name = tk.Button(fm2, text=Ly4star_data[8][1], width=6, height=1, command = lambda:line34(drawtray,'1')).place(x=180,y=120)

    fm3 =LabelFrame(root_4star,width=w_frame,height=h_frame,relief="groove")
    fm3.grid(row=3,column=0)#寅
    tk.Label(fm3, text=Ly4star_data[9][0][2][0], width=3, height=1,bg=lfpbg).place(x=0,y=0)#紫微星系
    tk.Label(fm3, text=Ly4star_data[9][1][2][0], width=3, height=1,bg=lfpbg).place(x=0,y=25)#天府星系
    tk.Label(fm3, text=Ly4star_data[9][2][2][0], width=3, height=1,bg=lfpbg).place(x=0,y=50)#文昌
    tk.Label(fm3, text=Ly4star_data[9][3][2][0], width=3, height=1,bg=lfpbg).place(x=0,y=75)#文曲
    tk.Label(fm3, text=Ly4star_data[9][4][2][0], width=3, height=1,bg=lfpbg).place(x=0,y=100)#左輔
    tk.Label(fm3, text=Ly4star_data[9][5][2][0], width=3, height=1,bg=lfpbg).place(x=0,y=125)#右弼

    tk.Label(fm3, text=Ly4star_data[9][0][2][1], width=3, height=1,bg=lfpbg).place(x=35,y=0)#
    tk.Label(fm3, text=Ly4star_data[9][1][2][1], width=3, height=1,bg=lfpbg).place(x=35,y=25)#
    tk.Label(fm3, text=Ly4star_data[9][2][2][1], width=3, height=1,bg=lfpbg).place(x=35,y=50)#
    tk.Label(fm3, text=Ly4star_data[9][3][2][1], width=3, height=1,bg=lfpbg).place(x=35,y=75)#
    tk.Label(fm3, text=Ly4star_data[9][4][2][1], width=3, height=1,bg=lfpbg).place(x=35,y=100)#
    tk.Label(fm3, text=Ly4star_data[9][5][2][1], width=3, height=1,bg=lfpbg).place(x=35,y=125)#

    tk.Label(fm3, text=Ly4star_data[10][0][2][1], width=3, height=1,bg=lfpbg).place(x=70,y=0)#
    tk.Label(fm3, text=Ly4star_data[10][1][2][1], width=3, height=1,bg=lfpbg).place(x=70,y=25)#
    tk.Label(fm3, text=Ly4star_data[10][2][2][1], width=3, height=1,bg=lfpbg).place(x=70,y=50)#
    tk.Label(fm3, text=Ly4star_data[10][3][2][1], width=3, height=1,bg=lfpbg).place(x=70,y=75)#
    tk.Label(fm3, text=Ly4star_data[10][4][2][1], width=3, height=1,bg=lfpbg).place(x=70,y=100)#
    tk.Label(fm3, text=Ly4star_data[10][5][2][1], width=3, height=1,bg=lfpbg).place(x=70,y=125)#

    tk.Label(fm3, text=Ly4star_data[11][0][2][1], width=3, height=1,bg=lfpbg).place(x=105,y=0)#
    tk.Label(fm3, text=Ly4star_data[11][1][2][1], width=3, height=1,bg=lfpbg).place(x=105,y=25)#
    tk.Label(fm3, text=Ly4star_data[11][2][2][1], width=3, height=1,bg=lfpbg).place(x=105,y=50)#
    tk.Label(fm3, text=Ly4star_data[11][3][2][1], width=3, height=1,bg=lfpbg).place(x=105,y=75)#
    tk.Label(fm3, text=Ly4star_data[11][4][2][1], width=3, height=1,bg=lfpbg).place(x=105,y=100)#
    tk.Label(fm3, text=Ly4star_data[11][5][2][1], width=3, height=1,bg=lfpbg).place(x=105,y=125)#

    tk.Label(fm3, text=Ly4star_data[5][0][2], width=3, height=1,bg=lfpbg).place(x=180,y=0)#大限火鈴
    tk.Label(fm3, text=Ly4star_data[5][1][2], width=3, height=1,bg=lfpbg).place(x=180,y=30)#大限羊陀
    tk.Label(fm3, text=Ly4star_data[6][0][2], width=3, height=1,bg=lfpbg).place(x=220,y=0)#小限火鈴
    tk.Label(fm3, text=Ly4star_data[6][1][2], width=3, height=1,bg=lfpbg).place(x=220,y=30)#小限羊陀
    tk.Label(fm3, text=Ly4star_data[7][0][2], width=3, height=1,bg=lfpbg).place(x=260,y=0)#太歲火鈴
    tk.Label(fm3, text=Ly4star_data[7][1][2], width=3, height=1,bg=lfpbg).place(x=260,y=30)#太歲羊陀

    fm3_sm_li = tk.Label(fm3, text=Ly4star_data[3][2], width=4, height=1).place(x=250,y=80)
    fm3_local_t = tk.Label(fm3, text=Ly4star_data[0][2], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm3_local = tk.Label(fm3, text='寅', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm3_name = tk.Button(fm3, text=Ly4star_data[8][2], width=6, height=1, command = lambda:line34(drawtray,'2')).place(x=180,y=120)

    fm4 =LabelFrame(root_4star,width=w_frame,height=h_frame,relief="groove")
    fm4.grid(row=2,column=0)#卯
    tk.Label(fm4, text=Ly4star_data[9][0][3][0], width=3, height=1,bg=lfpbg).place(x=0,y=0)#紫微星系
    tk.Label(fm4, text=Ly4star_data[9][1][3][0], width=3, height=1,bg=lfpbg).place(x=0,y=25)#天府星系
    tk.Label(fm4, text=Ly4star_data[9][2][3][0], width=3, height=1,bg=lfpbg).place(x=0,y=50)#文昌
    tk.Label(fm4, text=Ly4star_data[9][3][3][0], width=3, height=1,bg=lfpbg).place(x=0,y=75)#文曲
    tk.Label(fm4, text=Ly4star_data[9][4][3][0], width=3, height=1,bg=lfpbg).place(x=0,y=100)#左輔
    tk.Label(fm4, text=Ly4star_data[9][5][3][0], width=3, height=1,bg=lfpbg).place(x=0,y=125)#右弼

    tk.Label(fm4, text=Ly4star_data[9][0][3][1], width=3, height=1,bg=lfpbg).place(x=35,y=0)#
    tk.Label(fm4, text=Ly4star_data[9][1][3][1], width=3, height=1,bg=lfpbg).place(x=35,y=25)#
    tk.Label(fm4, text=Ly4star_data[9][2][3][1], width=3, height=1,bg=lfpbg).place(x=35,y=50)#
    tk.Label(fm4, text=Ly4star_data[9][3][3][1], width=3, height=1,bg=lfpbg).place(x=35,y=75)#
    tk.Label(fm4, text=Ly4star_data[9][4][3][1], width=3, height=1,bg=lfpbg).place(x=35,y=100)#
    tk.Label(fm4, text=Ly4star_data[9][5][3][1], width=3, height=1,bg=lfpbg).place(x=35,y=125)#

    tk.Label(fm4, text=Ly4star_data[10][0][3][1], width=3, height=1,bg=lfpbg).place(x=70,y=0)#
    tk.Label(fm4, text=Ly4star_data[10][1][3][1], width=3, height=1,bg=lfpbg).place(x=70,y=25)#
    tk.Label(fm4, text=Ly4star_data[10][2][3][1], width=3, height=1,bg=lfpbg).place(x=70,y=50)#
    tk.Label(fm4, text=Ly4star_data[10][3][3][1], width=3, height=1,bg=lfpbg).place(x=70,y=75)#
    tk.Label(fm4, text=Ly4star_data[10][4][3][1], width=3, height=1,bg=lfpbg).place(x=70,y=100)#
    tk.Label(fm4, text=Ly4star_data[10][5][3][1], width=3, height=1,bg=lfpbg).place(x=70,y=125)#

    tk.Label(fm4, text=Ly4star_data[11][0][3][1], width=3, height=1,bg=lfpbg).place(x=105,y=0)#
    tk.Label(fm4, text=Ly4star_data[11][1][3][1], width=3, height=1,bg=lfpbg).place(x=105,y=25)#
    tk.Label(fm4, text=Ly4star_data[11][2][3][1], width=3, height=1,bg=lfpbg).place(x=105,y=50)#
    tk.Label(fm4, text=Ly4star_data[11][3][3][1], width=3, height=1,bg=lfpbg).place(x=105,y=75)#
    tk.Label(fm4, text=Ly4star_data[11][4][3][1], width=3, height=1,bg=lfpbg).place(x=105,y=100)#
    tk.Label(fm4, text=Ly4star_data[11][5][3][1], width=3, height=1,bg=lfpbg).place(x=105,y=125)#

    tk.Label(fm4, text=Ly4star_data[5][0][3], width=3, height=1,bg=lfpbg).place(x=180,y=0)#大限火鈴
    tk.Label(fm4, text=Ly4star_data[5][1][3], width=3, height=1,bg=lfpbg).place(x=180,y=30)#大限羊陀
    tk.Label(fm4, text=Ly4star_data[6][0][3], width=3, height=1,bg=lfpbg).place(x=220,y=0)#小限火鈴
    tk.Label(fm4, text=Ly4star_data[6][1][3], width=3, height=1,bg=lfpbg).place(x=220,y=30)#小限羊陀
    tk.Label(fm4, text=Ly4star_data[7][0][3], width=3, height=1,bg=lfpbg).place(x=260,y=0)#太歲火鈴
    tk.Label(fm4, text=Ly4star_data[7][1][3], width=3, height=1,bg=lfpbg).place(x=260,y=30)#太歲羊陀

    fm4_sm_li = tk.Label(fm4, text=Ly4star_data[3][3], width=4, height=1).place(x=250,y=80)
    fm4_local_t = tk.Label(fm4, text=Ly4star_data[0][3], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm4_local = tk.Label(fm4, text='卯', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm4_name = tk.Button(fm4, text=Ly4star_data[8][3], width=6, height=1, command = lambda:line34(drawtray,'3')).place(x=180,y=120)

    fm5 =LabelFrame(root_4star,width=w_frame,height=h_frame,relief="groove")
    fm5.grid(row=1,column=0)#辰
    tk.Label(fm5, text=Ly4star_data[9][0][4][0], width=3, height=1,bg=lfpbg).place(x=0,y=0)#紫微星系
    tk.Label(fm5, text=Ly4star_data[9][1][4][0], width=3, height=1,bg=lfpbg).place(x=0,y=25)#天府星系
    tk.Label(fm5, text=Ly4star_data[9][2][4][0], width=3, height=1,bg=lfpbg).place(x=0,y=50)#文昌
    tk.Label(fm5, text=Ly4star_data[9][3][4][0], width=3, height=1,bg=lfpbg).place(x=0,y=75)#文曲
    tk.Label(fm5, text=Ly4star_data[9][4][4][0], width=3, height=1,bg=lfpbg).place(x=0,y=100)#左輔
    tk.Label(fm5, text=Ly4star_data[9][5][4][0], width=3, height=1,bg=lfpbg).place(x=0,y=125)#右弼

    tk.Label(fm5, text=Ly4star_data[9][0][4][1], width=3, height=1,bg=lfpbg).place(x=35,y=0)#
    tk.Label(fm5, text=Ly4star_data[9][1][4][1], width=3, height=1,bg=lfpbg).place(x=35,y=25)#
    tk.Label(fm5, text=Ly4star_data[9][2][4][1], width=3, height=1,bg=lfpbg).place(x=35,y=50)#
    tk.Label(fm5, text=Ly4star_data[9][3][4][1], width=3, height=1,bg=lfpbg).place(x=35,y=75)#
    tk.Label(fm5, text=Ly4star_data[9][4][4][1], width=3, height=1,bg=lfpbg).place(x=35,y=100)#
    tk.Label(fm5, text=Ly4star_data[9][5][4][1], width=3, height=1,bg=lfpbg).place(x=35,y=125)#

    tk.Label(fm5, text=Ly4star_data[10][0][4][1], width=3, height=1,bg=lfpbg).place(x=70,y=0)#
    tk.Label(fm5, text=Ly4star_data[10][1][4][1], width=3, height=1,bg=lfpbg).place(x=70,y=25)#
    tk.Label(fm5, text=Ly4star_data[10][2][4][1], width=3, height=1,bg=lfpbg).place(x=70,y=50)#
    tk.Label(fm5, text=Ly4star_data[10][3][4][1], width=3, height=1,bg=lfpbg).place(x=70,y=75)#
    tk.Label(fm5, text=Ly4star_data[10][4][4][1], width=3, height=1,bg=lfpbg).place(x=70,y=100)#
    tk.Label(fm5, text=Ly4star_data[10][5][4][1], width=3, height=1,bg=lfpbg).place(x=70,y=125)#

    tk.Label(fm5, text=Ly4star_data[11][0][4][1], width=3, height=1,bg=lfpbg).place(x=105,y=0)#
    tk.Label(fm5, text=Ly4star_data[11][1][4][1], width=3, height=1,bg=lfpbg).place(x=105,y=25)#
    tk.Label(fm5, text=Ly4star_data[11][2][4][1], width=3, height=1,bg=lfpbg).place(x=105,y=50)#
    tk.Label(fm5, text=Ly4star_data[11][3][4][1], width=3, height=1,bg=lfpbg).place(x=105,y=75)#
    tk.Label(fm5, text=Ly4star_data[11][4][4][1], width=3, height=1,bg=lfpbg).place(x=105,y=100)#
    tk.Label(fm5, text=Ly4star_data[11][5][4][1], width=3, height=1,bg=lfpbg).place(x=105,y=125)#

    tk.Label(fm5, text=Ly4star_data[5][0][4], width=3, height=1,bg=lfpbg).place(x=180,y=0)#大限火鈴
    tk.Label(fm5, text=Ly4star_data[5][1][4], width=3, height=1,bg=lfpbg).place(x=180,y=30)#大限羊陀
    tk.Label(fm5, text=Ly4star_data[6][0][4], width=3, height=1,bg=lfpbg).place(x=220,y=0)#小限火鈴
    tk.Label(fm5, text=Ly4star_data[6][1][4], width=3, height=1,bg=lfpbg).place(x=220,y=30)#小限羊陀
    tk.Label(fm5, text=Ly4star_data[7][0][4], width=3, height=1,bg=lfpbg).place(x=260,y=0)#太歲火鈴
    tk.Label(fm5, text=Ly4star_data[7][1][4], width=3, height=1,bg=lfpbg).place(x=260,y=30)#太歲羊陀

    fm5_sm_li = tk.Label(fm5, text=Ly4star_data[3][4], width=4, height=1).place(x=250,y=80)
    fm5_local_t = tk.Label(fm5, text=Ly4star_data[0][4], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm5_local = tk.Label(fm5, text='辰', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm5_name = tk.Button(fm5, text=Ly4star_data[8][4], width=6, height=1, command = lambda:line34(drawtray,'4')).place(x=180,y=120)

    fm6 =LabelFrame(root_4star,width=w_frame,height=h_frame,relief="groove")
    fm6.grid(row=0,column=0)#巳
    tk.Label(fm6, text=Ly4star_data[9][0][5][0], width=3, height=1,bg=lfpbg).place(x=0,y=0)#紫微星系
    tk.Label(fm6, text=Ly4star_data[9][1][5][0], width=3, height=1,bg=lfpbg).place(x=0,y=25)#天府星系
    tk.Label(fm6, text=Ly4star_data[9][2][5][0], width=3, height=1,bg=lfpbg).place(x=0,y=50)#文昌
    tk.Label(fm6, text=Ly4star_data[9][3][5][0], width=3, height=1,bg=lfpbg).place(x=0,y=75)#文曲
    tk.Label(fm6, text=Ly4star_data[9][4][5][0], width=3, height=1,bg=lfpbg).place(x=0,y=100)#左輔
    tk.Label(fm6, text=Ly4star_data[9][5][5][0], width=3, height=1,bg=lfpbg).place(x=0,y=125)#右弼

    tk.Label(fm6, text=Ly4star_data[9][0][5][1], width=3, height=1,bg=lfpbg).place(x=35,y=0)#
    tk.Label(fm6, text=Ly4star_data[9][1][5][1], width=3, height=1,bg=lfpbg).place(x=35,y=25)#
    tk.Label(fm6, text=Ly4star_data[9][2][5][1], width=3, height=1,bg=lfpbg).place(x=35,y=50)#
    tk.Label(fm6, text=Ly4star_data[9][3][5][1], width=3, height=1,bg=lfpbg).place(x=35,y=75)#
    tk.Label(fm6, text=Ly4star_data[9][4][5][1], width=3, height=1,bg=lfpbg).place(x=35,y=100)#
    tk.Label(fm6, text=Ly4star_data[9][5][5][1], width=3, height=1,bg=lfpbg).place(x=35,y=125)#

    tk.Label(fm6, text=Ly4star_data[10][0][5][1], width=3, height=1,bg=lfpbg).place(x=70,y=0)#
    tk.Label(fm6, text=Ly4star_data[10][1][5][1], width=3, height=1,bg=lfpbg).place(x=70,y=25)#
    tk.Label(fm6, text=Ly4star_data[10][2][5][1], width=3, height=1,bg=lfpbg).place(x=70,y=50)#
    tk.Label(fm6, text=Ly4star_data[10][3][5][1], width=3, height=1,bg=lfpbg).place(x=70,y=75)#
    tk.Label(fm6, text=Ly4star_data[10][4][5][1], width=3, height=1,bg=lfpbg).place(x=70,y=100)#
    tk.Label(fm6, text=Ly4star_data[10][5][5][1], width=3, height=1,bg=lfpbg).place(x=70,y=125)#

    tk.Label(fm6, text=Ly4star_data[11][0][5][1], width=3, height=1,bg=lfpbg).place(x=105,y=0)#
    tk.Label(fm6, text=Ly4star_data[11][1][5][1], width=3, height=1,bg=lfpbg).place(x=105,y=25)#
    tk.Label(fm6, text=Ly4star_data[11][2][5][1], width=3, height=1,bg=lfpbg).place(x=105,y=50)#
    tk.Label(fm6, text=Ly4star_data[11][3][5][1], width=3, height=1,bg=lfpbg).place(x=105,y=75)#
    tk.Label(fm6, text=Ly4star_data[11][4][5][1], width=3, height=1,bg=lfpbg).place(x=105,y=100)#
    tk.Label(fm6, text=Ly4star_data[11][5][5][1], width=3, height=1,bg=lfpbg).place(x=105,y=125)#

    tk.Label(fm6, text=Ly4star_data[5][0][5], width=3, height=1,bg=lfpbg).place(x=180,y=0)#大限火鈴
    tk.Label(fm6, text=Ly4star_data[5][1][5], width=3, height=1,bg=lfpbg).place(x=180,y=30)#大限羊陀
    tk.Label(fm6, text=Ly4star_data[6][0][5], width=3, height=1,bg=lfpbg).place(x=220,y=0)#小限火鈴
    tk.Label(fm6, text=Ly4star_data[6][1][5], width=3, height=1,bg=lfpbg).place(x=220,y=30)#小限羊陀
    tk.Label(fm6, text=Ly4star_data[7][0][5], width=3, height=1,bg=lfpbg).place(x=260,y=0)#太歲火鈴
    tk.Label(fm6, text=Ly4star_data[7][1][5], width=3, height=1,bg=lfpbg).place(x=260,y=30)#太歲羊陀

    fm6_sm_li = tk.Label(fm6, text=Ly4star_data[3][5], width=4, height=1).place(x=250,y=80)
    fm6_local_t = tk.Label(fm6, text=Ly4star_data[0][5], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm6_local = tk.Label(fm6, text='巳', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm6_name = tk.Button(fm6, text=Ly4star_data[8][5], width=6, height=1, command = lambda:line34(drawtray,'5')).place(x=180,y=120)

    fm7 =LabelFrame(root_4star,width=w_frame,height=h_frame,relief="groove")
    fm7.grid(row=0,column=1)#午
    tk.Label(fm7, text=Ly4star_data[9][0][6][0], width=3, height=1,bg=lfpbg).place(x=0,y=0)#紫微星系
    tk.Label(fm7, text=Ly4star_data[9][1][6][0], width=3, height=1,bg=lfpbg).place(x=0,y=25)#天府星系
    tk.Label(fm7, text=Ly4star_data[9][2][6][0], width=3, height=1,bg=lfpbg).place(x=0,y=50)#文昌
    tk.Label(fm7, text=Ly4star_data[9][3][6][0], width=3, height=1,bg=lfpbg).place(x=0,y=75)#文曲
    tk.Label(fm7, text=Ly4star_data[9][4][6][0], width=3, height=1,bg=lfpbg).place(x=0,y=100)#左輔
    tk.Label(fm7, text=Ly4star_data[9][5][6][0], width=3, height=1,bg=lfpbg).place(x=0,y=125)#右弼

    tk.Label(fm7, text=Ly4star_data[9][0][6][1], width=3, height=1,bg=lfpbg).place(x=35,y=0)#
    tk.Label(fm7, text=Ly4star_data[9][1][6][1], width=3, height=1,bg=lfpbg).place(x=35,y=25)#
    tk.Label(fm7, text=Ly4star_data[9][2][6][1], width=3, height=1,bg=lfpbg).place(x=35,y=50)#
    tk.Label(fm7, text=Ly4star_data[9][3][6][1], width=3, height=1,bg=lfpbg).place(x=35,y=75)#
    tk.Label(fm7, text=Ly4star_data[9][4][6][1], width=3, height=1,bg=lfpbg).place(x=35,y=100)#
    tk.Label(fm7, text=Ly4star_data[9][5][6][1], width=3, height=1,bg=lfpbg).place(x=35,y=125)#

    tk.Label(fm7, text=Ly4star_data[10][0][6][1], width=3, height=1,bg=lfpbg).place(x=70,y=0)#
    tk.Label(fm7, text=Ly4star_data[10][1][6][1], width=3, height=1,bg=lfpbg).place(x=70,y=25)#
    tk.Label(fm7, text=Ly4star_data[10][2][6][1], width=3, height=1,bg=lfpbg).place(x=70,y=50)#
    tk.Label(fm7, text=Ly4star_data[10][3][6][1], width=3, height=1,bg=lfpbg).place(x=70,y=75)#
    tk.Label(fm7, text=Ly4star_data[10][4][6][1], width=3, height=1,bg=lfpbg).place(x=70,y=100)#
    tk.Label(fm7, text=Ly4star_data[10][5][6][1], width=3, height=1,bg=lfpbg).place(x=70,y=125)#

    tk.Label(fm7, text=Ly4star_data[11][0][6][1], width=3, height=1,bg=lfpbg).place(x=105,y=0)#
    tk.Label(fm7, text=Ly4star_data[11][1][6][1], width=3, height=1,bg=lfpbg).place(x=105,y=25)#
    tk.Label(fm7, text=Ly4star_data[11][2][6][1], width=3, height=1,bg=lfpbg).place(x=105,y=50)#
    tk.Label(fm7, text=Ly4star_data[11][3][6][1], width=3, height=1,bg=lfpbg).place(x=105,y=75)#
    tk.Label(fm7, text=Ly4star_data[11][4][6][1], width=3, height=1,bg=lfpbg).place(x=105,y=100)#
    tk.Label(fm7, text=Ly4star_data[11][5][6][1], width=3, height=1,bg=lfpbg).place(x=105,y=125)#

    tk.Label(fm7, text=Ly4star_data[5][0][6], width=3, height=1,bg=lfpbg).place(x=180,y=0)#大限火鈴
    tk.Label(fm7, text=Ly4star_data[5][1][6], width=3, height=1,bg=lfpbg).place(x=180,y=30)#大限羊陀
    tk.Label(fm7, text=Ly4star_data[6][0][6], width=3, height=1,bg=lfpbg).place(x=220,y=0)#小限火鈴
    tk.Label(fm7, text=Ly4star_data[6][1][6], width=3, height=1,bg=lfpbg).place(x=220,y=30)#小限羊陀
    tk.Label(fm7, text=Ly4star_data[7][0][6], width=3, height=1,bg=lfpbg).place(x=260,y=0)#太歲火鈴
    tk.Label(fm7, text=Ly4star_data[7][1][6], width=3, height=1,bg=lfpbg).place(x=260,y=30)#太歲羊陀

    fm7_sm_li = tk.Label(fm7, text=Ly4star_data[3][6], width=4, height=1).place(x=250,y=80)
    fm7_local_t = tk.Label(fm7, text=Ly4star_data[0][6], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm7_local = tk.Label(fm7, text='午', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm7_name = tk.Button(fm7, text=Ly4star_data[8][6], width=6, height=1, command = lambda:line34(drawtray,'6')).place(x=180,y=120)

    fm8 =LabelFrame(root_4star,width=w_frame,height=h_frame,relief="groove")
    fm8.grid(row=0,column=2)#未
    tk.Label(fm8, text=Ly4star_data[9][0][7][0], width=3, height=1,bg=lfpbg).place(x=0,y=0)#紫微星系
    tk.Label(fm8, text=Ly4star_data[9][1][7][0], width=3, height=1,bg=lfpbg).place(x=0,y=25)#天府星系
    tk.Label(fm8, text=Ly4star_data[9][2][7][0], width=3, height=1,bg=lfpbg).place(x=0,y=50)#文昌
    tk.Label(fm8, text=Ly4star_data[9][3][7][0], width=3, height=1,bg=lfpbg).place(x=0,y=75)#文曲
    tk.Label(fm8, text=Ly4star_data[9][4][7][0], width=3, height=1,bg=lfpbg).place(x=0,y=100)#左輔
    tk.Label(fm8, text=Ly4star_data[9][5][7][0], width=3, height=1,bg=lfpbg).place(x=0,y=125)#右弼

    tk.Label(fm8, text=Ly4star_data[9][0][7][1], width=3, height=1,bg=lfpbg).place(x=35,y=0)#
    tk.Label(fm8, text=Ly4star_data[9][1][7][1], width=3, height=1,bg=lfpbg).place(x=35,y=25)#
    tk.Label(fm8, text=Ly4star_data[9][2][7][1], width=3, height=1,bg=lfpbg).place(x=35,y=50)#
    tk.Label(fm8, text=Ly4star_data[9][3][7][1], width=3, height=1,bg=lfpbg).place(x=35,y=75)#
    tk.Label(fm8, text=Ly4star_data[9][4][7][1], width=3, height=1,bg=lfpbg).place(x=35,y=100)#
    tk.Label(fm8, text=Ly4star_data[9][5][7][1], width=3, height=1,bg=lfpbg).place(x=35,y=125)#

    tk.Label(fm8, text=Ly4star_data[10][0][7][1], width=3, height=1,bg=lfpbg).place(x=70,y=0)#
    tk.Label(fm8, text=Ly4star_data[10][1][7][1], width=3, height=1,bg=lfpbg).place(x=70,y=25)#
    tk.Label(fm8, text=Ly4star_data[10][2][7][1], width=3, height=1,bg=lfpbg).place(x=70,y=50)#
    tk.Label(fm8, text=Ly4star_data[10][3][7][1], width=3, height=1,bg=lfpbg).place(x=70,y=75)#
    tk.Label(fm8, text=Ly4star_data[10][4][7][1], width=3, height=1,bg=lfpbg).place(x=70,y=100)#
    tk.Label(fm8, text=Ly4star_data[10][5][7][1], width=3, height=1,bg=lfpbg).place(x=70,y=125)#

    tk.Label(fm8, text=Ly4star_data[11][0][7][1], width=3, height=1,bg=lfpbg).place(x=105,y=0)#
    tk.Label(fm8, text=Ly4star_data[11][1][7][1], width=3, height=1,bg=lfpbg).place(x=105,y=25)#
    tk.Label(fm8, text=Ly4star_data[11][2][7][1], width=3, height=1,bg=lfpbg).place(x=105,y=50)#
    tk.Label(fm8, text=Ly4star_data[11][3][7][1], width=3, height=1,bg=lfpbg).place(x=105,y=75)#
    tk.Label(fm8, text=Ly4star_data[11][4][7][1], width=3, height=1,bg=lfpbg).place(x=105,y=100)#
    tk.Label(fm8, text=Ly4star_data[11][5][7][1], width=3, height=1,bg=lfpbg).place(x=105,y=125)#

    tk.Label(fm8, text=Ly4star_data[5][0][7], width=3, height=1,bg=lfpbg).place(x=180,y=0)#大限火鈴
    tk.Label(fm8, text=Ly4star_data[5][1][7], width=3, height=1,bg=lfpbg).place(x=180,y=30)#大限羊陀
    tk.Label(fm8, text=Ly4star_data[6][0][7], width=3, height=1,bg=lfpbg).place(x=220,y=0)#小限火鈴
    tk.Label(fm8, text=Ly4star_data[6][1][7], width=3, height=1,bg=lfpbg).place(x=220,y=30)#小限羊陀
    tk.Label(fm8, text=Ly4star_data[7][0][7], width=3, height=1,bg=lfpbg).place(x=260,y=0)#太歲火鈴
    tk.Label(fm8, text=Ly4star_data[7][1][7], width=3, height=1,bg=lfpbg).place(x=260,y=30)#太歲羊陀

    fm8_sm_li = tk.Label(fm8, text=Ly4star_data[3][7], width=4, height=1).place(x=250,y=80)
    fm8_local_t = tk.Label(fm8, text=Ly4star_data[0][7], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm8_local = tk.Label(fm8, text='未', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm8_name = tk.Button(fm8, text=Ly4star_data[8][7], width=6, height=1, command = lambda:line34(drawtray,'7')).place(x=180,y=120)

    fm9 =LabelFrame(root_4star,width=w_frame,height=h_frame,relief="groove")
    fm9.grid(row=0,column=3)#申
    tk.Label(fm9, text=Ly4star_data[9][0][8][0], width=3, height=1,bg=lfpbg).place(x=0,y=0)#紫微星系
    tk.Label(fm9, text=Ly4star_data[9][1][8][0], width=3, height=1,bg=lfpbg).place(x=0,y=25)#天府星系
    tk.Label(fm9, text=Ly4star_data[9][2][8][0], width=3, height=1,bg=lfpbg).place(x=0,y=50)#文昌
    tk.Label(fm9, text=Ly4star_data[9][3][8][0], width=3, height=1,bg=lfpbg).place(x=0,y=75)#文曲
    tk.Label(fm9, text=Ly4star_data[9][4][8][0], width=3, height=1,bg=lfpbg).place(x=0,y=100)#左輔
    tk.Label(fm9, text=Ly4star_data[9][5][8][0], width=3, height=1,bg=lfpbg).place(x=0,y=125)#右弼

    tk.Label(fm9, text=Ly4star_data[9][0][8][1], width=3, height=1,bg=lfpbg).place(x=35,y=0)#
    tk.Label(fm9, text=Ly4star_data[9][1][8][1], width=3, height=1,bg=lfpbg).place(x=35,y=25)#
    tk.Label(fm9, text=Ly4star_data[9][2][8][1], width=3, height=1,bg=lfpbg).place(x=35,y=50)#
    tk.Label(fm9, text=Ly4star_data[9][3][8][1], width=3, height=1,bg=lfpbg).place(x=35,y=75)#
    tk.Label(fm9, text=Ly4star_data[9][4][8][1], width=3, height=1,bg=lfpbg).place(x=35,y=100)#
    tk.Label(fm9, text=Ly4star_data[9][5][8][1], width=3, height=1,bg=lfpbg).place(x=35,y=125)#

    tk.Label(fm9, text=Ly4star_data[10][0][8][1], width=3, height=1,bg=lfpbg).place(x=70,y=0)#
    tk.Label(fm9, text=Ly4star_data[10][1][8][1], width=3, height=1,bg=lfpbg).place(x=70,y=25)#
    tk.Label(fm9, text=Ly4star_data[10][2][8][1], width=3, height=1,bg=lfpbg).place(x=70,y=50)#
    tk.Label(fm9, text=Ly4star_data[10][3][8][1], width=3, height=1,bg=lfpbg).place(x=70,y=75)#
    tk.Label(fm9, text=Ly4star_data[10][4][8][1], width=3, height=1,bg=lfpbg).place(x=70,y=100)#
    tk.Label(fm9, text=Ly4star_data[10][5][8][1], width=3, height=1,bg=lfpbg).place(x=70,y=125)#

    tk.Label(fm9, text=Ly4star_data[11][0][8][1], width=3, height=1,bg=lfpbg).place(x=105,y=0)#
    tk.Label(fm9, text=Ly4star_data[11][1][8][1], width=3, height=1,bg=lfpbg).place(x=105,y=25)#
    tk.Label(fm9, text=Ly4star_data[11][2][8][1], width=3, height=1,bg=lfpbg).place(x=105,y=50)#
    tk.Label(fm9, text=Ly4star_data[11][3][8][1], width=3, height=1,bg=lfpbg).place(x=105,y=75)#
    tk.Label(fm9, text=Ly4star_data[11][4][8][1], width=3, height=1,bg=lfpbg).place(x=105,y=100)#
    tk.Label(fm9, text=Ly4star_data[11][5][8][1], width=3, height=1,bg=lfpbg).place(x=105,y=125)#

    tk.Label(fm9, text=Ly4star_data[5][0][8], width=3, height=1,bg=lfpbg).place(x=180,y=0)#大限火鈴
    tk.Label(fm9, text=Ly4star_data[5][1][8], width=3, height=1,bg=lfpbg).place(x=180,y=30)#大限羊陀
    tk.Label(fm9, text=Ly4star_data[6][0][8], width=3, height=1,bg=lfpbg).place(x=220,y=0)#小限火鈴
    tk.Label(fm9, text=Ly4star_data[6][1][8], width=3, height=1,bg=lfpbg).place(x=220,y=30)#小限羊陀
    tk.Label(fm9, text=Ly4star_data[7][0][8], width=3, height=1,bg=lfpbg).place(x=260,y=0)#太歲火鈴
    tk.Label(fm9, text=Ly4star_data[7][1][8], width=3, height=1,bg=lfpbg).place(x=260,y=30)#太歲羊陀

    fm9_sm_li = tk.Label(fm9, text=Ly4star_data[3][8], width=4, height=1).place(x=250,y=80)
    fm9_local_t = tk.Label(fm9, text=Ly4star_data[0][8], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm9_local = tk.Label(fm9, text='申', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm9_name = tk.Button(fm9, text=Ly4star_data[8][8], width=6, height=1, command = lambda:line34(drawtray,'8')).place(x=180,y=120)

    fm10 =LabelFrame(root_4star,width=w_frame,height=h_frame,relief="groove")
    fm10.grid(row=1,column=3)#酉
    tk.Label(fm10, text=Ly4star_data[9][0][9][0], width=3, height=1,bg=lfpbg).place(x=0,y=0)#紫微星系
    tk.Label(fm10, text=Ly4star_data[9][1][9][0], width=3, height=1,bg=lfpbg).place(x=0,y=25)#天府星系
    tk.Label(fm10, text=Ly4star_data[9][2][9][0], width=3, height=1,bg=lfpbg).place(x=0,y=50)#文昌
    tk.Label(fm10, text=Ly4star_data[9][3][9][0], width=3, height=1,bg=lfpbg).place(x=0,y=75)#文曲
    tk.Label(fm10, text=Ly4star_data[9][4][9][0], width=3, height=1,bg=lfpbg).place(x=0,y=100)#左輔
    tk.Label(fm10, text=Ly4star_data[9][5][9][0], width=3, height=1,bg=lfpbg).place(x=0,y=125)#右弼

    tk.Label(fm10, text=Ly4star_data[9][0][9][1], width=3, height=1,bg=lfpbg).place(x=35,y=0)#
    tk.Label(fm10, text=Ly4star_data[9][1][9][1], width=3, height=1,bg=lfpbg).place(x=35,y=25)#
    tk.Label(fm10, text=Ly4star_data[9][2][9][1], width=3, height=1,bg=lfpbg).place(x=35,y=50)#
    tk.Label(fm10, text=Ly4star_data[9][3][9][1], width=3, height=1,bg=lfpbg).place(x=35,y=75)#
    tk.Label(fm10, text=Ly4star_data[9][4][9][1], width=3, height=1,bg=lfpbg).place(x=35,y=100)#
    tk.Label(fm10, text=Ly4star_data[9][5][9][1], width=3, height=1,bg=lfpbg).place(x=35,y=125)#

    tk.Label(fm10, text=Ly4star_data[10][0][9][1], width=3, height=1,bg=lfpbg).place(x=70,y=0)#
    tk.Label(fm10, text=Ly4star_data[10][1][9][1], width=3, height=1,bg=lfpbg).place(x=70,y=25)#
    tk.Label(fm10, text=Ly4star_data[10][2][9][1], width=3, height=1,bg=lfpbg).place(x=70,y=50)#
    tk.Label(fm10, text=Ly4star_data[10][3][9][1], width=3, height=1,bg=lfpbg).place(x=70,y=75)#
    tk.Label(fm10, text=Ly4star_data[10][4][9][1], width=3, height=1,bg=lfpbg).place(x=70,y=100)#
    tk.Label(fm10, text=Ly4star_data[10][5][9][1], width=3, height=1,bg=lfpbg).place(x=70,y=125)#

    tk.Label(fm10, text=Ly4star_data[11][0][9][1], width=3, height=1,bg=lfpbg).place(x=105,y=0)#
    tk.Label(fm10, text=Ly4star_data[11][1][9][1], width=3, height=1,bg=lfpbg).place(x=105,y=25)#
    tk.Label(fm10, text=Ly4star_data[11][2][9][1], width=3, height=1,bg=lfpbg).place(x=105,y=50)#
    tk.Label(fm10, text=Ly4star_data[11][3][9][1], width=3, height=1,bg=lfpbg).place(x=105,y=75)#
    tk.Label(fm10, text=Ly4star_data[11][4][9][1], width=3, height=1,bg=lfpbg).place(x=105,y=100)#
    tk.Label(fm10, text=Ly4star_data[11][5][9][1], width=3, height=1,bg=lfpbg).place(x=105,y=125)#

    tk.Label(fm10, text=Ly4star_data[5][0][9], width=3, height=1,bg=lfpbg).place(x=180,y=0)#大限火鈴
    tk.Label(fm10, text=Ly4star_data[5][1][9], width=3, height=1,bg=lfpbg).place(x=180,y=30)#大限羊陀
    tk.Label(fm10, text=Ly4star_data[6][0][9], width=3, height=1,bg=lfpbg).place(x=220,y=0)#小限火鈴
    tk.Label(fm10, text=Ly4star_data[6][1][9], width=3, height=1,bg=lfpbg).place(x=220,y=30)#小限羊陀
    tk.Label(fm10, text=Ly4star_data[7][0][9], width=3, height=1,bg=lfpbg).place(x=260,y=0)#太歲火鈴
    tk.Label(fm10, text=Ly4star_data[7][1][9], width=3, height=1,bg=lfpbg).place(x=260,y=30)#太歲羊陀

    fm10_sm_li = tk.Label(fm10, text=Ly4star_data[3][9], width=4, height=1).place(x=250,y=80)
    fm10_local_t = tk.Label(fm10, text=Ly4star_data[0][9], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm10_local = tk.Label(fm10, text='酉', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm10_name = tk.Button(fm10, text=Ly4star_data[8][9], width=6, height=1, command = lambda:line34(drawtray,'9')).place(x=180,y=120)

    fm11 =LabelFrame(root_4star,width=w_frame,height=h_frame,relief="groove")
    fm11.grid(row=2,column=3)#戌
    tk.Label(fm11, text=Ly4star_data[9][0][10][0], width=3, height=1,bg=lfpbg).place(x=0,y=0)#紫微星系
    tk.Label(fm11, text=Ly4star_data[9][1][10][0], width=3, height=1,bg=lfpbg).place(x=0,y=25)#天府星系
    tk.Label(fm11, text=Ly4star_data[9][2][10][0], width=3, height=1,bg=lfpbg).place(x=0,y=50)#文昌
    tk.Label(fm11, text=Ly4star_data[9][3][10][0], width=3, height=1,bg=lfpbg).place(x=0,y=75)#文曲
    tk.Label(fm11, text=Ly4star_data[9][4][10][0], width=3, height=1,bg=lfpbg).place(x=0,y=100)#左輔
    tk.Label(fm11, text=Ly4star_data[9][5][10][0], width=3, height=1,bg=lfpbg).place(x=0,y=125)#右弼

    tk.Label(fm11, text=Ly4star_data[9][0][10][1], width=3, height=1,bg=lfpbg).place(x=35,y=0)#
    tk.Label(fm11, text=Ly4star_data[9][1][10][1], width=3, height=1,bg=lfpbg).place(x=35,y=25)#
    tk.Label(fm11, text=Ly4star_data[9][2][10][1], width=3, height=1,bg=lfpbg).place(x=35,y=50)#
    tk.Label(fm11, text=Ly4star_data[9][3][10][1], width=3, height=1,bg=lfpbg).place(x=35,y=75)#
    tk.Label(fm11, text=Ly4star_data[9][4][10][1], width=3, height=1,bg=lfpbg).place(x=35,y=100)#
    tk.Label(fm11, text=Ly4star_data[9][5][10][1], width=3, height=1,bg=lfpbg).place(x=35,y=125)#

    tk.Label(fm11, text=Ly4star_data[10][0][10][1], width=3, height=1,bg=lfpbg).place(x=70,y=0)#
    tk.Label(fm11, text=Ly4star_data[10][1][10][1], width=3, height=1,bg=lfpbg).place(x=70,y=25)#
    tk.Label(fm11, text=Ly4star_data[10][2][10][1], width=3, height=1,bg=lfpbg).place(x=70,y=50)#
    tk.Label(fm11, text=Ly4star_data[10][3][10][1], width=3, height=1,bg=lfpbg).place(x=70,y=75)#
    tk.Label(fm11, text=Ly4star_data[10][4][10][1], width=3, height=1,bg=lfpbg).place(x=70,y=100)#
    tk.Label(fm11, text=Ly4star_data[10][5][10][1], width=3, height=1,bg=lfpbg).place(x=70,y=125)#

    tk.Label(fm11, text=Ly4star_data[11][0][10][1], width=3, height=1,bg=lfpbg).place(x=105,y=0)#
    tk.Label(fm11, text=Ly4star_data[11][1][10][1], width=3, height=1,bg=lfpbg).place(x=105,y=25)#
    tk.Label(fm11, text=Ly4star_data[11][2][10][1], width=3, height=1,bg=lfpbg).place(x=105,y=50)#
    tk.Label(fm11, text=Ly4star_data[11][3][10][1], width=3, height=1,bg=lfpbg).place(x=105,y=75)#
    tk.Label(fm11, text=Ly4star_data[11][4][10][1], width=3, height=1,bg=lfpbg).place(x=105,y=100)#
    tk.Label(fm11, text=Ly4star_data[11][5][10][1], width=3, height=1,bg=lfpbg).place(x=105,y=125)#

    tk.Label(fm11, text=Ly4star_data[5][0][10], width=3, height=1,bg=lfpbg).place(x=180,y=0)#大限火鈴
    tk.Label(fm11, text=Ly4star_data[5][1][10], width=3, height=1,bg=lfpbg).place(x=180,y=30)#大限羊陀
    tk.Label(fm11, text=Ly4star_data[6][0][10], width=3, height=1,bg=lfpbg).place(x=220,y=0)#小限火鈴
    tk.Label(fm11, text=Ly4star_data[6][1][10], width=3, height=1,bg=lfpbg).place(x=220,y=30)#小限羊陀
    tk.Label(fm11, text=Ly4star_data[7][0][10], width=3, height=1,bg=lfpbg).place(x=260,y=0)#太歲火鈴
    tk.Label(fm11, text=Ly4star_data[7][1][10], width=3, height=1,bg=lfpbg).place(x=260,y=30)#太歲羊陀

    fm11_sm_li = tk.Label(fm11, text=Ly4star_data[3][10], width=4, height=1).place(x=250,y=80)
    fm11_local_t = tk.Label(fm11, text=Ly4star_data[0][10], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm11_local = tk.Label(fm11, text='戌', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm11_name = tk.Button(fm11, text=Ly4star_data[8][10], width=6, height=1, command = lambda:line34(drawtray,'10')).place(x=180,y=120)

    fm12 =LabelFrame(root_4star,width=w_frame,height=h_frame,relief="groove")
    fm12.grid(row=3,column=3)#亥
    tk.Label(fm12, text=Ly4star_data[9][0][11][0], width=3, height=1,bg=lfpbg).place(x=0,y=0)#紫微星系
    tk.Label(fm12, text=Ly4star_data[9][1][11][0], width=3, height=1,bg=lfpbg).place(x=0,y=25)#天府星系
    tk.Label(fm12, text=Ly4star_data[9][2][11][0], width=3, height=1,bg=lfpbg).place(x=0,y=50)#文昌
    tk.Label(fm12, text=Ly4star_data[9][3][11][0], width=3, height=1,bg=lfpbg).place(x=0,y=75)#文曲
    tk.Label(fm12, text=Ly4star_data[9][4][11][0], width=3, height=1,bg=lfpbg).place(x=0,y=100)#左輔
    tk.Label(fm12, text=Ly4star_data[9][5][11][0], width=3, height=1,bg=lfpbg).place(x=0,y=125)#右弼

    tk.Label(fm12, text=Ly4star_data[9][0][11][1], width=3, height=1,bg=lfpbg).place(x=35,y=0)#
    tk.Label(fm12, text=Ly4star_data[9][1][11][1], width=3, height=1,bg=lfpbg).place(x=35,y=25)#
    tk.Label(fm12, text=Ly4star_data[9][2][11][1], width=3, height=1,bg=lfpbg).place(x=35,y=50)#
    tk.Label(fm12, text=Ly4star_data[9][3][11][1], width=3, height=1,bg=lfpbg).place(x=35,y=75)#
    tk.Label(fm12, text=Ly4star_data[9][4][11][1], width=3, height=1,bg=lfpbg).place(x=35,y=100)#
    tk.Label(fm12, text=Ly4star_data[9][5][11][1], width=3, height=1,bg=lfpbg).place(x=35,y=125)#

    tk.Label(fm12, text=Ly4star_data[10][0][11][1], width=3, height=1,bg=lfpbg).place(x=70,y=0)#
    tk.Label(fm12, text=Ly4star_data[10][1][11][1], width=3, height=1,bg=lfpbg).place(x=70,y=25)#
    tk.Label(fm12, text=Ly4star_data[10][2][11][1], width=3, height=1,bg=lfpbg).place(x=70,y=50)#
    tk.Label(fm12, text=Ly4star_data[10][3][11][1], width=3, height=1,bg=lfpbg).place(x=70,y=75)#
    tk.Label(fm12, text=Ly4star_data[10][4][11][1], width=3, height=1,bg=lfpbg).place(x=70,y=100)#
    tk.Label(fm12, text=Ly4star_data[10][5][11][1], width=3, height=1,bg=lfpbg).place(x=70,y=125)#

    tk.Label(fm12, text=Ly4star_data[11][0][11][1], width=3, height=1,bg=lfpbg).place(x=105,y=0)#
    tk.Label(fm12, text=Ly4star_data[11][1][11][1], width=3, height=1,bg=lfpbg).place(x=105,y=25)#
    tk.Label(fm12, text=Ly4star_data[11][2][11][1], width=3, height=1,bg=lfpbg).place(x=105,y=50)#
    tk.Label(fm12, text=Ly4star_data[11][3][11][1], width=3, height=1,bg=lfpbg).place(x=105,y=75)#
    tk.Label(fm12, text=Ly4star_data[11][4][11][1], width=3, height=1,bg=lfpbg).place(x=105,y=100)#
    tk.Label(fm12, text=Ly4star_data[11][5][11][1], width=3, height=1,bg=lfpbg).place(x=105,y=125)#

    tk.Label(fm12, text=Ly4star_data[5][0][11], width=3, height=1,bg=lfpbg).place(x=180,y=0)#大限火鈴
    tk.Label(fm12, text=Ly4star_data[5][1][11], width=3, height=1,bg=lfpbg).place(x=180,y=30)#大限羊陀
    tk.Label(fm12, text=Ly4star_data[6][0][11], width=3, height=1,bg=lfpbg).place(x=220,y=0)#小限火鈴
    tk.Label(fm12, text=Ly4star_data[6][1][11], width=3, height=1,bg=lfpbg).place(x=220,y=30)#小限羊陀
    tk.Label(fm12, text=Ly4star_data[7][0][11], width=3, height=1,bg=lfpbg).place(x=260,y=0)#太歲火鈴
    tk.Label(fm12, text=Ly4star_data[7][1][11], width=3, height=1,bg=lfpbg).place(x=260,y=30)#太歲羊陀

    fm12_sm_li = tk.Label(fm12, text=Ly4star_data[3][11], width=4, height=1).place(x=250,y=80)
    fm12_local_t = tk.Label(fm12, text=Ly4star_data[0][11], width=4, height=1,bg='yellow').place(x=250,y=105)
    fm12_local = tk.Label(fm12, text='亥', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm12_name = tk.Button(fm12, text=Ly4star_data[8][11], width=6, height=1, command = lambda:line34(drawtray,'11')).place(x=180,y=120)
    #---------***** 排大限流年 *****----------
    #*********************** 大限流年資料 ****************************
    s_y = Ly4star_data[2][0]   #大限流年起始數
    b_g = Ly4star_data[2][1]   #男女性別
    p_m = Ly4star_data[2][2]   #本生年天干陰陽
    if b_g == 1:
        temp_b_g = '男'
    else:
        temp_b_g = '女'
    if p_m == 0:
        temp_p_m = '陽'
    else:
        temp_p_m = '陰'        
 
    for j in range(0,12):
        if ((j+ftype_place)%12) == 0 :
            bg_lim=[]
            if (temp_p_m+temp_b_g == '陽男') or (temp_p_m+temp_b_g == '陰女'):
                for i in range(0,12):
                    bg_lim.append( str(s_y+10*i)+' ~ '+str(((s_y+10*i)+10-1)))
                tk.Label(fm1, text=bg_lim[(0+j)%12], width=8, height=1,bg='lightgreen').place(x=180,y=80)
                tk.Label(fm2, text=bg_lim[(1+j)%12], width=8, height=1,bg='lightgreen').place(x=180,y=80)
                tk.Label(fm3, text=bg_lim[(2+j)%12], width=8, height=1,bg='lightgreen').place(x=180,y=80)
                tk.Label(fm4, text=bg_lim[(3+j)%12], width=8, height=1,bg='lightgreen').place(x=180,y=80)
                tk.Label(fm5, text=bg_lim[(4+j)%12], width=8, height=1,bg='lightgreen').place(x=180,y=80)
                tk.Label(fm6, text=bg_lim[(5+j)%12], width=8, height=1,bg='lightgreen').place(x=180,y=80)
                tk.Label(fm7, text=bg_lim[(6+j)%12], width=8, height=1,bg='lightgreen').place(x=180,y=80)
                tk.Label(fm8, text=bg_lim[(7+j)%12], width=8, height=1,bg='lightgreen').place(x=180,y=80)
                tk.Label(fm9, text=bg_lim[(8+j)%12], width=8, height=1,bg='lightgreen').place(x=180,y=80)
                tk.Label(fm10, text=bg_lim[(9+j)%12], width=8, height=1,bg='lightgreen').place(x=180,y=80)
                tk.Label(fm11, text=bg_lim[(10+j)%12], width=8, height=1,bg='lightgreen').place(x=180,y=80)
                tk.Label(fm12, text=bg_lim[(11+j)%12], width=8, height=1,bg='lightgreen').place(x=180,y=80)

            else:
                for i in range(0,12):
                    bg_lim.append( str(s_y+10*i)+' ~ '+str(((s_y+10*i)+10-1)))

                tk.Label(fm1, text=bg_lim[(0-j)%12], width=8, height=1,bg='lightblue').place(x=180,y=80)
                tk.Label(fm2, text=bg_lim[(11-j)%12], width=8, height=1,bg='lightblue').place(x=180,y=80)
                tk.Label(fm3, text=bg_lim[(10-j)%12], width=8, height=1,bg='lightblue').place(x=180,y=80)
                tk.Label(fm4, text=bg_lim[(9-j)%12], width=8, height=1,bg='lightblue').place(x=180,y=80)
                tk.Label(fm5, text=bg_lim[(8-j)%12], width=8, height=1,bg='lightblue').place(x=180,y=80)
                tk.Label(fm6, text=bg_lim[(7-j)%12], width=8, height=1,bg='lightblue').place(x=180,y=80)
                tk.Label(fm7, text=bg_lim[(6-j)%12], width=8, height=1,bg='lightblue').place(x=180,y=80)
                tk.Label(fm8, text=bg_lim[(5-j)%12], width=8, height=1,bg='lightblue').place(x=180,y=80)
                tk.Label(fm9, text=bg_lim[(4-j)%12], width=8, height=1,bg='lightblue').place(x=180,y=80)
                tk.Label(fm10, text=bg_lim[(3-j)%12], width=8, height=1,bg='lightblue').place(x=180,y=80)
                tk.Label(fm11, text=bg_lim[(2-j)%12], width=8, height=1,bg='lightblue').place(x=180,y=80)
                tk.Label(fm12, text=bg_lim[(1-j)%12], width=8, height=1,bg='lightblue').place(x=180,y=80)
    #'''
    root_4star.mainloop()
    return

def fateplat_4star_data(fate_data): #大小限流年四煞星排盤程式keyin資料
    #*-----安大限、小限、流年的四煞-----*
    #1.找出大限命宮 =>ok
    #2.找出小限命宮 =>ok
    #3.找出流年命宮 =>ok
    #4.算出命主當下幾歲 =>ok
    #5.安化忌 =>ok

    #*-----當下時間 -----*
    fdata = fate_data[22]  #出生日期時間
    td_fdata = datetime.datetime.now()  #當下日期時間
    old_year=(abs(td_fdata-fdata).days)/365 #實際歲數
    dichi_4star={0:'子',1:'丑',2:'寅',3:'卯',4:'辰',5:'巳',6:'午',7:'未',8:'申',9:'酉',10:'戌',11:'亥'}    #十二地支

    big_limit_start = fate_data[7][0] #大限起始歲數
    ftype_place_m = fate_data[4]   #命宮所在為置,起大限用

    s_y = fate_data[7][0]   #大限流年起始數
    b_g = fate_data[7][1]   #男女性別
    p_m = fate_data[7][2]   #本生年天干陰陽
    if b_g == 1:
        temp_b_g = '男'
    else:
        temp_b_g = '女'
    if p_m == 0:
        temp_p_m = '陽'
    else:
        temp_p_m = '陰'        

    #*----- 大限命宮推算 -----*
    bg_lim_mk=[]
    temp_aa = (12-ftype_place_m)

    if (temp_p_m+temp_b_g == '陽男') or (temp_p_m+temp_b_g == '陰女'):
        for j in range(temp_aa,(12+temp_aa)):
            i = j%12
            if (s_y+10*i)<= old_year and old_year<=((s_y+10*i)+10-1) :
                bg_lim_mk.append('大限命宮')
            else:
                bg_lim_mk.append('')
    else:
        for j in range(0,12):
            i = (12-(temp_aa+j)) if (12-(temp_aa+j)) >= 0 else abs(12-(temp_aa+j)+12)
            #print(i)
            if (s_y+10*i)<= old_year and old_year<=((s_y+10*i)+10-1) :
                bg_lim_mk.append('大限命宮')
            else:
                bg_lim_mk.append('')

    #*----- 小限命宮推算 -----*
    small_limit = fate_data[8]
    sm_lim_mk = []
    temp_aa = (12-ftype_place_m)
    if (temp_b_g == '男'):
        if int(old_year) > small_limit[0]:
            temp_sm_aa =(int(old_year)-small_limit[0])%12
        else:
            temp_sm_aa =(12-(small_limit[0]-int(old_year)))%12
    else:#temp_b_g == '女'   待驗算
        if int(old_year) > small_limit[0]:
            temp_sm_aa =((temp_aa-(int(old_year)+small_limit[0])+1)%12)
        else:
            temp_sm_aa =(small_limit[0]-int(old_year))

    for k in range(0,12):
        if k ==temp_sm_aa :
            sm_lim_mk.append('小限命宮')
        else:
            sm_lim_mk.append('')
    bs_lim_mk = bg_lim_mk
    if bs_lim_mk[sm_lim_mk.index('小限命宮')] =='大限命宮':
        temp_zzz=0
        #print('大小限命宮相同宮位')
    else:
        del bs_lim_mk[sm_lim_mk.index('小限命宮')]
        bs_lim_mk.insert(sm_lim_mk.index('小限命宮'),'小限命宮')

    #*---- 四化星對應表 ----*
    star_a_6 = fate_data[2]    #紫微星系
    star_a_8 = fate_data[3]    #天府星系
    month_start_1 = fate_data[9]   #左輔
    month_start_2 = fate_data[10]   #右弼
    time_start_1 = fate_data[12]    #文昌
    time_start_2 = fate_data[13]    #文曲 


    l_4hwa = {'甲':['廉貞','破軍','武曲','太陽'],'乙':['天機','天梁','紫微','太陰'],
              '丙':['天同','天機','文昌','廉貞'],'丁':['太陰','天同','天機','巨門'],
              '戊':['貪狼','太陰','右弼','天機'],'己':['武曲','貪狼','天梁','文曲'],
              '庚':['太陽','武曲','天同','天相'],'辛':['巨門','太陽','文曲','文昌'],
              '壬':['天梁','紫微','左輔','武曲'],'癸':['破軍','巨門','太陰','貪狼'],}
    #清除具有四化星的主星曜之化星欄位資料
    for i in range(0,12):
        star_a_6[i][1] = ''    #紫微星系
        star_a_8[i][1] = ''    #天府星系
        time_start_1[i][1] = ''    #文昌
        time_start_2[i][1] = ''    #文曲    
        month_start_1[i][1] = ''   #左輔
        month_start_2[i][1] = ''   #右弼

    #*----- 求大小限及太歲的四煞星 -----*
    eing_so = fate_data[17]
    step1_a={'子':0,'丑':1,'寅':2,'卯':3,'辰':4,'巳':5,'午':6,'未':7,'申':8,'酉':9,'戌':10,'亥':11}
    f_time = fate_data[0][3]
    #大限天干,地支
    b_year_tenkan = eing_so[(bg_lim_mk.index('大限命宮'))]
    b_year_dichi = dichi_4star[bg_lim_mk.index('大限命宮')]
    #大限火鈴羊陀
    big_4star = set_4star_limit(b_year_tenkan,b_year_dichi,step1_a,f_time)  
    #大限四化星
    tt_temp_4star = fly_4star(b_year_tenkan,star_a_6,star_a_8,time_start_1,time_start_2,month_start_1,month_start_2,'big_limit')
    bl_temp_4star = copy.deepcopy(tt_temp_4star)    #防止資料被覆蓋

    #清除具有四化星的主星曜之化星欄位資料
    for i in range(0,12):
        star_a_6[i][1] = ''    #紫微星系
        star_a_8[i][1] = ''    #天府星系
        time_start_1[i][1] = ''    #文昌
        time_start_2[i][1] = ''    #文曲    
        month_start_1[i][1] = ''   #左輔
        month_start_2[i][1] = ''   #右弼

    #小限天干,地支
    s_year_tenkan = eing_so[temp_sm_aa]
    s_year_dichi =dichi_4star[temp_sm_aa]
    #小限火鈴羊陀
    small_4star = set_4star_limit(s_year_tenkan,s_year_dichi,step1_a,f_time)    #小限火鈴羊陀
    #小限四化星
    tt_temp_4star = fly_4star(s_year_tenkan,star_a_6,star_a_8,time_start_1,time_start_2,month_start_1,month_start_2,'small_limit')
    sl_temp_4star = copy.deepcopy(tt_temp_4star)    #防止資料被覆蓋

    #清除具有四化星的主星曜之化星欄位資料
    for i in range(0,12):
        star_a_6[i][1] = ''    #紫微星系
        star_a_8[i][1] = ''    #天府星系
        time_start_1[i][1] = ''    #文昌
        time_start_2[i][1] = ''    #文曲    
        month_start_1[i][1] = ''   #左輔
        month_start_2[i][1] = ''   #右弼
    #太歲天干,地支
    yy=clander_cc.changecc(td_fdata)  #年,月,日,時,分,秒
    L_year_tenkan = yy[0][0]
    L_year_dichi =yy[0][1]
    #太歲火鈴羊陀
    Ly_4star = set_4star_limit(L_year_tenkan,L_year_dichi,step1_a,f_time)
    #太歲四化星
    tt_temp_4star = fly_4star(L_year_tenkan,star_a_6,star_a_8,time_start_1,time_start_2,month_start_1,month_start_2,'L_year_limit')
    Ll_temp_4star = copy.deepcopy(tt_temp_4star)    #防止資料被覆蓋
    #各流年四化飛星資料
    ll_4flystar =[l_4hwa[b_year_tenkan],l_4hwa[s_year_tenkan],l_4hwa[L_year_tenkan]]

    L_year = '' #流年資料-->4  沒有被使用的變數
    big_limit = fate_data[7]
    #eing_so #寅首-->個宮位的天干-->0
    #ftype_place_m  #基本命宮所在位置,啟大限用-->1
    #big_limit  #大限資料-->2
    #small_limit    #小限資料-->3
    #L_year #流年資料-->4
    #big_4star  #大限四煞星-->5
    #small_4star#小限四煞星-->6
    #Ly_4star  #流年四煞星-->7
    #bg_lim_mk  #大限流年命宮-->8
    #bl_temp_4star  #大限流年四化飛星-->9
    #sl_temp_4star  #小限流年四化飛星-->10
    #Ll_temp_4star  #太歲流年四化飛星-->11
    #ll_4flystar    #各流年四化飛星-->12
    temp_bsl =[eing_so,ftype_place_m,big_limit,small_limit,L_year,
               big_4star,small_4star,Ly_4star,
               bs_lim_mk,bl_temp_4star,sl_temp_4star,Ll_temp_4star,
               ll_4flystar]#
    #print(temp_bsl)
    fateplat_4star(temp_bsl)   #呼叫大小限流年四煞星排盤程式

    return

#*-----大小限及太歲的火鈴羊陀及祿權科忌運算及排盤 End----*

def fly_4star(argu_year,star_a_6,star_a_8,time_start_1,time_start_2,
              month_start_1,month_start_2,use_place):   #產生四化飛星資料
    use_place   #四化飛星使用的命盤類別
    argu_year   #本生年天干
    star_a_6    #紫微星系
    star_a_8    #天府星系
    time_start_1    #文昌
    time_start_2   #文曲    
    month_start_1   #左輔
    month_start_2   #右弼

    step13_1 ={'甲':'廉貞','乙':'天機','丙':'天同','丁':'太陰','戊':'貪狼','己':'武曲','庚':'太陽','辛':'巨門','壬':'天梁','癸':'破軍'}#化祿
    step13_2 ={'甲':'破軍','乙':'天梁','丙':'天機','丁':'天同','戊':'太陰','己':'貪狼','庚':'武曲','辛':'太陽','壬':'紫微','癸':'巨門'}#化權
    step13_3 ={'甲':'武曲','乙':'紫微','丙':'文昌','丁':'天機','戊':'右弼','己':'天梁','庚':'天同','辛':'文曲','壬':'左輔','癸':'太陰'}#化科
    step13_4 ={'甲':'太陽','乙':'太陰','丙':'廉貞','丁':'巨門','戊':'天機','己':'文曲','庚':'天相','辛':'文昌','壬':'武曲','癸':'貪狼'}#化忌

    hwa_lu = step13_1[argu_year]
    hwa_cheng = step13_2[argu_year]
    hwa_ka = step13_3[argu_year]
    hwa_gi = step13_4[argu_year]
    temp_lckg = [hwa_lu,hwa_cheng,hwa_ka,hwa_gi]
    temp_lckg_text=['化祿','化權','化科','化忌']
    for i in range(0,4):
        try:         
            temp_tt=(star_a_6.index([temp_lckg[i],'']))
            del star_a_6[temp_tt]
            star_a_6.insert(temp_tt,[temp_lckg[i],temp_lckg_text[i]])
            #print(star_a_6)
        except:
            temp = 0                           
            #print(temp_lckg[i],'不在紫微星系內')
        
        try:
            temp_tt=(star_a_8.index([temp_lckg[i],'']))
            del star_a_8[temp_tt]
            star_a_8.insert(temp_tt,[temp_lckg[i],temp_lckg_text[i]])        
            #print(star_a_8)
        except:                           
            temp = 0
            #print(temp_lckg[i],'不在天府星系內')

        try:
            temp_tt=(month_start_1.index([temp_lckg[i],'']))
            del month_start_1[temp_tt]
            month_start_1.insert(temp_tt,[temp_lckg[i],temp_lckg_text[i]])        
            #print(month_start_1)
        except:                           
            temp = 0
            #print(temp_lckg[i],'不在左輔內')

        try:
            temp_tt=(month_start_2.index([temp_lckg[i],'']))
            del month_start_2[temp_tt]
            month_start_2.insert(temp_tt,[temp_lckg[i],temp_lckg_text[i]])        
            #print(month_start_2)
        except:                           
            temp = 0
            #print(temp_lckg[i],'不在右弼內')           

        try:
            temp_tt=(time_start_1.index([temp_lckg[i],'']))
            del time_start_1[temp_tt]
            time_start_1.insert(temp_tt,[temp_lckg[i],temp_lckg_text[i]])        
            #print(time_start_1)
        except:                           
            temp = 0
            #print(temp_lckg[i],'不在文昌內')

        try:
            temp_tt=(time_start_2.index([temp_lckg[i],'']))
            del time_start_2[temp_tt]
            time_start_2.insert(temp_tt,[temp_lckg[i],temp_lckg_text[i]])        
            #print(time_start_2)
        except:                           
            temp = 0
            #print(temp_lckg[i],'不在文曲內')
    if use_place == 'noth_4fly':    #北派四化飛星
        messagebox.showinfo('四化飛星', temp_lckg)
        #print(temp_lckg)
    return(star_a_6,star_a_8,month_start_1,month_start_2,time_start_1,time_start_2,temp_lckg)

def data_save(save_data):   #儲存命主資料
    with open((save_data[1]+save_data[0]+'.txt'),"w",encoding='utf-8') as output:
        for i in save_data:
            output.write(str(i))
            output.write('\n')

    return

def save_img(fname):    #儲存命盤影像
    w_win = 1200
    h_win = 652
    x_offset = (1536 - w_win) / 2
    y_offset = (864 - h_win) / 2
    #print(x_offset)
    #print(y_offset)
    img = ImageGrab.grab(bbox=(220, 120, 1720, 940))  # X1, Y1, X2, Y2
    #img.show()  
    img.save(fname+'.jpg', quality=100)
  
    return()

def main_module(b_d):   #產生排盤資料

    #b_d = base_data:0:編號,1:姓名,2:男女,3:年,4:月,5:日,6:點,7:分,8:時辰
    
    #******-----將地支時辰轉成24小時制的時間-----******
    time_c = {'子':23,'丑':2,'寅':4,'卯':6,'辰':8,'巳':10,'午':12,'未':14,'申':16,'酉':18,'戌':20,'亥':22}
    if b_d[8] == '':
        fdata=datetime.datetime(int(b_d[3]),int(b_d[4]),int(b_d[5]),int(b_d[6]),int(b_d[7]),00)
    else:
        fdata=datetime.datetime(int(b_d[3]),int(b_d[4]),int(b_d[5]),time_c[b_d[8]],00,00)

    #******-----fdata 的格式為 yyyymmddttmmss(年月日時分秒)-----******
    xx=clander_cc.changecc(fdata)   #透過萬年曆將陽曆轉換後的生辰八字所有資料
    #print(xx)
    #年:xx[0],月-日:xx[1],日:xx[2],:xx[3]
    #*-----將生辰八字分離出來作為排盤所需資料-----*****************************
    f_year_a = xx[0][0] #本生年天干
    f_year_b = xx[0][1] #本生年地支
    chinese_month = ['正','二','三','四','五','六','七','八','九','十','冬','臘']
    i = 0
    for trm in chinese_month:
        i += 1
        if trm == xx[1][0]:
           f_month = i  #生月
    f_date = xx[1][-2:] #生日
    f_time = xx[3]

    tenkan = {'甲':0,'乙':1,'丙':0,'丁':1,'戊':0,'己':1,'庚':0,'辛':1,'壬':0,'癸':1}   #十天干
    dichi = {'子':0,'丑':1,'寅':2,'卯':3,'辰':4,'巳':5,'午':6,'未':7,'申':8,'酉':9,'戌':10,'亥':11}    #十二地支

    #*step_1-----命宮身宮-----fmx_name_d******************************
    #ftype_place_m = 0 #= 0 命宮在子位, = 1 命宮在丑位  ::測試資料
    step1_a = dichi
    tp=step1_a[f_time]   #求出時辰位置

    mk_start_1=['寅','丑','子','亥','戌','酉','申','未','午','巳','辰','卯']#1月命宮位置
    mk_start_2=['寅','卯','辰','巳','午','未','申','酉','戌','亥','子','丑']#子時命宮位置
    c=mk_start_2.index(mk_start_1[tp])  #找出生時正月份命宮所在的索引值
    temp_yy=mk_start_2[(c+int(f_month)-1)%12] #由正月找到的索引值+出生月-1 ->本命宮所在位置
    ftype_place_m = step1_a[temp_yy] #十二宮分佈的型態
    #print('命宮所在型態:',temp_yy,ftype_place_m)
    sk_start_1=['寅','卯','辰','巳','午','未','申','酉','戌','亥','子','丑']#1月身宮位置
    sk_start_2=['寅','卯','辰','巳','午','未','申','酉','戌','亥','子','丑']#子時命宮位置
    d=sk_start_2.index(sk_start_1[tp])
    temp_zz=sk_start_2[(d+int(f_month)-1)%12]
    ftype_place_s = step1_a[temp_zz]
    #print('身宮所在型態:',temp_zz,ftype_place_s)

    #*step_2-----定寅首-----******************************
    eing_so =[]
    step2_a={'甲':0,'乙':1,'丙':2,'丁':3,'戊':4,'己':0,'庚':1,'辛':2,'壬':3,'癸':4}
    step2_b=[['丙','丁','丙','丁','戊','己','庚','辛','壬','癸','甲','乙'],
             ['戊','己','戊','己','庚','辛','壬','癸','甲','乙','丙','丁'],
             ['庚','辛','庚','辛','壬','癸','甲','乙','丙','丁','戊','己'],
             ['壬','癸','壬','癸','甲','乙','丙','丁','戊','己','庚','辛'],
             ['甲','乙','甲','乙','丙','丁','戊','己','庚','辛','壬','癸']]
    temp_uu=step2_a[f_year_a]
    eing_so=step2_b[temp_uu]
    #寅首的串列:eing_so

    #*step_3-----定五行局-----******************************
    step3_a={'子':0,'丑':0,'寅':1,'卯':1,'辰':2,'巳':2,'午':3,'未':3,'申':4,'酉':4,'戌':5,'亥':5}
    step3_b={'甲':0,'乙':1,'丙':2,'丁':3,'戊':4,'己':0,'庚':1,'辛':2,'壬':3,'癸':4}
    step3_c=[['水二局','火六局','土五局','木三局','金四局'],
             ['火六局','土五局','木三局','金四局','水二局'],
             ['木三局','金四局','水二局','火六局','土五局'],        
             ['土五局','木三局','金四局','水二局','火六局'],
             ['金四局','水二局','火六局','土五局','木三局'],
             ['火六局','土五局','木三局','金四局','水二局']]
    temp_mk = step3_a[temp_yy]
    temp_tenkan = step3_b[f_year_a]
    five_code =step3_c[temp_mk][temp_tenkan]    #五行局
    #五行局:five_code

    #*step_4-----定十二宮-----******************************
    plate_place_d =['命宮','兄弟宮','夫妻宮','子女宮','財帛宮','疾厄宮','遷移宮','僕役宮','官祿宮','田宅宮','福德宮','父母宮']
    plate_place=[]
    plate_place.append(plate_place_d[ftype_place_m])
    for i in range(11,0,-1):
        plate_place.append(plate_place_d[(i+ftype_place_m)%12])
    #本命盤十二宮的串列:plate_place

    #*step_5-----起大限-----******************************
    step5_1={'水二局':2,'火六局':6,'土五局':5,'木三局':3,'金四局':4}
    big_limit_start = step5_1[five_code]  #大限起始歲數(一宮10歲:ex:2-11)
    b_d[2] #1=男 , 2=女
    pmbg = tenkan[f_year_a] #定出生年陰陽 0:陽, 1:陰
    if b_d[2] == 1:
        temp_b_g = '男'
    else:
        temp_b_g = '女'
    if pmbg == 0:
        temp_p_m = '陽'
    else:
        temp_p_m = '陰'        
    #big_limit =[大限起始歲數,男女,出生年陰陽,命宮所在位置,五行局]
    
    for j in range(0,12):
        if ((j+ftype_place_m)%12) == 0 :
            bg_lim=[]
            temp_bg_lim=[]
            if (temp_p_m+temp_b_g == '陽男') or (temp_p_m+temp_b_g == '陰女'):
                for i in range(0,12):
                    temp_bg_lim.append( str(big_limit_start+10*i)+' ~ '+str(((big_limit_start+10*i)+10-1)))
                for k in range(0,12):
                    bg_lim.append(temp_bg_lim[(k+j)%12])
            else:
                for i in range(0,12):
                    temp_bg_lim.append( str(big_limit_start+10*i)+' ~ '+str(((big_limit_start+10*i)+10-1)))
                bg_lim.append(temp_bg_lim[(0-j)%12])
                for k in range(11,0,-1):
                    bg_lim.append(temp_bg_lim[(k-j)%12])
    big_limit =[big_limit_start,b_d[2],pmbg,ftype_place_m,five_code,bg_lim]
    #大限的串列:big_limit

    #*step_6-----起小限-----******************************
    step6_1={'寅':'辰','午':'辰','戌':'辰','申':'戌','子':'戌','辰':'戌',
             '巳':'未','酉':'未','丑':'未','亥':'丑','卯':'丑','未':'丑'}
    small_limit=[]
    small_limit_a = step6_1[xx[0][1]]
    small_limit_b = step1_a[small_limit_a] #小限起始位置
    #print(small_limit_b)
    if b_d[2] ==1 :
        for i in range(0,12):
            small_limit.append((i+(12-small_limit_b))%12+1)
    else:
        for i in range(12,0,-1):
            small_limit.append((i+(small_limit_b))%12+1)

    #小限的串列:small_limit

    #*step_7-----起紫微星-----******************************
    step_7_1 = {'水二局':0,'火六局':4,'土五局':3,'木三局':1,'金四局':2}
    step_7_2 = [['丑','辰','亥','午','酉'],['寅','丑','辰','亥','午'],
                ['寅','寅','丑','辰','亥'],['卯','巳','寅','丑','辰'],
                ['卯','寅','子','寅','丑'],['辰','卯','巳','未','寅'],
                ['辰','午','寅','子','戌'],['巳','卯','卯','巳','未'],
                ['巳','辰','丑','寅','子'],['午','未','午','卯','巳'],
                ['午','辰','卯','申','寅'],['未','巳','辰','丑','卯'],
                ['未','申','寅','午','亥'],['申','巳','未','卯','申'],
                ['申','午','辰','辰','丑'],['酉','酉','巳','酉','午'],
                ['酉','午','卯','寅','卯'],['戌','未','申','未','辰'],
                ['戌','戌','巳','辰','子'],['亥','未','午','巳','酉'],
                ['亥','申','辰','戌','寅'],['子','亥','酉','卯','未'],
                ['子','申','午','申','辰'],['丑','酉','未','巳','巳'],
                ['丑','子','巳','午','丑'],['寅','酉','戌','亥','戌'],
                ['寅','戌','未','辰','卯'],['卯','丑','申','酉','申'],
                ['卯','戌','午','午','巳'],['辰','亥','亥','未','午']]
    star_type = step_7_2[(int(f_date)-1)][step_7_1[five_code]]

    #*step_8-----安14顆甲級正星-----******************************
    ftype_star_14 = step1_a[star_type] #= 0 紫微星在子位, = 1 紫微星在丑位
    star_a_6_d =['紫微','天機','','太陽','武曲','天同','','','廉貞','','','']
    star_a_8_d =['天府','太陰','貪狼','巨門','天相','天梁','七殺','','','','破軍','']
    star_a_6 = []
    for j in range(12,0,-1):
        star_a_6.append([star_a_6_d[((j)%12+ftype_star_14)%12],''])
    #紫微星系的串列:star_a_6
    star_a_8 = []
    for j in range(0,12):
        star_a_8.append([star_a_8_d[((8+j)%12+ftype_star_14)%12],'']) 
    #天府星系的串列:star_a_8

    #*step_9-----安月系星座----- 左輔,右弼******************************
    step_9_1 = ['辰','巳','午','未','申','酉','戌','亥','子','丑','寅','卯'] #左輔
    step_9_2 = ['戌','酉','申','未','午','巳','辰','卯','寅','丑','子','亥'] #右弼
    month_start_1 =[]
    for i in range(0,12):
        if i ==(step1_a[step_9_1[f_month-1]])  :
            month_start_1.append(['左輔',''])
        else:
            month_start_1.append(['',''])
    #左輔星的串列:month_start_1     
 
    month_start_2 =[]
    for i in range(0,12):
        if i ==(step1_a[step_9_2[f_month-1]])  :
            month_start_2.append(['右弼',''])
        else:
            month_start_2.append(['',''])
    #右弼星的串列:month_start_2  

    #天刑、天馬 ---->陣列完成，排盤待完工---一個位置
    step_9_3 = ['酉','戌','亥','子','丑','寅','卯','辰','巳','午','未','申'] #天刑
    step_9_4 = ['申','巳','寅','亥','申','巳','寅','亥','申','巳','寅','亥'] #天馬
    month_start_3 =[]
    for i in range(0,12):
        if i ==(step1_a[step_9_3[f_month-1]])  :
            month_start_3.append('天刑')
        elif i ==(step1_a[step_9_4[f_month-1]])  :
            month_start_3.append('天馬')
        else:
            month_start_3.append('')
    #天刑、天馬的串列:month_start_3

    #*step_10-----安日系星座-----******************************
    #三台、八座 ---->陣列完成，排盤待完工---二個位置
    #三台：左輔(month_start_1)起初一，順行數到本生日
    #八座：右弼(month_start_2)起初一，逆行數到本生日
    f_date  #本生日
    date_start_1 = []   #三台
    date_start_2 = []   #八座
    for i in range(0,12):
        if month_start_1[i][0] == '左輔':
           temp_date_1=((i-1+int(f_date))%12)
        if month_start_2[i][0] == '右弼':
            temp_date_2=(i-(int(f_date))%12)+1
            print(temp_date_2)

    for j in range(0,12):
        if j == temp_date_1:
            date_start_1.append('三台')
        else:
            date_start_1.append('')
        if j == temp_date_2:
            date_start_2.append('八座')
        else:
            date_start_2.append('')
    #三台的串列:date_start_1
    #八座的串列:date_start_2

    #*step_11-----安時系星座-----******************************
    #*火星,鈴星,文昌,文曲*
    f_year_b  #本生年地支
    f_time  #出生時辰
    time_start =[]  #火星,鈴星
    time_start_1 =[]    #文昌
    time_start_2 =[]    #文曲

    step11_1 = {'寅':'丑','午':'丑','戌':'丑',
                '申':'寅','子':'寅','辰':'寅',
                '巳':'卯','酉':'卯','丑':'卯',
                '亥':'酉','卯':'酉','未':'酉'}#火星起始
    step11_2 = {'寅':'卯','午':'卯','戌':'卯',
                '申':'戌','子':'戌','辰':'戌',
                '巳':'戌','酉':'戌','丑':'戌',
                '亥':'戌','卯':'戌','未':'戌'}#鈴星起始
    
    temp_F_1 = step11_1[f_year_b]#求出火星起始地支
    temp_F_2 = step1_a[temp_F_1]#求出起始地支的數
    temp_F_3 = step1_a[f_time]#求出出生時的數
    temp_F_4 = (temp_F_2+temp_F_3)%12 #火星的數

    temp_L_1 = step11_2[f_year_b]#求出鈴星起始地支
    temp_L_2 = step1_a[temp_L_1]#求出起始地支的數
    temp_L_3 = step1_a[f_time]#求出出生時的數
    temp_L_4 = (temp_L_2+temp_L_3)%12 #鈴星的數

    for i in range(0,12):
        if i ==temp_F_4:
            time_start.append('火星')
        else:
            time_start.append('')
    del time_start[temp_L_4]
    time_start.insert(temp_L_4,'鈴星')
    #火星鈴星的串列:time_start

    step11_3 = ['戌','酉','申','未','午','巳','辰','卯','寅','丑','子','亥']#文昌
    step11_4 = ['辰','巳','午','未','申','酉','戌','亥','子','丑','寅','卯']#文曲
    temp_wenchong = step1_a[step11_3[temp_F_3]]#文昌宮位
    temp_wenchyu = step1_a[step11_4[temp_F_3]]#文曲宮位

    for i in range(0,12):
        if i ==temp_wenchong:
            time_start_1.append(['文昌',''])
        else:
            time_start_1.append(['',''])
        if i ==temp_wenchyu:
            time_start_2.append(['文曲',''])
        else:
            time_start_2.append(['',''])
    #文昌星的串列:time_start_1
    #文曲星的串列:time_start_2

    #*地劫，地空(天空)*
    f_time  #出生時辰
    step11_5 = ['亥','子','丑','寅','卯','辰','巳','午','未','申','酉','戌']#地劫
    step11_6 = ['亥','戌','酉','申','未','午','巳','辰','卯','寅','丑','子']#地空
    di_jey = []    #地劫
    di_kwng = []    #地空

    temp_11_a_1 = step1_a[step11_5[step1_a[f_time]]] #地劫宮位
    temp_11_a_2 = step1_a[step11_6[step1_a[f_time]]] #地空宮位

    for i in range(0,12):
        if i == temp_11_a_1:
            di_jey.append('地劫')
        else:
            di_jey.append('')
    #地劫星的串列:di_jey

        if i == temp_11_a_2:
            di_kwng.append('地空')
        else:
            di_kwng.append('')
    #地空星的串列:di_kwng

    #*step_12-----安年干星座----- 魁、鉞、祿、羊、陀******************************
    f_year_a  #本生年天干
    lu_yan_tuo = []
    kwe_yuei = []
    step1_a #十二宮位置
    step12_1 = {'甲':'寅','乙':'卯','丙':'巳','丁':'午','戊':'巳','己':'午','庚':'申','辛':'酉','壬':'亥','癸':'子'}#祿存
    step12_2 = {'甲':'卯','乙':'辰','丙':'午','丁':'未','戊':'午','己':'未','庚':'酉','辛':'戌','壬':'子','癸':'丑'}#擎羊
    step12_3 = {'甲':'丑','乙':'寅','丙':'辰','丁':'巳','戊':'辰','己':'巳','庚':'未','辛':'申','壬':'戌','癸':'亥'}#陀羅
    step12_4 = {'甲':'未','乙':'申','丙':'酉','丁':'亥','戊':'丑','己':'子','庚':'丑','辛':'寅','壬':'卯','癸':'巳'}#天魁
    step12_5 = {'甲':'丑','乙':'子','丙':'亥','丁':'酉','戊':'未','己':'申','庚':'未','辛':'午','壬':'巳','癸':'卯'}#天鉞

    temp_luchun = step1_a[step12_1[f_year_a]]
    temp_cheinyan = step1_a[step12_2[f_year_a]]
    temp_tuolo = step1_a[step12_3[f_year_a]]
    temp_tenkwe = step1_a[step12_4[f_year_a]]
    temp_tenyuei = step1_a[step12_5[f_year_a]]

    for i in range(0,12):
        if i ==temp_tenkwe:
            kwe_yuei.append('天魁')
        elif i ==temp_tenyuei:
            kwe_yuei.append('天鉞')
        else:
            kwe_yuei.append('')
    #天魁、天鉞的串列:kwe_yuei

    for i in range(0,12):
        if i ==temp_luchun:
            lu_yan_tuo.append('祿存')
        elif i ==temp_cheinyan:
            lu_yan_tuo.append('擎羊')
        elif i ==temp_tuolo:
            lu_yan_tuo.append('陀羅')
        else:
            lu_yan_tuo.append('')
    #祿存、擎羊、陀羅的串列:lu_yan_tuo

    #*step_13-----安四化星-----******************************
    use_place = 'base_plate'
    temp_4star = fly_4star(f_year_a,star_a_6,star_a_8,time_start_1,
                           time_start_2,month_start_1,month_start_2,use_place)    #由出生年天干求出四化星的位置
    #將四化星寫入相關星曜的串列位置
    star_a_6 = temp_4star[0]
    star_a_8 = temp_4star[1]
    month_start_1 = temp_4star[2]
    month_start_2 = temp_4star[3]
    time_start_1 = temp_4star[4]
    time_start_2 = temp_4star[5]

    #*step_14-----安年支星座----- 紅鸞、天喜*ok
    #本生年地支:f_year_b
    step14_1 = ['卯','寅','丑','子','亥','戌','酉','申','未','午','巳','辰']#紅鸞
    step14_2 = ['酉','申','未','午','巳','辰','卯','寅','丑','子','亥','戌']#天喜
    lwang_si = []
    temp_14_a_1 = step1_a[step14_1[step1_a[f_year_b]]]#紅鸞宮位
    temp_14_a_2 = step1_a[step14_2[step1_a[f_year_b]]]#天喜宮位
  
    for i in range(0,12):
        if i == temp_14_a_1:
            lwang_si.append('紅鸞')
        elif i == temp_14_a_2:
            lwang_si.append('天喜')
        else:
            lwang_si.append('')
    #紅鸞、天喜的串列:lwang_si

    #*-----排盤資料整合-----******************************
    
    #*-----傳入排盤程式的變數內容-----*
    #xx  #基本資料 -->0
    #    xx[0][0] = f_year_a #本生年天干
    #    xx[0][1] = f_year_b #本生年地支
    #    xx[1]   = # 生月-日
    #    xx[2]   = # 生日干支
    #    xx[3]   = # 生時
    #plate_place = 定十二宮 -->1
    #star_a_6 = 紫微星系 -->2
    #star_a_8 = 天府星系 -->3
    #ftype_place_m   = #命宮所在為置,起大限用 -->4
    #ftype_place_s   = #身宮所在為置 -->5
    #ftype_star_14   #紫微星起始位置 -->6
    #big_limit[0]   #大限流年起始數 -->7[0]
    #big_limit[1]   #男女性別 -->7[1]
    #big_limit[2]   #本生年天干陰陽 -->7[2]
    #big_limit[3]    #命宮起始位置 -->7[3]
    #big_limit[4]    #五行局 -->7[4]
    #big_limit[5]    #大限流年 -->7[5]

    #small_limit    #小限流年 -->8
    #month_start_1   #左輔 -->9
    #month_start_2   #右弼 -->10
    #time_start    #火星,鈴星 -->11
    #time_start_1    #文昌 -->12
    #time_start_2    #文曲 -->13
    #lu_yan_tuo  #祿存、擎羊、陀羅 -->14
    #kwe_yuei    #天魁、天鉞 -->15
    #name_label  #姓名 -->16
    #eing_so #寅首-->個宮位的天干 -->17
    #temp_zz #身宮 -->18
    #di_jey  #地劫 -->19
    #di_kwng #地空 -->20
    #lwang_si    #紅鸞、天喜 -->21
    #fdata  #出生年月日時分秒資料 -->22
    #month_start_3  #天刑、天馬 -->23
    #date_start_1   #三台 -->24
    #date_start_2   #八座 -->25

    name_label=b_d[1]
    # 0~6,7~8,9~10,11~13,14~15,16~18,19~22,23~25
    fate_data = [xx,plate_place,star_a_6,star_a_8,ftype_place_m,ftype_place_s,ftype_star_14,
                 big_limit,small_limit,
                 month_start_1,month_start_2,
                 time_start,time_start_1,time_start_2,
                 lu_yan_tuo,kwe_yuei,
                 name_label,eing_so,temp_zz,
                 di_jey,di_kwng,lwang_si,fdata,
                 month_start_3,date_start_1,date_start_2]

    return(fate_data)

def quit_prg(): #離開程式
    root_quit = Tk()
    screenwidth = root_quit.winfo_screenwidth()
    screenheight = root_quit.winfo_screenheight()
    w_win = 600
    h_win = 200
    x_offset = (screenwidth - w_win) / 2
    y_offset = ((screenheight - h_win) / 2)
    root_quit.title("離開程式")
    root_quit.geometry("%dx%d+%d-%d" %(w_win,h_win,x_offset,y_offset))
    root_quit.resizable(False, False)
    style = Style()
    style.theme_use("alt")
    fontStyle = tkFont.Font(family="標楷體", size=20)#Keiu 16
    #*********************** 離開程式 ****************************
    Label(root_quit, font=fontStyle, text='離開程式?', width=10, height=1,bg='lightblue').place(x=20,y=100)
    var_quit = tk.IntVar()
    var_quit.set(1)

    rbquit_y = Radiobutton(root_quit, font=fontStyle, text="Yes",variable=var_quit,value=9,command='')
    rbquit_y.place(x = 200, y = 100)
    rbquit_n = Radiobutton(root_quit, font=fontStyle, text="No",variable=var_quit,value=0,command='')
    rbquit_n.place(x = 300, y = 100)
    tk.Button(root_quit, font=fontStyle, text='確定', width = 4, height=1,command=root_quit.destroy).place(x=450,y=100)
    root_quit.mainloop()
    return(var_quit.get())  #將命主資料儲存

def health():   #十二宮代表的身體部位
    fpbg ='#F0F0F0'#'lightgreen''#F0F0F0'
    health =[['生殖','泌尿'],['肛門',''],['右腳',''],['右腹','右腰'],['右胸',''],['右手','右肩'],
             ['頭部','右眼'],['臉部','左眼'],['左手','左肩'],['左胸',''],['左腹','卵巢'],['左腳','']]
    root_hralth = Tk()
    screenwidth = root_hralth.winfo_screenwidth()
    screenheight = root_hralth.winfo_screenheight()
    #print(screenwidth)
    #print(screenheight)
    w_win = 1200
    h_win = 652
    w_frame = 300
    h_frame = 163
    x_offset = (screenwidth - w_win) / 2
    y_offset = ((screenheight - h_win) / 2)
    root_hralth.title("身體健康")
    root_hralth.geometry("%dx%d+%d-%d" %(w_win,h_win,x_offset,y_offset))
    root_hralth.resizable(False, False)
    style = Style()
    style.theme_use("alt")
    fontStyle = tkFont.Font(family="標楷體", size=14)
    fontStyle_1 = tkFont.Font(family="標楷體", size=20)
   
    #*********************** 十二宮繪製布局 ****************************
    fm1 =LabelFrame(root_hralth,width=w_frame,height=h_frame,relief="groove")
    fm1.grid(row=3,column=2)#子
    tk.Label(fm1, text=health[0][0],font=fontStyle, width=4, height=1, bg=fpbg).place(x=0,y=0)  #紫微星系  
    tk.Label(fm1, text=health[0][1],font=fontStyle, width=4, height=1, bg=fpbg).place(x=50,y=0) #紫微星系四化
    fm1_local = tk.Label(fm1, text='子', width=4, height=1,bg='yellow').place(x=250,y=130)  #命盤宮位地支--固定
    fm1_name = tk.Button(fm1, font=fontStyle, text='', width=6, height=1, command='').place(x=120,y=120)   #命盤宮位名稱

    fm2 =LabelFrame(root_hralth,width=w_frame,height=h_frame,relief="groove")
    fm2.grid(row=3,column=1)#丑
    tk.Label(fm2, text=health[1][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm2, text=health[1][1],font=fontStyle, width=4, height=1).place(x=60,y=0)
    fm2_local = tk.Label(fm2, text='丑', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm2_name = tk.Button(fm2, font=fontStyle, text='', width=6, height=1, command='').place(x=120,y=120)

    fm3 =LabelFrame(root_hralth,width=w_frame,height=h_frame,relief="groove")
    fm3.grid(row=3,column=0)#寅
    tk.Label(fm3, text=health[2][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm3, text=health[2][1],font=fontStyle, width=4, height=1).place(x=60,y=0)
    fm3_local = tk.Label(fm3, text='寅', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm3_name = tk.Button(fm3, font=fontStyle, text='', width=6, height=1, command='').place(x=120,y=120)

    fm4 =LabelFrame(root_hralth,width=w_frame,height=h_frame,relief="groove")
    fm4.grid(row=2,column=0)#卯
    tk.Label(fm4, text=health[3][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm4, text=health[3][1],font=fontStyle, width=4, height=1).place(x=60,y=0)
    fm4_local = tk.Label(fm4, text='卯', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm4_name = tk.Button(fm4, font=fontStyle, text='', width=6, height=1, command='').place(x=120,y=120)

    fm5 =LabelFrame(root_hralth,width=w_frame,height=h_frame,relief="groove")
    fm5.grid(row=1,column=0)#辰
    tk.Label(fm5, text=health[4][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm5, text=health[4][1],font=fontStyle, width=4, height=1).place(x=60,y=0)
    fm5_local = tk.Label(fm5, text='辰', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm5_name = tk.Button(fm5, font=fontStyle, text='', width=6, height=1, command='').place(x=120,y=120)

    fm6 =LabelFrame(root_hralth,width=w_frame,height=h_frame,relief="groove")
    fm6.grid(row=0,column=0)#巳
    tk.Label(fm6, text=health[5][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm6, text=health[5][1],font=fontStyle, width=4, height=1).place(x=60,y=0)
    fm6_local = tk.Label(fm6, text='巳', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm6_name = tk.Button(fm6, font=fontStyle, text='', width=6, height=1, command='').place(x=120,y=120)

    fm7 =LabelFrame(root_hralth,width=w_frame,height=h_frame,relief="groove")
    fm7.grid(row=0,column=1)#午
    tk.Label(fm7, text=health[6][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm7, text=health[6][1],font=fontStyle, width=4, height=1).place(x=60,y=0)
    fm7_local = tk.Label(fm7, text='午', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm7_name = tk.Button(fm7, font=fontStyle, text='', width=6, height=1, command='').place(x=120,y=120)

    fm8 =LabelFrame(root_hralth,width=w_frame,height=h_frame,relief="groove")
    fm8.grid(row=0,column=2)#未
    tk.Label(fm8, text=health[7][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm8, text=health[7][1],font=fontStyle, width=4, height=1).place(x=60,y=0)
    fm8_local = tk.Label(fm8, text='未', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm8_name = tk.Button(fm8, font=fontStyle, text='', width=6, height=1, command='').place(x=120,y=120)

    fm9 =LabelFrame(root_hralth,width=w_frame,height=h_frame,relief="groove")
    fm9.grid(row=0,column=3)#申
    tk.Label(fm9, text=health[8][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm9, text=health[8][1],font=fontStyle, width=4, height=1).place(x=60,y=0)
    fm9_local = tk.Label(fm9, text='申', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm9_name = tk.Button(fm9, font=fontStyle, text='', width=6, height=1, command='').place(x=120,y=120)

    fm10 =LabelFrame(root_hralth,width=w_frame,height=h_frame,relief="groove")
    fm10.grid(row=1,column=3)#酉
    tk.Label(fm10, text=health[9][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm10, text=health[9][1],font=fontStyle, width=4, height=1).place(x=60,y=0)
    fm10_local = tk.Label(fm10, text='酉', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm10_name = tk.Button(fm10, font=fontStyle, text='', width=6, height=1, command='').place(x=120,y=120)

    fm11 =LabelFrame(root_hralth,width=w_frame,height=h_frame,relief="groove")
    fm11.grid(row=2,column=3)#戌
    tk.Label(fm11, text=health[10][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm11, text=health[10][1],font=fontStyle, width=4, height=1).place(x=60,y=0)
    fm11_local = tk.Label(fm11, text='戌', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm11_name = tk.Button(fm11, font=fontStyle, text='', width=6, height=1, command='').place(x=120,y=120)

    fm12 =LabelFrame(root_hralth,width=w_frame,height=h_frame,relief="groove")
    fm12.grid(row=3,column=3)#亥
    tk.Label(fm12, text=health[11][0],font=fontStyle, width=4, height=1).place(x=0,y=0)
    tk.Label(fm12, text=health[11][1],font=fontStyle, width=4, height=1).place(x=60,y=0)
    fm12_local = tk.Label(fm12, text='亥', width=4, height=1,bg='yellow').place(x=250,y=130)
    fm12_name = tk.Button(fm12, font=fontStyle, text='', width=6, height=1, command='').place(x=120,y=120)
    #'''
    root_hralth.mainloop()
    return

if __name__ == '__main__':
    run_fate = 0
    #基本資料格式
    #0:編號，1:姓名，2:男女，3:陰陽曆，4:陽年，5:陽月，6:陽日，7:陰年，8:陰月，9:陰日，10:時，11:分，12:時辰
    sbase_data =['0001','林昱廷',1,1,87,5,21,56,8,2,13,30,0]
    while run_fate <= 2:
        b_d=keyin_data(sbase_data)      #輸入命主的基本資料
        fate_data = main_module(b_d)    #產生排盤所需資料
        fateplat_new(fate_data)         #將資料傳入排盤程式_new
        run_fate = quit_prg()           #是否離開程式
    print("end_program")




