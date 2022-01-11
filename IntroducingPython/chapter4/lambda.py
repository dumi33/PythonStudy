def edit_story(words, func) :
    for word in words :
        print(func(word))
def enliven(word) :
    return word.capitalize() + '!'

stair = ['thud','meow','thud','hiss']

edit_story(stair, enliven)
edit_story(stair,lambda word:word.capitalize() + '!')
'''
Thud!
Meow!
Thud!
Hiss!
Thud!
Meow!
Thud!
Hiss!
'''
