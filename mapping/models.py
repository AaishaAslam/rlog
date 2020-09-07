from django.db import models, migrations
from django.contrib.postgres.fields import HStoreField


# Create your models here.
class Mapping(models.Model):
	MappingID = models.IntegerField(primary_key = True)
	UserID = models.IntegerField(null = True)
	MappingFor = models.TextField(null = True)
	CreatedOn = models.DateField(auto_now_add = True, null = True)
	Mappings = HStoreField(null = True)

def read_file():
	path_name = request.GET.get('df')
	df = pd.read_excel(path_name)
	names = list(df.columns)
	fields = [field.name for field in [names]._meta.get_fields()]
	return render(request, 'mapping.html', {'fields' : fields, 'path_name': path_name, 'names' : names})

fields = [field.name for field in [Mapping]._meta.get_fields()]
for field in fields:
	option_value={{field}}>{{field}}(option_value)   

for name in names ({name}):
	select_name="{{name}}"

for field in fields:
	option_value={{field}}>{{field}}(option_value)    

select
input_type="hidden"
name="path_name"
value={{path_name}}

if request.method == 'POST':
   path_name = request.POST['excel_path']
   df = pd.read_excel(path_name)
   names = list(df.columns)

matched = { key:request.POST.get(key, False) for key in names }
df.rename(columns = matched, inplace = True)

df.set_index("index_column", drop=True, inplace=True)
dictionary = df.to_dict(orient="index")
for index, object in dictionary.items():
			model = MODEL_NAME()
			for key,value in object.items():
				setattr(model, key, value)
			setattr(m, 'index', index)
			model.save()

