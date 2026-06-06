# 分科成績計算機 Advanced Subjects Test (AST) score calculator

To the calculator: https://devboring.github.io/taiwan-ast-exam-score-calculator/

嗨～ 我是一名剛從師大附中畢業，正在準備分科的學生。

某天我去查了大考中心的　"OOO學年度大學分發入學 各系組最低錄取標準及錄取人數一覽表"　來大概計算剩餘科目所需的平均分數。

因為考慮的校系不少，因此一直重複計算非常麻煩，想想自己也會寫python為何不寫個程式輔助我計算，做著做著就想搞一個使用者導向的網頁版。
但因為html忘的差不多了，程式問題百出，感謝Google Gemini幫助除錯與優化。（但也因此讓一大段程式長的跟AI寫的一樣，讓我很不爽）

僅收錄民國111年(實行分科測驗)及以後的資料。只包含普通生最低錄取分數，原住民、退伍軍人、僑生、蒙藏生、派外子女等並不適用。

歡迎回報任何bug

# 各檔案意義

`README.md`：就是這篇，應該不用解釋

`source.txt`：為直接從大考中心`.pdf`中`ctrl + a`複製後直接貼上(包含一些垃圾文字)

`convert.py`：讀取`source.txt`並分類與過濾，最後後輸出`data.json`

`data.json`：就是database

`index.html`：讀取`data.json`與建構整個網頁

# 資料來源：大考中心

111年: https://www2.uac.edu.tw/111data/111_result_school_data.pdf

112年: https://www.uac.edu.tw/112data/112_result_school_data.pdf

113年: https://www2.uac.edu.tw/113data/113_result_school_data.pdf

114年: https://www.uac.edu.tw/114data/114_result_school_data.pdf

# 已知bug

暫無
