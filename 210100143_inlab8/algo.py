import re
from symbol import parameters

##########
#### SEARCH FOR TODO and fix


# Anything following "//" is a comment until end of line
commentPat = re.compile(r'//.*')

# Grab anything within $...$. Make sure to use 
mathPat =  re.compile(r'\$.*?\$')

#All id-like words, including optional leading '\' and 
# field access sequences 
# Examples: abc,  foo.length, \xxx
wordPat = re.compile(r'\\?i?d?{?[a-zA-Z]+\.?[a-zA-Z.]*}?')

#Take a set of all the unique symbols in opsToTex's keys. 
#Like this r'[<=>.]+'   etc. 
opPat = re.compile(r'[<=>.!+-]+')

# A line of the form "proc myfunc(a, b)".
procPat = re.compile(r'^proc.*\)$')

keywordsToTex = {
    'for'    : r'\For'        ,     'if'     : r'\If'          , 
    'end'    : r'\End'        ,     'then'   : r'\Then'        , 
    'while'  : r'\While'      ,     'do'     : r'\Do'          ,  
    'to'     : r'\To'         ,     'by'     : r'\By'          , 
    'downto' : r'\Downto'     ,     'repeat' : r'\Repeat'      , 
    'until'  : r'\Until'      ,     'elseif' : r'\Elseif'      ,
    'elsif'  : r'\Elseif'     ,     'return' : r'\Return'      , 
    'error'  : r'\Error'      ,     'nil'    : r'\const{nil}'  , 
    'true'   : r'\const{true}',     'false'  : r'\const{false}'
}

opsToTeX = {
    '<-' : r'\leftarrow' ,      '->' : r'\rightarrow',      '==' : r'\isequal' ,
    '<=' : r'\leq'       ,      '>=' : r'\geq'        ,      '>' : '>'          , 
    '<' : '<'            ,      '!=' : r'\neq'       ,      '=' : r'\eq'       , 
    '...' : r'\threedots',      '..' : r'\twodots'
}

def processLine(line):
    if("// " in line):
        info = line.split("// ",1)
        content = info[0]
        comment = info[1]
        return processContent(content) + processComment(comment)
    else:
        return processContent(line)
    # Split line into content part and comment part
    # Comments are always to the right, but are optional
    # return processContent(content) + processComment(comment)

def processContent(content):
    if(re.match(procPat,content) != None):
        return processProc(content)
    else:
        content = processMath(content)
        content = processWords(content)
        content = processOps(content)
        return "\zi" + content
    # Treat the entire content as if it is already in math mode
    # processProc if it matches a proc line
    # Otherwise,
    # Treat the entire content as if it is already in math mode.
    # If there are any embedded '$...$' fragments, then strip the dollar signs
    # out.
    # Prepend '\zi' to the returned line, unless content matches a proc declaration

def processProc(lineMatch):
    s = "\Procname{\proc{"
    index = lineMatch.index(' ') +1
    leftbracketindex = lineMatch.index('(')
    s = s + lineMatch[index:leftbracketindex] + '}('
    rightbracketindex = lineMatch.index(')')
    parameters = lineMatch[leftbracketindex+1:rightbracketindex]
    parameter_list = parameters.split(', ')
    for i in range(0,len(parameter_list)-1):
        s= s+"\id{"+parameter_list[i]+"}, "
    s = s + "\id{"+parameter_list[len(parameter_list)-1]+"})}"
    return s

def processMath(fragment):
    return re.sub(mathPat,processMaths,fragment)

def processMaths(math):
    mathPart = math.group(0)
    mathPart = mathPart.replace("$",'')
    mathPart = re.sub(wordPat,processWord,mathPart)
    mathPart = re.sub(opPat,processOp,mathPart)
    return mathPart
    # call processOps(processWords) on the matching part.

def processWords(fragment):
    return re.sub(wordPat,processWord,fragment)
    # call re.sub with wordPat and processWord

def processWord(wordMatch):
    word = wordMatch.group(0)
    if word[0:3] == "\\id":
        return word
    if word[0] == "\\":
        return word 
    elif '.' in word:
        subwords = word.split('.')
        s = "\\attri"
        for i in range(0,len(subwords)-1):
            s = s+'b'
        for i in range(0,len(subwords)):
            s = s + '{' + subwords[i] + '}'
        return s
    elif word in keywordsToTex.keys():
        return keywordsToTex[word]
    else:
        return "\id{" + word + '}'
    # Handle four cases. 
    #   Word starts with '\' ... return word untouched
    #   Word has embedded '.'. Convert "abc.def.ghi" to "\attribbb{abc}{def}{ghi}"
    #            The number of 'b's following attrib should equal the number of dots
    #   Word belongs to keywords (see testalgo.py for all keywords). Replace with latex substitute
    #   Otherwise replace with "\id{word}"

def processOps(fragment):
    return re.sub(opPat, processOp, fragment)

def processOp(opMatch):
    op = opMatch.group(0)
    if op in opsToTeX:
        return '$' + opsToTeX[op] + '$'
    elif op == "+":
        return "$+$"
    elif op == "-":
        return "$-$"
    else:
        return op
    # replace op with matching latex equivalent if any, and surround with '$'
    # That is, '==' becomes '$\isequal$', but '===' remains unchanged.

def processComment(comment):
    comment = processMath(comment)
    return "\Comment " + comment
    #Treat comment as if it is in text mode, but all embedded math expressions must be translated
    #by processMath
    # See testalgo.py for expected behaviur


def main(filename):
    with open(filename) as f:
        print(r'\begin{codebox}')
        for line in f:
            line = line.rstrip()
            print(processLine(line))
        print(r'\end{codebox}')

def usage():
    print("""
algo.py <file.algo>
Translates a pseudocode algorithm to LaTeX's clrscode3e environment. 
The format is a simplification of that environment, the objective being to 
not have to introduce math-mode or have special keywords like \For and \If 

Keywords: 
- Loops: for, to, by, downto, do, while, repeat, until
- Selection: if, then, else, elseif/elsif
- Jumps: return, error, goto
- Constants: nil, true, false

do/end blocks are required for indent/dedent, but do not appear in final output

Operators like <-, !=, ==, <= etc are replaced by the LaTeX equivalents.

Example:

proc insertion-sort(A, B)
   for j <- 2 to A.length do
      key <- A[j] // Insert $A[j]$ into the sorted sequence $A[1 .. j-1]$
      i <- j - 1
      while i > 0 and A[i] > key do
         A[i+1] <- A[i]
         i <- i - 1
      end
      A[i+1] <- key
   end
   if x == 3 then do
      {{Do something special}}
   end
end

""")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    main(sys.argv[1])
    
   
