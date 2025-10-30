def func(request):
    if request.method == 'post':
        dataform = LoginForm(request.post)
            # LoginForm => class name in file form.py
        if dataform.is_valid():
            dataform.save()
    return render(request 'path', {'form': LoginForm})

# form => هي اللي هتتحط في صفحة الhtml
