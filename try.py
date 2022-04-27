class student:
	def __init__(self,rollno,name,cls,perc,grade=None):
		self.rollno=rollno
		self.name=name
		self.cls=cls
		self.perc=perc
		self.grade=grade
class school:
	def __init__(self,slist):
		self.slist=slist
	def grading(self):
		count={}
		for i in "ABCDE":
			count[i]=0
		for i in self.slist:
			if i.perc<100 and i.perc>74:
				i.grade='A'
				count['A']=count.get('A',0)+1
			elif i.perc>59:
				i.grade='B'
				count['B']=count.get('B',0)+1
			elif i.perc>39:
				i.grade='C'
				count['C']=count.get('C',0)+1
			elif i.perc>29:
				i.grade='D'
				count['D']=count.get('D',0)+1
			elif i.perc>-1:
				i.grade='C'
				count['E']=count.get('E',0)+1
		return sorted(count.items())
	def rank(self,cutoff):
		passed=[]
		for i in self.slist:
			if i.perc>=cutoff:
				passed.append(i)
		if passed:
			return sorted(passed,key=lambda x:x.perc,reverse=True)
		else:
			return None

slist=[]
for i in range(int(input())):
	slist.append(student(int(input()),input(),input(),int(input())))
cutoff=int(input())
sch=school(slist)
d=sch.grading()
for i in d:
	print(i[0],':',i[1])
r=sch.rank(cutoff)
if r:
	for i in r:
		print(i.rollno,i.name,i.cls,float(i.perc))
else:
	print("No student hscored more than the cutoff percentage")
