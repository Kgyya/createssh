"""
Authod: Kgyya
Gitcrod: github.com/Kgyya
"""
# Belajar Dari Isinya Ngemtod
# Malah Di Rikod

from bs4 import BeautifulSoup as bs
import requests
import os; os.system("clear")
import sys
import re

def list_server():
	ses = requests.Session()
	readyssh = "https://www.readyssh.net/server/ssh"
	r = ses.get(readyssh,headers={"User-Agent":"Chrome"})
	soup = bs(r.text,"html.parser")
	count = 1
	jud = []
	for list_jud in soup.find_all("h3",class_="pb-2 mb-3"):
		print(str(count)+") "+list_jud.text.replace("SSH ",""))
		count += 1
		jud.append(list_jud.text.replace("SSH ","").lower())
	pilih = input("Select Server: ")
	pil = jud[int(pilih) - 1]
	print("Proccessing...")
	list_link_jud = "https://readyssh.net/server/ssh/"+str(pil)
	raw = ses.get(list_link_jud)
	soupp = bs(raw.text,"html.parser")
	os.system("clear")
	print("Server: "+str(pil))
	cound = 1
	isp = []
	for list_isp in re.findall("<h4>(.*?)</h4>",raw.text):
		print(str(cound)+") "+str(list_isp))
		cound += 1
		isp.append(list_isp)
	pilih_isp = input("Select Server ISP: ")
	pil_isp = isp[int(pilih_isp) - 1]
	link_isp = list_link_jud+"/buat-akun/"+pil_isp.replace(" ","-").lower()
	print("[Info] Username Tidak Boleh Berisi Angka")
	user = input("Input Username: ")
	pw = input("Input Password: ")
	print("Proccessing...")
	raw_isp = ses.get(link_isp)
	soupe = bs(raw_isp.text,"html.parser")
	create = soupe.find("form",attrs={"id":"create-account"})
	token = soupe.find("input",attrs={"name":"_token"})
	data = {
		"_token":token.get("value"),
		"username":user,
		"password":pw,

}
	create_ssh = ses.post(create.get("action"),data=data)
	if "Berhasil!" in create_ssh.text:
		print("Host/IP : "+re.search("<li>Host: (.*?)<",create_ssh.text).group(1))
		print("Username: "+re.search("<li>Username: (.*?)<",create_ssh.text).group(1))
		print("Password: "+re.search("<li>Password: (.*?)<",create_ssh.text).group(1))
		print("Port Information: ")
		print("OpenSSH        : 22, 152")
		print("OpenSSH+SSL    : 990")
		print("Dropbear       : 80,115")
		print("Dropbear+SSL   : 443")
		print("Squid Proxy    : 8080, 3128, 8118")
		print("Squid Proxy+SSL: 8000")
		print("Expired : "+re.search("<li>Aktif Sampai: (.*?)<",create_ssh.text).group(1))
	elif "Sorry" in create_ssh.text:
		exit("Limit Exceeded!, Server Full")
	elif "Warning!" in create_ssh.text:
		exit("Username/Password Invalid Input.")
	else:
		exit("Skmething Wrong.")
list_server()
