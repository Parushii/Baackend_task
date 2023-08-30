from django.http import JsonResponse
import json

def get_range(request):
    a=int(request.GET.get('a',1))
    b=int(request.GET.get('b',10))

    dictionary={}
    for i in range(a,b):
        if i==1:
            prime=False
        else:
            prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
        if prime==False:
            print(i,"Not prime")
            n=i
            l=[]
            for k in range(1,n+1):
                if(n%k==0):
                    l.append(i)
            print(l)
            dictionary[i]=l
        else:
            print(i," prime")
            n=i
            sum=""
            while n>0:
                r=n%2
                sum=sum+str(r)
                n=n//2
            binary="".join(reversed(sum))
            print(binary)
            dictionary[i]=binary
# print(dictionary)
    return JsonResponse(dictionary)