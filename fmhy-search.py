## Streamlit
import streamlit as st

st.set_page_config(
    page_title="FMHY Search",
    page_icon="https://www.fmhy.ml/assets/logo.png",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/Rust1667/a-FMHY-search-engine',
        'Report a bug': "https://github.com/Rust1667/a-FMHY-search-engine",
        'About': "https://www.reddit.com/r/FREEMEDIAHECKYEAH/wiki/index/"
    }
)

#st.image("https://i.imgur.com/s9abZgP.png", width=60)
st.title("Search FMHY")


queryInput = st.text_input("")


import requests

#enable text coloring only if the requirements are met
coloring = False
#try:
#    from termcolor import colored
#    import colorama
#    colorama.init()
#except:
#    coloring = False


def splitSentenceIntoWords(searchInput):
    searchInput = searchInput.lower()
    searchWords = searchInput.split(' ')
    return searchWords

def getAllLines():
    print("Loading FMHY single-page file from Github...")
    response1 = requests.get("https://raw.githubusercontent.com/nbats/FMHYedit/main/single-page")
    print("Loaded.\n")

    data = response1.text
    lines = data.split('\n')
    return lines

def filterLines(lineList, filterWords):
    sentences = lineList
    words = filterWords
    sentence = [sentence for sentence in sentences if all(
        w.lower() in sentence.lower() for w in words
    )]
    return sentence

def filterOutTitleLines(lineList):
    filteredList = []
    sectionTitleList = []
    for line in lineList:
        if line[0] != "#":
            filteredList.append(line)
        else:
            sectionTitleList.append(line)
    return [filteredList, sectionTitleList]


#def highlightWord(sentence, word):
#    return sentence.replace(word, colored(word,'red'))
#
#def colorLinesFound(linesFound, filterWords):
#    coloredLinesList = []
#    filterWordsCapitalizedToo=[]
#    for word in filterWords:
#        filterWordsCapitalizedToo.append(word.capitalize())
#    filterWordsCapitalizedToo.extend(filterWords)
#    for line in linesFound:
#        for word in filterWordsCapitalizedToo:
#            line = highlightWord(line, word)
#        coloredLine = line
#        coloredLinesList.append(coloredLine)
#    return coloredLinesList

#---------

lineList = getAllLines()
# print("Search examples: 'youtube frontend', 'streaming site', 'rare movies', 'userscripts'... You can also type 'exit' or nothing to close the script.\n")
# doASearch()



def doASearch():
    #intro
#    print("STARTING NEW SEARCH...\n")
    searchInput = queryInput #input("Type a search string:     ")

    #make sure the input is right before continuing
#    if searchInput == "exit" or searchInput == "":
#        print("The script is closing...")
#        return

    #intro to the search results
    myFilterWords = splitSentenceIntoWords(searchInput)
    #print("Looking for lines that contain all of these words:")
    #print(myFilterWords)
    print("searching: " + searchInput)

    #main results
    myLineList = lineList
    linesFoundPrev = filterLines(lineList=myLineList, filterWords=myFilterWords)
    linesFoundAll = filterOutTitleLines(linesFoundPrev)
    linesFound = linesFoundAll[0]
    sectionTitleList = linesFoundAll[1]
    if coloring == True:
        linesFoundColored = colorLinesFound(linesFound, myFilterWords)
        textToPrint = "\n\n".join(linesFoundColored)
    else:
        textToPrint = "\n\n".join(linesFound)
    #print("Printing " + str(len(linesFound)) + " search results:\n")
    st.text(str(len(linesFound)) + " search results:\n")
    #print(textToPrint)
    st.markdown(textToPrint)
    #print("\nSearch ended with " + str(len(linesFound)) + " results found.\n")

    #title section results
    if len(sectionTitleList)>0:
        #print("Also there are these section titles: ")
        st.text("Also there are these section titles: ")
        #print("\n".join(sectionTitleList))
        st.text("\n".join(sectionTitleList))

    #repeat the search
    #print("\n\n\n")   
    #doASearch()


if(st.button("Search")):
    queryInput = queryInput.title()
    doASearch()

with st.sidebar:
    st.markdown("[Wiki on Reddit](https://www.reddit.com/r/FREEMEDIAHECKYEAH/wiki/index/)")
    st.markdown("[Wiki as Raw Markdown](https://raw.githubusercontent.com/nbats/FMHYedit/main/single-page)")
    st.markdown("[Repository for this search tool](https://github.com/Rust1667/a-FMHY-search-engine)")
    st.markdown("[List of Search tools for FMHY](https://www.reddit.com/r/FREEMEDIAHECKYEAH/comments/105xraz/howto_search_fmhy/)")


