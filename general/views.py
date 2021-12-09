from django.shortcuts import render, redirect
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
import mimetypes
from general.models import excelFolder, excelFile
from general.forms import excelFileForm, excelFolderForm
from config.settings import MEDIA_ROOT
import general.functions as genFunc
import general.db_init as dbIn
import tables.tableCheckFunctions as tc
import boto3
import os


def test(request):
    return HttpResponse("Test")


def home(request):
    """View with home template rendering"""
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        return render(request, 'home.html')


# main folder evaluation
def prFold(request, *args, **kwargs):
    """Main function of 'general' app. Generate a 'folder' with it's belongings like tables, files and folders."""
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        # checking if database initialised correctly
        if not dbIn.dbCheckInit():
            dbIn.dbInit()
        # this function is supposed to calculate three variables - full path to the folder, it's name and name + path.
        folderUID, folderPath, fullPath = genFunc.pathCalculation(**kwargs)

        # Handling main folder structure
        foldersTree = genFunc.mainFoldStruct(folderUID=folderUID, folderPath=folderPath)
        theFolderObject = foldersTree[0]
        treeTitlesLinks = genFunc.namesLinksFolder(foldersTree)
        # checking if main folder contains any table inside
        # and taking table data if it is
        tableInfoProc = tc.tableInfoProcessor()

        tables = tableInfoProc.getTablesInfo(theFolderObject)
        tableType = theFolderObject.tableName.replace("Table", "")
        # handling info about files and folders inside of the main folder
        folders = excelFolder.objects.filter(path=fullPath).order_by('title')
        files = excelFile.objects.filter(path=fullPath).order_by('title')
        return render(request, 'general/prFold.html', {
            'folders': folders,  # all directories inside of this directory
            'foldPath': fullPath,  # full path to this directory
            'files': files,  # all files inside of this directory
            'theFolderObject': theFolderObject,
            'tables': tables,  # equipment, materials, organisations etc.
            'previousFolder': folderPath,  # path to previous directory
            'pathBack': fullPath,  # tell the template it's parent
            'treeTitlesLinks': treeTitlesLinks,
            'tableTypeRedirect': tableType
        })


def newExcelFolder(request):
    """ Form creation function for new folders"""
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        if request.method == 'POST':
            form = excelFolderForm(request.POST)
            if form.is_valid():
                form.save(author=request.user.get_username())
            else:
                print(form.is_valid())
            return redirect(request.POST['pathBack'])

        form = excelFolderForm()
        if 'path' in request.GET and 'pathBack' in request.GET:
            return render(request, 'general/createFolder.html', {'excelFolderForm': form,
                                                                 'path': request.GET['path'],
                                                                 'pathBack': request.GET['pathBack']})
        else:
            return redirect('home')


def uploadExcelFile(request):
    """Uploading new file into a folder"""
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        if request.method == 'POST':
            fileTitle = request.FILES['file'].name
            form = excelFileForm(request.POST, request.FILES, )
            if form.is_valid():
                form.save(title=fileTitle,
                          author=request.user.get_username(),
                          )
            else:
                print("Form is not valid")
            return redirect(request.POST['pathBack'])

        form = excelFileForm()
        if 'path' in request.GET and 'pathBack' in request.GET:
            return render(request, 'general/uploadFile.html', {'excelFileForm': form,
                                                               'path': request.GET['path'],
                                                               'pathBack': request.GET['pathBack']})
        else:
            redirect('home')


def deleteExcel(request, pk, type):
    """Deleting file from the structure"""
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        if request.method == 'POST':
            if type == 'file':
                book = excelFile.objects.get(pk=pk)
                book.falseDeletion()
            elif type == 'folder':
                book = excelFolder.objects.get(pk=pk)
                book.falseDeletion()
            else:
                return redirect('home')
            # Костыль костылём
            if request.POST['pathBack'].split('/')[0] == 'prFold':
                return redirect('/' + request.POST['pathBack'])
            return redirect(request.POST['pathBack'])


def renameExcelFile(request, pk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        if request.method == 'POST':
            book = excelFile.objects.get(pk=pk)
            if 'newTitle' in request.POST:
                book.rename(request.POST['newTitle'])
            if 'additionalInfo' in request.POST:
                book.additionalInfo = request.POST['additionalInfo']
            book.save()
        return redirect("/" + request.POST['pathBack'])


def renameExcelFolder(request, pk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        if request.method == 'POST':
            if request.POST['newTitle'] != "":
                book = excelFolder.objects.get(pk=pk)
                book.rename(request.POST['newTitle'])
        return redirect("/" + request.POST['pathBack'])


def downloadExcelFile(request, pk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        file = excelFile.objects.get(pk=pk)
        fileName = file.title
        filePath = file.path + "/" + file.UID
        mime_type, _ = mimetypes.guess_type(filePath)
        bufferFileName = os.path.join(MEDIA_ROOT, "buffer", fileName)

        BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(BUCKET_NAME)
        bucket.download_file(filePath, bufferFileName)

        fs = FileSystemStorage()
        if fs.exists(bufferFileName):
            with fs.open(bufferFileName) as file:
                mime_type, _ = mimetypes.guess_type(bufferFileName)
                response = HttpResponse(file, content_type=mime_type)
                response['Content-Disposition'] = 'attachment; filename="' + fileName + '"'
                os.remove(bufferFileName)
                return response
        else:
            return HttpResponseNotFound('The file wasnt found at the server')