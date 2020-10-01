
def rettop(stk):
	try:
		return stk[-1]
	except IndexError:
		return '$'


def precedence(x):
	if x in ['/', '*']:
		return 2
	elif x in ['+', '-']:
		return 1
	else :
		return 0


def postfix(s, flg = 0):
	op_stk = []
	res = []
	i=0
	while(i < len(s)):
		q=''
		c = s[i]
		if s[i] in ['b', 'o', 'd', 'h']:
			j=i+2
			while(s[j] != ')'):
				q += s[j]
#				print(q)
				j+=1
			res.append(base1(q, s[i]))
			i=j		
		elif s[i] == '(':
			op_stk.append(s[i])
		elif s[i] == ')':
			p = op_stk.pop()
			while p != '(':
				res.append(p)
				p = op_stk.pop()
		else:
#			op_stk.append(s[i])
#			print(op_stk)
			pre1 = precedence(s[i])
			pre2 = precedence(rettop(op_stk))
			while pre2 >= pre1:
				p = op_stk.pop()
				res.append(p)
				pre2 = precedence(rettop(op_stk))
			op_stk.append(s[i])
#		print(res)
#		print(op_stk)
		i+=1
	p = op_stk.pop()
	while p != '$':
		res.append(p)
		try:
			p = op_stk.pop()
		except IndexError:
			break
	return(res)