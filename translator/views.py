from django.shortcuts import render
from googletrans import Translator
from .forms import languageForm


def translationForm(request):
    trans = Translator()
    translation = ""
    original = ""
    language = 'af'
    form = languageForm()
    lang_detect = "Unknown"
    if request.method == 'POST':
        form = languageForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
        original = request.POST.get('original')
        if original and not(original.isspace()):
            translation = trans.translate(original, dest=language).text
            lang_detect = trans.detect(original).lang
    context = {'translation': translation, "original": original, "form": form, "lang": lang_detect}
    return render(request, 'translation-form.html', context)
