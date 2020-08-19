from django.shortcuts import render
# from .models import Mapping
import pandas as pd
from records.models import StagingRecords

# Create your views here.

def disp(request):
    data = pd.read_excel(r"D:\Candidate Report.xlsx")
    df = []
    db = []
    context = {
        'df' : list(data.columns),
        'db' : list(field.name for field in StagingRecords._meta.get_fields())
    }

    return render(request, 'mapping.html',  context)
