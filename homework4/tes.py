def Bs(num,lower,upper):
	#   before inclusive ,after exclusive
	string=""
	mid = (lower + upper)/2
	while (lower<=upper):
		mid= (lower+upper)/2
		string += ",%d" % mid
		if mid==num:
			break
		elif mid<num:
			lower =mid+1
		else:
			upper =mid

	return string


print Bs(27,16,32)
# %s %d %(sign,mid)