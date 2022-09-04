#!/bin/bash

pattern=''
word=''

first_word=$(grep -o "#@\$ [a-zA-Z]*" $1|grep -o "[a-zA-Z]*$") 
second_word=$(grep -o "$first_word [!@#$%^&*]* [a-zA-Z]*" $1|grep -o "[a-zA-Z]*$")
word=$(grep -o "$second_word [!@#$%^&*]* [a-zA-Z]*" $1|grep -o "[a-zA-Z]*$")
pattern=$(grep -o "$word [!@#$%^&*]*" $1|grep -o "[!@#$%^&*]*$")
echo "Last Word found: $word"
echo "Last Pattern found: $pattern"
