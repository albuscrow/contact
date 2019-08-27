import csv

from django.contrib import admin
from django.http import HttpResponse

from db.models import Contact


def export_cvs(modeladmin, request, queryset):
    header = ["姓名", "手机", "公司", "职务", "居住地址", "毕业院校"]
    response = HttpResponse(content_type='text/csv', charset='gbk')
    response['Content-Disposition'] = 'attachment; filename="symptom_explain.csv"'

    writer = csv.DictWriter(response, fieldnames=header)
    writer.writeheader()
    for c in Contact.objects.all():
        writer.writerow(
            {"姓名": c.name, "手机": c.phone, "公司": c.company, "职务": c.title, "居住地址": c.city, "毕业院校": c.graduated})
    return response


export_cvs.acts_on_all = True
export_cvs.short_description = "导出cvs文件"


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'company', 'title', 'city', 'graduated')
    actions = [export_cvs]


# Register your models here.
admin.site.register(Contact, ContactAdmin)
