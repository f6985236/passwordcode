password = 'cf5454321'
x = 3 #宣告都寫在上面
while True:
	pwd = input('請輸入密碼:')  #要用代號「pwd」不然會造成password的定義混亂
	if pwd == password : #就直接定義成password
		print('登入成功！')
		break  #逃出迴圈
		
	else :
		x =  x - 1
		print('密碼錯誤！,還有',x,'次機會') #印出x次剩餘機會

		if x == 0:
			break

		

		


