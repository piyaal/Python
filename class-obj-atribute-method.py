#Student ক্লাস তৈরি করছি

'''ধাপ ১: ক্লাস তৈরি করা

class Student:
    def __init__(self, name, age):
        self.name = name      # অ্যাট্রিবিউট
        self.age = age

    def introduce(self):      # মেথড
        print(f"আমার নাম {self.name}, আমার বয়স {self.age} বছর।")


---

ধাপ ২: ইনস্ট্যান্স তৈরি করা

s1 = Student("Rahim", 16)
s2 = Student("Karim", 17)

এখানে s1 ও s2 দুইজন ছাত্রের উদাহরণ (instance)। তারা Student ক্লাসের তৈরি।


---

ধাপ ৩: অ্যাট্রিবিউট ব্যবহার করা

print(s1.name)   # Output: Rahim
print(s2.age)    # Output: 17

আমরা object.attribute ব্যবহার করে তথ্য বের করেছি।


---

ধাপ ৪: মেথড ব্যবহার করা

s1.introduce()   # Output: আমার নাম Rahim, আমার বয়স 16 বছর।
s2.introduce()   # Output: আমার নাম Karim, আমার বয়স 17 বছর।

object.method() দিয়ে আমরা কাজ করিয়েছি।


---

সংক্ষেপে মনে রাখার জন্য:

অ্যাট্রিবিউট = অবজেক্টের তথ্য (যেমন নাম, বয়স)

মেথড = অবজেক্টের কাজ (যেমন পরিচয় দেওয়া)

ব্যবহার পদ্ধতি: object.attribute এবং object.method()'''



class Student:
    def __init__(self, name, age):
        self.name = name      # অ্যাট্রিবিউট
        self.age = age        # অ্যাট্রিবিউট

    def introduce(self):      # মেথড
        print(f"আমার নাম {self.name}, আমার বয়স {self.age} বছর।")

# দুটি Student ইনস্ট্যান্স তৈরি করছি
s1 = Student("Rahim", 16)
s2 = Student("Karim", 17)

# অ্যাট্রিবিউট ব্যবহার
print("s1 এর নাম:", s1.name)
print("s2 এর বয়স:", s2.age)

# মেথড কল
s1.introduce()
s2.introduce()

