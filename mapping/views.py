from django.shortcuts import render
# from .models import Mapping
import pandas as pd
from records.models import StagingRecords

# Create your views here.

def fieldmatching(request):
    if request.method == 'POST':
        path_name = request.POST['path_name']
        df = pd.read_csv(r"D:\Candidate Report.xlsx")
        names = list(df.columns)
if request.POST.get('checkBox') == None:   
###To keep the same columns in case of matching 'fields' and ###'names', add a checkbox on the html page
            matched = { key:request.POST.get(key, False) for key in names }
            df.rename(columns = matched, inplace = True)
        df.set_index("index", drop=True, inplace=True)
        dictionary = df.to_dict(orient="index")
        for index, object in dictionary.items():
            model = MODEL_NAME()
            for key,value in object.items():
                setattr(model, key, value)
            setattr(m, 'index', index)
            model.save()
return redirect('redirect_to_view')
    else:
        path_name = request.GET.get('df')
        df = pd.read_csv(path_name)
        names = list(df.columns)
        fields = [field.name for field in MODEL_NAME._meta.get_fields()]
        return render(request, 'mapping.html', {'fields' : fields, 'path_name': path_name, 'names' : names})
