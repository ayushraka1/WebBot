import random
import os
import requests
os.system("apt install toilet")
color1=["\033[1;31;40m","\033[1;32;40m","\033[1;33;40m","\033[1;34;40m","\033[1;35;40m","\033[1;36;40m"]
def color():
 return str(random.choice(color1))
def banner():
 os.system("clear")
 os.system("toilet -fmono12 -F gay WebBot")
 print("    \033[1;36;40m Code made by: \033[1;32;40m tuhin1729")
 print("    \033[1;36;40m Instagram id: \033[1;32;40m www.instagram.com/tuhin1729")
 print("    \033[1;36;40m Github      : \033[1;32;40m www.github.com/tuhin1729")
 print("    \033[1;36;40m YouTube     : \033[1;32;40m https://bit.ly/TuhinTheHacker")
 print("    \033[1;36;40m Dedicated to: \033[1;34;40m Diya Saha")
 print("\n\n")
banner()
url = raw_input("\033[1;33;40mEnter the URL(Ex: https://www.google.com) :")

useragentlist=['Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; EasyBits GO v1.0; (R1 1.6); .NET CLR 1.1.4322; .NET CLR 2.0.50727; SpamBlockerUtility 4.8.4; InfoPath.1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; WinNT-EVI 19.01.2010; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; msn OptimizedIE8;ENGB)','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; ELT; BTRS1229395; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  Embedded Web Browser from: http://bsalsa.com/; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 1.1.4322; ELT; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; FDM; .NET4.0C; .NET4.0E; ELT)','Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/AT&T]','Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0','Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; Iphone 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A500FU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/80.0.3987.132 Mobile Safari/537.36','Mozilla/5.0 (X11; Linux; x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.4.3-g','Mozilla/5.0 (X11; Linux) AppleWebKit/534.34 (KHTML, like Gecko) QtCarBrowser Safari/534.34','Mozilla/5.0 (X11; Linux; ja-JP) AppleWebKit/534.34 (KHTML, like Gecko) QtCarBrowser Safari/534.34JP','Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.8.1-ae1963092ff8','Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/75.0.3770.100 Chrome/75.0.3770.100 Safari/537.36 Tesla/2019.32.12.6-1a714d2','Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.8.2-dc9bc402da23','Opera/9.50 (Nintendo DSi; Opera/446; U; ja)','Mozilla/5.0 (Nintendo Switch; WebApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.10.7 NintendoBrowser/5.2.1.17381','Mozilla/5.0 (Nintendo Switch; WebApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.7.9 NintendoBrowser/5.1.0.15850','Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/606.4 (KHTML, like Gecko) NF/6.0.1.13.17 NintendoBrowser/5.1.0.19907','Mozilla/5.0 (PlayStation Vita 3.73) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2','Mozilla/5.0 (PlayStation Vita 3.72) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2','Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7636.US','Mozilla/5.0 (Nintendo Switch; ShareApplet) AppleWebkit/601.6 (KHTML, like Gecko) NF/4.0.0.11.6 NintendoBrowser/5.1.0.18855','Mozilla/5.0 (New Nintendo 3DS like iPhone) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.0.5.22 Mobile NintendoBrowser/1.10.10166.US','Mozilla/5.0 (PlayStation Vita 3.60) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2','Mozilla/5.0 (Nintendo 3DS; U; Factory Media Production; en) Version/1.7498.US','Mozilla/5.0 (PlayStation Vita 3.36) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2','Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2','Mozilla/5.0 (Nintendo 3DS; U; ; pt) Version/1.7630.EU','Mozilla/5.0 (New Nintendo 3DS like iPhone) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.0.5.20 Mobile NintendoBrowser/1.9.10160.JP','Opera/9.50 (Nintendo DSi; Opera/507; U; en-US)','Mozilla/5.0 (PlayStation Vita 3.67) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2','Opera/9.50 (Nintendo DSi; Opera/507; U; fr)','Mozilla/5.0 (PlayStation Vita 3.63) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2','Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7630.US','Mozilla/5.0 (New Nintendo 3DS like iPhone) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.0.5.20 Mobile NintendoBrowser/1.9.10160.EU','Mozilla/5.0 (PlayStation Vita 3.65) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2','Mozilla/4.0 (PSP (PlayStation Portable); 2.00)','Mozilla/5.0 (PlayStation Vita 3.68) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2','Mozilla/5.0 (New Nintendo 3DS like iPhone) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.0.5.20 Mobile NintendoBrowser/1.9.10160.US','Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.8.9 NintendoBrowser/5.1.0.16739','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.45','Cursos%20UMCE/136 CFNetwork/1125.2 Darwin/19.4.0','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 3.5.30729; Media Center PC 6.0; Tablet PC 2.0; wbx 1.0.0; Zoom 3.6.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.2511.97 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3506.71 Safari/537.36','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.2360.79 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.2448.68 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3170.81 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.2300.61 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3133.26 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.2918.40 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v432194043572249480 t3345461284722333977','Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 UCURSOS/v1.5.4_223-android','Mozilla/5.0 (Linux; Android 9; POT-LX3 Build/HUAWEIPOT-L03; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 128.0.0.26.128 Android (28/9; 480dpi; 1080x2139; HUAWEI; POT-LX3; HWPOT-H; kirin710; es_','U-Cursos/132 CFNetwork/808.2.16 Darwin/16.3.0','Mozilla/5.0 (Linux; Android 9; H3113) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; ASUS_Z017D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36 OPR/57.1.2830.52480','Mozilla/5.0 (Linux; Android 7.0; TECNO K7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX3 Build/HUAWEIDUB-LX3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.162 Mobile Safari/537.36 UCURSOS/v1.5.4_227-android','Mozilla/5.0 (Linux; Android 9; SM-A600GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; SM-G610M Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36 UMCE/v1.5.4_223-android','Mozilla/5.0 (Linux; Android 8.1.0; SM-J710MN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36 OPR/57.1.2830.52480','Mozilla/5.0 (Linux; Android 9; SM-A750G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.162 Mobile Safari/537.36 UCURSOS/v1.5.4_227-android','Mozilla/5.0 (Linux; Android 5.0.1; ALE-L21 Build/HuaweiALE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36 UCURSOS/v1.5.4_227-android','Mozilla/5.0 (Linux; Android 8.0.0; SM-J720M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.62 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; FIG-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-N9600) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; STK-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; moto g(6)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 135.1.0.23.118 (iPhone11,8; iOS 13_3_1; en_AE; en-AE; scale=2.00; 828x1792; 206833405)','Mozilla/5.0 (Linux; Android 6.0; CAM-L03) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36 OPR/56.1.2780.51589','Mozilla/5.0 (Linux; Android 7.0; BLL-L23) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; RNE-L03) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; moto x4 Build/PPW29.69-40-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36 UCURSOS/v1.5.4_227-android','Mozilla/5.0 (Linux; Android 8.1.0; Digi_K1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; X1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Chrome/75.0.3770.143 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SC-03L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.1.2; es-es) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 8.0.0; LG-H918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; RMX1911) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; G3223) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36']

banner()

i=1
while(1):
 try:
  os.system("cd tor && bash change.sh")
  useragent=random.choice(useragentlist)
  r=requests.get(url,headers={'User-Agent':useragent})
  print("\033[1;32;40mView increased = "+color()+str(i))
  i=i+1
 except Exception as e:
  print(e)
