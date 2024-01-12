from django.shortcuts import render, redirect
from .models import userinfo, userclass
from .forms import Userinfo


# Create your views here.
def index(request):
    # searching
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    print(q)
    info = userinfo.objects.filter(userclass__student_class__icontains=q)

    # ---------------
    classes = userclass.objects.all()
    # checking if class has no user then it should delete
    for i in classes:
        countuser = i.userinfo_set.all()
        if countuser.count() is 0:
            i.delete()
            return redirect("/")

    return render(request, "index.html", {"info": info, "classes": classes, "q": q})


def adduser(request):
    classes = userclass.objects.all()
    form = Userinfo()
    if request.method == "POST":
        getclass = request.POST.get("userclass").lower()
        getclass, created = userclass.objects.get_or_create(student_class=getclass)
        userinfo.objects.create(
            name=request.POST.get("name"),
            address=request.POST.get("address"),
            phone=request.POST.get("phone"),
            userclass=getclass,
        )
        return redirect("/")
    # if request.method == "POST":
    #     form=Userinfo(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    return render(request, "add.html", {"form": form, "classes": classes})


def delete(request, item_id):
    info = userinfo.objects.get(id=item_id)
    print(info)
    if request.method == "POST":
        info.delete()
        return redirect("/")

    return render(request, "delete.html", {"info": info})


def edit(request, item_id):
    classes = userclass.objects.all()
    info = userinfo.objects.get(id=item_id)
    form = Userinfo(instance=info)
    if request.method == "POST":
        getclass = request.POST.get("userclass").lower()
        getclass, created = userclass.objects.get_or_create(student_class=getclass)
        info.name = request.POST.get("name")
        info.userclass = getclass
        info.address = request.POST.get("address")
        info.phone = request.POST.get("phone")
        info.save()
        redirect("/")
    # if request.method == 'POST':
    #     form =Userinfo(request.POST,instance=info)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')

    return render(
        request, "edit.html", {"form": form, "classes": classes, "info": info}
    )


# ------plz delete this
def Edit(request, item_id):
    classes = userclass.objects.all()
    info = userinfo.objects.get(id=item_id)
    form = Userinfo(instance=info)
    if request.method == "POST":
        getclass = request.POST.get("userclass").lower()
        getclass, created = userclass.objects.get_or_create(student_class=getclass)
        info.name = request.POST.get("name")
        info.userclass = getclass
        info.address = request.POST.get("address")
        info.phone = request.POST.get("phone")
        info.save()
        redirect("/")
    # if request.method == 'POST':
    #     form =Userinfo(request.POST,instance=info)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')

    return render(
        request, "edit.html", {"form": form, "classes": classes, "info": info}
    )
