import os
from bs4 import BeautifulSoup

folderPath = os.path.join(os.environ['HOME'], 'Google Drive', 'Greek Texts', 'Plain Text',
                          'OpenGreekAndLatin-First1KGreek-0e92640', '1.1 No Notes')
os.chdir(folderPath)
indir = os.listdir(folderPath)
fileCount = 1
greekChars = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'ς', 'τ', 'υ',
              'φ', 'χ', 'ψ', 'ω']
for file in indir:
    noteCount = 0
    greekCount = 0
    if file[-4:] == '.xml':
        print(fileCount, file)
        greekFile = open(file, 'r')
        greekText = BeautifulSoup(greekFile, 'lxml')
        if greekText.author:
            author = greekText.author.text
        else:
            author = 'Unknown'
        if greekText.title.text == 'Machine readable text':
            title = greekText.find_all('title')[1].text
        else:
            title = greekText.title.text
        print(author, title)
        for paragraphs in greekText.find_all('note'):
            paragraphs.decompose()
            noteCount += 1
        fileCount += 1
        print(noteCount, 'notes extracted.')
        greekFile.close()
        with open(file, 'w') as writefile:
            writefile.write(greekText.prettify())

print(fileCount-1, 'files in', folderPath)
