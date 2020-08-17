import pandas as pd
from django.contrib.auth.models import Mapping

# making data frame
data = pd.read_excel(r"D:\Candidate Report.xlsx")

# list(data) or
df=[]

df= list(data.columns)
print (df)

db = Mapping._meta.get_fields()

print(db)

#mappings = {'db_fields':db,
#            'excel_fields': df}

#ab= pd.DataFrame(mappings, columns = ['db_fields', 'excel_fields'])

#ab#.to_excel (r'D:\mappings.xlsx', index = False, header=True)
