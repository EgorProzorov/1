x=1000000
days=x//(24*60*60)
x=x%(24*60*60)
hours=x//(60*60)
x=x%(60*60)
minutes=x//60
seconds=x%60

print(days,':', hours,':', minutes,':', seconds)