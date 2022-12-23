# from django.http import HttpResponse
# from django.shortcuts import render

# def index (request):
#     row={'name':'rohan','place':'indor'}
#     return render(request,'index.html',row)
# # def removepunc(request):
# def analize(request):
#     djtext = request.POST.get('text','off')
#     removepunc=request.POST.get('removepunc','off')
#     fullcaps = request.POST.get('fullcaps', 'off')
#     newlineremover=request.POST.get('newlineremover','off')
#     extraspaceremover = request.POST.get('extraspaceremover', 'off')
#     charcount = request.POST.get('charcount', 'off')
#     print(removepunc)
#     print(djtext)
#     analized = djtext
#     if removepunc == 'on':
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analized = ""
#         for char in djtext:
#             if char  not in punctuations:
#                 analized = analized + char
#         params = {'purpose':'remove punctuation' , 'a': analized }
#         return render(request,'analized.html',params)
#     elif fullcaps=='on':
#         punctuations=' '
#         analized = ""
#         for char in djtext:
#             if char  not in punctuations:
#                 analized = analized + char.upper()
#         params = {'purpose':'upper case converting' , 'a': analized }
#         return render(request,'analized.html',params)
#     elif newlineremover=='on' :
#         analized=""
#         for char in djtext:
#             if char != "\n" and char !='\r':
#                 analized=analized+char
#         params={'purpose':'lineremover','a':analized}
#         return render(request,'analized.html',params)
    
#     elif ( extraspaceremover=='on'):
#         analized = ""   
#         for index, char in  enumerate( djtext):
#             if  djtext[ index ] == " " and djtext [index + 1] == " ":
#                 pass
#             else:
#                 analized=analized+char 
#         params = {'purpose':'extaspaceremove' , 'a': analized }
#         return render(request,'analized.html',params) 
#     elif ( charcount=='on'):
#         analized = 0   
#         for char in djtext:
#             analized=analized+1 
#         params = {'purpose':'counting' , 'a': analized }
#         return render(request,'analized.html',params)
#     else:
#          return HttpResponse('error')      
               
    # if ( removepunc == 'on' and  fullcaps=='on' ) :
    #     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #     analized=""
    #     for char in djtext:
    #         if char not in punctuations:
    #             analized = analized + char.upper()

    #     params = {'purpose':'upper case converting' , 'a': analized }
    #     return render(request,'analized.html',params) 
    # else:
    #     if (removepunc=='on') :
    #         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #         analized=""
    #         for char in djtext:
    #             if char not in punctuations:
    #                 analized = analized + char
    #     elif(fullcaps=='on') :
    #         punctuations=''

    #         analized=""
    #         for char in djtext:
    #             if char not in punctuations:
    #                 analized = analized + char.upper()      
    #     params = {'purpose':'upper case converting' , 'a': analized }
    #     return render(request,'analized.html',params)        
        # return HttpResponse('error')   

        # return HttpResponse('remove punc')   
        



from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    row={'name':'rohan','place':'indor'}
    return render(request,'index.html',row)
# def removepunc(request):
def analize(request):
    djtext = request.POST.get('text','off')
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # print(removepunc)
    # print(djtext)
   
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analized = ""
        for char in djtext:
            if char  not in punctuations:
                analized = analized + char
        params = {'purpose':'remove punctuation' , 'a': analized }
        djtext=analized
        # return render(request,'analized.html',params)
    if fullcaps=='on':
        punctuations=' '
        analized = ""
        for char in djtext:
            if char  not in punctuations:
                analized = analized + char.upper()
        params = {'purpose':'upper case converting' , 'a': analized }
        djtext=analized
        # return render(request,'analized.html',params)
         
    if newlineremover=='on' :
        analized=""
        for char in djtext:
            if char != "\n" and char !='\r':
                analized=analized+char
        params={'purpose':'lineremover','a':analized}
        djtext=analized
        # return render(request,'analized.html',params)
    
    elif ( extraspaceremover=='on'):
        analized = ""   
        for index, char in  enumerate( djtext):
            if  djtext[ index ] == " " and djtext [index + 1] == " ":
                pass
            else:
                analized=analized+char 
        params = {'purpose':'extaspaceremove' , 'a': analized }
        djtext=analized
        # return render(request,'analized.html',params) 
    if ( charcount=='on'):
        analized = 0   
        for char in djtext:
            analized=analized+1 
        params = {'purpose':'counting' , 'a': analized }
        djtext=analized

    return render(request,'analized.html',params)
    # else:
    #      return HttpResponse('error')      
               