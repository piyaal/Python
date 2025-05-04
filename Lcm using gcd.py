#LCM হলো দুটি (বা ততোধিক) সংখ্যার এমন একটি সর্বনিম্ন সংখ্যা, যা ঐ সব সংখ্যার গুণিতক এবং সবার দ্বারা বিভাজ্য।
#সংখ্যা: ৪ ও ৬

#৪-এর গুণিতক: ৪, ৮, ১২, ১৬, ২০, ২৪, ...

#৬-এর গুণিতক: ৬, ১২, ১৮, ২৪, ৩০, ...

#সাধারণ গুণিতক: ১২, ২৪, ...
#সর্বনিম্ন সাধারণ গুণিতক: ১২
#তাই, LCM(4, 6) = 12

#for negative numbers gcd will be always positive
#lcm using euclidean algorithom and negetive value

a=int(input("enter 1st number:\n"))
b=int(input("enter 2nd number:\n"))
c,d=a,b
a=abs(a)
b=abs(b)
def find_gcd(x,y):
      while y!=0:
        x,y=y,x%y
      return x
gcd=find_gcd(a,b)
#if we use one  / divide it will show float lcm, thats why we use two // for integer output for lcm
lcm=(a*b)//gcd 
print("GCD is:\n",gcd)
print("LCM is:\n",lcm)

 
