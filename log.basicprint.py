Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello Wold')
Hello Wold
>>> print('Hello Loong')
Hello Loong
>>> name = 'Artit'
>>> lastname = 'Phromnog'
>>> fullname = mame + ' ' + lastname
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    fullname = mame + ' ' + lastname
NameError: name 'mame' is not defined. Did you mean: 'name'?
>>> fullname = name + ' ' + lastname
>>> print(fullname)
Artit Phromnog
>>> fullname = name + lastname
>>> print(fullname)
ArtitPhromnog
>>> age = 10
>>> type(age)
<class 'int'>
>>> print('ลุงครับผมชื่อ{} นามสกุล {} อายุ {} ขวบ'.format(name,lastname,age))
ลุงครับผมชื่อArtit นามสกุล Phromnog อายุ 10 ขวบ
>>> print(f'ลุงครับผมชื่อ{name} นามสกุล {lastname} อายุ {age} ขวบ')
ลุงครับผมชื่อArtit นามสกุล Phromnog อายุ 10 ขวบ
