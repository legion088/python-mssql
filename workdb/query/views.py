from django.shortcuts import render
from query.services import execute_query


def main(request):
    query, result = request.POST.get('query'), []
    error = None

    if query:
        result = execute_query(query)
        if type(result) is tuple:
            error = result

    return render(
        request,
        template_name='query/index.html',
        context={'result': result, 'error': error}
    )
