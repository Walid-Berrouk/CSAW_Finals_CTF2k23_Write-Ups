# Emoji

## Description

> 🤬

## Write-Up

As we look deeply in the series of the emojis, we can see that it's no a matter of how each emoji is encoded or their unicodes that relates them to the flag, but it's a matter of binaries.

You can see that each emoji has it's own opposite emoji in the list, which can give us a series of ones and zeros :

```py
one =  ['👍','🥩','🌝','⚽️','🔔','❤️‍🩹','❌','➕','📈','🍺']
zero = ['👎','🦴','🌚','🏈','🔕','💔','⭕️','➖','📉','🍼']
```

after mapping on the set of emojis and testing for binary chars, we get the flag.

## Flag

csawctf{emoji_game_on_fleeeeeeeeeek}