password = 'cf5454321'
x = 3 #宣告都寫在上面
while x > 0 :  #這個迴圈條件可以幫助整個程式碼變的更簡單
	x =  x - 1
	pwd = input('請輸入密碼:')  #要用代號「pwd」不然會造成password的定義混亂
	if pwd == password : #就直接定義成password
		print('登入成功！')
		break  #逃出迴圈
		
	else :
		print('密碼錯誤！') #印出x次剩餘機會
		if x > 0 :
			print('還有',x,'次機會')  #因為通常不會印出還有零次機會，這樣比較好
		else:
			print('沒機會嘗試了！要鎖住帳號囉！')
#----------------------------------
		if x == 0:  #最後的結局，是在上面用x>o做迴圈，這行下面就都可以刪掉
			break 

		

		


