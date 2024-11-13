'''
concrete mrthod
'''
'''

class Sample:
    def code(self):
        print('code')
s=Sample()
s.code()




from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print('Bark')
class Cat(Animal):
    def sound(self):
        print('Meow')
a=Animal()
a.sound()
d=Dog()
d.sound()
c=Cat()
c.sound()






from abc import ABC,abstractmethod
class Demo(ABC):
    @abstractmethod
    def chat(self):
        pass

    @abstractmethod
    def reels(self):
        pass

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def filter(self):
        pass

    @abstractmethod
    def story(self):
        pass

    @abstractmethod
    def gifs(self):
        pass
class Instagram(Demo):
    def chat(self):
        print('Chatting')
    def reels(self):
        print('Reels')
    def post(self):
        pass
    def filter(self):
        print('Filter')
    def story(self):
        print('Story')
    def gifs(self):
        print('gifs')
class Whatsapp(Demo):
    def chat(self):
        print('Chat')
    def reels(self):
        print('Reels')
    def post(self):
        print('Post')
    def filter(self):
        print('filter')
    def story(self):
        print('story')
    def gifs(self):
        print('Gifd')

i=Instagram()
i.chat()
i.reels()
i.post()
i.filter()
i.story()
i.gifs()
print('='*20)
w=Whatsapp()
w.chat()
w.reels()
w.post()
w.filter()
w.story()
w.gifs()








from abc import ABC,abstractmethod
class Animal:
    def eat(self):
        print('Eating')
    def sleep(self):
        print('sleep')
    @abstractmethod
    def sound(self):
        pass
class Rat(Animal):
    def sound(self):
        print('Rat sound')
class Cat(Animal):
    def sound(self):
        print('Cat sound')
a=Animal()
a.sleep()
a.sound()
a.eat()
r=Rat()
r.sound()
c=Cat()
c.sound()
c.eat()
c.sleep()




'''