#localWord dictionary source: http://www.wickedgood.info/cgi-bin/forum/gforum.cgi?post=16775;search...
#accent example: http://www.youtube.com/watch?v=RbK4cL3QSc0

def bostonify(filename):

    textFile = open(filename, 'r')
    parsedTextRaw = textFile.read()
    textFile.close()

    localWordConversion = {' very ':' wicked ',' extremely ':' wicked ',' cool ':' pissa ',' excellent ':' wicked pissa ','freeway':'highway','highway shoulder':'breakdown lane','potatoes':'b\'daydas','potato':'b\'dayda','soda':'tonic','soda pop':'tonic','water fountain':'bubbla','hero sandwich':'grinda','subway car':'cah','can get':'can\'t get','corner':'cawna','first':'fihst','four':'foah','sure':'shoe-ah','Cuba':'Cuber','Havana':'Havannar','Brenda':'Brender','weird':'wee-id','stupid':'retahded','dumb':'retahded','basement':'down cella','dresser drawer':'dressa drawah','jeans':'dungies','bluejeans':'dungies','kaiser roll':'egg roll','rubber band':'elastic','40':'foddy','forty':'foddy','30':'thihdy','thirdy':'thihdy','third':'thihd','3rd':'thihd','milkshake':'frappe','malted':'frappe','bizarre':'bizah','fudgsicle':'fudgicle','garbage':'gahbidge','tomato sauce':'gravy','hamburger':'hamburg','frankfurter':'frankfurt','Hyde Park':'Hipahk','Mattapan':'Da Pan','Dorchester':'Dawchesta','Quincy':'Quinzee','ice cream':'Hoodsie','crazy':'hoopie','Boston':'the Hub','Shore':'Shoah','North':'Nawth','Medford':'Meffid','No sir!':'Na-ah!','On account of':'onna conna','drive-in':'open air','liquor store':'packie','liquor':'likka','living room':'Pahlah','front porch':'piazza','party':'potty','pierced':'pee-ihced','resident':'rat','Roslindale':'Rozzie','West Roxbury':'Westie','Jamaica Plain':'JP','traffic circle':'rotahry','roundabout':'rotahry','foreign':'westa Wuhstuh','tourist':'fohreigna','Saturday':'Saddadee','here':'heah'}
    charConversion = {'ar':'ah','ore':'ah','or':'ah','ere':'eah','er':'uh', 'ol':'ahl','oa':'a','om':'ahm','on':'ahn','ing':'in\'','ire ':'iyah ','you':'yah','oce':'ahs','our':'oah','ture':'chah',' and, ':' and ahh, ', 'ure ':'oo-ah '}
    falsePositiveConversion = {'ahe':'are','ahy':'ary','uhe':'ure','ane':'one','uha':'ura','aha':'ara', 'in\' to ':'inna ','teah':'tere','rin\'':'ring','ahce':'ace','ered ':'uhd ','ahi':'ari','eahnt':'\'rent','uhie':'erie', ' ura ':' era ',' mah ':' moah '}

    parsedText = []

    for word in parsedTextRaw:
        for ch in localWordConversion.keys():
            if ch in parsedTextRaw:
                parsedTextRaw=parsedTextRaw.replace(ch,localWordConversion[ch])
    
    for word in parsedTextRaw:
        for ch in charConversion.keys():
            if ch in parsedTextRaw:
                parsedTextRaw=parsedTextRaw.replace(ch,charConversion[ch])

    for word in parsedTextRaw:
        for ch in falsePositiveConversion.keys():
            if ch in parsedTextRaw:
                parsedTextRaw=parsedTextRaw.replace(ch,falsePositiveConversion[ch])

    print parsedTextRaw

while True:
    inputText = input("\nEnter a text filename (e.g. \'filename.txt\'): ")
    print "Boston-ifying your text... please wait... \nFor a pronunciation guide, please see: http://www.youtube.com/watch?v=RbK4cL3QSc0\n"
    bostonify(inputText)
