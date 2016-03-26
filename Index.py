import os

class indexer:
	path = "~"
	site = "http://krewn.github.io"
	proj = "datasci"
	prod = []
	def __init__(self,p):
		self.path=p
	def HtmlFrek(self,k):
		print("rek")
		os.chdir(k)
		ret="<h2>"+k+"</h2>"
		files = [f for f in os.listdir('.') if os.path.isfile(f) and f.split(".")[len(f.split("."))-1]=="html"]
		for t in files:
			print t
			t.replace(".","")
			t.replace("\\","/")
			ref = site+"/"+proj
			for k in loc:
				ref+="/"+k
			ret+= "<a href ="+ref+t+">"+t+"</a><br>\n"
		images = [f for f in os.listdir('.') if os.path.isfile(f) and f.split(".")[len(f.split("."))-1]=="png"]
		for i in images:
			i.replace(".","")
			i.replace("\\","/")
			ref = site+"/"+proj
			for k in loc:
				ref+="/"+k
			ret+= "<img src="+ref+"/"+i+">\n"
		folders = [f for f in os.listdir(".") if not os.path.isfile(f)]
		print folders
		for k in folders:
			print k
			if(k == '.'):
				print k
				continue
			print k
			ret+="<div class='blue1'>"
			ret+=self.HtmlFrek(k)
			ret += "</div>"
		os.chdir("..")
		return(ret)
		
	def HtmlProd(self):
		location = []
		print("start")
		ret = ""
		ret+="""<!DOCTYPE html><html>"""
		ret+="<div>"
		folders = [f for f in os.listdir(".") if not os.path.isfile(f)]
		for k in folders:
			if(k == '.'):
				continue
			print k
			ret+="<div>"
			ret+=self.HtmlFrek(k)
			ret+="</div>"
			
		ret+="</div>"
		ret+="""</html>"""
		self.prod = ret
		return(ret)
		
i = indexer(".")
q=i.HtmlProd()
print i.prod

w = open("index.html","w")
w.write(q)
w.close()
