import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4235')
print(mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4235')
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 333-3323.')

print(mo.group(1))
print(mo.group(2))

# 使用管道匹配多个分组
hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey.')
print(mo1.group())
mo1 = hero_regex.search(' Tina Fey and Batman.')
print(mo1.group())

hero_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = hero_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# 用问号实现可选匹配

hero_regex = re.compile(r'Bat(wo)?man')
mo = hero_regex.search('The Adventures of Batman')
print(mo.group())

mo = hero_regex.search('The Adventures of Batwoman')
print(mo.group())

phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4343')
print(mo.group())

mo = phoneNumRegex.search('My number is 444-3432')
print(mo.group())

# 用星号匹配零次或多次
hero_regex = re.compile(r'Bat(wo)*man')
print(hero_regex.search('The Adventures of Batman').group())
print(hero_regex.search('The Adventures of Batwoman').group())
print(hero_regex.search('The Adventures of Batwowowowoman').group())

# 用加号匹配一次或多次
hero_regex = re.compile(r'Bat(wo)+man')
print(hero_regex.search('The Adventures of Batwoman').group())
print(hero_regex.search('The Adventures of Batwowowowoman').group())
print(hero_regex.search('The Adventures of Batman') is None)

# 用花括号匹配特定次数

hero_regex = re.compile(r'(ha){3}')
print(hero_regex.search('hahaha').group())
print(hero_regex.search('ha') is None)

# 贪心和非贪心匹配
# 默认是贪心的，所以下述正则会匹配到最长的那个字符串
greedy_ha_regex = re.compile(r'(Ha){3,5}')
mo = greedy_ha_regex.search('HaHaHaHaHa')
print(mo.group())
# 加了一个问好，则变成非贪心的，所以下述正则会匹配到最短的那个字符串
greedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo = greedy_ha_regex.search('HaHaHaHaHa')
print(mo.group())

# findAll 方法 找到所有匹配的字符串
# 如果在一个没有分组的正则表达式上调用，例如下述情况
# findAll方法将返回一个匹配字符串的列表
phone_reg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_reg.findall('Cell: 453-432-5555 Work: 453-908-8887')
print(mo)
# 如果在一个有分组的正则表达式上调用，例如下述情况
# findAll方法将返回一个字符串的元组的列表
phone_reg = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phone_reg.findall('Cell: 453-432-5555 Work: 453-908-8887')
print(mo)

# 字符分类

# \d : 0 ~ 9 的任何数字
# \D : 除 0 ~ 9 的数字以外的任何字符
# \w : 任何字符、数字或下划线字符（可以认为是匹配“单词”字符）
# \W : 除字母、数字和下划线以外的任何字符
# \s : 空格、制表符或换行符（可以认为是匹配空白字符）
# \S : 除空格、制表符和换行符以外的任何字符
xmas_regex = re.compile(r'\d+\s\w+')
print(xmas_regex.findall('12 abc, 23 bbb, d 44 ,34    abc, 44 444, 33 abc'))
# 匹配元音字符
reg = re.compile(r'[aeiouAEIOU]')
print(reg.findall('I love you'))
# 匹配非元音字符
reg = re.compile(r'[^aeiouAEIOU]')
print(reg.findall('I love you'))