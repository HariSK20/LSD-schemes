#
#		usage : import script
#		script.evaluate('expression', 'return base')
#
def chid(c):
	if c >= '0' and c <= '9':
		return ord(c) - ord ('a')
	elif c >= 'A' and c <= 'Z':
		return ord(c) - ord('A')
	elif c >= 'a' and c <= 'z':
		return ord(c) - ord('a')

def toDeci(str, base):
	llen= len(str)
	power = 1
	num = 0
	chidcache=0
	for i in range(llen-1, -1 ,-1):
		chidcache = chid(str[i])
		if chidcache >= base:
			return -1
		num+= chidcache*power
		power = power*base

	return num
def reVal(num): 
  
    if (num >= 0 and num <= 9): 
        return chr(num + ord('0'))
    else: 
        return chr(num - 10 + ord('A'))

def fromDeci(res, base, inputNum): 
  
    while inputNum > 0: 
        res+= reVal(inputNum % base)
        inputNum = int(inputNum / base)

    res = res[::-1]
  
    return res

def base1(val, op):
	'''
	converts val from any base to decimal
	
	Parameters:
			'string' val, 'string' op

	Returns:
			'int' val in decimal form
	'''
	if op == 'b':
		return int(val, 2)
	elif op == 'o':
		return int(val, 8)
	elif op == 'd':
		return int(val, 10)
	elif op == 'h':
		return int(val, 16)
	else:
		return toDeci(val , op)


def base2(val, op):
	'''
	Converts decimal val to any base op

	Parameters: 
			'int' val, 'string' op

	Returns:
			'string' val in the base op 
	'''
	if op == 'b':
		return bin(int(val)).replace("0b", "")
	elif op == 'o':
		return oct(int(val)).replace("0o", "")
	elif op == 'd':
		return val
	elif op == 'h':
		return hex(int(val)).replace("0x", "")
##	else
##		return fromDeci() use the from deciFucntion here @FIX


def operate(a , b, op):
	if op == '*':
		return a*b
	elif op == '/':
		return a/b
	elif op == '+':
		return a+b
	elif op == '-':
		return a-b
	else:
		return 0


def eval_post(l):
	if len(l) == 1:
		return(l[0])
	num_stk = []
	for i in l:
		if type(i) is int:
			num_stk.append(i)
		else:
			a = num_stk.pop()
			b = num_stk.pop()
			num_stk.append(operate(b, a, i))
#		print(num_stk)
	return(num_stk.pop())


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
	op_stk = ['$']
	res = []
	i=0
	while(i < len(s)):
		q=''
		c = s[i]
		if s[i] in ['b', 'o', 'd', 'h']: # I think the issue could be fixed here, but im not touching it as I dont have any idea about the logic @FIX
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
		elif s[i] in ['+', '-', '*', '/']:
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
	if len(res)==1:
		return(res)
	p = op_stk.pop()
	while p != '$':
		res.append(p)
		try:
			p = op_stk.pop()
		except IndexError:
			break
	return(res)


def evaluate(s, op='d'):
	'''

	Evaluates infix expression containing different bases

	Parameters:
			'string' s the expression, 'string' op the return base

	Returns:
			'string' evaluated value

	'''
	try:
		return(base2(eval_post(postfix(s)), op))
	except:
		return('ERROR')