paragraph = """
Python is an interpreted, high-level programming language for general-purpose programming. Created by Guido van Rossum 
and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant 
whitespace. It provides constructs that enable clear programming on both small and large scales.[26] In July 2018, 
Van Rossum stepped down as the leader in the language community.[27][28]
Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, 
including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[29]
Python interpreters are available for many operating systems. CPython, the reference implementation of Python, 
is open source software[30] and has a community-based development model, as do nearly all of Python's other implementations. 
Python and CPython are managed by the non-profit Python Software Foundation.
"""


list1 = paragraph.split() #Splitting words of paragraph in list 

print("\n Modifications without punctuation             \n")

clean_para =''

new_paragraph = ""
i = 0
for e in list1:
    if e[-1]=='s':
        e = e[:-1]
        i = i + 1
        
    new_paragraph = new_paragraph +' '+ e

print(new_paragraph,'\n')
print('### There were a total of '+str(i)+' words altered ###')

print("\nModifications considering punctuation          \n")

puntuation = '''`~!@#$%^&*()_+-={[\|;'/.,:"?><"']}1234567890''' # Punctuations and Numbers
final_list =[]
for i in list1:
    a = list(i)
    if 's' in i:
        if len(i) -1 == i.rindex('s'): # Cases where 's' is not followed by a punctuation or number
            i = i[:i.rindex('s')] 
        elif i[i.rindex('s') + 1]  in list(puntuation): # Cases where 's' is followed by a punctuation or a number
            i= i[: i.rindex('s') ] + i[i.rindex('s')+1:] 
        
    final_list.append(i)
clean_para =' '.join(final_list)
print(clean_para)
