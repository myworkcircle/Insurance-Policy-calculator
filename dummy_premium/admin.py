from django.contrib import admin
from .models import file
from import_export.admin import ImportExportModelAdmin


admin.site.register(file)

# admin.site.register(dummy)

# class company1Admin(ImportExportModelAdmin):
#     class Meta:
#         model = company1
#         exclude = ('id',)
# admin.site.register(company1,company1Admin)
# admin.site.register(company2,company1Admin)
# admin.site.register(company3,company1Admin)
# admin.site.register(company4,company1Admin)



